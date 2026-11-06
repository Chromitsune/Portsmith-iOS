# Xiaomi Mi 11 M2011K2C: single-CPU platform bring-up (`venus`)

**Upstream source:** [https://github.com/Sulee7z/UniXNU-venus@`9b1402a99d9ee37d8aa4a980eceff18a4c993e02`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `venus`
- **SoC:** `SM8350`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, GopFramebuffer, AppleKeyStoreState, ShengHidInput, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Sulee7z/UniXNU-venus/blob/9b1402a99d9ee37d8aa4a980eceff18a4c993e02/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | An exact 012 run reached the system welcome page; later runs include SIGTRAP exits/no UI, so this is not a usable/complete boot qualification. Evidence: README.md; SHENG-CHAIN-010-RESULT.md. |
| GPU | Partial / limited | Device log reports A660 GMU/context, clocks, HFI, GX and client rounds; no frame, desktop or Metal frontend was observed. Device evidence: A660-LIVE-DIAGNOSTICS.md. |
| Display | Partial / limited | Welcome/Hello/BootProgress output is reported, but the display-enabled image did not reach SpringBoard/desktop or present a frame. Device evidence: README.md; LEGACY-MIGRATION.md. |
| Touch & Buttons | Partial / limited | Physical touch worked on historical exact035 image; current later ST-touch image validation is explicitly pending/unverified. Evidence: evidence/touch035-phone.json; TOUCH-015-FIX.md. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | Power/PMGR ABI and QEMU modes are host-verified; no device sleep/charging qualification. HOST ONLY, not device-verified: PMGR-DEPENDENCY.md; porting.toml [area power]. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | Device SystemOS/Data mount and same-boot write succeeded, but a controlled post-restart read returned ENOENT; persistence failed. Device evidence: DATA-QUALIFICATION.md; DATA-PUBLICATION.md. |
| Stability | Partial / limited | Records report repeated SpringBoard SIGTRAP exits and no stable desktop; one historical welcome-page checkpoint is not a stability pass. Device evidence: SHENG-CHAIN-010-RESULT.md; LEGACY-MIGRATION.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
