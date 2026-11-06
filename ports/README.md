# Device ports

Each folder represents a device/port. It contains a small Portsmith-owned `AGENTS.md` and `port.toml`, plus the complete upstream-derived source in `repo/`. Most ports are pinned Git submodules; Dada is a vendored snapshot at a recorded upstream commit. The original README and license/notice files are kept with each port. After a plain clone, run `git submodule update --init` to materialize the direct port/framework source trees. Do not recursively initialize the UniXNU framework's nested pins; see [`../sources/README.md`](../sources/README.md). Component code snapshots are already in `components/`.

The rationale and evidence comparison for selecting sheng is in [`selection.md`](selection.md). The top-level README's status table is a short summary of upstream reports, not a claim of independent Portsmith verification. Hardware groups below are for discovery only; reuse still requires a source/license and controller-level review. Run `python3 tools/portsmith.py ports --group-by storage` or `--group-by soc` for other views.

## Xiaomi

| Device / Port | SoC | Storage |
|---|---|---|
| Redmi Note 7 — `lavender` | Qualcomm SDM660 | eMMC |
| Redmi Note 10 Pro — `sweet` | Qualcomm SM7150 / Snapdragon 732G | UFS |
| Redmi Note 10 Pro — `sweet-native-metal` (DC28088 default `main`) | Qualcomm SM7150 / Snapdragon 732G | UFS |
| Mi 10T family — `apollo` | Qualcomm SM8250 / Snapdragon 865 | UFS |
| Xiaomi 15 — `dada` | Qualcomm SM8750 / Snapdragon 8 Elite | UFS (per source tree) |
| Xiaomi Pad 6S Pro — `sheng` | Qualcomm SM8550 / Snapdragon 8 Gen 2 | UFS (board-specific integration) |

## OnePlus

| Device / Port | SoC | Storage |
|---|---|---|
| OnePlus 7 Pro — `guacamole` | Qualcomm SM8150 / Snapdragon 855 | UFS 3.0 |
| OnePlus 9 Pro — `lemonadep` | Qualcomm SM8350 / Snapdragon 888 | UFS |
| OnePlus 10 Pro — `negroni` | Qualcomm SM8450 / Snapdragon 8 Gen 1 | UFS |

## Google

| Device / Port | SoC | Storage |
|---|---|---|
| Pixel 4 — `flame` | Qualcomm SM8150 / Snapdragon 855 | UFS |

## Samsung

| Device / Port | SoC | Storage |
|---|---|---|
| Galaxy S9 Snapdragon — `starqltechn` | Qualcomm SDM845 / Snapdragon 845 | UFS |
| Galaxy S7 Exynos — `herolte` | Samsung Exynos 8890 | UFS |

The `herolte` repository also contains early A5XELTE work on a different Exynos/eMMC device; it is not the same board as the Galaxy S7 port.

## Full upstream catalog

The complete UniXNU device-record list is indexed separately in [`catalog/`](catalog/README.md). Its 265 entries are metadata references; they are not all Portsmith-managed ports or verified devices.

## Shared framework

The common UniXNU framework is in `sources/UniXNU`; it is not a device port. Shared component families and compatibility limits are cataloged in [`../components/`](../components/). Do not copy board configuration or drivers across ports without a source-level compatibility review.

## Selection note

`sheng` is the current lead **advanced** UniXNU reference: the modern SM8550/Adreno 740 stack has upstream reports across UI, graphics, Wi-Fi and audio, but also documented limitations and profile-specific evidence. The RK3588 `evb10` development board has the clearest upstream end-to-end device-verification record (including eMMC-backed storage and a SpringBoard boot) and is a useful eMMC/Mali benchmark; it is not imported as a phone port in this selection. Neither project's upstream reports are Portsmith device verification.
