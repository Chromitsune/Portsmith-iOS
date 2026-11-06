# Xiaomi MIX Fold 2 (zizhan, SM8475): UniXNU bring-up derived from Pong (`zizhan`)

**Upstream source:** [https://github.com/qiumochen/UniXNU-zizhan@`3b3c52fb5ba11b0a185703d7832fd567c94e770e`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `zizhan`
- **SoC:** `SM8475`
- **OS profile:** `ipados-18.7.10-22H374`
- **Catalog-listed components:** PongPlatform24
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** NOTICE identifies third-party sources and APSL-2.0 XNU patches; preserve and review per-file terms.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/qiumochen/UniXNU-zizhan/blob/3b3c52fb5ba11b0a185703d7832fd567c94e770e/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | README reports fastboot temporary UEFI→UniXNU→DarwinBoot24→XNU boot to the iPadOS Home Screen and automatic return to Android. Evidence: README.md. |
| GPU | Partial / limited | Turnip/metal2vulkan compositing reports 95.3 fps moving synthetic scroll, but first frame is 75–80 ms and wallpaper extension cannot use GPU; not global 120-fps support. Evidence: README.md; docs/progress/2026-11-03-photos-context.md. |
| Display | Partial / limited | Internal panel shows Home Screen at 120 Hz; brightness adjustment and external display are not supported. Evidence: README.md; docs/progress/2026-11-02-shot-and-watermark.md. |
| Touch & Buttons | Partial / limited | Internal touch taps/swipes work; long-press Power resets to fastboot, but other buttons are unchecked. Evidence: README.md; docs/progress/2026-11-04-displaylink-device.md. |
| Audio | Reported unavailable | README says the CS35L41 amplifier is not yet integrated; no device audio result. SOURCE STATUS, not device-tested: README.md. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Reported working (upstream) | Native Settings WPA2 join, DHCP/HTTPS, reconnect, roaming between 2.4/5 GHz BSSIDs and lease renewal are reported; extended stress remains pending. Evidence: README.md; docs/progress/2026-11-05-wifi-lifecycle.md. |
| Cellular | Reported unavailable | README explicitly says cellular is not implemented; source status, not a device test. Evidence: README.md. |
| Power & Sleep | Partial / limited | Battery values agree with Android; status-bar battery and charging plug/unplug reported. Sleep/wake not qualified. Evidence: README.md; docs/progress/2026-11-01-battery.md. |
| Camera & Sensors | Partial / limited | ADSP/battery telemetry is reported; no camera result is cited. Evidence: README.md; docs/progress/2026-11-01-battery.md. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Reported working (upstream) | Root image with OS, SystemOS and writable Data volumes boots from a file on Android /data; APFS mount-deadlock repair documented. Evidence: README.md; docs/progress/2026-10-30-root-and-autoloop.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
