# Samsung Galaxy Tab A7 10.4 (2020) (gta4lunix) (`gta4l-gta4lunix`)

**Upstream source:** [https://github.com/gta4lunix/UniXNU-gta4l@`bc3e47c0cd516dda23296a1e235e6a6125885f05`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `gta4l`
- **SoC:** `SM6115`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/gta4lunix/UniXNU-gta4l/blob/bc3e47c0cd516dda23296a1e235e6a6125885f05/docs/evidence-baseline.md).

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
| Storage | Work in progress / incomplete | Host-only source and electrical dependency analysis; the report explicitly says no device write, image build, flash, boot or power change occurred. The SDHC decision remains NO-GO, not a device storage result. See docs/evidence-baseline.md and docs/sdhc-power-pad-dependency-report.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
