# Xiaomi Pad 6S Pro (Lithosss) (`sheng-lithosss`)

**Upstream source:** [https://github.com/Lithosss/UniXNU-sheng@`429956ec5e44aaefca5c95d7c565b03d2b0c140c`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, AdrenoMetal
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Lithosss/UniXNU-sheng/blob/429956ec5e44aaefca5c95d7c565b03d2b0c140c/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | No device boot result is cited for this pin. SOURCE/HOST ONLY, not device-verified: porting.toml [area firmware]. |
| GPU | Partial / limited | Device log reports GPU mapping and idle frame measurements, with a refused WidgetRenderer command buffer. Device evidence: scripts/read-sheng-log.py. |
| Display | Work in progress / incomplete | Display source/configuration is recorded without a device display result. SOURCE ONLY, not device-verified: porting.toml [area display]. |
| Touch & Buttons | Work in progress / incomplete | Input source and host models are cited; no device input result is cited. HOST/SOURCE ONLY, not device-verified: porting.toml [area input]. |
| Audio | Reported working (upstream) | Device evidence reports speaker playback and microphone capture. Device evidence: scripts/read-sheng-log.py. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Device evidence reports WPA2 association, DHCP and traffic. Device evidence: scripts/read-sheng-log.py. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Charging and CPU/GPU frequency telemetry reported; sleep/wake is not established. Device evidence: scripts/read-sheng-log.py. |
| Camera & Sensors | Partial / limited | Temperature/power telemetry reported; no camera result is cited. Device evidence: scripts/read-sheng-log.py. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Storage source/host checks are cited; no device storage result is cited. HOST/SOURCE ONLY, not device-verified: porting.toml [area storage]. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
