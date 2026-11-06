# Portsmith-iOS

An agent-friendly workbench for researching and bringing up XNU/iOS on non-Apple ARM64 devices.

Portsmith is a **workspace and toolbox**, not a mash-up of every port's kernel and drivers. Device ports remain separate full repositories in `ports/<port>/repo/`; shared framework references live under `sources/`. Workflows, skills, docs, and host-side utilities live here. Submodule pins record exactly which revisions were reviewed.

> Experimental platform research only. Do not use a phone with irreplaceable data. Never flash or reset a device without explicit, current authorization and a verified restore path.

## Start here

Clone the workbench and its port repositories with:

```sh
git clone --recurse-submodules https://github.com/Chromitsune/Portsmith-iOS.git
```

1. Read [`AGENTS.md`](AGENTS.md) for workspace navigation and safety rules.
2. Read the relevant [`ports/<device>/AGENTS.md`](ports/README.md) and source project notes.
3. Run host-only checks before any hardware test; distinguish host-verified from device-verified results.

## Layout

- `AGENTS.md` — workspace instructions for agents.
- `docs/architecture.md` — repository boundaries, evidence labels, and source/license rules.
- `ports/` — per-device `AGENTS.md`/manifests plus each complete source repository as a pinned Git submodule; its original README and history remain intact.
- `sources/` — shared framework references (currently UniXNU), not device-specific ports.
- `skills/` — reusable task playbooks.
- `tools/` — cross-port utilities. `tools/portsmith-image-tools` contains a reviewed, MIT-licensed subset adapted from iOSPlus10's generic image/IPSW tooling; Negroni-only `ctl` and `bootlog` commands are intentionally excluded.
- `docs/` — design notes and contribution/evidence conventions.

## Initial source set

See [`ports/README.md`](ports/README.md), [`sources/README.md`](sources/README.md), and [`sources/manifest.toml`](sources/manifest.toml) for port folders, upstream maintainers, licenses, and pinned revisions. Each port folder contains a complete source-repository submodule with its original README.

## Port catalog: upstream-reported support

These are **reports from the pinned upstream projects**, not independent Portsmith qualification or daily-driver recommendations. Hardware support is incomplete and varies by exact model/firmware.

| Port | Reported working | Reported missing / limitations |
|---|---|---|
| [Negroni / iOSPlus10](https://github.com/Chromitsune/iOSPlus10) — OnePlus 10 Pro, SM8450 | iOS 16 home screen; project notes report GPU-rendered UI and USB log tooling | Experimental; many peripherals/features remain incomplete. OnePlus 10 Pro work is paused; iOS 26 is a separate WIP track. |
| [Sweet](https://github.com/Chromitsune/ios-sweet) — Redmi Note 10 Pro, SM7150 | iOS 16.7.16 home screen, touch, and buttons | CPU-rendered UI; Wi-Fi, cellular, audio, camera, and many services unavailable. |
| [Flame](https://github.com/Chromitsune/ios-flame) — Pixel 4, SM8150 | iOS 16 UI, touch, USB tools, and GPU-rendered UI through the documented Metal/Vulkan path | Experimental; audio, cellular, camera, sensors, and other services remain incomplete. |
| [Galaxy S9 Snapdragon](https://github.com/Chromitsune/ios-s9) — SM-G9600/SDM845 | iOS 16.7.16 home screen, panic hold, and persistent logs | CPU-rendered UI; no GPU driver, Wi-Fi, cellular, camera, or many other features. This is not the Exynos S9. |
| [Lavender](https://github.com/Chromitsune/UniXNU-Lavender) — Redmi Note 7, SDM660 | Custom UEFI/UniXNU boot chain and fixture payload reported device-tested | XNU/iOS handover, OrangeFox BCB behavior, and panic-log recovery are not verified; prior panic-recovery run was inconclusive. |

Use the port-specific `AGENTS.md`, README, and handoff for the exact source revision and current status. Portsmith must update this table only with dated evidence and must not turn upstream claims into “supported” guarantees.

## Safety and evidence

- Do not flash without explicit authorization. A prior authorization for one test is not standing permission.
- Inspect the phone's current state before any reset; do not force a reset just to collect data.
- Never write `LOGFS`, guess register addresses, or infer DRAM retention from a PSCI reset request.
- Do not commit IPSWs, vendor firmware, device dumps, identifiers, root images, generated payloads, or personal calibration data.
- Label results `host-verified`, `device-verified`, `inferred`, or `unknown`; a build or screenshot alone is not proof of a working port.

## Credits and contributors

Upstream project authors and maintainers: **akshaynexus** (iOSPlus10), the **UniXNU contributors**, **dipa-studio** (ios-sweet), **NWylynko** (ios-flame), and **syncmodz** (ios-s9), plus **Chromitsune** (Lavender port and Portsmith workspace). Detailed project/license provenance is in [`CREDITS.md`](CREDITS.md); original contributor histories and acknowledgements remain in each port repository.

These upstream authors are **not represented as Portsmith contributors** unless they actually contribute to this repository. GitHub's Contributors view is generated from commits; our README credits upstream work accurately without implying endorsement or direct contribution.
