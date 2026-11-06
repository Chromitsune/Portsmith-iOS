# Redmi K60 (mondrian/SM8475): UniXNU UEFI bring-up (mzyxsl) (`mondrian-mzyxsl`)

**Upstream source:** [https://github.com/mzyxsl/UniXNU-mondrian@`76552b88441757defce4080a241c2f0ea7464538`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `mondrian`
- **SoC:** `SM8475`
- **OS profile:** `ipados-16.6.1-20G81`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, PongUfs
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/mzyxsl/UniXNU-mondrian/blob/76552b88441757defce4080a241c2f0ea7464538/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | README_EN.md reports ABL/fastboot/UEFI menu and trampoline bar, but no XNU-side log. |
| GPU | Reported unavailable | README_EN.md says Adreno implementation is disabled by board config; no device GPU result. |
| Display | Work in progress / incomplete | README_EN.md describes native canvas/IOAccelerator stub and first-frame log, but no device display confirmation. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | README_EN.md describes UFS/GPT/SHNGROOT read-path source, but persistent storage is not device-qualified. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
