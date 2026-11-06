# Redmi Note 10 Pro native-Metal development branch

Source is `repo/`, pinned to `DC28088/ios-sweet` branch `codex/native-adreno-metal`; read its README, NOTES, PRIVACY, and branch-specific source/credits. The repository's default `main` branch explicitly does **not** contain all of the native-Metal work described in the README, so Portsmith tracks the named development branch and records its exact commit.

Upstream reports iOS 16.7.16 on Redmi Note 10 Pro/SM7150 with the working UI rendered through a Metal→Vulkan/Turnip bridge, plus Wi-Fi, Bluetooth, USB debugging, and battery/charging support. The separate direct AIR→NIR/freedreno native-Metal backend is experimental: its README says the latest hardware trial stopped at a draw-validation error. Animations and other daily-driver services remain incomplete. Status is upstream-reported, not independently reproduced by Portsmith.

The repo is a fork of `dipa-studio/ios-sweet`, but GitHub does not report a recognized license for this fork. Keep it as a source reference; do not copy/redistribute branch-specific code until its license is clarified with the maintainer. Never flash its images without explicit authorization.
