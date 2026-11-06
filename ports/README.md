# Device ports

Each folder represents a device/port. It contains a small Portsmith-owned `AGENTS.md` and `port.toml`, plus the **complete upstream-derived repository** in `repo/` as a pinned Git submodule. The source README, code, history, and license stay together in that submodule. Use `git clone --recurse-submodules` (or `git submodule update --init --recursive`) to materialize the full source trees.

The top-level README's status table is a short summary of upstream reports, not a claim of independent Portsmith verification.

- `lavender/` — Xiaomi Redmi Note 7, SDM660, eMMC, Xiaomi ABL/custom EDK2.
- `negroni/` — OnePlus 10 Pro, SM8450, UFS, Mu-Silicium/UniXNU.
- `sweet/` — Redmi Note 10 Pro, SM7150/Snapdragon 732G.
- `flame/` — Google Pixel 4, SM8150/Snapdragon 855.
- `galaxy-s9-snapdragon/` — Samsung Galaxy S9 Snapdragon variant, SM-G9600/SDM845.

The common UniXNU framework is in `sources/UniXNU`; it is not a device port. Do not copy board configuration or drivers across ports without a source-level compatibility review.
