# Portsmith-iOS

An agent-friendly workbench for researching and bringing up XNU/iOS on non-Apple ARM64 devices.

Portsmith is a **workspace and toolbox**, not a mash-up of every port's kernel and drivers. Device ports remain separate, reproducible source references under `sources/`; shared workflows, skills, documentation, and host-side utilities live here. Submodule pins record exactly which upstream revisions were reviewed.

> Experimental platform research only. Do not use a phone with irreplaceable data. Never flash or reset a device without explicit, current authorization and a verified restore path.

## Start here

1. Read [`AGENTS.md`](AGENTS.md) for workspace navigation and safety rules.
2. Read the relevant [`ports/<device>/AGENTS.md`](ports/README.md) and source project notes.
3. Run host-only checks before any hardware test; distinguish host-verified from device-verified results.

## Layout

- `AGENTS.md` — workspace instructions for agents.
- `docs/architecture.md` — repository boundaries, evidence labels, and source/license rules.
- `ports/` — small per-device guides and state; each port has its own `AGENTS.md`.
- `sources/` — pinned forks/upstream projects as Git submodules; do not merge their trees into this repository.
- `skills/` — reusable task playbooks.
- `tools/` — cross-port utilities. `tools/portsmith-image-tools` contains a reviewed, MIT-licensed subset adapted from iOSPlus10's generic image/IPSW tooling; Negroni-only `ctl` and `bootlog` commands are intentionally excluded.
- `docs/` — design notes and contribution/evidence conventions.

## Initial source set

See [`sources/README.md`](sources/README.md) and [`sources/manifest.toml`](sources/manifest.toml) for projects, upstream maintainers, licenses, and pinned revisions. Initial references include UniXNU, iOSPlus10, ios-sweet, ios-flame, ios-s9, and the existing Lavender device repository.

## Credits and contributors

Upstream projects and their creators are credited here and in [`CREDITS.md`](CREDITS.md): **akshaynexus** (iOSPlus10), the **UniXNU contributors**, **dipa-studio** (ios-sweet), **NWylynko** (ios-flame), and **syncmodz** (ios-s9), plus the Lavender work maintained by **Chromitsune**. Please read each upstream project's own license and notices.

These upstream authors are **not represented as Portsmith contributors** unless they actually contribute to this repository. GitHub's Contributors view is generated from commits; we credit reused/reference work without implying endorsement or direct contribution.

## Safety and evidence

- Do not flash without explicit authorization. A prior authorization for one test is not standing permission.
- Inspect the phone's current state before any reset; do not force a reset just to collect data.
- Never write `LOGFS`, guess register addresses, or infer DRAM retention from a PSCI reset request.
- Do not commit IPSWs, vendor firmware, device dumps, identifiers, root images, generated payloads, or personal calibration data.
- Label results `host-verified`, `device-verified`, `inferred`, or `unknown`; a build or screenshot alone is not proof of a working port.
