#!/usr/bin/env python3
"""Validate the boot-menu staging JSON with the standard library only; no device I/O."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ID = re.compile(r"^[a-z][a-z0-9-]*$")
TARGET = re.compile(r"^opaque:[a-z0-9._:-]+$")
COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")
LAYOUTS = {"vertical-icon-stack", "vertical-text-list", "responsive-card-grid"}


def read_json(path: Path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: {exc}") from exc


def check_look(path: Path) -> str:
    data = read_json(path)
    required = {"schema_version", "look_id", "description", "layout", "background", "palette", "geometry", "icon_policy", "text_fallback"}
    if set(data) != required:
        raise ValueError(f"{path.relative_to(ROOT)}: expected keys {sorted(required)}")
    if data["schema_version"] != 1 or not ID.fullmatch(data["look_id"]):
        raise ValueError(f"{path.relative_to(ROOT)}: invalid schema_version/look_id")
    if data["layout"] not in LAYOUTS:
        raise ValueError(f"{path.relative_to(ROOT)}: unknown layout {data['layout']!r}")
    if not COLOR.fullmatch(data["background"]):
        raise ValueError(f"{path.relative_to(ROOT)}: background must be #RRGGBB")
    if set(data["palette"]) != {"surface", "selection", "text", "secondary_text", "disabled"}:
        raise ValueError(f"{path.relative_to(ROOT)}: incomplete palette")
    if any(not COLOR.fullmatch(color) for color in data["palette"].values()):
        raise ValueError(f"{path.relative_to(ROOT)}: palette colors must be #RRGGBB")
    if not isinstance(data["geometry"], dict) or not data["geometry"]:
        raise ValueError(f"{path.relative_to(ROOT)}: geometry must be a non-empty object")
    if data["icon_policy"] not in {"none", "optional-abstract-icon-id"} or not isinstance(data["text_fallback"], bool):
        raise ValueError(f"{path.relative_to(ROOT)}: invalid icon/text fallback policy")
    return data["look_id"]


def check_options(path: Path) -> str:
    data = read_json(path)
    required = {"schema_version", "options_id", "timeout_ms", "default_entry_id", "auto_boot", "remember_selection", "persist_selection", "skip_disabled_entries", "require_confirmation_for", "unknown_action_policy"}
    if set(data) != required:
        raise ValueError(f"{path.relative_to(ROOT)}: expected keys {sorted(required)}")
    if data["schema_version"] != 1 or not ID.fullmatch(data["options_id"]):
        raise ValueError(f"{path.relative_to(ROOT)}: invalid schema_version/options_id")
    if not isinstance(data["timeout_ms"], int) or data["timeout_ms"] < 0:
        raise ValueError(f"{path.relative_to(ROOT)}: timeout_ms must be a non-negative integer")
    for field in ("auto_boot", "remember_selection", "persist_selection", "skip_disabled_entries"):
        if not isinstance(data[field], bool):
            raise ValueError(f"{path.relative_to(ROOT)}: {field} must be boolean")
    if data["unknown_action_policy"] != "reject":
        raise ValueError(f"{path.relative_to(ROOT)}: unknown actions must be rejected")
    if not isinstance(data["require_confirmation_for"], list) or any(x not in {"restart", "power-off", "firmware-update"} for x in data["require_confirmation_for"]):
        raise ValueError(f"{path.relative_to(ROOT)}: invalid confirmation action")
    if data["auto_boot"] or data["remember_selection"] or data["persist_selection"]:
        raise ValueError(f"{path.relative_to(ROOT)}: staging profiles cannot enable auto-boot or persistent selection")
    return data["options_id"]


def check_profile(path: Path, looks: set[str], options: set[str]) -> str:
    data = read_json(path)
    required = {"schema_version", "profile_id", "title", "look_id", "options_id", "entries"}
    if set(data) != required:
        raise ValueError(f"{path.relative_to(ROOT)}: expected keys {sorted(required)}")
    if data["schema_version"] != 1 or not ID.fullmatch(data["profile_id"]):
        raise ValueError(f"{path.relative_to(ROOT)}: invalid schema_version/profile_id")
    if data["look_id"] not in looks or data["options_id"] not in options:
        raise ValueError(f"{path.relative_to(ROOT)}: missing look/options reference")
    if not isinstance(data["entries"], list) or not data["entries"]:
        raise ValueError(f"{path.relative_to(ROOT)}: entries must be a non-empty list")
    seen = set()
    for entry in data["entries"]:
        keys = {"id", "label", "detail", "icon_id", "target_id", "enabled"}
        if set(entry) != keys or not ID.fullmatch(entry["id"]) or entry["id"] in seen:
            raise ValueError(f"{path.relative_to(ROOT)}: invalid/duplicate entry ID or entry fields")
        seen.add(entry["id"])
        if not isinstance(entry["label"], str) or not entry["label"] or not isinstance(entry["detail"], str):
            raise ValueError(f"{path.relative_to(ROOT)}: invalid label/detail")
        if entry["icon_id"] is not None and not isinstance(entry["icon_id"], str):
            raise ValueError(f"{path.relative_to(ROOT)}: icon_id must be a string or null")
        if not isinstance(entry["target_id"], str) or not TARGET.fullmatch(entry["target_id"]):
            raise ValueError(f"{path.relative_to(ROOT)}: target_id must be an opaque token")
        if not isinstance(entry["enabled"], bool):
            raise ValueError(f"{path.relative_to(ROOT)}: enabled must be boolean")
    return data["profile_id"]


def main() -> int:
    try:
        looks = {check_look(path) for path in sorted((ROOT / "looks").glob("*.json"))}
        options = {check_options(path) for path in sorted((ROOT / "options").glob("*.json"))}
        profiles = [check_profile(path, looks, options) for path in sorted((ROOT / "profiles").glob("*.json"))]
        if not looks or not options or not profiles:
            raise ValueError("at least one look, options file, and sample profile are required")
        print(f"PASS: {len(looks)} looks, {len(options)} options, {len(profiles)} profiles; no hardware/runtime behavior tested")
        return 0
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
