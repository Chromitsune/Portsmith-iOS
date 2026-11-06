# Xiaomi Mi 8 SE (sirius) (`sirius`)

**Upstream source:** [https://github.com/57UU/UniXNU-sirius@`f269452c36eceb7f91446fccc4c3bed175aaa98e`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sirius`
- **SoC:** `SDM710`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/57UU/UniXNU-sirius/blob/f269452c36eceb7f91446fccc4c3bed175aaa98e/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device reaches APFS mounts, bsd_init and launchd exec, then stalls after storage traffic stops; not a complete usable boot. Device evidence: docs/HANDOFF.zh-CN.md. |
| GPU | Partial / limited | GMU firmware/HFI initialization and GX power-on were observed on hardware; this is not full GPU rendering qualification. Device evidence: docs/evidence/sirius-gpu-20261029-gmu.log. |
| Display | Partial / limited | GOP boot-progress/console panel is shown; README says this is a firmware framebuffer console, not a Darwin display driver. Evidence: docs/HANDOFF.zh-CN.md; README.md. |
| Touch & Buttons | Partial / limited | A cited historical device run reports Setup reacting to physical touch, but other touch runs did not attach/respond; not a general input pass. Device evidence: docs/evidence/sirius-touch-hid-20261029-combined.log. |
| Audio | Reported unavailable | Record states no audio support at any layer; source/porting statement, not a device test. SOURCE ONLY: porting.toml [area audio]. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | Record states no network support at any layer; source/porting statement, not a device test. SOURCE ONLY: porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Partial / limited | DWC3 CDC-ACM USB console logs were captured on hardware; no general USB data/peripheral support is established. Device evidence: docs/evidence/sirius-usb-console-20261026-1605.log. |
| Storage | Partial / limited | eMMC reads/GPT/APFS root and launchd exec are reported, but the run ends waiting beyond storage. Device evidence: docs/HANDOFF.zh-CN.md. |
| Stability | Partial / limited | Boot reaches launchd but stalls after storage reads stop; userland completion is not established. Device evidence: docs/HANDOFF.zh-CN.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
