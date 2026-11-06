# Xiaomi Pad 7 / POCO Pad X1 (uke) (`uke`)

**Upstream source:** [https://github.com/Allenwdk/UniXNU-uke@`fcf9fd3f31be4618a48d33fd7cf161e0da75b573`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `uke`
- **SoC:** `SM7675`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, AppleKeyStoreState, Adreno740, AdrenoMetal, AdrenoFirmware, AdrenoPM4, ArmSmmu4K, AirNir, Sm7675Platform, GopFramebuffer, QcomGeniSpi, ShengNovatekTouch, ShengHidInput, ShengUfs, VirtioMmioBlock, RamBlock, VerifiedRoot, SoftwareAES
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Allenwdk/UniXNU-uke/blob/fcf9fd3f31be4618a48d33fd7cf161e0da75b573/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Owner reports boot beyond Apple to desktop/Settings, with icons/widgets and Settings/Dock interaction on the cited image; no broad regression or long-run claim. Device evidence: docs/GPU-IOS27.md. |
| GPU | Partial / limited | Kernel Metal publication and user-stream heartbeat pass; this is not a full rendering/performance qualification. Device evidence: docs/GPU-PORT.md; docs/GPU-IOS27.md. |
| Display | Partial / limited | DPU scanout works, but user reports artifacts/some scenes and roughly 10 fps in the cited presentation test. Device evidence: docs/DPU-PORT.md. |
| Touch & Buttons | Partial / limited | Touch scan/report counters advance; physical gesture/button coverage is not established. Device evidence: docs/TOUCH-PORT.md. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | GX off/on with performance vote and heartbeat reported; battery, suspend and wake behavior are not established. Device evidence: docs/GPU-PORT.md. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | UFS root boot and owner Data-volume mount reported on hardware. Device evidence: docs/PROGRESS.md. |
| Stability | Partial / limited | Basic desktop/Settings interaction reported on the repaired image; README/evidence do not qualify extended runtime, repeated reboot or stress. Device evidence: docs/GPU-IOS27.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
