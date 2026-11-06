# Samsung Galaxy S9 (starlte, SM-G960F, Exynos 9810): HakiOS, iOS 16.5 on XNU; not built on the UniXNU tree (`starlte`)

**Upstream source:** [https://github.com/Scion-Project/scion-starlte@`76bbd6000aeea88c4da5e3e0cdc2225178d1eac0`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `starlte`
- **SoC:** `Exynos 9810`
- **OS profile:** `ios-16.5-20F66`
- **Catalog-listed components:** not specified
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Mixed license file explicitly describes component-specific terms; firmware redistribution remains to be checked. Keep separate and do not flatten.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Scion-Project/scion-starlte/blob/76bbd6000aeea88c4da5e3e0cdc2225178d1eac0/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Scion record reports an iOS 16.5 device boot from an image flashed to BOOT, on six cores. This is Scion/HakiOS, not a UniXNU-tree build. Device evidence cited at https://github.com/Scion-Project/scion-kernel/commit/486e4528b985c8dee53ed51e32b0d1c812bf8480. |
| GPU | Reported working (upstream) | Device run reports CoreAnimation drawing through Mesa Panfrost. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/402471149a39a4ebc6f260ec2f0b6ffa8f1ff503. |
| Display | Reported working (upstream) | Device run reports scaled panel frames and a working Control Center brightness slider. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/245dbcc5303e9036e5e0a2f6c40ffa288ae8eb76; https://github.com/Scion-Project/scion-kernel/commit/f15c752f419bd99be6529b2a84b97755da25fbc9. |
| Touch & Buttons | Partial / limited | Touch in SpringBoard reported; physical-button coverage is not cited. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/402471149a39a4ebc6f260ec2f0b6ffa8f1ff503. |
| Audio | Reported working (upstream) | Device runs report tone/iOS sounds through ABOX and both MAX98512 amplifiers. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/dc5fbb431909904560cc13f0dac3801143f6434c. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Device runs report WPA2 join, DHCP, gateway/Internet ping and Settings join. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/f4a0b823f2f852ab237fac9daa621a8853cfa061. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Battery/charger, DVFS and eight thermal sensor readings reported; sleep/wake not qualified. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/027dd2bdab502fb86795df3b0005168d7cf02d16; https://github.com/Scion-Project/scion-kernel/commit/85dcf35b0be14bde7de40a2d574781d92e5e95e6. |
| Camera & Sensors | Partial / limited | Front camera preview reported at 30 fps and eight thermal sensors read; other camera/sensor coverage is not established. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/b0a0d91a8decfed727631d111e3be34762baab94; https://github.com/Scion-Project/scion-kernel/commit/85dcf35b0be14bde7de40a2d574781d92e5e95e6. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | Device runs report Data mounted on ufs_USERDATA_data and /private/var contents retained across boots; one native read-only mode also had fallback runs. External Scion evidence: https://github.com/Scion-Project/scion-kernel/commit/85d4705e44d55d95c48075282bfa773c62445229; https://github.com/Scion-Project/scion-kernel/commit/e5bc2eb48c85b5c8317476a3ffcaf26bb5afe44d. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
