# Xiaomi POCO F7 / Redmi Turbo 4 Pro (`onyx`) — reference only

**Pinned source:** [Aymon-njz/hackios-xnu-kernel-Onyx](repo/) at `1a1f3d3510ccf3f1a92afd7238ac406dd9d6897a`.

The repository is a HackiOS XNU/UEFI project with an Onyx device profile (`common/devices/onyx.conf`). That profile records Qualcomm SM8735/Pakala, UEFI target `onyx`, AOSP boot header v4, and framebuffer base `0xFC800000`; it expects an externally supplied UEFI FD and DTB. The repository README's on-device results are for POCO X5 Pro `redwood`, and its other reported run is QEMU. **No Onyx build, boot, or feature result is reported at this pin.** Redwood evidence is not Onyx evidence.

The source repository is licensed under APSL-2.0 for its project sources, with separate third-party notices and firmware provenance (see `repo/LICENSE` and `repo/prebuilt/NOTICES.md`). This folder is an external source pointer, not copied code or a reuse grant.

## Compatibility at the pinned source

All features remain **Not tested for Onyx**. The upstream device profile is configuration, not a device result.

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Not tested | Upstream README reports redwood/QEMU; no Onyx boot result. |
| GPU | Not tested | No Onyx-specific GPU driver or device evidence. |
| Display | Not tested | Profile has no Onyx-specific display test. |
| Touch & Buttons | Not tested | No Onyx-specific input test. |
| Audio | Not tested | No Onyx-specific audio result. |
| Bluetooth | Not tested | No Onyx-specific Bluetooth result. |
| Wi-Fi | Not tested | Onyx profile disables ath11k; no Onyx network test. |
| Cellular | Not tested | No Onyx cellular result. |
| Power & Sleep | Not tested | No Onyx power/sleep result. |
| Camera & Sensors | Not tested | No Onyx camera/sensor result. |
| USB | Not tested | No Onyx USB result. |
| Storage | Not tested | Onyx profile does not specify storage behavior. |
| Stability | Not tested | No Onyx stability run. |

See the [Portsmith compatibility matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
