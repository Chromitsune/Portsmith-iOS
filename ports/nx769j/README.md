# nubia RedMagic 9 Pro / 9 Pro+ / 9S Pro / 9S Pro+ (NX769J) (`nx769j`)

**Upstream source:** [https://github.com/Asultop/UniXNU-NX769J@`2a265afdbd95d45e4a90664157e793c3bfee3755`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `nx769j`
- **SoC:** `SM8650`
- **OS profile:** `ios-16.5-20F66`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot, ShengUfs, VirtioMmioBlock, VerifiedRoot, GopFramebuffer
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Asultop/UniXNU-NX769J/blob/2a265afdbd95d45e4a90664157e793c3bfee3755/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | Firmware/payload/boot image are host-built, but README.md explicitly says hardware bring-up has not run and boot was not attempted; not device evidence. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
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
