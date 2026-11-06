# Nothing Phone (3a) (asteroids) (`asteroids`)

**Upstream source:** [https://github.com/rootstockos/UniXNU-asteroids@`6370e66cc460202756058ae53f73afdb69abd364`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `asteroids`
- **SoC:** `SM7635`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, RamBlock, XnuPrelink, DarwinBoot, GopFramebuffer, AppleKeyStoreState, QcomGeniSpi, AdrenoPM4, ArmSmmu4K, AdrenoFirmware, Adreno740, ShengUfs, ShengHidInput, Sm7635Platform, QcomPmicRtc
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/rootstockos/UniXNU-asteroids/blob/6370e66cc460202756058ae53f73afdb69abd364/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Board evidence records iPadOS booting from UFS through the first picture; see board.toml, T29. |
| GPU | Reported working (upstream) | Device evidence records GPU compositing and panel copy; see package/GpuPowerProbe.cpp and porting.toml. |
| Display | Reported working (upstream) | T34b records GPU copy to panel without tearing or stale patches; see board.toml. |
| Touch & Buttons | Reported working (upstream) | Touch works on the desktop (stage 6); see package/AsteroidsTouchProbe.cpp and porting.toml. |
| Audio | Reported working (upstream) | Device report records boot tone and iOS sounds through both speakers, with 8.3M frames over 494 seconds without gaps; see porting.toml, audio evidence. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | T29 records UFS root and persistent Data to the first picture; see board.toml. |
| Stability | Partial / limited | The audio run lasted 494 seconds without gaps; this is a bounded test, not a general stability claim. See porting.toml, audio evidence. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
