# Xiaomi Pad 6S Pro (hxzbaka) (`sheng-hxzbaka`)

**Upstream source:** [https://github.com/hxzbaka/UniXNU-sheng@`0e1f6e52638137db15905db8d775ad73757f39fa`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, ShengUfs, VirtioMmioBlock, RamBlock, Adreno740, AdrenoMetal, GopFramebuffer, ShengHidInput, ShengNovatekTouch, QcomGeniSpi, AppleKeyStoreState, XnuPrelink, DarwinBoot, VerifiedRoot, ShengPreflight, AirNir, Ath12kWifi
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/hxzbaka/UniXNU-sheng/blob/0e1f6e52638137db15905db8d775ad73757f39fa/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | No device boot result is cited for this pin; firmware/source evidence does not verify a boot. SOURCE ONLY, not device-verified: porting.toml [area firmware]. |
| GPU | Work in progress / incomplete | GPU source/configuration is recorded without a device GPU result. SOURCE ONLY, not device-verified: porting.toml [area gpu]. |
| Display | Work in progress / incomplete | Display source/configuration is recorded without a device display result. SOURCE ONLY, not device-verified: porting.toml [area display]. |
| Touch & Buttons | Work in progress / incomplete | Input source/configuration is recorded without a device input result. SOURCE ONLY, not device-verified: porting.toml [area input]. |
| Audio | Work in progress / incomplete | Audio source/configuration is recorded without a device playback/capture result. SOURCE ONLY, not device-verified: porting.toml [area audio]. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Work in progress / incomplete | Network source/configuration is recorded without a device Wi-Fi result. SOURCE ONLY, not device-verified: porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Device log reports charging measurements, including positive battery current on one adapter and discharge on another; no sleep/wake result. Device evidence: scripts/read-sheng-log.py. |
| Camera & Sensors | Partial / limited | Temperature/power telemetry reported; no camera result is cited. Device evidence: scripts/read-sheng-log.py. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Storage source/configuration is recorded without a device storage result. SOURCE ONLY, not device-verified: porting.toml [area storage]. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
