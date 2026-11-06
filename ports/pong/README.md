# Nothing Phone (2) (pong) (`pong`)

**Upstream source:** [https://github.com/Chengdong-Yu/UniXNU-pong@`e0ee6df109b4b5dc706cac660d4f8210dc911dac`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `pong`
- **SoC:** `SM8475`
- **OS profile:** `ipados-18.7.10-22H374`
- **Catalog-listed components:** PongPlatform24
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Notice says core/modules retain per-file/upstream licenses; Apple restore assets are fetched separately and not included.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Chengdong-Yu/UniXNU-pong/blob/e0ee6df109b4b5dc706cac660d4f8210dc911dac/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | README_EN.md describes prior device UI results, but explicitly says current CI artifacts have not been on hardware; no exact-image boot qualification. |
| GPU | Work in progress / incomplete | README_EN.md describes prior Metal desktop rendering and remaining slow-frame/resume work; current CI artifact is not device-tested. |
| Display | Work in progress / incomplete | README_EN.md reports prior desktop/brightness observations, but says current CI artifacts have not been on hardware. |
| Touch & Buttons | Work in progress / incomplete | README_EN.md describes prior device touch/button actions; current CI artifacts are explicitly not device-tested. |
| Audio | Work in progress / incomplete | README_EN.md reports prior audio playback/volume results and unresolved wake recovery; current CI artifact itself was not on-device. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Work in progress / incomplete | README_EN.md reports prior Wi-Fi scan/association results; current CI artifact is explicitly not device-tested. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | README_EN.md reports native power/volume actions, but full suspend/resume remains incomplete. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Work in progress / incomplete | README_EN.md says native USB/Finder fixes are included, but provides no current-pin USB device operation. |
| Storage | Work in progress / incomplete | README_EN.md reports prior native UFS/APFS boot and writable Data; it says CI artifacts are not sent to devices. |
| Stability | Partial / limited | README_EN.md reports unresolved slow-frame, audio-wake, and resume issues; no sustained stability qualification. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
