# Upstream credits

Portsmith is an independent workbench. The projects below are pinned as separate repositories; Portsmith does not claim their authors as contributors to this project. Contributions to Portsmith itself are recorded through actual commits and pull requests.

| Project | Upstream maintainer / authors to credit | Why it is referenced | License / provenance |
|---|---|---|---|
| [iOSPlus10](https://github.com/akshaynexus/iOSPlus10) | [akshaynexus](https://github.com/akshaynexus) | OnePlus 10 Pro port; carefully documented workflows, agent handoff, host tools | MIT for repository-owned files; third-party components retain their licenses |
| [UniXNU](https://github.com/UniXNU/UniXNU) | [UniXNU contributors](https://github.com/UniXNU/UniXNU/graphs/contributors) | Shared UEFI/ARM64 build and driver framework | BSD-2-Clause-Patent |
| [ios-sweet](https://github.com/dipa-studio/ios-sweet) | [dipa-studio](https://github.com/dipa-studio) | Foundational Qualcomm XNU/iOS 16 port and saved-log tooling | MIT |
| [ios-flame](https://github.com/NWylynko/ios-flame) | [NWylynko](https://github.com/NWylynko) | Pixel 4 port; GPU rendering, log capture and userland tools | MIT |
| [ios-s9](https://github.com/syncmodz/ios-s9) | [syncmodz](https://github.com/syncmodz), building on [dipa-studio/ios-sweet](https://github.com/dipa-studio/ios-sweet) | Snapdragon Galaxy S9 port and persistent logging/recovery workflow | MIT; see the repository's included notice |
| [hakios-arm64e-dada](https://github.com/superboyyy/hakios-arm64e-dada) | [superboyyy](https://github.com/superboyyy) | Xiaomi 15/SM8750 iOS 26 arm64e port; Adreno 830 Metal-to-Vulkan path | Mixed; see the preserved `ports/dada/repo/NOTICE.md` and `LICENSES/` |
| [ios-sweet / guacamole](https://github.com/OtVaL228/ios-sweet/tree/guacamole) | [OtVaL228](https://github.com/OtVaL228), building on [dipa-studio/ios-sweet](https://github.com/dipa-studio/ios-sweet) | OnePlus 7 Pro/SM8150 port and Mesa/freedreno GLES work | No recognized license metadata for fork; base ios-sweet is MIT, check fork additions |
| [ios-lemonadep](https://github.com/popovluka/ios-lemonadep/tree/lemonadep) | [popovluka](https://github.com/popovluka), building on ios-sweet/HackiOS work | OnePlus 9 Pro/SM8350 port; GPU, Wi-Fi and standalone boot work | No recognized license metadata; preserve notices and check additions |
| [ios-sweet (DC28088 default main)](https://github.com/DC28088/ios-sweet) | [DC28088](https://github.com/DC28088), building on [dipa-studio/ios-sweet](https://github.com/dipa-studio/ios-sweet) | Maintained Redmi Note 10 Pro/SM7150 port; upstream reports native Adreno 618 Metal UI, connectivity and UFS root | No root LICENSE or recognized grant in the fork; reference-only until maintainer clarifies |
| [ios-apollo](https://github.com/aTechGeekDev/ios-apollo) | [aTechGeekDev](https://github.com/aTechGeekDev) | Mi 10T family/SM8250 iOS 16 port | MIT |
| [ios-a5xelte / herolte](https://github.com/wardevsa/ios-a5xelte/tree/herolte) | [wardevsa](https://github.com/wardevsa), building on [orhunnx/ios-a5xelte](https://github.com/orhunnx/ios-a5xelte) | Galaxy S7 Exynos 8890/Herolte GPU-accelerated iOS 16 port; repo also contains A5XELTE work | No recognized license metadata for fork; preserve notices and check before reuse |
| [UniXNU-Lavender](https://github.com/Chromitsune/UniXNU-Lavender) | Chromitsune | Lavender/SDM660 board port | See its license and component notices |
| [HackiOS XNU kernel — Onyx profile](https://github.com/Aymon-njz/hackios-xnu-kernel-Onyx) | Aymon-njz / OOSEX GANG | Reference-only POCO F7 / Redmi Turbo 4 Pro profile; no Onyx device result reported | APSL-2.0 project license; retain per-component/prebuilt notices |
| [viva-gpu](https://github.com/Nik300/viva-gpu) | Nik300 | Mali-G57 userland Metal/Panfrost research reference for Redmi Note 11 Pro 4G | No root license found; reference only, no code copied |
| [ios-viva](https://github.com/Nik300/ios-viva) | Nik300 fork of [dipa-studio/ios-sweet](https://github.com/dipa-studio/ios-sweet) | Alternate URL for the exact `45263bee` sweet source pin already tracked under `ports/sweet/repo` | Same pinned tree as existing MIT ios-sweet source; no duplicate checkout |

## Adapted utilities

`tools/portsmith-image-tools` and `tools/jobs/` are adapted from `akshaynexus/iOSPlus10` (`scripts/bg.sh`, `scripts/lib/notify.sh`, and generic modules in `tools/op10tool/`). The original iOSPlus10 MIT license is included as `UPSTREAM-LICENSE` in both adapted tool directories; source paths and excluded device-specific commands are documented in `tools/README.md`.

Third-party Apple, Qualcomm, Google, Xiaomi and OnePlus firmware, IPSWs, keys, and device dumps are not included in this repository.

## Dada acknowledgements

The Dada upstream README/NOTICE additionally credits [OOSEX GANG / HakiOS](https://github.com/oosexgang/hakios-xnu-kernel), [UniXNU](https://github.com/UniXNU/UniXNU), [ShueiTsuki / Data A Live](https://github.com/ShueiTsuki/data-a-live), [steelbrain / metal2vulkan](https://github.com/steelbrain/metal2vulkan), [Mesa](https://mesa3d.org/), [Project Silicium / Mu-Silicium](https://github.com/Project-Silicium/Mu-Silicium), [7Night-kqx / uefi-dada](https://github.com/7Night-kqx/uefi-dada), and Linux MSM/ath12k/QCOM driver contributors. Their notices are preserved in the Dada snapshot; this list is not a claim that they contributed directly to Portsmith.

## Additional upstream acknowledgements

- **Guacamole:** OtVaL228's OnePlus 7 Pro work also credits [HakiOS/OOSEX GANG](https://github.com/oosexgang/hakios-xnu-kernel), [MakrSas/ios-topaz](https://github.com/MakrSas/ios-topaz), Mesa/freedreno, Linux msm, and Dortania KdkSupportPkg.
- **Lemonadep:** [popovluka](https://github.com/popovluka) credits the iOS-Sweet base by dipa-studio and the HackiOS kernel/userland work by [furangelz](https://github.com/furangelz), plus hardware-source maintainers and OrangeFox; see its own README and notices.
- **Apollo:** aTechGeekDev credits [hakios-apollo](https://github.com/enesuzun2002/hakios-apollo), [HackiOS](https://github.com/oosexgang/hakios-xnu-kernel), [JopangJovan's Mi 10 port](https://github.com/JopangJovan/hackios-xnu-kernel-umi), ios-spes, ios-sailfish, Mesa, BearSSL, Linux ath11k/FreeBSD LinuxKPI, and OrangeFox.
- **Herolte:** wardevsa credits [orhunnx/ios-a5xelte](https://github.com/orhunnx/ios-a5xelte), ios-sweet, HakiOS, Bergamota, [syncmodz/ios-s9](https://github.com/syncmodz/ios-s9), Mesa/Panfrost, and LineageOS Exynos 8890 kernel sources.

Each port's own README/NOTICE remains the authoritative full list of source authors and licenses.

## UniXNU component and sheng references

Portsmith now indexes the [UniXNU sheng device repository](https://github.com/UniXNU/UniXNU-sheng), pinned at `460179565a018c741b93e0b1efa07c55d4de497a`, and component repositories listed by the pinned UniXNU `components.toml`. Credit the UniXNU contributors and the individual authors recorded in each source repository. Preserve each component's own LICENSE, NOTICE, README, copyright headers, and pinned revision; the top-level UniXNU BSD-2-Clause-Patent license does not replace a component's license. These sources are references, not Portsmith-verified ports or a claim of endorsement.

See [`components/CREDITS.md`](components/CREDITS.md) for exact component source repositories and commit pins, and [`components/LICENSE-AUDIT.md`](components/LICENSE-AUDIT.md) for per-repository license classifications and why two component repositories remain catalog-only. The eMMC `NativeMsdc` snapshot also preserves its own credits to mouseos/edk2-mtk, mouseos/xnu_kernel_benesse_a04br3, and UniXNU. No code was imported from Ath12kWifi or QcaBluetooth because their licensing requires additional file-level handling.

The 79 UniXNU device records marked `available` were individually checked for pinned-source reachability and root license/notice presence before adding the 73 reachable source references. See [`ports/catalog/available/LICENSE-AUDIT.md`](ports/catalog/available/LICENSE-AUDIT.md) for per-repository pins, credits, and license caveats; six inaccessible pins remain metadata-only. These are upstream source references, not Portsmith verification.

The broader UniXNU device-catalog source references are inventoried in [`ports/catalog/available/LICENSE-AUDIT.md`](ports/catalog/available/LICENSE-AUDIT.md), with per-repository pins, owners, root-license findings, and caveats. The catalog snapshot and unavailable entries remain linked in [`ports/catalog/unixnu-devices.toml`](ports/catalog/unixnu-devices.toml).
