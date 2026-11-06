# OnePlus 13T (oneplus13t) (`oneplus13t`)

**Upstream source:** [https://github.com/IssacL04/UniXNU-Pagani_SM8750@`ba694e1b3e2db7e1f2b9c92df21f864eef804158`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `oneplus13t`
- **SoC:** `SM8750`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** BootProgress, NativeAES, NativeKeyStoreEvents, NativeMobileDisplay, NativeRamBlock, NativeUfs, NativeVirtioBlock, PaganiArmCpu, PaganiArmDTPlatform, PaganiDarwinBoot, ShengPlatformPower, Stage7Probe, NativePrelink, PaganiVerifiedRoot, Sm8750Platform, PaganiInput, PaganiPanel, QcomGeniSpi
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/IssacL04/UniXNU-Pagani_SM8750/blob/ba694e1b3e2db7e1f2b9c92df21f864eef804158/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | README.md/STAGE6.md report system startup on recorded temporary-boot images; Build 63 startup is reported. |
| GPU | Partial / limited | README.md/STAGE6.md report Metal registration/completed submissions on one run, but slow presentation, unsupported operations, and other candidate startup failures. |
| Display | Partial / limited | STAGE6.md reports desktop startup, correct colors, readable diagnostics on a recorded image; timing/brightness and sustained presentation remain unqualified. |
| Touch & Buttons | Reported working (upstream) | STAGE6.md reports normal basic touch (Build 57/63); README.md reports power/volume key actions on an earlier build. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | README.md reports short power presses switching screen off/on and long press opening shutdown UI; suspend/resume is not established. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | README.md reports UFS root reads reaching UI, but another device run panicked on a UFS read timeout; Data is volatile RAM seed. |
| Stability | Partial / limited | README.md/STAGE6.md record successful startup and separate scheduler/UFS panic observations; sustained stability is unqualified. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
