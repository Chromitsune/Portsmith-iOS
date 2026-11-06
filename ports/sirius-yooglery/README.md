# Xiaomi Mi 8 SE (Yooglery) (`sirius-yooglery`)

**Upstream source:** [https://github.com/Yooglery/UniXNU-sirius@`528fac52a751bb2b4c7f24574b8c890229f73ce2`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sirius`
- **SoC:** `SDM710`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Yooglery/UniXNU-sirius/blob/528fac52a751bb2b4c7f24574b8c890229f73ce2/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device evidence reaches APFS/launchd but records the boot waiting beyond completed storage I/O. Device evidence: docs/HANDOFF.zh-CN.md. |
| GPU | Partial / limited | GMU/HFI initialization reported in the cited hardware log; full rendering is not qualified. Device evidence: docs/evidence/sirius-gpu-20261029-gmu.log. |
| Display | Partial / limited | GOP boot-progress console is reported, not a Darwin display driver. Evidence: docs/HANDOFF.zh-CN.md; README.md. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Reported unavailable | No audio support at any layer stated in the record; source-only, not device-tested. Evidence: porting.toml [area audio]. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | No network support at any layer stated in the record; source-only, not device-tested. Evidence: porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Partial / limited | Hardware DWC3 CDC-ACM console capture reported; no broader USB compatibility result. Device evidence: docs/evidence/sirius-usb-console-20261026-1605.log. |
| Storage | Partial / limited | Bounded eMMC/GPT/APFS root operations are reported; boot subsequently waits beyond storage. Device evidence: docs/HANDOFF.zh-CN.md. |
| Stability | Partial / limited | Boot does not establish completed/stable userland. Device evidence: docs/HANDOFF.zh-CN.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
