# Redmi K60 (mondrian/SM8475): UniXNU UEFI bring-up (`mondrian`)

**Upstream source:** [https://github.com/Emilelu/UniXNU-mondrian@`c39ff292eee2726c0135f3ba3a98462c9c21d8de`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `mondrian`
- **SoC:** `SM8475`
- **OS profile:** `ipados-16.6.1-20G81`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, PongUfs
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Emilelu/UniXNU-mondrian/blob/c39ff292eee2726c0135f3ba3a98462c9c21d8de/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device loader and early-XNU probes run, but the port still reports an early boot/userland blocker; docs/ROUTE-A-18-STATE.md. |
| GPU | Reported unavailable | README.md and README_EN.md say Adreno is not started/on-device; linked source is not runtime evidence. |
| Display | Reported working (upstream) | README.md reports CPU framebuffer rendering/swaps at 1440x3200; no GPU acceleration. |
| Touch & Buttons | Partial / limited | README_EN.md reports physical buttons working; touch is TODO/not started. |
| Audio | Reported unavailable | README_EN.md lists audio as TODO/not started. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | README_EN.md lists network as TODO/not started. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Reported unavailable | README_EN.md lists camera as TODO/not started. |
| USB | Reported unavailable | README.md says XNU handoff leaves USB/debug logging disconnected; this is specifically the debug path. |
| Storage | Partial / limited | README_EN.md reports read-only OS/SystemOS UFS root; Data is read-only/space-limited with an ENOSPC blocker. |
| Stability | Partial / limited | README.md and porting.toml record early boot/panic and userland failures; stable full session not established. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
