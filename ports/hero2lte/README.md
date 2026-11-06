# Samsung Galaxy S7 Edge (hero2lte) (`hero2lte`)

**Upstream source:** [https://github.com/DokuroMitsukai/UniXNU-hero2lte@`33ca6933fc94aeced28610b9e1fe5743e7f172dd`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `hero2lte`
- **SoC:** `Exynos 8890`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/DokuroMitsukai/UniXNU-hero2lte/blob/33ca6933fc94aeced28610b9e1fe5743e7f172dd/evidence/uefi-bringup-20261026.txt).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Standalone UEFI probe reached its UI; integrated UniXNU payload/hardware boot is not validated. See evidence/uefi-bringup-20261026.txt and porting.toml. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Reported working (upstream) | UEFI logo, missing-OS screen and diagnostic graphics appeared on the device panel; see evidence/uefi-bringup-20261026.txt. |
| Touch & Buttons | Partial / limited | Physical volume/home/power keys were accepted by the UEFI probe; touch is not evidenced. See evidence/uefi-bringup-20261026.txt. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
