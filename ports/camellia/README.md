# Redmi Note 10 5G (camellia) (`camellia`)

**Upstream source:** [https://github.com/stanveyjiang/UniXNU-camellia@`0139bf0315f709e4efbd6f5b44ad19e8c9496087`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `camellia`
- **SoC:** `MT6833`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** not specified
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/stanveyjiang/UniXNU-camellia/blob/0139bf0315f709e4efbd6f5b44ad19e8c9496087/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device reached UEFI and the UniXNU payload menu through the pre-Android Linux handoff; no XNU boot is evidenced. See porting.toml, firmware evidence. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Reported working (upstream) | Device displayed the verified framebuffer stages, UEFI and payload menu. See porting.toml, display evidence. |
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
