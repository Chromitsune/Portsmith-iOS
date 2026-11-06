# Xiaomi Pad 6S Pro (FFT-infra) (`sheng-fft-infra`)

**Upstream source:** [https://github.com/FFT-infra/UniXNU-alioth-sheng-template@`516a780473a2ac59c8b438e132bb60204dda9e22`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, ShengUfs, VirtioMmioBlock, RamBlock, Adreno740, AdrenoMetal, GopFramebuffer, ShengHidInput, ShengNovatekTouch, QcomGeniSpi, AppleKeyStoreState, XnuPrelink, DarwinBoot, VerifiedRoot, ShengPreflight, AirNir, Ath12kWifi
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/FFT-infra/UniXNU-alioth-sheng-template/blob/516a780473a2ac59c8b438e132bb60204dda9e22/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | Source/configuration evidence only; this pinned record has no cited device boot result. SOURCE ONLY, not device-verified: porting.toml [area firmware]. |
| GPU | Work in progress / incomplete | GPU source/configuration area is recorded, but no device GPU result is cited. SOURCE ONLY, not device-verified: porting.toml [area gpu]. |
| Display | Work in progress / incomplete | Display source/configuration area is recorded, but no device display result is cited. SOURCE ONLY, not device-verified: porting.toml [area display]. |
| Touch & Buttons | Work in progress / incomplete | Input source/configuration area is recorded, but no device input result is cited. SOURCE ONLY, not device-verified: porting.toml [area input]. |
| Audio | Work in progress / incomplete | Audio source/configuration area is recorded, but no device playback/capture result is cited. SOURCE ONLY, not device-verified: porting.toml [area audio]. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Work in progress / incomplete | Network source/configuration area is recorded, but no device association/traffic result is cited. SOURCE ONLY, not device-verified: porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | Power source/configuration area is recorded, but no device power or sleep/wake result is cited. SOURCE ONLY, not device-verified: porting.toml [area power]. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Storage source/configuration area is recorded, but no device storage result is cited. SOURCE ONLY, not device-verified: porting.toml [area storage]. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
