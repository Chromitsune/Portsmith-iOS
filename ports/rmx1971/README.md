# Realme 5 Pro (`rmx1971`)

**Upstream source:** [https://github.com/AppleCampus/UniXNU-rmx1971@`e0c2df8bedf4292066372aa325c2ead0db02d1c5`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `rmx1971`
- **SoC:** `SDM710`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root GPL v2 text does not state its scope clearly; do not reuse without maintainer clarification.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/AppleCampus/UniXNU-rmx1971/blob/e0c2df8bedf4292066372aa325c2ead0db02d1c5/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | docs/bring-up.md reports U-Boot, UniXNU menu, DarwinBoot entry, and kernel panel, but root mount is in progress. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Reported working (upstream) | docs/bring-up.md reports readable kernel boot-progress/console output on panel. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Reported unavailable | README.md reports USB gadget fastboot never enumerates; flashing must use ABL. |
| Storage | Partial / limited | README.md says UFS host works, but root-device mounting is in progress and first hardware root run is pending. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
