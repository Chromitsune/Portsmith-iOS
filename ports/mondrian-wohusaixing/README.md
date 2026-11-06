# Redmi K60 (mondrian/SM8475): UniXNU UEFI bring-up (wohusaixing) (`mondrian-wohusaixing`)

**Upstream source:** [https://github.com/wohusaixing/UniXNU-mondrian@`092a61d8c20364eab86b35737c6b831c4cecc1ff`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `mondrian`
- **SoC:** `SM8475`
- **OS profile:** `ipados-16.6.1-20G81`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/wohusaixing/UniXNU-mondrian/blob/092a61d8c20364eab86b35737c6b831c4cecc1ff/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | README_EN.md reports ABL/fastboot/BootShim/UEFI menu, but says payload and boot image are not packaged; no XNU boot result. |
| GPU | Reported unavailable | README_EN.md explicitly lists GPU as not started; GOP display has no acceleration. |
| Display | Reported working (upstream) | README_EN.md reports ABL splash framebuffer/SimpleFbDxe GOP display; no GPU acceleration. |
| Touch & Buttons | Partial / limited | README_EN.md reports buttons working through KeypadDevice; touch is explicitly not started. |
| Audio | Reported unavailable | README_EN.md explicitly lists audio as not started. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | README_EN.md lists network as not started. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Reported unavailable | README_EN.md explicitly lists camera as not started. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported unavailable | README_EN.md says UFS/Data/root are TODO; a separate unixnu partition is only planned. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
