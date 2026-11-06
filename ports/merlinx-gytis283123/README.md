# Xiaomi Redmi Note 9 (Gytis283123) (`merlinx-gytis283123`)

**Upstream source:** [https://github.com/Gytis283123/UniXNU-merlinx@`21654d3062da9eccd2ac78827065d90487c55a2e`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `merlinx`
- **SoC:** `MT6768`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmCpu, ArmDTPlatform, SoftwareAES, NativeEmmc, RamBlock, DarwinBoot, XnuPrelink, MaliG52
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Gytis283123/UniXNU-merlinx/blob/21654d3062da9eccd2ac78827065d90487c55a2e/docs/devices/merlinx.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Device runs UEFI, DarwinBoot, XNU, initproc and launchd; see porting.toml, device evidence. |
| GPU | Partial / limited | Device reports Mali-G52 GPU_ID and MALI RC 0 through reset/MMU/job-write stages; no job/fence or PanVK device has run. See porting.toml, GPU evidence. |
| Display | Partial / limited | GOP console works, but IOMFB_FDR_loader exits 1 and no userland scanout provider is published; see docs/devices/merlinx.md. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Reported unavailable | The porting record says no audio path exists in the current image; see porting.toml, audio area. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported unavailable | The porting record says no network path exists in the current image; see porting.toml, network area. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | Platform power archive is linked, but battery reporting and suspend/resume are not implemented; source-only for these functions. See porting.toml, power area. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | SystemOS mounts and launchd runs, but Data is a volatile bring-up seed with persistence stubs; see porting.toml, storage evidence. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
