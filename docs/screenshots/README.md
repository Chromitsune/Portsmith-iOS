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
