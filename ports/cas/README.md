# Xiaomi 10 Ultra (cas) (`cas`)

**Upstream source:** [https://github.com/ht94911/UniXNU-cas@`5cba1411b76170abf027e312afee15669b9541d9`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `cas`
- **SoC:** `SM8250`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/ht94911/UniXNU-cas/blob/5cba1411b76170abf027e312afee15669b9541d9/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Three device runs completed the UniXNU menu and returned to Android; DarwinBoot/XNU is explicitly not tested. See docs/validation.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Reported working (upstream) | The device displayed the UniXNU menu during the validation runs; see docs/validation.md. |
| Touch & Buttons | Reported working (upstream) | Buttons worked during the three menu runs; see docs/validation.md. |
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
