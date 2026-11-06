# Xiaomi Mi 10 standalone UniXNU bring-up (JopangJovan) (`umi-jopangjovan`)

**Upstream source:** [https://github.com/JopangJovan/UniXNU-umi@`cc1cdff2ef87ff4d1c346f9f6eea2f4ef9b26442`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `umi`
- **SoC:** `SM8250`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/JopangJovan/UniXNU-umi/blob/cc1cdff2ef87ff4d1c346f9f6eea2f4ef9b26442/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Reduced UEFI reaches the UniXNU menu on hardware; XNU device handoff is explicitly unverified. Device evidence: README.md; BRINGUP.md. |
| GPU | Work in progress / incomplete | Adreno 650 adaptation is still required; no device GPU result. SOURCE ONLY, not device-verified: README.md; porting.toml [area gpu]. |
| Display | Partial / limited | UEFI menu is shown on hardware, but no XNU display result. Device evidence: README.md. |
| Touch & Buttons | Work in progress / incomplete | Touch still requires adaptation; no UniXNU hardware input result. SOURCE ONLY, not device-verified: README.md; porting.toml [area input]. |
| Audio | Work in progress / incomplete | Audio adaptation is still required; no device playback/capture result. SOURCE ONLY, not device-verified: README.md; porting.toml [area audio]. |
| Bluetooth | Work in progress / incomplete | Bluetooth adaptation is still required; no device result. SOURCE ONLY, not device-verified: README.md; porting.toml [area network]. |
| Wi-Fi | Work in progress / incomplete | Wi-Fi adaptation is still required; no device networking result. SOURCE ONLY, not device-verified: README.md; porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | Battery/brightness and power adaptation are still required; no device power/sleep test. SOURCE ONLY, not device-verified: README.md; porting.toml [area power]. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | README says native UFS still requires adaptation; source/bring-up only, no XNU device storage test. SOURCE ONLY, not device-verified: README.md; porting.toml [area storage]. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
