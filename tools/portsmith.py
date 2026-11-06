#!/usr/bin/env python3
"""Read-only Portsmith workspace inventory, pin validation, and host-tool check."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import textwrap
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_toml(path: Path) -> dict:
    with path.open("rb") as f:
        return tomllib.load(f)


def git(*args: str, cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=cwd, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=check,
    )


def norm_url(url: str) -> str:
    return url.removesuffix(".git").rstrip("/")


def port_records(root: Path = ROOT) -> list[tuple[Path, dict]]:
    out = []
    for path in sorted((root / "ports").glob("*/port.toml")):
        out.append((path, read_toml(path)))
    return out


def port_section(data: dict) -> dict:
    return data.get("port", {})


def cmd_ports(args: argparse.Namespace) -> int:
    records = port_records()
    if not records:
        print("No port.toml files found.")
        return 0
    print("Port catalog (status is upstream-reported, not independently verified)")
    field = {"vendor": "vendor", "soc": "soc", "storage": "storage", "gpu": "gpu_family", "bootloader": "boot_family"}.get(args.group_by)
    if field:
        groups: dict[str, list[tuple[Path, dict]]] = {}
        for path, data in records:
            p = port_section(data)
            group = p.get("soc", "Unknown") if args.group_by == "soc" else data.get("hardware", {}).get(field, "Unknown")
            groups.setdefault(group, []).append((path, data))
        for group, items in sorted(groups.items(), key=lambda item: item[0].casefold()):
            print(f"\n## {args.group_by}: {group}")
            for path, data in items:
                _print_port(path, data)
    else:
        for path, p in records:
            _print_port(path, p)
    return 0


def _print_port(path: Path, data: dict) -> None:
    p = port_section(data)
    name = p.get("name", path.parent.name)
    device = p.get("model", "?")
    soc = p.get("soc", "?")
    status = p.get("status", "status not recorded")
    print(f"- {name}: {device} ({soc})")
    print(textwrap.fill(f"Status: {status}", width=100, subsequent_indent="  "))


def source_index(root: Path = ROOT) -> dict[str, dict]:
    data = read_toml(root / "sources/manifest.toml")
    return {s["path"]: s for s in data.get("source", [])}


def gitlink_oid(path: str) -> tuple[str | None, str | None]:
    result = git("ls-files", "-s", "--", path, check=False)
    if result.returncode:
        return None, result.stderr.strip()
    for line in result.stdout.splitlines():
        meta, sep, name = line.partition("\t")
        fields = meta.split()
        if sep and name == path and len(fields) >= 3 and fields[0] == "160000":
            return fields[1], None
    return None, None


def submodule_url(path: str) -> str | None:
    result = git("config", "-f", ".gitmodules", "--get", f"submodule.{path}.url", check=False)
    return result.stdout.strip() if result.returncode == 0 else None



def license_matches(path: Path, spdx: str | None) -> bool:
    if not spdx:
        return True
    text = path.read_text(errors="replace")
    if spdx == "MIT":
        return "MIT License" in text or "Permission is hereby granted, free of charge" in text
    if spdx == "Apache-2.0":
        return "Apache License" in text and "Version 2.0" in text
    if spdx == "BSD-2-Clause-Patent":
        return "BSD-2-Clause-Patent" in text or "patent license" in text.lower()
    if spdx == "BSD-2-Clause":
        return "BSD 2-Clause License" in text or "BSD-2-Clause" in text or "Redistribution and use in source and binary forms" in text
    return True

def cmd_sources(_: argparse.Namespace) -> int:
    failures = 0
    print(f"{'PATH':40} {'PIN':12} {'KIND':18} UPSTREAM")
    print("-" * 125)
    for path, item in source_index().items():
        expected = item.get("revision", "?")
        mode = item.get("source_mode", "submodule")
        upstream = item.get("upstream", "?")
        if mode == "vendored-snapshot":
            pin, state = expected[:12], "snapshot"
            full = ROOT / path
            if not (full / "README.md").is_file():
                state = "snapshot?"
                failures += 1
            elif item.get("license_file") and not (full / item["license_file"]).is_file():
                state = "license-missing"
                failures += 1
            elif item.get("license_file") and not license_matches(full / item["license_file"], item.get("license")):
                state = "license-mismatch"
                failures += 1
            elif item.get("upstream_file") and not (full / item["upstream_file"]).is_file():
                state = "provenance-missing"
                failures += 1
            elif item.get("upstream_file"):
                provenance = read_toml(full / item["upstream_file"]).get("upstream", {})
                if provenance.get("revision") != expected or norm_url(provenance.get("repository", "")) != norm_url(upstream):
                    state = "provenance-mismatch"
                    failures += 1
        else:
            oid, _ = gitlink_oid(path)
            pin = (oid or "not-pinned")[:12]
            if oid != expected:
                state = "pin-mismatch"
                failures += 1
            else:
                state = "submodule"
        print(f"{path:40} {pin:12} {state:18} {upstream}")
    return 1 if failures else 0


def cmd_check(_: argparse.Namespace) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    ports = port_records()
    if not ports:
        errors.append("no ports/*/port.toml manifests found")
    required_port = {"name", "model", "codename", "soc", "source", "status"}
    for file, data in ports:
        p = port_section(data)
        missing = sorted(required_port - p.keys())
        if missing:
            errors.append(f"{file.relative_to(ROOT)} missing [port] fields: {', '.join(missing)}")
        source_path = p.get("source")
        if source_path and not (ROOT / source_path).exists():
            errors.append(f"{file.relative_to(ROOT)} source path does not exist: {source_path}")

    for path, item in source_index().items():
        full = ROOT / path
        if not full.exists():
            errors.append(f"source path missing: {path}")
            continue
        expected = item.get("revision")
        mode = item.get("source_mode", "submodule")
        if mode == "vendored-snapshot":
            if not expected:
                errors.append(f"{path}: snapshot has no recorded revision")
            if not (full / "README.md").is_file():
                errors.append(f"{path}: vendored snapshot is missing README.md")
            if not (full / "NOTICE.md").is_file() and not (full / "LICENSE").is_file():
                warnings.append(f"{path}: no top-level NOTICE.md or LICENSE; review per-component licenses")
            if item.get("license_file"):
                license_path = full / item["license_file"]
                if not license_path.is_file():
                    errors.append(f"{path}: recorded license file is missing: {item['license_file']}")
                elif not license_matches(license_path, item.get("license")):
                    errors.append(f"{path}: license file does not match manifest license {item.get('license')}")
            if item.get("upstream_file"):
                provenance_path = full / item["upstream_file"]
                if not provenance_path.is_file():
                    errors.append(f"{path}: upstream provenance metadata is missing: {item['upstream_file']}")
                else:
                    provenance = read_toml(provenance_path).get("upstream", {})
                    if provenance.get("revision") != expected:
                        errors.append(f"{path}: UPSTREAM revision does not match manifest pin")
                    if norm_url(provenance.get("repository", "")) != norm_url(item.get("upstream", "")):
                        errors.append(f"{path}: UPSTREAM repository does not match source manifest")
                    if provenance.get("license") != item.get("license"):
                        errors.append(f"{path}: UPSTREAM license does not match source manifest")
            continue

        oid, _ = gitlink_oid(path)
        if oid is None:
            errors.append(f"{path}: manifest expects a submodule, but the Git index has no gitlink")
            continue
        if expected and oid != expected:
            errors.append(f"{path}: manifest revision {expected} != Git submodule pin {oid}")
        url = submodule_url(path)
        upstream = item.get("upstream")
        if url and upstream and norm_url(url) != norm_url(upstream):
            warnings.append(f"{path}: .gitmodules URL is {url}, manifest upstream is {upstream}")
        marker = full / ".git"
        if not marker.exists():
            warnings.append(f"{path}: submodule is not initialized locally (run git submodule update --init --recursive)")
        else:
            head = git("rev-parse", "HEAD", cwd=full, check=False)
            if head.returncode == 0 and head.stdout.strip() != oid:
                errors.append(f"{path}: checkout {head.stdout.strip()} != pinned gitlink {oid}")
            dirty = git("status", "--porcelain", cwd=full, check=False)
            if dirty.stdout.strip():
                warnings.append(f"{path}: submodule has local modifications")

    port_ids = {port_section(data).get("name", file.parent.name) for file, data in ports}
    for c in component_records():
        if not c.get("id") or not c.get("category"):
            errors.append("components/manifest.toml: each component needs id and category")
        missing = sorted(set(c.get("ports", [])) - port_ids)
        if missing:
            errors.append(f"component {c.get('id', '?')}: unknown port ids: {', '.join(missing)}")
        for ref in c.get("source_paths", []):
            if not (ROOT / ref).exists():
                errors.append(f"component {c.get('id', '?')}: missing source reference {ref}")

    for message in warnings:
        print(f"WARN: {message}", file=sys.stderr)
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: {len(ports)} port manifests and {len(source_index())} source pins checked")
    return 0


def component_records(root: Path = ROOT) -> list[dict]:
    records = read_toml(root / "components/manifest.toml").get("component", [])
    imported = root / "components/imported.toml"
    if imported.is_file():
        records.extend(read_toml(imported).get("component", []))
    return records


def cmd_components(_: argparse.Namespace) -> int:
    ports = {port_section(p).get("name", path.parent.name) for path, p in port_records()}
    for c in component_records():
        missing = sorted(set(c.get("ports", [])) - ports)
        print(f"{c.get('id', '?')} [{c.get('category', '?')}] — {c.get('media', '?')}")
        print(f"  ports: {', '.join(c.get('ports', [])) or 'none'}")
        print(textwrap.fill(c.get("status", "status not recorded"), width=100, initial_indent="  ", subsequent_indent="  "))
        if missing:
            print(f"  WARN: unknown port ids in catalog: {', '.join(missing)}")
        upstream = c.get("upstream_repository")
        if upstream:
            print(f"  source: {upstream}@{c.get('revision', '?')} | license: {c.get('license', 'unknown')}")
        selected = c.get("upstream_selected_by", [])
        if selected:
            print(f"  upstream selected by: {', '.join(selected)} (not Portsmith verification)")
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    """Report host tools only; does not probe or control a phone."""
    required = ("git", "python3")
    optional = ("cargo", "tmux", "adb", "fastboot", "clang", "mtools")
    missing_required = []
    for name in required + optional:
        path = shutil.which(name)
        label = "required" if name in required else "optional"
        if path is None:
            print(f"{name:10} not found ({label})")
            if name in required:
                missing_required.append(name)
            continue
        if name == "cargo":
            version = subprocess.run([path, "--version"], text=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, check=False)
            detail = version.stdout.strip() if version.returncode == 0 else "Rust toolchain not configured"
        else:
            detail = path
        print(f"{name:10} {detail} ({label})")
    return 1 if missing_required else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, func, help_text in (
        ("ports", cmd_ports, "list ports, optionally grouped by hardware family"),
        ("sources", cmd_sources, "show pinned source revisions and upstream URLs"),
        ("components", cmd_components, "list shared component families and compatible ports"),
        ("check", cmd_check, "validate manifests, source pins, component references, and local checkouts"),
        ("doctor", cmd_doctor, "check host tools only; never probes a device"),
    ):
        p = sub.add_parser(name, help=help_text)
        if name == "ports":
            p.add_argument("--group-by", choices=("vendor", "soc", "storage", "gpu", "bootloader"),
                           help="group port manifests by a hardware field")
        p.set_defaults(func=func)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
