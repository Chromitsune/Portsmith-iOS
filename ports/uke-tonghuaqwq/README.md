# Xiaomi Pad 7 (TongHuaQWQ) (`uke-tonghuaqwq`)

**Upstream source:** [https://github.com/TongHuaQWQ/UniXNU-uke@`3ae7d90a8e524d8c0888e90343a99a98d953b388`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `uke`
- **SoC:** `SM7675`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, ArmVirtPlatform, SoftwareAES, ShengUfs, ShengHidInput, ShengNovatekTouch, AppleKeyStoreState, RamBlock, VirtioMmioBlock, VirtioMmioConsole, GopFramebuffer, QcomGeniSpi, XnuPrelink, DarwinBoot, VerifiedRoot, AirNir, AdrenoPM4, AdrenoFirmware, ArmSmmu4K
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/TongHuaQWQ/UniXNU-uke/blob/3ae7d90a8e524d8c0888e90343a99a98d953b388/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Bring-up image boot/userland reached on hardware with platform/Data seed handoff; no full stability qualification. Device evidence: docs/PROGRESS.md; docs/GPU-PORT.md. |
| GPU | Partial / limited | Kernel Metal publication and user-stream heartbeat reported; full rendering/performance not established. Device evidence: docs/GPU-PORT.md. |
| Display | Partial / limited | DPU scanout/presentBase works, with roughly 10 fps and artifacts reported in some scenes. Device evidence: docs/DPU-PORT.md. |
| Touch & Buttons | Partial / limited | Touch driver scanning/report counters advance; the cited report does not establish successful physical interaction. Device evidence: docs/TOUCH-PORT.md. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | GX off/on and performance-vote heartbeat reported; sleep/battery management not qualified. Device evidence: docs/GPU-PORT.md. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | UFS root boot and owner Data-volume mount reported on hardware. Device evidence: docs/PROGRESS.md. |
| Stability | Partial / limited | Hardware userland boot reported, but long-run/stress qualification is absent. Device evidence: docs/GPU-PORT.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
