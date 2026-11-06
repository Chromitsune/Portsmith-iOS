# AYN Odin 3 (Dragonwing Q8, SM8750), 16 GiB (`odin3`)

**Upstream source:** [https://github.com/darkplace/UniXNU-Odin3@`6d58c09d1529fb22dba8e3d6f74d8d4c7f9f8306`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `odin3`
- **SoC:** `SM8750`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** BootProgress, PaganiDarwinBoot, PaganiArmCpu, PaganiArmDTPlatform, Sm8750Platform, SoftwareAES, ShengPlatformPower, NativePrelink, PaganiVerifiedRoot, NativeVirtioBlock, NativeRamBlock, NativeMobileDisplay
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** NOTICE identifies separately licensed OpenABL GPL-3.0-or-later (reported not redistributed), EDK2/Mu, Linux reference material and XNU patches; retain/inspect notice.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/darkplace/UniXNU-Odin3/blob/6d58c09d1529fb22dba8e3d6f74d8d4c7f9f8306/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | README.md reports reaching the lock screen from microSD. |
| GPU | Reported unavailable | README.md says GPU is out of scope for this tree. |
| Display | Partial / limited | README.md reports GOP handover/software rotation but no panel/DSI/DPU programming; a scheduler patch blocking SpringBoard handover is excluded. |
| Touch & Buttons | Work in progress / incomplete | README.md says touch identity stages exist but touch has not been demonstrated; identity read is not reproduced. |
| Audio | Reported unavailable | README.md says audio is out of scope for this tree. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | README.md says Wi-Fi is out of scope for this tree. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | README.md lists power work, but no tested sleep/resume or device power controls. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | README.md reports OdinSd PIO/ADMA2-64 root I/O and verified read windows; internal UFS was not written. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
