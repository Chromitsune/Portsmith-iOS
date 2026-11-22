# Boot-menu design workspace

This folder is Portsmith-owned, platform-neutral menu data plus a host-only selection/preview prototype. It is not a bootloader, shim, EFI application, device-control utility or image builder. Read `README.md` and the schemas before editing.

## Rules

- Keep this layer to presentation, selection state and declarative options. Menu entries use opaque `target_id` values; never put shell commands, boot arguments, partition names/offsets, MMIO addresses, firmware paths or reset sequences in a look/profile.
- Do not copy Guacamole or UniXNU menu code or icon artwork here without a separate per-file license/provenance audit. Existing upstreams are references, not permission to import code.
- `timeout_ms=0`, `auto_boot=false`, `remember_selection=false`, and `persist_selection=false` are the safe defaults. A profile that changes these needs a rationale and an explicitly reviewed platform policy.
- No generic configuration may write storage, alter boot order, select a slot, reboot, or power off. A separate platform executor must own those operations and their authorization.
- Run `python3 boot-menu/check-configs.py` and `python3 -m unittest discover -s boot-menu/tests -v`; validate JSON syntax/schema references. Keep visual tokens dimension-relative; a layout must not assume any panel dimensions or pixel format.

## Contents

- `looks/`: palette, layout and rendering choices only.
- `options/`: navigation, timeout, persistence and confirmation policy examples.
- `profiles/`: composed sample menu data with opaque target IDs; not executable boot configurations.
- `icons/`: generated abstract iOS-version labels only, no Apple artwork.
- `qemu/` and `qemu-preview.py`: generic profile renderer fixture in QEMU RAM, no device backend or boot action.
- `tests/`: host-only model/preview tests.
- `schema/`: JSON schemas defining the data contract.
