# Device ports

Each folder represents a device/port. It contains a small Portsmith-owned `AGENTS.md` and `port.toml`, plus the complete upstream-derived source in `repo/`. Most ports are pinned Git submodules; Dada is a vendored snapshot at a recorded upstream commit. The original README and license/notice files are kept with each port. Use `git clone --recurse-submodules` (or `git submodule update --init --recursive`) to materialize the full source trees.

The top-level README's status table is a short summary of upstream reports, not a claim of independent Portsmith verification.

- `lavender/` — Xiaomi Redmi Note 7, SDM660, eMMC, Xiaomi ABL/custom EDK2.
- `negroni/` — OnePlus 10 Pro, SM8450, UFS, Mu-Silicium/UniXNU.
- `sweet/` — Redmi Note 10 Pro, SM7150/Snapdragon 732G.
- `flame/` — Google Pixel 4, SM8150/Snapdragon 855.
- `galaxy-s9-snapdragon/` — Samsung Galaxy S9 Snapdragon variant, SM-G9600/SDM845.
- `dada/` — Xiaomi 15, SM8750/Snapdragon 8 Elite; iOS 26 arm64e research port (vendored snapshot).
- `guacamole/` — OnePlus 7 Pro, SM8150/Snapdragon 855.
- `lemonadep/` — OnePlus 9 Pro, SM8350/Snapdragon 888.
- `sweet-native-metal/` — Redmi Note 10 Pro, SM7150; DC28088 native-Metal development branch.
- `apollo/` — Xiaomi Mi 10T family, SM8250/Snapdragon 865.
- `herolte/` — Samsung Galaxy S7 Exynos 8890 (branch name; repository also contains A5XELTE work).

The common UniXNU framework is in `sources/UniXNU`; it is not a device port. Do not copy board configuration or drivers across ports without a source-level compatibility review.
