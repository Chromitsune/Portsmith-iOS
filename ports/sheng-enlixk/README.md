# Xiaomi Pad 6S Pro (Enlixk) (`sheng-enlixk`)

**Upstream source:** [https://github.com/Enlixk/UniXNU-sheng@`460179565a018c741b93e0b1efa07c55d4de497a`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `sheng`
- **SoC:** `SM8550`
- **OS profile:** `ipados-27.0.1-24A446`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, AdrenoMetal
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/Enlixk/UniXNU-sheng/blob/460179565a018c741b93e0b1efa07c55d4de497a/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device reports show iPadOS desktop/Settings, but missing icon artwork and a Jetsam termination; limited boots, not general boot stability. Device evidence: reports/ipados27-touch-frame-gaps.md. |
| GPU | Partial / limited | Device logs show Metal command submission/draws and retired work, but a reported idle-home-screen panic; later run reports a responsive desktop with deferred preemption. Device evidence: reports/ipados27-touch-frame-gaps.md; package/GpuPowerProbe.cpp. |
| Display | Partial / limited | Photographed Home Screen had missing artwork/cache variants; some icon artwork appeared on a separate cold-cache run. Device evidence: reports/ipados27-touch-frame-gaps.md. |
| Touch & Buttons | Partial / limited | HID reports and multiple contact IDs were recorded, but App Switcher gestures failed and rapid typing sometimes selected alternate characters. Device evidence: reports/ipados27-touch-frame-gaps.md. |
| Audio | Reported working (upstream) | Bounded speaker playback and microphone capture reported; amplifier PLLs locked and 200/200 capture periods returned. Device evidence: scripts/read-sheng-log.py. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Wi-Fi toggle/scan, WPA2 association, DHCP and traffic reported on device. Device evidence: reports/ipados27-wifi-association.md. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Partial / limited | Charging, battery/temperature and CPU/GPU frequency telemetry reported; sleep/wake is not established. Device evidence: scripts/read-sheng-log.py. |
| Camera & Sensors | Partial / limited | Battery/temperature telemetry reported; no camera result is cited. Device evidence: scripts/read-sheng-log.py. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | A retained Data marker and owner-confirmed unlock/taps were reported after the dedicated unixnu installation; Android boot and long-term/power-loss storage behavior were not qualified. Device evidence: docs/evidence/dual-system-reinstall-2026-11-01.json. |
| Stability | Partial / limited | A responsive-desktop run was reported through 360 seconds, but other recorded runs had missing icons or a process termination; no broader stability qualification. Device evidence: reports/ipados27-touch-frame-gaps.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
