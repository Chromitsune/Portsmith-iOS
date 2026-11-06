# Xiaomi Mi 8 SE (dddqmmx) (`sirius-dddqmmx`)

**Upstream source:** [https://github.com/dddqmmx/UniXNU-sirius@`b0e8023540f212625bd86a32a8bb512b410b59ed`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sirius`
- **SoC:** `SDM710`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, GopFramebuffer, AppleKeyStoreState, ShengHidInput
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/dddqmmx/UniXNU-sirius/blob/b0e8023540f212625bd86a32a8bb512b410b59ed/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device reaches APFS mounts, bsd_init and launchd exec, then stalls after storage traffic stops; not a complete usable boot. Device evidence: docs/HANDOFF.zh-CN.md. |
| GPU | Partial / limited | GMU/HFI initialization and GX power-on were observed; rendering is not qualified. Device evidence: docs/evidence/sirius-gpu-20261029-gmu.log. |
| Display | Partial / limited | GOP boot-progress console works; README distinguishes it from a Darwin display driver. Evidence: docs/HANDOFF.zh-CN.md; README.md. |
| Touch & Buttons | Partial / limited | A cited historical device run reports Setup reacting to physical touch; other runs did not establish a working event path. Device evidence: docs/evidence/sirius-touch-hid-20261029-combined.log. |
| Audio | Reported unavailable | No audio support at any layer is stated in the record; source statement, not a device test. SOURCE ONLY: porting.toml [area audio]. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | No network support at any layer is stated in the record; source statement, not a device test. SOURCE ONLY: porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Partial / limited | DWC3 CDC-ACM console captured on hardware; broader USB support not established. Device evidence: docs/evidence/sirius-usb-console-20261026-1605.log. |
| Storage | Partial / limited | eMMC reads/GPT/APFS root and launchd exec are reported, but the run ends waiting beyond storage. Device evidence: docs/HANDOFF.zh-CN.md. |
| Stability | Partial / limited | Device boot reaches launchd but stalls after storage activity; no stable usable userland result. Device evidence: docs/HANDOFF.zh-CN.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
