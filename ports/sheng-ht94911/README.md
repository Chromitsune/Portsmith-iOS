# Xiaomi Pad 6S Pro (ht94911) (`sheng-ht94911`)

**Upstream source:** [https://github.com/ht94911/UniXNU-sheng@`08cde20edc3254ed6f7df8d0f5384fb887786e8f`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, ShengUfs, VirtioMmioBlock, RamBlock, Adreno740, AdrenoMetal, GopFramebuffer, ShengHidInput, ShengNovatekTouch, QcomGeniSpi, AppleKeyStoreState, XnuPrelink, DarwinBoot, VerifiedRoot, ShengPreflight, AirNir, Ath12kWifi
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/ht94911/UniXNU-sheng/blob/08cde20edc3254ed6f7df8d0f5384fb887786e8f/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | No device boot result is cited for this pin; boot/firmware evidence is source-only. SOURCE ONLY, not device-verified: porting.toml [area firmware]. |
| GPU | Partial / limited | Device log reports idle GPU frame rate and mapping/pool measurements, but a WidgetRenderer command buffer was refused. Device evidence: scripts/read-sheng-log.py. |
| Display | Work in progress / incomplete | Display source implementation is recorded without a device display result. SOURCE ONLY, not device-verified: porting.toml [area display]. |
| Touch & Buttons | Work in progress / incomplete | Input implementation is source-only in this record; no device input result is cited. SOURCE ONLY, not device-verified: porting.toml [area input]. |
| Audio | Reported working (upstream) | Device evidence reports speaker playback and microphone capture. Device evidence: scripts/read-sheng-log.py. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Device evidence reports WPA2 association, DHCP and traffic. Device evidence: scripts/read-sheng-log.py. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Charging and CPU/GPU frequency telemetry reported; sleep/wake is not established. Device evidence: scripts/read-sheng-log.py. |
| Camera & Sensors | Partial / limited | Temperature/power telemetry reported; no camera result is cited. Device evidence: scripts/read-sheng-log.py. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Storage source/configuration is recorded without a device storage result. SOURCE ONLY, not device-verified: porting.toml [area storage]. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
