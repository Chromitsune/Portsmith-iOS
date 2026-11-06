# OnePlus 9 Pro (`lemonadep`) port

Source is `repo/`, pinned to `popovluka/ios-lemonadep` branch `lemonadep`; read its top-level README and `lemonadep/README.md`, `lemonadep/FINDINGS-2026-11-01-03.md`, and `lemonadep/HANDOFF.md`. It contains both an older ios-sweet shim bring-up and a newer HackiOS-based standalone path; do not conflate their status.

Upstream's current branch reports a standalone iOS 16.5 UI, touch, GPU-rendered OpenGL ES interface, Wi-Fi/Safari and some connectivity. Metal for the window server is explicitly not working yet; audio, Bluetooth, cellular, cameras, and other features remain incomplete. Treat as upstream-reported experimental status.

The board is OnePlus 9 Pro / SM8350 / Snapdragon 888. Do not transfer its registers, firmware, PMIC, display, or boot assumptions to other boards.
