# Samsung Galaxy Tab S7+ Wi-Fi (`gts7xlwifi`) — reference-only profile

**Pinned source:** [rui12366B/UniXNU-gts7xlwifi](repo/) at [`88b34f97100a01aab4ea6b86dc9c748b2114c382`](https://github.com/rui12366B/UniXNU-gts7xlwifi/tree/88b34f97100a01aab4ea6b86dc9c748b2114c382), branch `main`. This is distinct from the catalog `sm-t970` single-core bootstrap under [`ports/sm-t970/`](../sm-t970/). The [UniXNU page](https://unixnu.com/devices/gts7xlwifi) and pinned `porting.toml` describe a later, much more capable source profile. All compatibility statements below are upstream device reports and logs, not Portsmith tests.

## Evidence and limits at this pin

| Feature | Status | Upstream evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Device record describes the iPadOS 17.7.11 desktop reached through the separate Samsung UEFI selector. The UEFI firmware itself is not included in this repo. |
| GPU | Reported working (upstream) | Device evidence reports an Adreno 650-composited UI and GPU client activity; the record still lists fault/mediaserver limits. |
| Display | Reported working (upstream) | Device logs report a 2800x1752 panel with GOP framebuffer/direct scanout and composited desktop. |
| Touch & Buttons | Reported working (upstream) | Device log records touch/HID submissions; S Pen behavior remains incomplete. |
| Audio | Reported working (upstream) | Device records report speaker output and microphone capture; volume remains limited without speaker protection firmware. |
| Bluetooth | Reported working (upstream) | Later device log reports Bluetooth Settings power-on; preserve exact run context. |
| Wi-Fi | Partial / limited | The source record's top summary says PCIe stage 4; detailed findings also describe join/DHCP/DNS/TCP and some app traffic. The record keeps Network at `implemented`, not `device-verified`; conservatively Partial. |
| Cellular | Not tested | No end-to-end cellular result is documented in the reviewed record. |
| Power & Sleep | Partial / limited | Battery/charging and shutdown work are documented, but record limits conflict about shutdown completion; sleep is not established. |
| Camera & Sensors | Partial / limited | Sensor/camera stages and raw frame work are reported; built-in camera apps do not consume the frames, and real sensor streaming is incomplete. |
| USB | Reported working (upstream) | The device record reports CDC debug and Apple USB-device enumeration; not Portsmith-verified. |
| Storage | Reported working (upstream) | Native UFS root/Data, persistent data and per-4KiB verification are reported in device logs. |
| Stability | Partial / limited | The active port record still identifies known GPU/storage/network and power limits; no Portsmith long-run qualification. |

## Port and license boundaries

The board is a Samsung SM-T970, Qualcomm SM8250/Snapdragon 865 tablet with UFS, Adreno 650, Samsung S-Boot and a separate UEFI boot selector. Keep these assumptions and this evidence separate from other SM8250 tablets and the `sm-t970` bootstrap profile.

The root `LICENSE` is BSD-2-Clause-Patent by default. It says `drivers/*` and `kits/*` retain upstream licenses, SPDX-MIT files stay MIT, and `patches/xnu/*.patch` remain APSL-2.0. Proprietary firmware is not included; source scripts may read files from the tablet or a local cache. Portsmith stores a pinned submodule pointer only—no source or firmware was copied.
