---
name: device-log-triage
description: Acquire and interpret existing device logs without an unnecessary reset/write; normalize local captures with a provenance manifest.
---

# Device log triage

Use this skill for logs from Android, recovery, UEFI, XNU, UART/USB CDC, ramoops/pstore, persistent boot-log windows, or QEMU. It is a workflow, not a universal reader for every board.

## Inputs to establish

- Exact Portsmith profile/source commit and intended image/payload hash, if known.
- Current device state as observed by the owner or already-recorded session: Android, recovery, bootloader, UEFI, XNU, powered off, etc. Do not infer state from transport enumeration alone.
- Existing log paths, capture date/run ID, transport, and whether the relevant log survives the current state.
- The port's local `AGENTS.md`, log writer/reader/decoder documentation, range and format. Search for default reboot/reset behavior before invoking any helper.

## Acquisition order

1. Check prior host artifacts and saved logs first. Preserve originals; decode/symbolize a copy.
2. Choose the least disruptive transport that can contain the needed evidence. Prefer an already-running authorized ADB session or an already-streaming serial/CDC console over rebooting or booting a reader image.
3. Use only the exact port's documented reader and bounded range. Do not guess partition offsets, read a whole partition as a shortcut, write LOGFS, clear logcat, or treat a stale/header-only ring as a complete log.
4. Distinguish the read from the state change. `adb logcat -d`/`adb pull` from an already available session can be read-only; `adb reboot recovery`, booting a helper/reader image, console reset commands, automatic `rebootbl`, and temporary files written on the device change state or storage. Inspect scripts before use. Any required reboot/boot/reset/write needs current explicit user authorization.
5. For a pipe or local file already obtained by a reviewed read-only method, use `python3 tools/device-log-capture.py`. It only reads local input/stdin; it never contacts a device. Store captures under ignored `logs/<port>/<run-id>/`.

Example (only for an already-running Android session with authorized ADB; redact the actual serial in metadata):

```sh
adb -s "$SERIAL" logcat -b all -d -v threadtime \
  | python3 tools/device-log-capture.py \
      --port <port-id> --transport adb-logcat --evidence-level device \
      --input - --label android-logcat.txt \
      --source-revision <exact-source-commit> \
      --command-redacted 'adb -s <redacted> logcat -b all -d -v threadtime' \
      --state-before 'Android already running'
```

ADB `logcat` is Android userspace logging, not XNU kernel logging. For XNU logs, identify the exact port's USB/UART stream, pstore/ramoops, boot-log ring, or persistent reader and decoder. The capture tool does not choose or run the transport.

## Preserve and report

- Keep the raw capture unchanged. Record byte count, SHA-256, UTC time, port/source commit, image hash, transport, redacted command, pre-capture state, range/format and evidence level in the generated manifest.
- Decode to a separate file and document tool version, symbol source/slide assumptions, truncation, missing header, overwrite or retrieval errors. A missing capture does not by itself prove a crash.
- Label QEMU/host output `host`; only actual device captures may be labeled `device`. Upstream logs/reports remain upstream evidence.
- Keep sensitive logs, serials, ECIDs, keys, private rootfs data, firmware and full device dumps out of Git. Commit only sanitized evidence summaries/excerpts after review.
- Do not reset or rerun the device just because an initial log is incomplete. First check transport, writer, ring retention and decode assumptions. If a new run is truly needed, stop and request explicit current authorization with target, image hashes, state transition, writes, and recovery plan.
