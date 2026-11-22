# Primary boot-menu reference: OnePlus 7 Pro / `ios-guacamole`

Portsmith's primary/default **reference implementation** for future boot-menu design/extraction work is [`coreycusick/ios-guacamole`](https://github.com/coreycusick/ios-guacamole), branch `ios27`, pinned at [`396a851ef112fd34003f0b37c3270bcd6c2e8cc2`](https://github.com/coreycusick/ios-guacamole/commit/396a851ef112fd34003f0b37c3270bcd6c2e8cc2), tracked at [`ports/guacamole-ios27/repo`](../ports/guacamole-ios27/repo). This means **primary source reference**, not a universal binary, recommended flash image, or Portsmith-qualified boot menu. See the [port notes](../ports/guacamole-ios27/README.md).

Keep this profile distinct from [`ports/guacamole/`](../ports/guacamole/AGENTS.md), which is the separate `OtVaL228/ios-sweet` OnePlus 7 Pro / iOS 16 source. Do not merge those reports or assumptions.

## Menu inspection

The pinned source has no running-menu screenshot. Its checked-in assets are OS icon artwork, not a screenshot. Portsmith now includes a [QEMU renderer preview](screenshots/guacamole-menu-qemu.png), captured by [`tools/qemu-guacamole-menu-preview.py`](../tools/qemu-guacamole-menu-preview.py); it calls the pinned drawing code with mock input/timer and is not a full shim or hardware test. Capture limits and source/license notes are in [`docs/screenshots/README.md`](screenshots/README.md). The upstream [`docs/dualboot.md`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/docs/dualboot.md) describes the UI as a black screen with a vertical stack of rounded OS pictures, a blue selection ring, and Restart/Power off buttons at the lower right. The menu supports volume-key navigation, power-to-select, touchscreen taps, a remembered default, and a five-second timeout.

Key source files at the exact pin:

- [`shim/menu.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/menu.c): menu rendering, PM8150 key polling, selection, touch interaction.
- [`shim/shim.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/shim.c): entry configuration and dispatch to Android/iOS/macOS, restart, and power-off.
- [`shim/touch.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/touch.c), [`shim/board.h`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/board.h), and [`shim/ufs.c`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/shim/ufs.c): target-specific drivers and persistence.
- [`tools/mkmenuboot.py`](https://github.com/coreycusick/ios-guacamole/blob/396a851ef112fd34003f0b37c3270bcd6c2e8cc2/tools/mkmenuboot.py): host-side composer for that project's Android boot-image-v2/shim/SWEETXNU-payload layout; it writes an image file, not a device.

Upstream README reports iOS 27.2 reaching the lock screen/SpringBoard through the selector. The README and dual-boot guide also describe a permanent setup using the OnePlus ABL/slot arrangement: selector in `boot_b`, Android chain-loaded from `boot_a`, and iOS/macOS payloads in the combined ramdisk. These are pinned upstream statements, **not Portsmith tests**.

## Why it is not universal

The UI is an excellent design reference, but its implementation is coupled to the OnePlus 7 Pro (`guacamole`, SM8150): fixed 1440x3120 framebuffer geometry and direct framebuffer writes; PM8150 SPMI key reads; Samsung S6SY761 touchscreen over a particular QUP/I²C/RPMh wiring; Qualcomm ABL entry conditions; Android boot-image-v2 wrapping; `SWEETXNU` payload parsing; board-specific Android chain-loading; and PSCI restart/power-off.

The selector also persists its choice by writing one 4 KiB `SWBM` record to the first block of the final unallocated 4 MiB on UFS LUN0, after checking the GPT for overlap. Upstream permanent setup flashes `boot_b` and changes the active slot. That storage and boot-partition behavior is **not** safe to infer for another phone. Portsmith did not run the build, boot the image, flash a device, change a slot, or write storage.

## Extraction boundary and license

No menu source code or original art files were copied in this addition; the QEMU screenshot is a rendered image containing the upstream icons and is attributed in the screenshot README. The root `LICENSE.txt` declares MIT for project work, but says XNU patches retain APSL-2.0, `userland/audio/` has a separate MIT notice, and ios-sweet-derived code retains prior authors' copyright notices. The touch code documents its derivation from kernel touch/RPMh sources. The icon PNGs are called user-provided by the conversion script, but their per-file provenance was not established during this audit; do not reuse them without review.

If extraction is pursued, start with an independently testable menu model and renderer, behind explicit interfaces for framebuffer geometry/format, timer, input, target dispatch, and optional preference persistence. Keep hardware drivers, boot-image formats, FDT/payload loaders, partition handling, and boot-slot changes in per-platform adapters. Persistence should be disabled by default and no boot or storage writes should be part of a generic UI. Preserve all applicable notices and verify asset provenance before redistribution. The current upstream menu is a reference, not drop-in universal tooling.
