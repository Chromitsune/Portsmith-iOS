# Xiaomi Redmi Note 12 Pro 5G (ruby, MediaTek Dimensity 1080 / MT6877) (`ruby`)

**Upstream source:** [https://github.com/lky005/UniXNU-ruby@`d321b43deae0fba70f3fd566fa25d41648b7bf82`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `ruby`
- **SoC:** `MT6877`
- **OS profile:** `ios-16.7.16-20H392`
- **Catalog-listed components:** not specified
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** LICENSE scopes MIT to original material and excludes XNU patches; it references a NOTICE absent at the pin. Preserve/review per-file terms.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/lky005/UniXNU-ruby/blob/d321b43deae0fba70f3fd566fa25d41648b7bf82/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | README.md describes direct stock-LK boot; porting.toml cites 0155 device probe run, but no sustained/full-OS boot qualification. |
| GPU | Reported unavailable | README.md explicitly lists GPU as not yet supported. |
| Display | Work in progress / incomplete | README.md describes IOMFB/LK framebuffer source; porting.toml has no device display result. |
| Touch & Buttons | Reported working (upstream) | porting.toml cites device run 0155: real GT9916R touch HID and volume/power keys. |
| Audio | Reported unavailable | README.md explicitly lists audio as not yet supported. |
| Bluetooth | Reported unavailable | README.md explicitly lists Bluetooth as not yet supported. |
| Wi-Fi | Reported unavailable | README.md explicitly lists Wi-Fi as not yet supported. |
| Cellular | Reported unavailable | README.md explicitly lists cellular as not yet supported. |
| Power & Sleep | Partial / limited | porting.toml cites 0155 battery/PMIC read-only probe; README.md says sleep/wake and charger control are not yet supported. |
| Camera & Sensors | Reported unavailable | README.md explicitly lists camera as not yet supported. |
| USB | Reported unavailable | README.md explicitly lists USB host/OTG as not yet supported. |
| Storage | Work in progress / incomplete | README.md describes UFS/HFS+ and rescue root, but porting.toml has no device storage qualification. |
| Stability | Partial / limited | porting.toml cites 19/19 probe checks and no panic in run 0155; bounded probe only. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
