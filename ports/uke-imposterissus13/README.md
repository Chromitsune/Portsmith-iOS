# Xiaomi Pad 7 (IMPOSTERiSSUS13) (`uke-imposterissus13`)

**Upstream source:** [https://github.com/IMPOSTERiSSUS13/UniXNU-uke@`11d40bc014cb5ea75554b5e0015e337b5704885a`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `uke`
- **SoC:** `SM7675`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, ArmVirtPlatform, SoftwareAES, ShengUfs, ShengHidInput, ShengNovatekTouch, AppleKeyStoreState, RamBlock, VirtioMmioBlock, VirtioMmioConsole, Adreno740, AdrenoMetal, GopFramebuffer, QcomGeniSpi, XnuPrelink, DarwinBoot, VerifiedRoot, AirNir, AdrenoPM4, AdrenoFirmware, ArmSmmu4K
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/IMPOSTERiSSUS13/UniXNU-uke/blob/11d40bc014cb5ea75554b5e0015e337b5704885a/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Bring-up image boot/userland reached on hardware with platform/Data seed handoff; this does not qualify full-system stability. Device evidence: docs/PROGRESS.md; docs/GPU-PORT.md. |
| GPU | Partial / limited | Kernel Metal publication and user-stream heartbeat reported; complete GPU rendering is not demonstrated by that test. Device evidence: docs/GPU-PORT.md. |
| Display | Partial / limited | DPU scanout/presentBase works, but reported output is around 10 fps with artifacts in some scenes. Device evidence: docs/DPU-PORT.md. |
| Touch & Buttons | Partial / limited | Touch driver scanning/report counters advance; successful physical interaction is not established in cited evidence. Device evidence: docs/TOUCH-PORT.md. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | GX off/on and performance-vote heartbeat reported; sleep/battery management not qualified. Device evidence: docs/GPU-PORT.md. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | UFS root boots and owner Data volume mounts on hardware. Device evidence: docs/PROGRESS.md. |
| Stability | Partial / limited | A bring-up userland boot is reported, but the records do not establish long-duration or stress stability. Device evidence: docs/GPU-PORT.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
