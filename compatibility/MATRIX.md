# Compatibility checklist

Statuses summarize evidence in each pinned upstream project; they are not independent Portsmith qualification.

| Device | Boot | CPU | GPU | Display | Touch & Buttons | Audio | Bluetooth | Wi-Fi | Cellular | Power & Sleep | Camera & Sensors | USB | Storage | Stability |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Xiaomi Mi 10T / Mi 10T Pro / Redmi K30S / `apollo`](https://github.com/aTechGeekDev/ios-apollo/blob/1f75f381e31da96de537653fbac2252d2eb80418/README.md)<br><sub>Qualcomm SM8250 / Snapdragon 865 · UFS · Adreno 650</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | 🔵 WIP | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Xiaomi 15 / `dada`](https://github.com/superboyyy/hakios-arm64e-dada/blob/f1ae906fcc43ba8f763663257724ba938fb820ab/README.md)<br><sub>Qualcomm SM8750 / Snapdragon 8 Elite · UFS · Adreno 830 · vendored snapshot</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ✅ Reported | 🟡 Partial | ✅ Reported | 🟡 Partial | 🔵 WIP | ☐ Not tested | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Google Pixel 4 / `flame`](https://github.com/NWylynko/ios-flame/blob/745c4341af86089efb0df851fa8a27fb8face624/README.md)<br><sub>Qualcomm SM8150 / Snapdragon 855 · UFS · Adreno 640</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🔵 WIP | ☐ Not tested | 🔵 WIP | ✅ Reported | ☐ Not tested | 🟡 Partial |
| [Samsung Galaxy S9 Snapdragon variant / `starqltechn`](https://github.com/syncmodz/ios-s9/blob/646570b679b8d9147557f993ebc3ae9500ab9cfd/README.md)<br><sub>Qualcomm SDM845 / Snapdragon 845 · UFS · Adreno 630</sub> | ✅ Reported | ☐ Not tested | 🔴 Unavailable | ✅ Reported | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🔴 Unavailable | 🔴 Unavailable | ☐ Not tested | 🔴 Unavailable | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [OnePlus 7 Pro / `guacamole`](https://github.com/OtVaL228/ios-sweet/blob/e66b14a9a2c8b576e7e179db4f26393698e5e49f/README.md)<br><sub>Qualcomm SM8150 / Snapdragon 855 · UFS · Adreno 640 · branch guacamole</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | ☐ Not tested | 🔵 WIP | 🔵 WIP | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Samsung Galaxy S7 (Exynos) / `herolte`](https://github.com/wardevsa/ios-a5xelte/blob/d6b6c7bbb4b2ab063ae833812db2efef094f834b/README.md)<br><sub>Samsung Exynos 8890 · UFS · ARM Mali-T880 MP12 · branch herolte</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ☐ Not tested | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Xiaomi Redmi Note 7 / `lavender`](https://github.com/Chromitsune/UniXNU-Lavender/blob/b74f2cff0321a1440a4ecc24bd7485d21512985f/README.md)<br><sub>Qualcomm SDM660 · eMMC</sub> | 🔵 WIP | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🔵 WIP | 🔵 WIP |
| [OnePlus 9 Pro / `lemonadep`](https://github.com/popovluka/ios-lemonadep/blob/d952f7d97ea075de9f6686cbbafbd55db6517e65/README.md)<br><sub>Qualcomm SM8350 / Snapdragon 888 · UFS · Adreno 660 · branch lemonadep</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | 🔵 WIP | ✅ Reported | 🔵 WIP | ☐ Not tested | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [OnePlus 10 Pro / `negroni`](https://github.com/akshaynexus/iOSPlus10/blob/146e889430bab755329dde7104cc0fa002f44bfb/README.md)<br><sub>Qualcomm SM8450 / Snapdragon 8 Gen 1 · UFS</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ✅ Reported | ☐ Not tested | 🟡 Partial |
| [Xiaomi Pad 6S Pro 12.4 / `sheng`](https://github.com/UniXNU/UniXNU-sheng/blob/460179565a018c741b93e0b1efa07c55d4de497a/porting.toml)<br><sub>Qualcomm SM8550 / Snapdragon 8 Gen 2 · UFS (SM8550 controller; sheng-specific integration) · Adreno 740</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | 🟡 Partial | ✅ Reported | ☐ Not tested | ✅ Reported | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🟡 Partial | 🟡 Partial |
| [Xiaomi Redmi Note 10 Pro / `sweet`](https://github.com/dipa-studio/ios-sweet/blob/45263bee51df4a0f55cdf9c649af886399488ddb/README.md)<br><sub>Qualcomm SM7150 / Snapdragon 732G · UFS · Adreno 618</sub> | ✅ Reported | ☐ Not tested | 🔴 Unavailable | ✅ Reported | ✅ Reported | 🔴 Unavailable | ☐ Not tested | 🔴 Unavailable | 🔴 Unavailable | ☐ Not tested | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Xiaomi Redmi Note 10 Pro / `sweet-native-metal`](https://github.com/DC28088/ios-sweet/blob/67448d2151ef7520a8c4417a62a85823c62b30b5/NOTES.md)<br><sub>Qualcomm SM7150 / Snapdragon 732G · UFS · Adreno 618 · branch codex/native-adreno-metal</sub> | ✅ Reported | ☐ Not tested | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | ✅ Reported | ✅ Reported | 🔵 WIP | ☐ Not tested | 🔵 WIP | ✅ Reported | ☐ Not tested | 🟡 Partial |

## Legend

| Mark | Meaning |
|---|---|
| ✅ | Reported working |
| 🟡 | Partial / limited |
| 🔵 | Work in progress / incomplete |
| 🔴 | Reported unavailable |
| ☐ | Not tested / no evidence |
| — | Not applicable |

**Evidence rule:** `Reported working` and `Reported unavailable` mean the pinned upstream project's own report—not independent Portsmith verification. `Not tested` means this checklist has no comparable evidence recorded; it does not mean the feature is broken. Details and source pins are on each device's `AGENTS.md`/README and at the linked upstream revision.

The interactive page lets you try statuses locally. Browser edits are stored only in local storage and are not committed. A permanent change requires editing `compatibility/ports.json` with an evidence note, exact source revision, and review.
