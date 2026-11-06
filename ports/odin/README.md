# Xiaomi Mi MIX 4 (odin, Snapdragon 888+ / SM8350) (`odin`)

**Upstream source:** [https://github.com/qine233/UniXNU-odin@`3f8df85bc2670da5619240febb33f47c32ba0bcb`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `odin`
- **SoC:** `SM8350`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/qine233/UniXNU-odin/blob/3f8df85bc2670da5619240febb33f47c32ba0bcb/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Touch & Buttons | Work in progress / incomplete | README.md/porting.toml describe touch/input source adaptation and host tests; no device input result. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | README.md/porting.toml describe host-reviewed SM8350/UFS implementation work, but no device storage test or boot. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
