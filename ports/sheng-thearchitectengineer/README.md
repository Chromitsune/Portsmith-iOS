# Xiaomi Pad 6S Pro (TheArchitectEngineer) (`sheng-thearchitectengineer`)

**Upstream source:** [https://github.com/TheArchitectEngineer/UniXNU-sheng@`d76556b8909e380961309e970d87b919a74e411e`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, ShengUfs, VirtioMmioBlock, RamBlock, Adreno740, AdrenoMetal, GopFramebuffer, ShengHidInput, ShengNovatekTouch, QcomGeniSpi, AppleKeyStoreState, XnuPrelink, DarwinBoot, VerifiedRoot, ShengPreflight, AirNir, Ath12kWifi
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/TheArchitectEngineer/UniXNU-sheng/blob/d76556b8909e380961309e970d87b919a74e411e/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | No device boot result is cited for this pin. SOURCE ONLY, not device-verified: porting.toml [area firmware]. |
| GPU | Work in progress / incomplete | GPU source/configuration is recorded without a device GPU result. SOURCE ONLY, not device-verified: porting.toml [area gpu]. |
| Display | Work in progress / incomplete | Display source/configuration is recorded without device display evidence. SOURCE ONLY, not device-verified: porting.toml [area display]. |
| Touch & Buttons | Work in progress / incomplete | Input source/configuration is recorded without a device input result. SOURCE ONLY, not device-verified: porting.toml [area input]. |
| Audio | Reported working (upstream) | Device logs report speaker playback and microphone capture. Device evidence: scripts/read-sheng-log.py. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Work in progress / incomplete | Network source/configuration is recorded without device Wi-Fi evidence. SOURCE ONLY, not device-verified: porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Charging/frequency and temperature telemetry reported; no sleep/wake test. Device evidence: scripts/read-sheng-log.py. |
| Camera & Sensors | Partial / limited | Temperature/power telemetry reported; camera not tested. Device evidence: scripts/read-sheng-log.py. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Storage source/configuration is recorded without a device storage result. SOURCE ONLY, not device-verified: porting.toml [area storage]. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
