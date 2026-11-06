# UniXNU device import selection

This selection favors a credible advanced port with real subsystem evidence, not every record in the 265-entry UniXNU device catalog. The imported device repository is **sheng**; the comparison below keeps upstream reports separate from Portsmith verification.

## Selected: `sheng` — Xiaomi Pad 6S Pro 12.4 / Qualcomm SM8550

- UniXNU device catalog pin: `sources/UniXNU` at `e2fdae4312d0acc3d8a52bc457101e7918095e6a`; its `devices.toml` record is `record_state = "available"`, selects `ipados-27.0.1-24A446`, and names 11 components.
- Device repository: [UniXNU/UniXNU-sheng](https://github.com/UniXNU/UniXNU-sheng), exact revision `460179565a018c741b93e0b1efa07c55d4de497a`, stored under [`sheng/repo/`](sheng/repo/).
- The pinned upstream `porting.toml` reports desktop responsiveness to 360 seconds, Adreno 740 Metal queue/draw activity, Wi-Fi scanning/association/DHCP/traffic, and audio playback/recording. It also records issues: transparent icon variants, an icon-services Jetsam event, touch/App Switcher problems, and an earlier GPU-related idle panic before a fix. The iPadOS 26 arm64e path is **planned**, not boot-qualified.
- Why it leads: the current highest-ceiling Qualcomm phone/tablet stack in this comparison, with UFS, Adreno 740/Metal, display, input, Wi-Fi, audio, and a modular component set. Its SM8550 UFS/GPU/power assumptions are board- and generation-specific.

This is evidence reported by UniXNU at its pinned project record, not a Portsmith build, boot, or hardware qualification. No build, firmware download, flash, or device action was done for this import.

## Stronger end-to-end benchmark: `evb10` — RK3588 development board

UniXNU's [Ken-u/UniXNU-evb10](https://github.com/Ken-u/UniXNU-evb10) record is pinned at `37befa9162d6b4b080cb63a95cccff0ebb4d34f5`. The upstream record reports device verification across almost every in-scope area and iPadOS 17.7.11 reaching SpringBoard with persistent eMMC-backed Data, touch, VOP2 display, Mali-composited scrolling (~52.6 fps), and 2.4-GHz Wi-Fi. Audio was sent to the I2S FIFO but not listened to; there are still GPU/power limitations.

This board is the clearer end-to-end **working-system** benchmark and the more relevant eMMC/Mali example, but it is not an Android phone/tablet and uses a different SoC/vendor. It was not added as a second full port for this scoped import. Portsmith has not independently verified any of these reports.

## Other records considered

- `pong` (Nothing Phone 2, SM8475) has a historical iOS 16.6.1 home-screen report, but current subsystem records include significant pending/unconfirmed hardware results.
- `a04br3` (Benesse TAB-A04-BR3, MT8167) has a home-screen/eMMC DMA/Vulkan summary, but less current structured whole-system evidence. Its current `NativeMsdc` component is separately imported as an MT8167-only code reference; that driver README says the current driver is not yet booted.

## Component organization

The 27 official UniXNU component records are copied to [`../components/catalog/unixnu-components.toml`](../components/catalog/unixnu-components.toml). The 25 source repositories with a clear root license at their exact catalog pins, plus mouseos/NativeMsdc, are stored as individual snapshots under `components/<scope>/<name>/source/`; license/provenance audits are in [`../components/LICENSE-AUDIT.md`](../components/LICENSE-AUDIT.md). Ath12kWifi and QcaBluetooth remain catalog-only due unresolved/mixed licensing.
