# Redmi Pad format-2 qualification candidate; boot Mu and cust UniXNU must remain separate (`yunluo`)

**Upstream source:** [https://github.com/woaphone/UniXNU-yunluo@`c2b81b9f4f5ded51b114008e60baadc1f53ee89b`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `yunluo`
- **SoC:** `MT6789`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/woaphone/UniXNU-yunluo/blob/c2b81b9f4f5ded51b114008e60baadc1f53ee89b/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
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
