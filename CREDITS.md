# Upstream credits

Portsmith is an independent workbench. The projects below are pinned as separate repositories; Portsmith does not claim their authors as contributors to this project. Contributions to Portsmith itself are recorded through actual commits and pull requests.

| Project | Upstream maintainer / authors to credit | Why it is referenced | License / provenance |
|---|---|---|---|
| [iOSPlus10](https://github.com/akshaynexus/iOSPlus10) | [akshaynexus](https://github.com/akshaynexus) | OnePlus 10 Pro port; carefully documented workflows, agent handoff, host tools | MIT for repository-owned files; third-party components retain their licenses |
| [UniXNU](https://github.com/UniXNU/UniXNU) | [UniXNU contributors](https://github.com/UniXNU/UniXNU/graphs/contributors) | Shared UEFI/ARM64 build and driver framework | BSD-2-Clause-Patent |
| [ios-sweet](https://github.com/dipa-studio/ios-sweet) | [dipa-studio](https://github.com/dipa-studio) | Foundational Qualcomm XNU/iOS 16 port and saved-log tooling | MIT |
| [ios-flame](https://github.com/NWylynko/ios-flame) | [NWylynko](https://github.com/NWylynko) | Pixel 4 port; GPU rendering, log capture and userland tools | MIT |
| [ios-s9](https://github.com/syncmodz/ios-s9) | [syncmodz](https://github.com/syncmodz), building on [dipa-studio/ios-sweet](https://github.com/dipa-studio/ios-sweet) | Snapdragon Galaxy S9 port and persistent logging/recovery workflow | MIT; see the repository's included notice |
| [UniXNU-Lavender](https://github.com/Chromitsune/UniXNU-Lavender) | Chromitsune | Lavender/SDM660 board port | See its license and component notices |

## Adapted utilities

`tools/portsmith-image-tools` and `tools/jobs/` are adapted from `akshaynexus/iOSPlus10` (`scripts/bg.sh`, `scripts/lib/notify.sh`, and generic modules in `tools/op10tool/`). The original iOSPlus10 MIT license is included as `UPSTREAM-LICENSE` in both adapted tool directories; source paths and excluded device-specific commands are documented in `tools/README.md`.

Third-party Apple, Qualcomm, Google, Xiaomi and OnePlus firmware, IPSWs, keys, and device dumps are not included in this repository.
