# Redmi Note 12 Turbo / POCO F5 (marble) (`marble`)

**Upstream source:** [https://github.com/sing0626/UniXNU-marble@`a63260314d130ebf02a987f0785f5ae3258c219c`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `marble`
- **SoC:** `SM7475`
- **OS profile:** `ios-16.7.16-20H392`
- **Catalog-listed components:** not specified
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** LICENSE and LICENSING.md limit MIT to Marble-authored material; XNU/Apple, BearSSL and other upstream code keep their own terms; review file-by-file.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/sing0626/UniXNU-marble/blob/a63260314d130ebf02a987f0785f5ae3258c219c/docs/REAL-DEVICE-TESTS.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device XNU console boot reached IOFindBSDRoot and stopped because the tested console image intentionally has no root; see docs/REAL-DEVICE-TESTS.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Partial / limited | Device console/Apple-logo/Hello observations are limited; broad rendering validation is explicitly missing. See docs/REAL-DEVICE-TESTS.md and README.md. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Current root image/ABI work is host-built and explicitly unverified/no device write; see configs/marble-root_defconfig and docs/REAL-DEVICE-TESTS.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
