# Xiaomi Pad 6S Pro (airalex002) (`sheng-airalex002`)

**Upstream source:** [https://github.com/airalex002/UniXNU-sheng@`f3640f52db3a97a9ea3f1675fe51700754b2ed02`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, AdrenoMetal
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/airalex002/UniXNU-sheng/blob/f3640f52db3a97a9ea3f1675fe51700754b2ed02/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | reports/ipados26-source-storage-runtime.json says new_device_boot=false; build/source evidence is not device boot evidence. |
| GPU | Partial / limited | porting.toml cites device GPU samples: 1024 MiB pool/zero fallbacks and 130 fps idle, but a WidgetRenderer command buffer was refused. |
| Display | Work in progress / incomplete | README.md describes display integration, but source-storage-runtime report says no new device boot and Display/Metal remain at unsupported iOS 26 ABI boundary. |
| Touch & Buttons | Work in progress / incomplete | reports/ipados26-source-drivers.json records host ASan/UBSan tests for input source; no device input result. |
| Audio | Reported working (upstream) | porting.toml cites device playback/recording traces with returned periods and no late periods; prior run, not a new boot of this candidate. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | porting.toml cites WPA2 association, DHCP, and measured transfers on-device; not a new boot of this candidate. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | porting.toml cites battery/charging/temperature readings; no sleep/resume result. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | reports/ipados26-source-storage-runtime.json records new_device_boot=false and unresolved storage ABI work; source implementation is not device storage operation. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
