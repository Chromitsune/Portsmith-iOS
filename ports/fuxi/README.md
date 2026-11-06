# Xiaomi 13 (fuxi) (`fuxi`)

**Upstream source:** [https://github.com/matejkoo217/UniXNU-fuxi@`b76a1679433b0ab5386ac9957715f5e3fecdf46e`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, AdrenoMetal
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/matejkoo217/UniXNU-fuxi/blob/b76a1679433b0ab5386ac9957715f5e3fecdf46e/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device-side network/audio/GPU logs demonstrate the OS ran on the recorded board; no full boot qualification is asserted here. See porting.toml, device evidence under network/audio. |
| GPU | Partial / limited | Device logs record GPU activity, but a WidgetRenderer command buffer was refused; see porting.toml, GPU evidence (scripts/read-sheng-log.py). |
| Display | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Reported working (upstream) | Device logs record speaker playback and capture periods; see porting.toml, audio evidence (scripts/read-sheng-log.py). |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Device log records WPA2 association, DHCP and throughput; see porting.toml, network evidence (scripts/read-sheng-log.py). |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Device charging and CPU/GPU governor measurements are recorded; no suspend/resume result is established. See porting.toml, power evidence (scripts/read-sheng-log.py). |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
