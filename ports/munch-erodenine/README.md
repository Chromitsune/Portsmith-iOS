# Xiaomi Redmi K40S (munch, 22021211RC) (ErodeNine) (`munch-erodenine`)

**Upstream source:** [https://github.com/ErodeNine/unixnu-munch@`42514dbf4b6a34f7a65171fcd02fa6c240a25038`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `munch`
- **SoC:** `SM8250`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, ShengUfs, VirtioMmioBlock, RamBlock, GopFramebuffer, XnuPrelink, DarwinBoot, AppleKeyStoreState, QcomXnuUsbDebug, ShengHidInput
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE is MIT; separately licensed upstream material remains separate.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/ErodeNine/unixnu-munch/blob/42514dbf4b6a34f7a65171fcd02fa6c240a25038/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | README.md reports a built/packaged kernel; device diagnostics show userland failures (docs/evidence/2026-10-27-boot-diagnostics.md). |
| GPU | Reported unavailable | README.md says GPU is not implemented (probe only); docs/evidence/2026-10-28-gpu-wifi-bringup.md records register probing, not graphics operation. |
| Display | Partial / limited | Device log shows an IOMobileFramebuffer client but zero swaps (docs/evidence/2026-10-27-boot-diagnostics.md). |
| Touch & Buttons | Work in progress / incomplete | README.md marks input stage 2; touch protocol source exists, but no working input is demonstrated on-device. |
| Audio | Reported unavailable | README.md explicitly says audio is not implemented. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | README.md says Wi-Fi is not implemented; docs/evidence/2026-10-28-gpu-wifi-bringup.md has controller probes, not network service. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Reported unavailable | README.md explicitly says power is not implemented. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Reported working (upstream) | Device diagnostics report QcomXnuUsbDebug enumerated and responding in both directions (docs/evidence/2026-10-27-boot-diagnostics.md); debug channel only. |
| Storage | Work in progress / incomplete | README.md marks storage as a stage; device boot diagnostics show cryptexd failing ENOSPC (docs/evidence/2026-10-27-boot-diagnostics.md). |
| Stability | Partial / limited | Device logs contain repeatable process crashes (docs/evidence/2026-10-27-serial-exit-records.log). |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
