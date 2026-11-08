---
name: device-log-triage
description: Retrieve and analyze existing boot logs without causing another boot, reset, or write.
---

# Device log triage

1. Inspect the screen and enumerate ADB/fastboot read-only before acting. Confirm product/codename and transport state; do not confuse `offline`, `unauthorized`, recovery ADB, ABL fastboot, or no enumeration.
2. Prefer existing logs, recovery ADB reads, or an ESP image already captured. Do not reboot or flash merely to make a log tool connect. Ask the owner to inspect or change the physical state when needed.
3. Read only the documented partition/range and record the exact byte count. Never write `LOGFS`, guessed blocks, or unknown BCB fields. Keep device dumps, serials, ECIDs, and firmware out of Git.
4. Preserve raw evidence separately from decoded output. A locator/header is not the log payload; a missing log may indicate lost/overwritten RAM, no console bytes, or an archive-path failure. Do not claim which without evidence.
5. Symbolize against the exact kernel/image revision and record any slide assumptions. Keep upstream reports, host tests, and device observations separate.
6. If a new hardware run is necessary, document the target, exact image hashes, partition writes, recovery path, and explicit current authorization before performing it.
