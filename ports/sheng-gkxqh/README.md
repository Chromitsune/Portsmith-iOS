# Xiaomi Pad 6S Pro (gkxqh) (`sheng-gkxqh`)

**Upstream source:** [https://github.com/gkxqh/UniXNU-sheng@`7cff07ea9933428e27769014e903f103ab31155d`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, AdrenoMetal
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/gkxqh/UniXNU-sheng/blob/7cff07ea9933428e27769014e903f103ab31155d/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | The cited boot-build report is host-side; it explicitly does not establish kernel/userspace execution. HOST ONLY, not device-verified: reports/ipados26-boot-build.json. |
| GPU | Work in progress / incomplete | Host/source GPU work is recorded, but no device GPU result is cited for this pin. HOST/SOURCE ONLY, not device-verified: porting.toml [area gpu]. |
| Display | Work in progress / incomplete | Display implementation/source is recorded without a device display result. SOURCE ONLY, not device-verified: porting.toml [area display]. |
| Touch & Buttons | Work in progress / incomplete | Input source and host models are cited; no device input result is cited. HOST/SOURCE ONLY, not device-verified: porting.toml [area input]. |
| Audio | Reported working (upstream) | Device evidence reports speaker tone playback and microphone capture, including returned periods. Device evidence: scripts/read-sheng-log.py. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Device evidence reports WPA2 association, DHCP and a traffic test. Device evidence: scripts/read-sheng-log.py. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Charging and CPU/GPU frequency telemetry reported; no sleep/wake result. Device evidence: scripts/read-sheng-log.py. |
| Camera & Sensors | Partial / limited | Temperature/power telemetry reported; no camera result is cited. Device evidence: scripts/read-sheng-log.py. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Storage source and host checks are cited; no device storage result is cited. HOST/SOURCE ONLY, not device-verified: porting.toml [area storage]. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
