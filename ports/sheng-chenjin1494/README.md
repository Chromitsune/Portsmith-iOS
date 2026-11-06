# Xiaomi Pad 6S Pro (chenjin1494) (`sheng-chenjin1494`)

**Upstream source:** [https://github.com/chenjin1494/UniXNU-sheng@`3730af8c1307d3fecda634c74999e380cffdd1ac`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, AdrenoMetal
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/chenjin1494/UniXNU-sheng/blob/3730af8c1307d3fecda634c74999e380cffdd1ac/README.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | reports/ipados27-startup-repair-2026-11-02.md reports 120 s diagnostic run with SpringBoard/backboardd/wifid and no panic; expressly historical/uncommitted, not exact-pin qualification. |
| GPU | Work in progress / incomplete | reports/ipados27-gpu.md reports host builds/tests pass but device frame pacing/repeated preemption pending; startup report says visual presentation unverified. |
| Display | Work in progress / incomplete | reports/ipados27-startup-repair-2026-11-02.md says NativeLegacyDisplay initialized, but visual presentation not verified; historical/uncommitted. |
| Touch & Buttons | Work in progress / incomplete | reports/ipados27-startup-repair-2026-11-02.md says NativeHidInput initialized; no actual touch/button operation established. |
| Audio | Reported working (upstream) | porting.toml cites device playback/recording traces with returned periods and no late periods; not a new pinned-image qualification. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Partial / limited | reports/ipados27-wifi-association-2026-11-02.md reports device-confirmed manual WPA2 association/DHCP, but candidate image was not booted and join/switch UI remains unvalidated. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | porting.toml cites device battery/charging/temperature readings; no sleep/resume result. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | reports/ipados27-startup-repair-2026-11-02.md reports APFS OS/SystemCryptex mounted but offline scratch Data mount failed; historical/uncommitted. |
| Stability | Partial / limited | reports/ipados27-startup-repair-2026-11-02.md reports a 120 s no-panic diagnostic run, not sustained or exact-pin qualification. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
