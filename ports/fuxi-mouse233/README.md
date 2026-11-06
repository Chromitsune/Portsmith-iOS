# Xiaomi 13 (mouse233) (`fuxi-mouse233`)

**Upstream source:** [https://github.com/mouse233/unixnu-fuxi@`4545692515a54d8bfc94597a7ba72fd9b25bead5`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `fuxi`
- **SoC:** `SM8550`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** not specified
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/mouse233/unixnu-fuxi/blob/4545692515a54d8bfc94597a7ba72fd9b25bead5/diagnostics/ram-root/usb-bulk.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device evidence records the RAM-root pivot and launchd/xpcproxy activity, not a complete persistent-system qualification. See diagnostics/ram-root/system-root-audit.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Work in progress / incomplete | A device trace confirms EP0 EndTransfer completion, while the bulk-transfer trace still records a stop boundary; partial USB bring-up only. See diagnostics/ram-root/usb-bulk.md. |
| Storage | Partial / limited | RAM-root pivot succeeded; this is not evidence of persistent onboard storage. See diagnostics/ram-root/usb-bulk.md and diagnostics/ram-root/system-root-audit.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
