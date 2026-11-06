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

## Initial source set

See [`ports/README.md`](ports/README.md), [`sources/README.md`](sources/README.md), and [`sources/manifest.toml`](sources/manifest.toml) for port folders, upstream maintainers, licenses, and pinned revisions. Each port folder contains its original README; most codebases are pinned submodules, while Dada is a vendored snapshot with an upstream commit recorded.

## Port catalog: upstream-reported support

These are **reports from the pinned upstream projects**, not independent Portsmith qualification or daily-driver recommendations. Hardware support is incomplete and varies by exact model/firmware.

| Port | Reported working | Reported missing / limitations |
|---|---|---|
| [Negroni / iOSPlus10](https://github.com/akshaynexus/iOSPlus10) — OnePlus 10 Pro, SM8450 | iOS 16 home screen; project notes report GPU-rendered UI and USB log tooling | Experimental; many peripherals/features remain incomplete. OnePlus 10 Pro work is paused; iOS 26 is a separate WIP track. |
| [Sweet](https://github.com/dipa-studio/ios-sweet) — Redmi Note 10 Pro, SM7150 | iOS 16.7.16 home screen, touch, and buttons | CPU-rendered UI; Wi-Fi, cellular, audio, camera, and many services unavailable. |
| [Flame](https://github.com/NWylynko/ios-flame) — Pixel 4, SM8150 | iOS 16 UI, touch, USB tools, and GPU-rendered UI through the documented Metal/Vulkan path | Experimental; audio, cellular, camera, sensors, and other services remain incomplete. |
| [Galaxy S9 Snapdragon](https://github.com/syncmodz/ios-s9) — SM-G9600/SDM845 | iOS 16.7.16 home screen, panic hold, and persistent logs | CPU-rendered UI; no GPU driver, Wi-Fi, cellular, camera, or many other features. This is not the Exynos S9. |
| [Dada](https://github.com/superboyyy/hakios-arm64e-dada) — Xiaomi 15, SM8750/Snapdragon 8 Elite | Upstream reports iOS 26 arm64e home screen, touch, Adreno 830 Metal translation via metal2vulkan/Turnip, and Bluetooth | Experimental; Wi-Fi is unreliable, audio is partial, camera/HDR/modem are not started. Vendored snapshot at `f1ae906`; not independently verified. |
| [Guacamole](https://github.com/OtVaL228/ios-sweet/tree/guacamole) — OnePlus 7 Pro, SM8150 | iOS 16 UI; Adreno 640 OpenGL ES rendering via Mesa/freedreno; touch/buttons | GPU path is GLES, not Metal; Wi-Fi, audio, cellular and other services incomplete. |
| [Lemonadep](https://github.com/popovluka/ios-lemonadep/tree/lemonadep) — OnePlus 9 Pro, SM8350 | iOS 16.5 UI, GPU-rendered GLES, touch, Wi-Fi/Safari reported | Metal window-server path, audio, Bluetooth, cellular and camera incomplete; installation overwrites boot/data. |
| [Sweet native Metal](https://github.com/DC28088/ios-sweet/tree/codex/native-adreno-metal) — Redmi Note 10 Pro, SM7150 | Development branch reports iOS UI via Metal→Vulkan/Turnip, Wi-Fi/Bluetooth and USB logs; direct native Metal remains experimental | Experimental branch (not default `main`); uneven performance and audio/video/camera/cellular/security gaps. |
| [Apollo](https://github.com/aTechGeekDev/ios-apollo) — Mi 10T family, SM8250 | iOS 16 UI, touch, Wi-Fi, Bluetooth, some audio, Adreno 650 OpenGL ES | Metal is in progress; camera, cellular, sleep and other features not started. |
| [Herolte](https://github.com/wardevsa/ios-a5xelte/tree/herolte) — Galaxy S7 Exynos, SM-G930F | iOS 16.7.16 home screen and Mali-T880 OpenGL ES/Panfrost path reported | Wi-Fi, cellular, Bluetooth, audio, camera, sensors and sleep unavailable. Repo also contains separate early A5XELTE work. |
| [Lavender](https://github.com/Chromitsune/UniXNU-Lavender) — Redmi Note 7, SDM660 | Custom UEFI/UniXNU boot chain and fixture payload reported device-tested | XNU/iOS handover, OrangeFox BCB behavior, and panic-log recovery are not verified; prior panic-recovery run was inconclusive. |
| [sheng](https://github.com/UniXNU/UniXNU-sheng) — Xiaomi Pad 6S Pro, SM8550 | UniXNU marks major device areas implemented across multiple iPadOS profiles; includes UFS, Adreno 740, display, input and networking work | Upstream-only evidence; profile and subsystem evidence differ, and Portsmith has not built or device-tested it. The source package workflow can download firmware and erase userdata. |

Use the port-specific `AGENTS.md`, README, and handoff for the exact source revision and current status. Portsmith must update this table only with dated evidence and must not turn upstream claims into “supported” guarantees.

## Safety and evidence

- Do not flash without explicit authorization. A prior authorization for one test is not standing permission.
- Inspect the phone's current state before any reset; do not force a reset just to collect data.
- Never write `LOGFS`, guess register addresses, or infer DRAM retention from a PSCI reset request.
- Do not commit IPSWs, vendor firmware, device dumps, identifiers, root images, generated payloads, or personal calibration data.
- Label results `host-verified`, `device-verified`, `inferred`, or `unknown`; a build or screenshot alone is not proof of a working port.

## Credits and contributors

Upstream project authors and maintainers: **akshaynexus** (iOSPlus10), the **UniXNU contributors**, **dipa-studio** (ios-sweet), **NWylynko** (ios-flame), **syncmodz** (ios-s9), **OtVaL228** (guacamole), **popovluka** (lemonadep), **furangelz** (lemonadep HackiOS kernel/userland base), **DC28088** (sweet native-Metal branch), **aTechGeekDev** (Apollo), **wardevsa** (herolte), and **superboyyy** (Dada), plus Dada acknowledgements to **OOSEX GANG/HakiOS**, **ShueiTsuki/Data A Live**, **steelbrain/metal2vulkan**, **Mesa**, **Project Silicium**, **7Night-kqx**, and the Linux MSM/ath12k/QCOM driver contributors. **Chromitsune** maintains the Lavender port and Portsmith workspace. Detailed project/license provenance is in [`CREDITS.md`](CREDITS.md); original contributor histories and acknowledgements remain in each port repository.

These upstream authors are **not represented as Portsmith contributors** unless they actually contribute to this repository. GitHub's Contributors view is generated from commits; our README credits upstream work accurately without implying endorsement or direct contribution.
