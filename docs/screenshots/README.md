# Repository screenshots

A screenshot is evidence only for the capture method and source revision recorded beside it. State whether it is a device capture, a full-system emulator run, or a renderer/mock fixture. Include the exact source pin, tool/version and meaningful mocks. Do not commit private logs, serials, credentials, firmware, device dumps, or images showing private data. Review licenses and asset provenance before redistributing generated images.

## Guacamole menu QEMU renderer preview

- Image: [`guacamole-menu-qemu.png`](guacamole-menu-qemu.png)
- Reproduce: `python3 tools/qemu-guacamole-menu-preview.py --output docs/screenshots/guacamole-menu-qemu.png`
- Source: `coreycusick/ios-guacamole` at `396a851ef112fd34003f0b37c3270bcd6c2e8cc2`, branch `ios27` (`ports/guacamole-ios27/repo`).
- Capture: QEMU `virt`, Cortex-A76, 2 GiB guest RAM, 1440x3120 framebuffer memory at `0x9c000000`; captured with QMP and converted to PNG. QEMU version used for the committed image: 11.1.3 (2026-11-22).
- SHA-256: `bc903e9f1d6c69bc122a5d75beca0b7b8891bc0e6f34bef1848a8ef956fe1320`.
- Scope: the harness compiles and calls the pinned upstream `shim/menu.c` renderer and `shim/art.S` assets. The PMIC/key/timer backend is replaced by a deterministic no-key fixture; touch calls are stubbed. It does **not** execute the actual shim boot chain, emulate ABL/PMIC/touch/UFS, test selection, persist a choice, load Android/iOS/macOS, or validate hardware behavior. The visible “keys not found” line is expected in the fixture.
- Evidence level: **QEMU renderer preview only**, not a boot result, not a device screenshot, and not Portsmith device verification.
- License: upstream `LICENSE.txt` declares MIT for project work with per-source carve-outs (XNU patches remain APSL-2.0; other files retain their specified terms). The screenshot contains the upstream menu artwork. Do not treat this screenshot as a separate license for the icons; consult the pinned source notices before reuse.

## Generic boot-menu look previews (iOS 16 and iOS 27 entries)

The [`boot-menu/qemu-preview.py`](../../boot-menu/qemu-preview.py) script and renders the `ios-dualboot-*` sample profiles in a small AArch64 QEMU `virt` guest. Its guest draws an in-memory framebuffer from profile data and the boot-menu look contract; it does not boot a target OS or execute the selection. The version badges under `boot-menu/icons/` are original Portsmith-generated labels (iOS 12–27), not official Apple app icons or copied OS artwork. The generic preview contains no vendor firmware or upstream menu artwork.

The profile screenshots are visual/layout evidence only. Input events, boot dispatch, timers, persistent selection and hardware framebuffer/format are not tested; the focused menu state machine is unit-tested on the host. QEMU version: 11.1.3. SHA-256: icon-stack `4dcbc79b8ee6408cb1dbc004d5dccf52df9972c069e4e37c84da264cf0d8eea5`; text-list `d2c611366a8e312a0dac6ea48428180670b19ec9a341d28edd8fa541877dd6f3`; landscape cards `0d6e8e533ddffdeb65344ed979764bb0ebff08aab7a0f5abea7cb26d8486cc9f`.

These three PNGs are QEMU guest-framebuffer renders of the **Portsmith-owned profile/layout fixture**, not Guacamole's boot chain or a device screenshot:

- [`boot-menu-icon-stack-qemu.png`](boot-menu-icon-stack-qemu.png): 1440×3120 `icon-stack` look.
- [`boot-menu-text-list-qemu.png`](boot-menu-text-list-qemu.png): 1440×3120 `text-list` look.
- [`boot-menu-landscape-cards-qemu.png`](boot-menu-landscape-cards-qemu.png): 1920×1080 `landscape-cards` look.

Reproduce each with `python3 boot-menu/qemu-preview.py boot-menu/profiles/ios-dualboot-<icon-stack|text-list|landscape>.json --output <path>`. The custom AArch64 guest draws the profile labels and generated version badges into guest RAM under QEMU `virt`; the host captures that RAM with QMP. It does not use a physical display/input driver, run a bootloader, execute a target, persist a selection, or access device storage. QEMU used for these captures: 11.1.3. Icons are original generic version badges under `boot-menu/icons/`, not official Apple assets.
