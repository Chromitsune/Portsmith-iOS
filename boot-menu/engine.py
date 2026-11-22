"""Host-testable boot-menu model and selection state; it executes no boot actions."""
from __future__ import annotations

from dataclasses import dataclass
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
_ID = re.compile(r"^[a-z][a-z0-9-]*$")
_TARGET = re.compile(r"^opaque:[a-z0-9._:-]+$")


@dataclass(frozen=True)
class Entry:
    id: str
    label: str
    detail: str
    icon_id: str | None
    target_id: str
    enabled: bool


@dataclass(frozen=True)
class MenuProfile:
    profile_id: str
    title: str
    look: dict
    options: dict
    entries: tuple[Entry, ...]


class MenuController:
    """Selection-only controller; activate() returns an opaque target ID."""

    def __init__(self, profile: MenuProfile, start_entry_id: str | None = None):
        self.profile = profile
        self._by_id = {entry.id: index for index, entry in enumerate(profile.entries)}
        enabled = [i for i, entry in enumerate(profile.entries) if entry.enabled]
        if not enabled:
            raise ValueError("menu profile has no enabled entries")
        if start_entry_id is not None:
            if start_entry_id not in self._by_id:
                raise ValueError(f"unknown start entry: {start_entry_id}")
            if not profile.entries[self._by_id[start_entry_id]].enabled:
                raise ValueError("start entry is disabled")
            self.selected_index = self._by_id[start_entry_id]
        else:
            # Focus the first enabled row for display only. This does not autoboot it.
            self.selected_index = enabled[0]

    @property
    def selected(self) -> Entry:
        return self.profile.entries[self.selected_index]

    def move(self, delta: int) -> Entry:
        if delta == 0:
            return self.selected
        count = len(self.profile.entries)
        direction = 1 if delta > 0 else -1
        for _ in range(abs(delta)):
            for _attempt in range(count):
                self.selected_index = (self.selected_index + direction) % count
                if self.profile.entries[self.selected_index].enabled:
                    break
        return self.selected

    def activate(self) -> str | None:
        """Return the selected opaque target token; never execute it."""
        return self.selected.target_id if self.selected.enabled else None

    def handle(self, event: str) -> str | None:
        event = event.lower()
        if event in {"up", "left"}:
            self.move(-1)
        elif event in {"down", "right"}:
            self.move(1)
        elif event in {"select", "confirm"}:
            return self.activate()
        elif event in {"cancel", "back"}:
            return None
        else:
            raise ValueError(f"unknown menu event: {event}")
        return None


def _read(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def load_profile(profile_path: Path) -> MenuProfile:
    """Load a profile and its look/options files, with strict safe-data checks."""
    profile_path = profile_path.resolve()
    profile = _read(profile_path)
    if profile.get("schema_version") != 1 or not _ID.fullmatch(str(profile.get("profile_id", ""))):
        raise ValueError("invalid profile schema_version or profile_id")
    look_id, options_id = profile.get("look_id"), profile.get("options_id")
    if not isinstance(look_id, str) or not _ID.fullmatch(look_id):
        raise ValueError("look_id must be a stable identifier")
    if not isinstance(options_id, str) or not _ID.fullmatch(options_id):
        raise ValueError("options_id must be a stable identifier")
    look = _read(ROOT / "looks" / f"{look_id}.json")
    options = _read(ROOT / "options" / f"{options_id}.json")
    if look.get("schema_version") != 1 or look.get("look_id") != look_id:
        raise ValueError("look profile ID/version mismatch")
    if options.get("schema_version") != 1 or options.get("options_id") != options_id:
        raise ValueError("options profile ID/version mismatch")
    if options.get("auto_boot") or options.get("remember_selection") or options.get("persist_selection"):
        raise ValueError("host model refuses boot/persistence behavior; this package has no platform adapter")
    entries = profile.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("profile must contain a non-empty entry list")
    parsed = []
    seen = set()
    for raw in entries:
        if not isinstance(raw, dict) or set(raw) != {"id", "label", "detail", "icon_id", "target_id", "enabled"}:
            raise ValueError("each entry must use exactly the documented presentation/opaque-target fields")
        ident = raw["id"]
        if not isinstance(ident, str) or not _ID.fullmatch(ident) or ident in seen:
            raise ValueError(f"invalid or duplicate entry ID: {ident!r}")
        seen.add(ident)
        if not isinstance(raw["label"], str) or not raw["label"] or not isinstance(raw["detail"], str):
            raise ValueError(f"invalid title/detail for {ident}")
        if raw["icon_id"] is not None and not isinstance(raw["icon_id"], str):
            raise ValueError(f"invalid icon ID for {ident}")
        if not isinstance(raw["target_id"], str) or not _TARGET.fullmatch(raw["target_id"]):
            raise ValueError(f"target_id for {ident} must be opaque; executable commands are forbidden")
        if not isinstance(raw["enabled"], bool):
            raise ValueError(f"enabled must be boolean for {ident}")
        parsed.append(Entry(**raw))
    if not any(entry.enabled for entry in parsed):
        raise ValueError("profile has no enabled entries")
    return MenuProfile(profile["profile_id"], profile.get("title", ""), look, options, tuple(parsed))
