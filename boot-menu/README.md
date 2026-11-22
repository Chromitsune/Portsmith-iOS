# Portsmith boot-menu design data

`boot-menu/` is a staging area for visual looks, safe menu options, a host-testable selection model and an SVG preview before any firmware/runtime adapter is considered. It takes design ideas from the Guacamole renderer and UniXNU's model/renderer separation, but copies no upstream implementation, image, font or firmware.

## What is here

- [`looks/`](looks/README.md): three renderer-independent themes/layout descriptions (icon stack, text list, landscape cards).
- [`options/`](options/README.md): explicit safe defaults and behavior controls.
- [`profiles/`](profiles/README.md): non-executable examples combining opaque target IDs, looks and options.
- [`tests/`](tests/AGENTS.md): host-only tests for the selection model and preview; no platform calls.
- [`icons/`](icons/README.md): original generic iOS-version badges 12–27; not official Apple artwork.
- [`qemu-preview.py`](qemu-preview.py) and [`qemu/`](qemu/AGENTS.md): QEMU framebuffer fixture for the generic looks, not a real boot chain.
- [`schema/`](schema/README.md): JSON schemas for the look, options and menu-profile data.

The generic version badge set `icons/ios-12.svg` through `ios-27.svg` includes the iOS 16 badge and a matching iOS 27 badge; these are original labels, not official Apple artwork. Run `python3 boot-menu/check-configs.py` to validate profiles and `python3 -m unittest discover -s boot-menu/tests -v` to test selection behavior. The host-only Python model/SVG preview is runnable and testable, and the `qemu-preview.py` fixture renders the profile through a small AArch64 QEMU guest. These previews do **not** make a universal boot menu run on hardware. A real adapter still needs a reviewed framebuffer/canvas backend, clock, input source and platform executor. Keep boot/image formats, payload parsing, firmware variables, device keys, storage and boot/reset/power-off behavior outside this folder. The Guacamole QEMU image is a renderer-only fixture, not a universal runtime; see [`docs/boot-menu-reference.md`](../docs/boot-menu-reference.md).

Run `python3 boot-menu/check-configs.py` and `python3 -m unittest discover -s boot-menu/tests -v` to validate the data and the selection model. `python3 boot-menu/preview.py boot-menu/profiles/portable-example-text.json --output /tmp/menu.svg` writes a host-only SVG mock. `python3 boot-menu/qemu-preview.py boot-menu/profiles/ios-dualboot-icon-stack.json --output /tmp/menu.png` renders the generic profile in QEMU RAM; no boot action is executed. The checked-in QEMU renders of all three looks are indexed in `docs/screenshots/README.md`.

`target_id` is an opaque lookup token for a separately configured platform adapter, not a command. The sample profiles use placeholder icons only; upstream Guacamole images are not redistributed here.
