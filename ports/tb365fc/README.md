# Lenovo Xiaoxin Pad 12.1 (2025), Lenovo TB365FC (board cava_prc_consumer_wifi) (`tb365fc`)

**Upstream source:** [https://github.com/LittleStar-OuO/UniXNU-tb365fc@`b13016b5088c91819dd4350f733a938e109723ad`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `tb365fc`
- **SoC:** `MT6835`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/LittleStar-OuO/UniXNU-tb365fc/blob/b13016b5088c91819dd4350f733a938e109723ad/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | UEFI firmware boots to the UniXNU menu on the tablet, but README says no XNU image has been built or booted. Evidence: README.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Partial / limited | UEFI menu shown at 1600x2560; no XNU display result. Evidence: README.md; porting.toml [area display]. |
| Touch & Buttons | Partial / limited | Volume/Power/Enter operate the firmware menu; touch is only inventoried, not validated under XNU. Evidence: README.md; dts/tb365fc.dts. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Work in progress / incomplete | MT6631 combo chip identified from stock inputs; no UniXNU Bluetooth operation. SOURCE/STOCK EVIDENCE ONLY: proprietary-files.txt; porting.toml [area network]. |
| Wi-Fi | Work in progress / incomplete | MT6631 combo chip/firmware identified from stock inputs; no UniXNU Wi-Fi operation. SOURCE/STOCK EVIDENCE ONLY: proprietary-files.txt; porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | Battery/charger state was inventoried from the stock device; no UniXNU power/sleep test. STOCK-DEVICE INVENTORY ONLY: tools/collect-device-info.sh; porting.toml [area power]. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Stock GPT/userdata geometry is measured, but no UniXNU UFS/storage boot is reported. STOCK-DEVICE INVENTORY ONLY: tools/pull-stock-images.sh; README.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
