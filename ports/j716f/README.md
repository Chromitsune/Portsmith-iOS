# Lenovo Xiaoxin Pad Pro 2021 (j716f) (`j716f`)

**Upstream source:** [https://github.com/Denis0x00/UniXNU-j716f@`b0b1409c2752d0791802f441bdc87ab4a9e050ce`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `j716f`
- **SoC:** `SM8250`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** XnuPrelink, DarwinBoot, ArmDTPlatform, ArmCpu, SoftwareAES, RamBlock, ShengUfs, GopFramebuffer, AppleKeyStoreState, ShengHidInput
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Denis0x00/UniXNU-j716f/blob/b0b1409c2752d0791802f441bdc87ab4a9e050ce/research/native-fast-vm-done-20261029.json).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Device report records boot into the iPadOS desktop; see research/native-fast-vm-done-20261029.json. |
| GPU | Partial / limited | Device GPU stack is verified through the named pipa-gpu stage, not a claim of complete acceleration; see package/GpuProbe.cpp and porting.toml. |
| Display | Reported working (upstream) | Device report confirms the desktop run; menu/reader pages are also photographed on-device. See research/native-reader-40458123294-20261027.json. |
| Touch & Buttons | Reported working (upstream) | Device desktop-touch test is recorded in the boot report; menu key interaction is also documented. See research/native-fast-vm-done-20261029.json and README.md. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | The desktop boot report identifies the tested TB-J716F boot; storage/root are used for that run. See research/native-fast-vm-done-20261029.json. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
