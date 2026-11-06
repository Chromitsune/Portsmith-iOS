# Device ports

Each directory contains port-specific instructions, evidence, and a manifest. The implementation remains in the pinned source repository listed in `sources/manifest.toml`.

- `lavender/` — Xiaomi Redmi Note 7, SDM660, eMMC, Xiaomi ABL/custom EDK2.
- `negroni/` — OnePlus 10 Pro, SM8450, UFS, Mu-Silicium/UniXNU.

Do not treat either board's memory map, boot chain, firmware, reset, display, or storage configuration as portable to another device.
