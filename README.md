# Portsmith-iOS

An agent-friendly workbench for researching and bringing up XNU/iOS on non-Apple ARM64 devices.

Portsmith is a **workspace and toolbox**, not a mash-up of every port's kernel and drivers. Device ports remain separate full repositories in `ports/<port>/repo/`; shared framework references live under `sources/`. Workflows, skills, docs, and host-side utilities live here. Port and framework submodule pins and component snapshot manifests record exact reviewed revisions.

> Experimental platform research only. Do not use a phone with irreplaceable data. Never flash or reset a device without explicit, current authorization and a verified restore path.

## Start here

Clone the workbench and initialize its direct port/framework submodules (without recursively following UniXNU’s nested component pins):

```sh
git clone https://github.com/Chromitsune/Portsmith-iOS.git
cd Portsmith-iOS
git submodule update --init
```

Do **not** add `--recursive`; see [`sources/README.md`](sources/README.md) for a pinned nested UniXNU submodule that is unavailable upstream. License-cleared shared component sources are already vendored under `components/`.

1. Read [`AGENTS.md`](AGENTS.md) for workspace navigation and safety rules.
2. Read the relevant [`ports/<device>/AGENTS.md`](ports/README.md) and source project notes.
3. Run host-only checks before any hardware test; distinguish host-verified from device-verified results.

## Layout

- `AGENTS.md` — workspace instructions for agents.
- `docs/architecture.md` — repository boundaries, evidence labels, and source/license rules.
- `ports/` — per-device `AGENTS.md`/manifests plus complete port source under `repo/`. Most ports are pinned Git submodules; Dada is a vendored snapshot with its original README, notices, and licenses retained.
- `components/` — license-audited upstream source snapshots grouped by function/hardware scope, plus cross-port compatibility notes. Each snapshot retains its own license/notices and exact source pin; unresolved mixed/unlicensed repositories remain catalog-only.
- `sources/` — shared framework references (currently UniXNU), not device-specific ports.
- `skills/` — reusable task playbooks.
- `tools/` — cross-port utilities. `tools/portsmith.py` inventories ports, groups them by vendor/SoC/storage/GPU/bootloader, lists shared components, checks source pins, and reports host tools without touching a device. `tools/portsmith-image-tools` contains a reviewed, MIT-licensed subset adapted from iOSPlus10's generic image/IPSW tooling; Negroni-only `ctl` and `bootlog` commands are intentionally excluded.
- `docs/` — design notes and contribution/evidence conventions.

## Repository scope

Portsmith is a research/coordination workspace for XNU/iOS bring-up on non-Apple ARM64 hardware—not a universal OS image or a claim that every catalog entry works.

- **12 Portsmith-managed port records** have agent notes, a pinned source/snapshot, hardware metadata, safety rules, and a compatibility checklist entry. These are curated workspace records, not all devices known to the community.
- **All 265 repository records from the pinned UniXNU device catalog** are indexed as metadata in [`ports/catalog/unixnu-devices.toml`](ports/catalog/unixnu-devices.toml): 150 legacy format 1 and 115 format 2; 79 marked `available`, 25 `invalid`, 11 `missing`, and 150 with no state. There are 52 named SoC values (one unlabeled), 122 board/codename values, and 48 repeated-board groups (179 records). All 265 owner/repository identities are distinct, but many are alternate repositories for the same board. For format 2, `available` means its upstream record validated—not that the source builds or the device works.
- **Shared code:** 25 license-audited UniXNU component snapshots plus the MT8167-only NativeMsdc eMMC reference live under `components/`. Two UniXNU component repos remain catalog-only pending license/provenance review. This code is grouped by function/hardware scope and is not assumed to be portable.
- **Evidence and automation:** the README checklist records per-feature upstream reports against exact source pins; host tools validate source/manifest consistency and a weekly watcher opens review PRs when upstream branches move. New commits never automatically become “working” statuses.
- **Not included:** firmware, IPSWs, device dumps, keys, or generated images; full source checkouts for all 265 device records are not mirrored. Additional full ports are added only after source/license, duplicate-device, safety, and evidence review.

Browse/search the full upstream device index with `python3 tools/portsmith.py device-catalog --summary`, `--state available`, `--soc SM8550`, or `--search sheng`. The live Portsmith-managed port list is separate: `python3 tools/portsmith.py ports --group-by <vendor|soc|storage|gpu|bootloader>`.

