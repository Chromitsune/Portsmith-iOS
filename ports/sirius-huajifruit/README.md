# Xiaomi Mi 8 SE (HuajiFruit) (`sirius-huajifruit`)

**Upstream source:** [https://github.com/HuajiFruit/UniXNU-sirius@`ac0c900485f3c0cd18de9707579a1cdcd3365503`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sirius`
- **SoC:** `SDM710`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, GopFramebuffer, AppleKeyStoreState, ShengHidInput
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/HuajiFruit/UniXNU-sirius/blob/ac0c900485f3c0cd18de9707579a1cdcd3365503/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | A device run reached early-boot completion and started SpringBoard, then Data ENOSPC/hash errors preceded a watchdog panic. Device evidence: docs/evidence/sirius-usb-console-20261028-early-boot.log. |
| GPU | Partial / limited | GMU/HFI startup reported in device evidence; no full rendering qualification. Device evidence: docs/evidence/sirius-gpu-20261029-gmu.log. |
| Display | Partial / limited | Console/display progress is reported, but the boot run panicked and does not establish a stable desktop. Device evidence: docs/evidence/sirius-usb-console-20261028-early-boot.log. |
| Touch & Buttons | Partial / limited | A historical run reports Setup reacting to touch; it also records a later SpringBoard restart. Device evidence: docs/evidence/sirius-touch-hid-20261029-combined.log. |
| Audio | Reported unavailable | No audio support at any layer stated; source-only, not a device test. Evidence: porting.toml [area audio]. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | No network support at any layer stated; source-only, not a device test. Evidence: porting.toml [area network]. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Partial / limited | DWC3 CDC-ACM console captures provide kernel/boot logs on hardware; broader USB support not established. Device evidence: docs/evidence/sirius-usb-console-20261028-early-boot.log. |
| Storage | Partial / limited | Data reached ENOSPC and APFS reported hash mismatches before panic; earlier bounded eMMC reads/root boot are documented. Device evidence: docs/evidence/sirius-usb-console-20261028-early-boot.log; docs/evidence/sirius-usb-console-20261028-data.log. |
| Stability | Partial / limited | Reported boot panicked after Data exhaustion/hash mismatches. Device evidence: docs/evidence/sirius-usb-console-20261028-early-boot.log. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
