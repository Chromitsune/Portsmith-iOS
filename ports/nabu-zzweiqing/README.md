# Xiaomi Pad 5 (zzweiqing) (`nabu-zzweiqing`)

**Upstream source:** [https://github.com/zzweiqing/UniXNU-nabu@`54b4f98457f8e9e232cc0a077c20d08d0b2f0ac9`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `nabu`
- **SoC:** `SM8150`
- **OS profile:** `ipados-17.7-21H16`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, DarwinBoot, XnuPrelink, ShengUfs, RamBlock, VirtioMmioBlock, GopFramebuffer, AppleKeyStoreState
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/zzweiqing/UniXNU-nabu/blob/54b4f98457f8e9e232cc0a077c20d08d0b2f0ac9/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Device record reports DarwinBoot handoff to XNU and captured kernel log; porting.toml firmware evidence, run 7831. |
| GPU | Reported working (upstream) | Device run reports AGXAccelerator/Metal active and 2752/2752 command buffers with GPU-composited UI; porting.toml, run 9048. |
| Display | Reported working (upstream) | Device run reports interactive UI and 1349 completed scanouts, zero fallbacks; porting.toml, run 9048. |
| Touch & Buttons | Partial / limited | Porting record reports interactive UI/navigation on-device (input area, run 9048); buttons not separately qualified. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | README.md explicitly says Wi-Fi is not implemented. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Reported unavailable | README.md says power management is not implemented. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | Device log reports UFS requests and system volume mount before userland, but persistent Data is not implemented (porting.toml; README.md). |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
