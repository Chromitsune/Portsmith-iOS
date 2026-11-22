# OnePlus 7 Pro (`guacamole`) — iOS 27 branch and boot-menu reference

**Pinned upstream:** [coreycusick/ios-guacamole](repo/) at [`396a851ef112fd34003f0b37c3270bcd6c2e8cc2`](https://github.com/coreycusick/ios-guacamole/commit/396a851ef112fd34003f0b37c3270bcd6c2e8cc2), branch `ios27`.

This is the primary/default **reference** for future Portsmith boot-menu design work. It is not a default boot image, does not replace the separate [`ports/guacamole/`](../guacamole/AGENTS.md) `ios-sweet` source, and has not been tested by Portsmith. The pinned upstream README reports iOS 27.2 reaching the lock screen/SpringBoard through its triple-boot selector on a OnePlus 7 Pro. Other feature states below are upstream statements, not independent verification.

## What the menu looks like and where it lives

The pinned upstream repository has no running-menu screenshot; it includes OS icon artwork and source-level documentation. Portsmith has a [QEMU renderer preview](../../docs/screenshots/guacamole-menu-qemu.png), not a full-system boot capture; see the [screenshot notes](../../docs/screenshots/README.md). `docs/dualboot.md` describes a black screen with a vertical column of rounded OS pictures, a blue selection ring, and small Restart/Power off buttons at lower right. Volume keys move the selection, power boots it, and touchscreen taps are supported. The default selection is remembered and starts after five seconds unless input arrives.

Relevant pinned files:

- [`shim/menu.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/menu.c): drawing and menu interaction.
- [`shim/shim.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/shim.c): entries, timeout/default, dispatch to Android/iOS/macOS, restart and power-off.
- [`shim/touch.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/touch.c): OnePlus-specific touch setup.
- [`shim/ufs.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/ufs.c): UFS read path and persistent menu-choice record.
- [`tools/mkmenuboot.py`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/tools/mkmenuboot.py): host-side Android boot-image-v2/payload composer; it writes an output image file, not a device.
- [`docs/dualboot.md`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/docs/dualboot.md): device-specific image layout and install workflow.

## Compatibility reported at this pin

| Feature | Status | Upstream evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | README says iOS 27.2 reaches lock screen/SpringBoard through the selector; not a Portsmith test. |
| GPU | Partial / limited | NativeAdrenoMetal + Turnip is reported to render UI, but stutters/textures remain and other apps are untested. |
| Display | Reported working (upstream) | README reports the UI on the panel; source notes the framebuffer flip path. |
| Touch & Buttons | Reported working (upstream) | README reports touch navigation; selector docs report volume/power controls and touch taps. |
| Audio | Reported working (upstream) | README reports speakers, system sounds, and haptics. |
| Bluetooth | Reported working (upstream) | README reports device discovery and Bluetooth audio. |
| Wi-Fi | Reported working (upstream) | README reports joining, remembered networks, and SSH. |
| Camera & Sensors | Partial / limited | Front/rear camera preview and photos are reported; ultra-wide/telephoto, smooth preview, and several sensors are not supported/qualified. |
| Cellular | Partial / limited | iOS sees a no-SIM modem/IMEI; calls, SMS, and mobile data are not implemented. |
| Power & Sleep | Partial / limited | Shutdown/reboot are reported; system sleep panicked and is disabled in the described build. |
| Storage | Partial / limited | The iOS root is on UFS and the selector uses UFS reads; no broad storage reliability/write qualification is reported. |
| USB | Not tested | No iOS USB support claim is established by the reviewed evidence. |
| Stability | Partial / limited | Upstream calls the bring-up experimental and not daily-use; no long-term qualification is reported. |

## Portability and safety boundary

The menu UI is promising, but the implementation is not universal. `menu.c` uses a fixed 1440x3120 framebuffer and PM8150 SPMI key reads; touchscreen code targets the Samsung S6SY761/QUP/RPMh wiring on this board. The shim assumes Qualcomm ABL entry conditions and Android boot image v2, understands the project's `SWEETXNU` payload, chain-loads `boot_a`, and uses device-specific PSCI/UFS behavior. The menu remembers selection by writing one 4 KiB `SWBM` record into the final unallocated 4 MiB on UFS LUN0 after checking the GPT. Upstream permanent setup flashes `boot_b` and changes the active slot. None of those write/layout assumptions may be carried to another device.

A future universalization should begin with a host-testable menu model/renderer and explicit interfaces for framebuffer, timer, input, target dispatch and optional preference persistence. Hardware, image-format, boot-slot, storage and handoff adapters must remain target-specific; persistence should be disabled by default. No implementation was extracted in this change.

`LICENSE.txt` declares MIT for the project's own work while retaining APSL-2.0 for XNU patches, a separate MIT notice for `userland/audio/`, and earlier ios-sweet copyright notices. The menu artwork's per-file provenance is not established. Portsmith stores the pinned source as a submodule and includes a QEMU-rendered menu screenshot (see its separate license/evidence notes); no source code, firmware, or original artwork files were copied.
