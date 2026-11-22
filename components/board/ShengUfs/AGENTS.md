# ShengUfs component wrapper

- **Folder purpose:** SM8550 UFS transport and sheng persistent storage (board scope).
- **Upstream pin:** https://github.com/UniXNU/ShengUfs.git@`99d8bcd3e43dd24fc3c8437c67b5d4cc71ab94d0`.
- **Recorded license/status:** BSD-2-Clause; vendored upstream snapshot; review hardware scope before reuse.
- **Use:** read this folder's `README.md` and `component.toml`, then compare `components/manifest.toml` before considering a port. Check SoC, controller, firmware, ABI and board dependencies; this component is not a universal driver or compatibility claim.

The `source/` directory is a vendored snapshot; inspect `source/UPSTREAM.toml` when present, original license/notices and any existing source-local guidance. Keep changes at this wrapper unless an explicitly reviewed source patch is required.

Never transfer hardware addresses, reset sequences, firmware or storage assumptions across ports. Preserve source notices and record any approved adaptation in `CREDITS.md`/component provenance. No device action is authorized by this folder.