## Initial source set

See [`ports/README.md`](ports/README.md), [`ports/catalog/README.md`](ports/catalog/README.md), [`sources/README.md`](sources/README.md), and [`sources/manifest.toml`](sources/manifest.toml) for port folders, the complete UniXNU device-record snapshot, upstream maintainers, licenses, and pinned revisions. Each port folder contains its original README; most codebases are pinned submodules, while Dada is a vendored snapshot with an upstream commit recorded.

## Compatibility checklist

The feature matrix is shown directly below and is generated from [`compatibility/ports.json`](compatibility/ports.json). It covers Boot, GPU, Display, Touch & Buttons, Audio, Bluetooth, Wi-Fi, Cellular, Power & Sleep, Camera & Sensors, USB, Storage, and Stability. For editable dropdowns, open the [interactive local view](docs/compatibility-matrix.html).

“Reported working” remains an upstream report—not independent Portsmith qualification. A missing status means “not tested,” not “broken.” The weekly upstream watcher flags new commits and opens a review PR; it never changes a feature status to working automatically. See [`compatibility/README.md`](compatibility/README.md) for evidence rules and automation details.

<!-- PORTSMITH-COMPATIBILITY-MATRIX-START -->
<!-- Generated by tools/build-compatibility-matrix.py; edit compatibility/ports.json instead. -->
| Device | Boot | GPU | Display | Touch & Buttons | Audio | Bluetooth | Wi-Fi | Cellular | Power & Sleep | Camera & Sensors | USB | Storage | Stability |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Xiaomi Mi 10T / Mi 10T Pro / Redmi K30S / `apollo`](https://github.com/aTechGeekDev/ios-apollo/blob/1f75f381e31da96de537653fbac2252d2eb80418/README.md)<br><sub>Qualcomm SM8250 / Snapdragon 865 · UFS · Adreno 650</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | 🔵 WIP | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Xiaomi 15 / `dada`](https://github.com/superboyyy/hakios-arm64e-dada/blob/f1ae906fcc43ba8f763663257724ba938fb820ab/README.md)<br><sub>Qualcomm SM8750 / Snapdragon 8 Elite · UFS · Adreno 830 · vendored snapshot</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🟡 Partial | ✅ Reported | 🟡 Partial | 🔵 WIP | ☐ Not tested | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Google Pixel 4 / `flame`](https://github.com/NWylynko/ios-flame/blob/745c4341af86089efb0df851fa8a27fb8face624/README.md)<br><sub>Qualcomm SM8150 / Snapdragon 855 · UFS · Adreno 640</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🔵 WIP | ☐ Not tested | 🔵 WIP | ✅ Reported | ☐ Not tested | 🟡 Partial |
| [Samsung Galaxy S9 Snapdragon variant / `starqltechn`](https://github.com/syncmodz/ios-s9/blob/646570b679b8d9147557f993ebc3ae9500ab9cfd/README.md)<br><sub>Qualcomm SDM845 / Snapdragon 845 · UFS · Adreno 630</sub> | ✅ Reported | 🔴 Unavailable | ✅ Reported | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🔴 Unavailable | 🔴 Unavailable | ☐ Not tested | 🔴 Unavailable | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [OnePlus 7 Pro / `guacamole`](https://github.com/OtVaL228/ios-sweet/blob/e66b14a9a2c8b576e7e179db4f26393698e5e49f/README.md)<br><sub>Qualcomm SM8150 / Snapdragon 855 · UFS · Adreno 640 · branch guacamole</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | ☐ Not tested | 🔵 WIP | 🔵 WIP | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Samsung Galaxy S7 (Exynos) / `herolte`](https://github.com/wardevsa/ios-a5xelte/blob/d6b6c7bbb4b2ab063ae833812db2efef094f834b/README.md)<br><sub>Samsung Exynos 8890 · UFS · ARM Mali-T880 MP12 · branch herolte</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ☐ Not tested | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | 🔴 Unavailable | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Xiaomi Redmi Note 7 / `lavender`](https://github.com/Chromitsune/UniXNU-Lavender/blob/b74f2cff0321a1440a4ecc24bd7485d21512985f/README.md)<br><sub>Qualcomm SDM660 · eMMC</sub> | 🔵 WIP | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🔵 WIP | 🔵 WIP |
| [OnePlus 9 Pro / `lemonadep`](https://github.com/popovluka/ios-lemonadep/blob/d952f7d97ea075de9f6686cbbafbd55db6517e65/README.md)<br><sub>Qualcomm SM8350 / Snapdragon 888 · UFS · Adreno 660 · branch lemonadep</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | 🔵 WIP | ✅ Reported | 🔵 WIP | ☐ Not tested | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [OnePlus 10 Pro / `negroni`](https://github.com/akshaynexus/iOSPlus10/blob/146e889430bab755329dde7104cc0fa002f44bfb/README.md)<br><sub>Qualcomm SM8450 / Snapdragon 8 Gen 1 · UFS</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | ✅ Reported | ☐ Not tested | 🟡 Partial |
| [Xiaomi Pad 6S Pro 12.4 / `sheng`](https://github.com/UniXNU/UniXNU-sheng/blob/460179565a018c741b93e0b1efa07c55d4de497a/porting.toml)<br><sub>Qualcomm SM8550 / Snapdragon 8 Gen 2 · UFS (SM8550 controller; sheng-specific integration) · Adreno 740</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | 🟡 Partial | ✅ Reported | ☐ Not tested | ✅ Reported | ☐ Not tested | ☐ Not tested | ☐ Not tested | ☐ Not tested | 🟡 Partial | 🟡 Partial |
| [Xiaomi Redmi Note 10 Pro / `sweet`](https://github.com/dipa-studio/ios-sweet/blob/45263bee51df4a0f55cdf9c649af886399488ddb/README.md)<br><sub>Qualcomm SM7150 / Snapdragon 732G · UFS · Adreno 618</sub> | ✅ Reported | 🔴 Unavailable | ✅ Reported | ✅ Reported | 🔴 Unavailable | ☐ Not tested | 🔴 Unavailable | 🔴 Unavailable | ☐ Not tested | 🔵 WIP | ☐ Not tested | ☐ Not tested | 🟡 Partial |
| [Xiaomi Redmi Note 10 Pro / `sweet-native-metal`](https://github.com/DC28088/ios-sweet/blob/8ba152f7132d3c25b5e2ff83b7f5455b8e01457f/README.md)<br><sub>Qualcomm SM7150 / Snapdragon 732G · UFS · Adreno 618 · branch main</sub> | ✅ Reported | 🟡 Partial | ✅ Reported | ✅ Reported | 🔵 WIP | ✅ Reported | 🟡 Partial | 🔵 WIP | 🟡 Partial | 🔵 WIP | ✅ Reported | ✅ Reported | 🟡 Partial |
<!-- PORTSMITH-COMPATIBILITY-MATRIX-END -->

## Safety and evidence

- Do not flash without explicit authorization. A prior authorization for one test is not standing permission.
- Inspect the phone's current state before any reset; do not force a reset just to collect data.
- Never write `LOGFS`, guess register addresses, or infer DRAM retention from a PSCI reset request.
- Do not commit IPSWs, vendor firmware, device dumps, identifiers, root images, generated payloads, or personal calibration data.
- Label results `host-verified`, `device-verified`, `inferred`, or `unknown`; a build or screenshot alone is not proof of a working port.

## Credits and contributors

Upstream project authors and maintainers: **akshaynexus** (iOSPlus10), the **UniXNU contributors**, **dipa-studio** (ios-sweet), **NWylynko** (ios-flame), **syncmodz** (ios-s9), **OtVaL228** (guacamole), **popovluka** (lemonadep), **furangelz** (lemonadep HackiOS kernel/userland base), **DC28088** (maintained `ios-sweet` default branch), **aTechGeekDev** (Apollo), **wardevsa** (herolte), and **superboyyy** (Dada), plus Dada acknowledgements to **OOSEX GANG/HakiOS**, **ShueiTsuki/Data A Live**, **steelbrain/metal2vulkan**, **Mesa**, **Project Silicium**, **7Night-kqx**, and the Linux MSM/ath12k/QCOM driver contributors. **Chromitsune** maintains the Lavender port and Portsmith workspace. Detailed project/license provenance is in [`CREDITS.md`](CREDITS.md); original contributor histories and acknowledgements remain in each port repository.

These upstream authors are **not represented as Portsmith contributors** unless they actually contribute to this repository. GitHub's Contributors view is generated from commits; our README credits upstream work accurately without implying endorsement or direct contribution.
