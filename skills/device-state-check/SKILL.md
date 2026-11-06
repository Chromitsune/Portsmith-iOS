---
name: device-state-check
description: Inspect a target phone's present state without resetting or writing to it.
---

# Device state check (read-only)

1. Confirm which physical device is connected and ask the user if the identity is uncertain.
2. Observe the screen/state first. Record whether it is powered off, in Android, recovery, fastboot/bootloader, UEFI, or unresponsive.
3. Only then use read-only discovery commands (for example `adb devices -l`, `fastboot devices`, `fastboot getvar ...`). Do not issue `reboot`, `flash`, erase, format, or partition writes.
4. Save exact command output and time; distinguish “not enumerated” from “powered off” or “bricked”—they are not equivalent.
5. If recovery is running, prefer pulling existing logs/backups over causing another failure.
6. Any reset or flash requires explicit, current user authorization and a reviewed restore path.
