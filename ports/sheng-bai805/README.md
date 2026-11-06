# Xiaomi Pad 6S Pro (bai805) (`sheng-bai805`)

**Upstream source:** [https://github.com/bai805/UniXNU-sheng@`6a3d35c02504b712897799c5481952a61761325d`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, AdrenoMetal
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/bai805/UniXNU-sheng/blob/6a3d35c02504b712897799c5481952a61761325d/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | reports/ipados27-startup-repair-2026-11-02.md reports a diagnostic run to 120 s with SpringBoard/backboardd/wifid and no panic, but labels observations historical/uncommitted, not commit-pinned qualification. |
| GPU | Partial / limited | porting.toml cites device GPU samples (1024 MiB pool/zero fallbacks, 130 fps idle) but one WidgetRenderer command buffer was refused; startup report is historical. |
| Display | Work in progress / incomplete | reports/ipados27-startup-repair-2026-11-02.md says NativeLegacyDisplay initialized, but visual presentation was not verified; historical/uncommitted. |
| Touch & Buttons | Work in progress / incomplete | reports/ipados27-startup-repair-2026-11-02.md says NativeHidInput initialized; no user-visible touch/button operation established. |
| Audio | Reported working (upstream) | porting.toml cites playback/recording device traces with returned periods and no late periods; not a new pinned-image qualification. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | porting.toml cites WPA2 association, DHCP, and transfers; reports/ipados27-wifi-association-2026-11-02.md says newer candidate image was not booted. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | porting.toml cites battery/charging/temperature readings; no sleep/resume result. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | reports/ipados27-startup-repair-2026-11-02.md reports APFS OS/SystemCryptex mounted but offline scratch Data mount failed; historical/uncommitted. |
| Stability | Partial / limited | reports/ipados27-startup-repair-2026-11-02.md reports 120 s/no panic, diagnostic image only, not commit-pinned qualification. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
