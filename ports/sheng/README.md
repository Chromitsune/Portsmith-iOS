# sheng — Xiaomi Pad 6S Pro

This port folder pins the upstream [UniXNU sheng project](https://github.com/UniXNU/UniXNU-sheng) at `460179565a018c741b93e0b1efa07c55d4de497a` under `repo/`. Device and component metadata are taken from the UniXNU catalog revision pinned at `sources/UniXNU`.

UniXNU's device record selects iPadOS 27.0.1 and lists ArmDTPlatform, ArmCpu, XnuPrelink, DarwinBoot, ShengPreflight, ShengUfs, RamBlock, GopFramebuffer, AppleKeyStoreState, Adreno740, and AdrenoMetal. Its pinned upstream porting record marks major areas implemented and reports a responsive desktop to 360 seconds, Adreno 740 Metal queue/draw activity, Wi-Fi scan/association/DHCP/traffic, and audio playback/recording. The same record documents issues including transparent icon variants, an icon-services Jetsam event, touch/App Switcher problems, and an earlier GPU-related idle panic. The iPadOS 26 arm64e path is planned, not boot-qualified. These are upstream reports with profile-specific evidence, not independent Portsmith testing or a recommendation to install it.

Read [`AGENTS.md`](AGENTS.md) before using the port. The source build/package workflow can download proprietary firmware and requires a device-specific identifier; Portsmith did not run it. No phone or tablet was built, booted, reset, or flashed for this import.
