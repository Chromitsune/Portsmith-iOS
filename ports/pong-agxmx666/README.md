# Nothing Phone (2): UniXNU UEFI bring-up (AGXMX666) (`pong-agxmx666`)

**Upstream source:** [https://github.com/AGXMX666/UniXNU-pong@`ffdad781cb16b42a1fb5c984f77998253b821d8c`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `pong`
- **SoC:** `SM8475`
- **OS profile:** `ipados-18.7.10-22H374`
- **Catalog-listed components:** PongPlatform24
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Notice identifies HackiOS userland with its own license; preserve component-level terms.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/AGXMX666/UniXNU-pong/blob/ffdad781cb16b42a1fb5c984f77998253b821d8c/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | README_EN.md reports desktop observation but says latest fixes were built without a temporary device boot. |
| GPU | Work in progress / incomplete | README_EN.md describes Metal desktop rendering/source integration, but no exact-pin device GPU result; latest repairs were not booted. |
| Display | Work in progress / incomplete | README_EN.md reports prior desktop/touch/wallpaper observations; latest build was not booted and brightness/refresh remain in development. |
| Touch & Buttons | Work in progress / incomplete | README_EN.md reports prior touch observation, but current build was not booted; physical button actions unresolved. |
| Audio | Work in progress / incomplete | README_EN.md says audio HAL/source is connected; actual PCM output unconfirmed. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Work in progress / incomplete | README_EN.md reports PCIe/BAR/DMA observations, but scanning/connectivity unconfirmed. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | README_EN.md says PMIC events reach HID, but power actions remain unresolved and suspend/resume incomplete. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Work in progress / incomplete | README_EN.md describes native USB implementation but no current-pin device result. |
| Storage | Work in progress / incomplete | README_EN.md describes UFS/APFS boot and Data layout, but no current-pin storage qualification. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
