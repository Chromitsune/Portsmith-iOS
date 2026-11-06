# Independent Redmi K20 Pro port; compile-only default with separately gated native handset bring-up (guowenye) (`raphael-guowenye`)

**Upstream source:** [https://github.com/guowenye/UniXNU-raphael@`4a4ca3e2301f8c6a5901786fc88206942607e0bd`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `raphael`
- **SoC:** `SM8150`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** XnuPrelink, DarwinBoot, ArmDTPlatform
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/guowenye/UniXNU-raphael/blob/4a4ca3e2301f8c6a5901786fc88206942607e0bd/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | README.md reports historical handset runs reaching launchd/SpringBoard, but latest candidate has not been booted. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Partial / limited | README.md reports 2237 completed display frames/no transfer error, but user saw a loading bar then black screen. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | README.md reports original APFS/SystemOS mounted and ephemeral writable Data; no persistent Data qualification. |
| Stability | Partial / limited | README.md describes a recovered 12-minute sample, but latest candidate is unbooted and observed UI went black. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
