# Orange Pi 5 (Rockchip RK3588S) (`orangepi5`)

**Upstream source:** [https://github.com/Ken-u/UniXNU-orangepi5@`f96d273b526254d700bd42bfeadef0359a1d3c46`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `orangepi5`
- **SoC:** `RK3588`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, GopFramebuffer, AppleKeyStoreState, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Ken-u/UniXNU-orangepi5/blob/f96d273b526254d700bd42bfeadef0359a1d3c46/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| GPU | Work in progress / incomplete | README.md says default console config excludes GPU; source/configuration scope, not hardware testing. |
| Display | Work in progress / incomplete | README.md describes HDMI target but default console configuration has no display; no device result. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | README.md describes NVMe driver/binding source, but no device storage result. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
