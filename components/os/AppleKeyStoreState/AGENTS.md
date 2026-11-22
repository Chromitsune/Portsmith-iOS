# AppleKeyStoreState component wrapper

- **Folder purpose:** AppleKeyStore state and selector handling (os scope).
- **Upstream pin:** https://github.com/UniXNU/AppleKeyStoreState.git@`8c70daf814aafdf4a3d35e40dde0322655fd0a83`.
- **Recorded license/status:** BSD-2-Clause-Patent; vendored upstream snapshot; review hardware scope before reuse.
- **Use:** read this folder's `README.md` and `component.toml`, then compare `components/manifest.toml` before considering a port. Check SoC, controller, firmware, ABI and board dependencies; this component is not a universal driver or compatibility claim.

The `source/` directory is a vendored snapshot; inspect `source/UPSTREAM.toml` when present, original license/notices and any existing source-local guidance. Keep changes at this wrapper unless an explicitly reviewed source patch is required.

Never transfer hardware addresses, reset sequences, firmware or storage assumptions across ports. Preserve source notices and record any approved adaptation in `CREDITS.md`/component provenance. No device action is authorized by this folder.
