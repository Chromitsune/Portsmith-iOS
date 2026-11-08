# Axon 7 source-reference notes

This folder tracks `devilAPI/zte-axon7` at the exact pin in `port.toml`. It is a reference-only source wrapper, not a Portsmith qualification. The pinned repository describes an A2017G (`ailsa_ii` / `axon7`) and includes separate iOS, postmarketOS, and LineageOS work. The README declares APSL-2.0 for project files, but the parent has no root LICENSE file; its `ios/` gitlink points to `devilAPI/ios-sailfish` at `aae05df53f4b6913b5aa3abb2ac763b7aeaf7295`.

Read the pinned `repo/README.md`, hardware/bootloader notes, `ios/PORTING-AXON7.md` at the recorded nested pin, and all source/license notices before adapting. The reported iOS 16.7.16 home-screen result is an upstream device report for A2017G, not Portsmith testing. Keep it separate from host/QEMU results and from other Snapdragon 820 devices.

The upstream test path writes a kernel to the boot partition from TWRP; the iOS root uses userdata. The repo says fastboot boot is unavailable. Never transfer that operation to a device without current explicit authorization, exact partition checks, and a verified restore path. No code is copied into Portsmith; nested submodules must not be initialized recursively by default.
