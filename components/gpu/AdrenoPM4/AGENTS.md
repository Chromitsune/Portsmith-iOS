# AdrenoPM4 component wrapper

- **Folder purpose:** Adreno PM4 packet encoding and A740 command helpers (gpu scope).
- **Upstream pin:** https://github.com/UniXNU/AdrenoPM4.git@`282606b528b2595bc4274ea7490b62b323f35a5f`.
- **Recorded license/status:** MIT; vendored upstream snapshot; review hardware scope before reuse.
- **Use:** read this folder's `README.md` and `component.toml`, then compare `components/manifest.toml` before considering a port. Check SoC, controller, firmware, ABI and board dependencies; this component is not a universal driver or compatibility claim.

The `source/` directory is a vendored snapshot; inspect `source/UPSTREAM.toml` when present, original license/notices and any existing source-local guidance. Keep changes at this wrapper unless an explicitly reviewed source patch is required.

Never transfer hardware addresses, reset sequences, firmware or storage assumptions across ports. Preserve source notices and record any approved adaptation in `CREDITS.md`/component provenance. No device action is authorized by this folder.
