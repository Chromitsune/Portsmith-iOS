# OnePlus 8T (stevedang67889) (`kebab-stevedang67889`)

**Upstream source:** [https://github.com/stevedang67889/UniXNU-kebab@`62d7738d3be89e271fb9b9c7ae6b8d5042d13a41`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `kebab`
- **SoC:** `SM8250`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/stevedang67889/UniXNU-kebab/blob/62d7738d3be89e271fb9b9c7ae6b8d5042d13a41/docs/bring-up.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device reaches the menu and kernel early logs, but the report has no root marker; see docs/bring-up.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Reported working (upstream) | Menu and firmware/DarwinBoot log render at 1080×2400; see docs/bring-up.md. |
| Touch & Buttons | Reported working (upstream) | Physical-key menu selection and confirmation work; see docs/bring-up.md. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Device log does not reach bsd_init/IOFindBSDRoot/KEBAB UFS marker; root is not confirmed. See docs/bring-up.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
