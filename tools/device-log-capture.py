#!/usr/bin/env python3
"""Normalize an already-acquired log into ignored logs/ with a provenance manifest.

This tool reads a local file or stdin only. It never invokes adb, fastboot, a serial
console, a recovery reader, or any device command. Acquire logs using the exact,
read-only method documented by the relevant port, then ingest the capture here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "logs"
SLUG = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{0,79}$")
SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")
TRANSPORTS = (
    "adb-logcat", "adb-pull", "recovery-adb", "uart", "usb-cdc",
    "ramoops", "persistent-log-reader", "port-reader", "qemu", "existing-log", "other",
)
EVIDENCE = ("device", "host", "upstream_report", "inference")


def safe_name(value: str, what: str) -> str:
    if not SLUG.fullmatch(value) or value in {".", ".."}:
        raise ValueError(f"unsafe {what}: {value!r}")
    return value


def copy_and_hash(source: str, destination: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    with destination.open("xb") as out:
        inp = sys.stdin.buffer if source == "-" else Path(source).open("rb")
        try:
            while True:
                block = inp.read(1024 * 1024)
                if not block:
                    break
                out.write(block)
                digest.update(block)
                size += len(block)
        finally:
            if source != "-":
                inp.close()
    return size, digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True, help="Portsmith port/profile ID; no device serial/ECID")
    parser.add_argument("--transport", required=True, choices=TRANSPORTS,
                        help="how the already-acquired data was read")
    parser.add_argument("--evidence-level", required=True, choices=EVIDENCE,
                        help="device, host/QEMU, upstream report, or inference")
    parser.add_argument("--input", required=True, help="local log file, or '-' to read stdin")
    parser.add_argument("--label", default="capture.log", help="safe local filename for the raw capture")
    parser.add_argument("--source-revision", help="exact source commit, if known")
    parser.add_argument("--image-sha256", help="image/payload SHA-256 (64 hex chars), if known")
    parser.add_argument("--state-before", default="unspecified",
                        help="sanitized pre-capture state, e.g. 'Android already running'")
    parser.add_argument("--source-range", default="", help="documented byte/block range, if applicable")
    parser.add_argument("--log-format", default="", help="reader/decoder format and version, if known")
    parser.add_argument("--command-redacted", default="",
                        help="sanitized read command; omit serials, account names and secrets")
    parser.add_argument("--notes", default="", help="sanitized capture caveats; do not include private log contents")
    parser.add_argument("--run-id", help="unique safe directory name; defaults to UTC timestamp")
    args = parser.parse_args()

    try:
        port = safe_name(args.port, "port ID")
        label = safe_name(args.label, "capture label")
        if args.run_id:
            run_id = safe_name(args.run_id, "run ID")
        else:
            run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        if args.image_sha256 and not SHA256.fullmatch(args.image_sha256):
            raise ValueError("--image-sha256 must be 64 hexadecimal characters")
        if args.input != "-" and not Path(args.input).is_file():
            raise ValueError(f"input is not a regular file: {args.input}")
        if args.transport == "qemu" and args.evidence_level != "host":
            raise ValueError("QEMU output must be labelled --evidence-level host")
        if args.evidence_level == "upstream_report" and not args.source_revision:
            raise ValueError("upstream reports require --source-revision")

        run_dir = LOGS / port / run_id
        raw_dir = run_dir / "raw"
        raw_dir.mkdir(parents=True, exist_ok=False)
        raw_path = raw_dir / label
        size, digest = copy_and_hash(args.input, raw_path)
        manifest = {
            "schema_version": 1,
            "port": port,
            "run_id": run_id,
            "captured_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "transport": args.transport,
            "evidence_level": args.evidence_level,
            "source_revision": args.source_revision or None,
            "image_sha256": args.image_sha256.lower() if args.image_sha256 else None,
            "device_state_before": args.state_before,
            "source_range": args.source_range,
            "log_format": args.log_format,
            "command_redacted": args.command_redacted,
            "notes": args.notes,
            "files": [{"path": f"raw/{label}", "size_bytes": size, "sha256": digest}],
        }
        (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"Captured {size} bytes to {raw_path.relative_to(ROOT)}")
        print(f"SHA-256 {digest}")
        print(f"Metadata { (run_dir / 'manifest.json').relative_to(ROOT) }")
        return 0
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
