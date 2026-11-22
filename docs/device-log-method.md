# Canonical device-log collection method

This is the shared workflow referenced by the root [`AGENTS.md`](../AGENTS.md) and [`device-log-triage` skill](../skills/device-log-triage/SKILL.md). It standardizes evidence handling; it does not pretend different device transports or boot-log formats are interchangeable.

## Acquisition order

1. Inspect existing host artifacts, issue notes and prior logs first. Preserve the original; decode or symbolize a copy.
2. Identify the exact device/port, source and image revisions, current observed state and transport. Never infer a phone is powered off/unresponsive solely because it is not enumerated.
3. Choose the least disruptive already-available transport that covers the needed boot stage. Use the port's exact reader/decoder and documented range.
4. Do not reboot to recovery, boot a reader image, send console commands, clear logs, or trigger a reset just to make collection easier without current explicit authorization. Reading a source partition into a temporary device file is still a device write and must be recorded.
5. Keep raw bytes and decoded text separate. Record size, SHA-256, capture command (redacted), transport, device state, source revision, image hash, log range/format and evidence level.
6. Keep raw device logs under the ignored `logs/` directory. Do not commit serials, ECIDs, credentials, firmware, personal data, full rootfs/device dumps or private logs. Commit only sanitized summaries with approved, minimal evidence excerpts.

## Transport decision table

| Existing source | Typical read path | Caveat |
|---|---|---|
| Android already running | Authorized ADB; e.g. `adb logcat -b all -d -v threadtime` | Android userspace logcat is not XNU kernel logging. Avoid `logcat -c`. |
| Recovery already running | Documented `adb pull` or bounded read-only port reader | `adb reboot recovery` changes state. Do not use a broad partition dump instead of the documented range. |
| UART / USB CDC already streaming | Passive serial capture using the port's pins, baud/protocol and exact port | Do not send shell, reset or bootloader commands as part of capture. |
| Retained RAM, ramoops, pstore | Read with the exact port's reader after verifying the region/format | Retention depends on configuration and reset type; do not generalize addresses or reset semantics. |
| Persistent boot-log window | Port-owned bounded reader + matching decoder | Confirm writer actually ran; a reader's existence does not prove a log was written. Inspect script defaults for reboot side effects. |
| QEMU | Host-generated serial log/framebuffer | Label `host`, not device evidence. Some runners delete an existing output path; choose a new output path. |

## Normalize an acquired file

`tools/device-log-capture.py` **only reads a local file or stdin**; it does not run ADB/fastboot/serial commands. Example for a device that is already running and has an authorized ADB session:

```sh
adb -s "$SERIAL" logcat -b all -d -v threadtime \
  | python3 tools/device-log-capture.py \
      --port <port-id> --transport adb-logcat --evidence-level device \
      --input - --label android-logcat.txt \
      --source-revision <exact-source-commit> \
      --command-redacted 'adb -s <redacted> logcat -b all -d -v threadtime' \
      --state-before 'Android already running'
```

The tool writes `logs/<port-id>/<UTC-run-id>/raw/` and a `manifest.json` with hashes and sanitized metadata. Review raw content locally; it may contain private information. For a port-specific kernel ring, first use that port's documented, reviewed read-only reader—then pass its output file to the same ingestion tool. For QEMU, set `--transport qemu --evidence-level host`.
