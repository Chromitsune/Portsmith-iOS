# OnePlus 13T PKX110 with the native Adreno 830 GPU (Shad0w23333) (`oneplus13t-shad0w23333`)

**Upstream source:** [https://github.com/Shad0w23333/UniXNU-Pagani_SM8750@`25b110978fec628cc29bf5bd1b5b5ce830156bfd`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `oneplus13t`
- **SoC:** `SM8750`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** BootProgress, NativeAES, NativeKeyStoreEvents, NativeMobileDisplay, NativeRamBlock, NativeUfs, NativeVirtioBlock, PaganiArmCpu, PaganiArmDTPlatform, PaganiDarwinBoot, ShengPlatformPower, Stage7Probe, NativePrelink, PaganiVerifiedRoot, Sm8750Platform, PaganiInput, PaganiPanel, QcomGeniSpi, Adreno830, AdrenoMetal, PaganiAdsp, PaganiAudio, PaganiBattery, PaganiHaptics, PaganiSensors, PaganiSpeaker, PaganiWifi, PaganiBt, PaganiCamera, PaganiTorch
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Shad0w23333/UniXNU-Pagani_SM8750/blob/25b110978fec628cc29bf5bd1b5b5ce830156bfd/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Work in progress / incomplete | README.md describes source/build work and cites runtime from a separate UniXNU-Pagani_SM8750 branch; not device qualification of this fork pin. |
| GPU | Work in progress / incomplete | README.md/porting.toml describe A830 source and host work; cited hardware runs are other source pins/forks. |
| Display | Work in progress / incomplete | README.md describes panel/display source and host ABI tests; no pinned-fork display result. |
| Touch & Buttons | Work in progress / incomplete | README.md describes touch/key implementation and host tests; cited hardware input observations are from a different source branch. |
| Audio | Work in progress / incomplete | porting.toml points to ADSP/audio source host-tested in another tree; no device audio result for this pin. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Work in progress / incomplete | porting.toml points to Wi-Fi/MHI source host-tested in another tree; no device Wi-Fi result for this pin. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | README.md/porting.toml describe source power work; other-fork battery reports/host tests do not establish this fork’s sleep/power operation. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | README.md describes UFS/Data source work; cited device evidence belongs to other source/build pins. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
