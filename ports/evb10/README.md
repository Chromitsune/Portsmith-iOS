# Rockchip RK3588 EVB10 V10 (`evb10`)

**Upstream source:** [https://github.com/Ken-u/UniXNU-evb10@`37befa9162d6b4b080cb63a95cccff0ebb4d34f5`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `evb10`
- **SoC:** `RK3588`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, GopFramebuffer, AppleKeyStoreState, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Ken-u/UniXNU-evb10/blob/37befa9162d6b4b080cb63a95cccff0ebb4d34f5/evidence/boot-v1-20261030.txt).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Device log records launchd and SpringBoard checkpoints; see evidence/boot-v1-20261030.txt. |
| GPU | Reported working (upstream) | Device runs record Mali compositing of the interface and GPU-governed gestures; see evidence/boot-v1-20261030.txt and evidence/dvfs-governor-20261101.txt. |
| Display | Reported working (upstream) | Panel was checked on the board and VOP2 scanned out the kernel framebuffer; see evidence/boot-v1-20261030.txt. |
| Touch & Buttons | Reported working (upstream) | Touchscreen operation was checked by hand on the board; see evidence/boot-v1-20261030.txt and evidence/wifi-settings-pane-20261031.txt. |
| Audio | Partial / limited | iPadOS sent frames to I2S, with four dropouts; the report says audio was not listened to. See evidence/audio-ipados-20261101.txt. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Device scans, joins WPA2, obtains DHCP and transfers traffic; see evidence/wifi-os-20261030.txt and evidence/wifi-settings-pane-20261031.txt. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | CPU/DVFS voltage and thermal behavior were measured; this does not establish suspend/resume. See evidence/dvfs-operating-points-20261101.txt and evidence/dvfs-thermal-20261101.txt. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | SystemOS was read-only; writable Data mounted as persistent /private/var and recovered across recorded boots. See evidence/boot-v1-20261030.txt. |
| Stability | Partial / limited | A 600-second governor run and 120–240-second Wi-Fi runs completed without panic; bounded tests only. See evidence/dvfs-governor-20261101.txt and evidence/wifi-os-20261030.txt. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
