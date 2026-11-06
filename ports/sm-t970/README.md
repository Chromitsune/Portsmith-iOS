# Samsung Galaxy Tab S7+ Wi-Fi (SM-T970, gts7xlwifi), single-core platform bootstrap (`sm-t970`)

**Upstream source:** [https://github.com/CakeAL/UniXNU-sm-t970@`37b439d75ded02edf01c0ed7f357ba0f746a811d`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sm-t970`
- **SoC:** `SM8250`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, VirtioMmioBlock, RamBlock, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/CakeAL/UniXNU-sm-t970/blob/37b439d75ded02edf01c0ed7f357ba0f746a811d/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device reached launchd main and later reported SpringBoard/runningboardd processes; other image runs stopped with SIGTRAP and desktop interaction is unverified. Evidence: README.md; evidence/storage/watchdogd/runtime-report/README.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Partial / limited | GOP Hello/display output is reported, but no desktop/frame presentation is established; one display-enabled run stopped at BootProgress. Evidence: README.md; evidence/display/springboard-dim-continuous-v69/README.md. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | Device UFS/DMA/root reads and APFS/Data mount checkpoints are reported, but persistence and actual Data operations remain unqualified. Evidence: README.md; evidence/storage/root-restore-twrp-20261102/README.md; evidence/storage/data-seed-preparation/README.md. |
| Stability | Partial / limited | A 60-second run had SpringBoard/runningboardd but no observed backboardd; other runs SIGTRAP or black-screened. Sustained stability is explicitly pending. Evidence: README.md; evidence/display/springboard-dim-continuous-v69/README.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
