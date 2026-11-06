# Xiaomi 13 (OddlyLabs) (`fuxi-oddlylabs`)

**Upstream source:** [https://github.com/OddlyLabs/unixnu-fuxi@`78f30b651c0ca6ea325682832bb25767523212f5`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `fuxi`
- **SoC:** `SM8550`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot, QcomGeniSpi, FuxiFtsTouch
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/OddlyLabs/unixnu-fuxi/blob/78f30b651c0ca6ea325682832bb25767523212f5/evidence/2026-11-02-first-boot.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | The first device boot reached a root-authentication failure/panic rather than a working system; see evidence/2026-11-02-first-boot.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Touch & Buttons | Partial / limited | Touch driver reports contact position on-device; this is not full UI-input qualification. See evidence/2026-11-02-first-boot.md. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Reported unavailable | Device panic reports “No PMGR?” at ConfigurationSettings.cpp:235; see evidence/2026-11-02-first-boot.md. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | Restore ramdisk volume was found and mounted as root, then rejected as unsealed; see evidence/2026-11-02-first-boot.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
