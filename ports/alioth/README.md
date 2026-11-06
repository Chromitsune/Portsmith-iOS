# Redmi K40 (alioth) (`alioth`)

**Upstream source:** [https://github.com/FFT-infra/UniXNU-alioth@`f1883782125c9e4c6f5f3324c85ce980737caded`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `alioth`
- **SoC:** `SM8250`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, ShengUfs, ShengHidInput, VirtioMmioBlock, RamBlock, GopFramebuffer, XnuPrelink, DarwinBoot, AppleKeyStoreState, QcomXnuUsbDebug, ArmSmmu4K, AdrenoPM4, AdrenoFirmware
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/FFT-infra/UniXNU-alioth/blob/f1883782125c9e4c6f5f3324c85ce980737caded/docs/evidence/2026-10-27-boot-diagnostics.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Device evidence reaches launchd from UFS root; see docs/evidence/2026-10-27-boot-diagnostics.md. |
| GPU | Partial / limited | Device GPU stages run, but the desktop loses its Metal device at the client IOVA window; see docs/evidence/2026-10-28-gpu-wifi-bringup.md and docs/evidence/2026-10-30-gpu-client-windows-and-wallpaper.md. |
| Display | Partial / limited | Framebuffer/display client connects, but the recorded DISPLAY stage has zero swaps; see docs/evidence/2026-10-27-boot-diagnostics.md. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | The device report says PCIe step 10 fails at the first DBI access; Wi-Fi does not work. See docs/evidence/2026-10-28-gpu-wifi-bringup.md. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | UFS-root boot is evidenced, but the report records cryptexd ENOSPC; see docs/evidence/2026-10-27-boot-diagnostics.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
