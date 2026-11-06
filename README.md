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

## Compatibility checklist

Use the [feature-by-feature compatibility checklist](compatibility/MATRIX.md), or open the [interactive matrix](docs/compatibility-matrix.html) for locally editable dropdowns. It tracks Boot, CPU, GPU, Display, Touch & Buttons, Audio, Bluetooth, Wi-Fi, Cellular, Power & Sleep, Camera & Sensors, USB, Storage, and Stability. The default is **Not tested / no evidence**; a blank cell is not a failure claim.

“Reported working” means the pinned upstream project says it works—not independent Portsmith qualification. Details and exact source pins are in [`compatibility/ports.json`](compatibility/ports.json). The weekly upstream watcher can flag new commits and open a review PR, but it never converts source activity into a “working” status automatically. See [`compatibility/README.md`](compatibility/README.md) for the evidence rules and automation design.

## Safety and evidence

- Do not flash without explicit authorization. A prior authorization for one test is not standing permission.
- Inspect the phone's current state before any reset; do not force a reset just to collect data.
- Never write `LOGFS`, guess register addresses, or infer DRAM retention from a PSCI reset request.
- Do not commit IPSWs, vendor firmware, device dumps, identifiers, root images, generated payloads, or personal calibration data.
- Label results `host-verified`, `device-verified`, `inferred`, or `unknown`; a build or screenshot alone is not proof of a working port.

## Credits and contributors

Upstream project authors and maintainers: **akshaynexus** (iOSPlus10), the **UniXNU contributors**, **dipa-studio** (ios-sweet), **NWylynko** (ios-flame), **syncmodz** (ios-s9), **OtVaL228** (guacamole), **popovluka** (lemonadep), **furangelz** (lemonadep HackiOS kernel/userland base), **DC28088** (sweet native-Metal branch), **aTechGeekDev** (Apollo), **wardevsa** (herolte), and **superboyyy** (Dada), plus Dada acknowledgements to **OOSEX GANG/HakiOS**, **ShueiTsuki/Data A Live**, **steelbrain/metal2vulkan**, **Mesa**, **Project Silicium**, **7Night-kqx**, and the Linux MSM/ath12k/QCOM driver contributors. **Chromitsune** maintains the Lavender port and Portsmith workspace. Detailed project/license provenance is in [`CREDITS.md`](CREDITS.md); original contributor histories and acknowledgements remain in each port repository.

These upstream authors are **not represented as Portsmith contributors** unless they actually contribute to this repository. GitHub's Contributors view is generated from commits; our README credits upstream work accurately without implying endorsement or direct contribution.
