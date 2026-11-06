# Xiaomi Pad 6S Pro (`sheng`) port notes

This is a Portsmith index around the original [UniXNU sheng repository](repo/). The upstream source is pinned at `460179565a018c741b93e0b1efa07c55d4de497a`; keep its original license, README, board record, and contributor history intact.

## Scope and evidence

- Board: Xiaomi Pad 6S Pro 12.4, codename `sheng`, Qualcomm SM8550.
- Storage and board integration are UFS-specific; do not treat the driver as a generic UFS controller implementation.
- GPU: Adreno 740. UniXNU's component catalog identifies SM8550, firmware, SMMU, display and power dependencies; this is not portable as a complete GPU stack to another Adreno generation.
- The pinned `sources/UniXNU/devices.toml` record lists iPadOS 27.0.1 and 11 component names. The port's own `porting.toml` marks major areas implemented and includes desktop, GPU, Wi-Fi and audio reports, while also recording UI/touch/Jetsam/GPU-idle issues and profile-specific evidence from different revisions. The iPadOS 26 arm64e path is planned, not boot-qualified. Treat all of this as upstream-reported evidence only, not Portsmith qualification.
- The upstream README's package workflow downloads/extracts proprietary firmware inputs and requires a device-specific unique chip ID. Do not run package, firmware, flash, or reset workflows as part of routine inspection. Never commit firmware, IPSWs, image outputs, device identifiers, or calibration data.

## Working rules

1. Read `repo/AGENTS.md`, `repo/README.md`, `repo/porting.toml`, and the relevant component's own README before proposing changes.
2. Keep sheng board details (DTS, clocks, regulators, UFS PHY/SMMU, GPU power/firmware, display and input) separate from generic interfaces.
3. For component reuse, verify the exact pinned source revision, its license/notices, OS ABI and hardware dependencies. The files under `components/` are separately attributed references, not evidence they work unchanged on another board.
4. Report host builds and device observations separately. Do not convert UniXNU's status into Portsmith device verification.
5. Do not flash or reset any device without explicit, current user authorization and a reviewed restore path.
