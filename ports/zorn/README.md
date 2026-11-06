# Redmi K80 (zorn) (`zorn`)

**Upstream source:** [https://github.com/kerrinz/UniXNU-zorn@`ef13dcc71b9ca97bde15381d51fe74aeff81f854`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `zorn`
- **SoC:** `SM8650`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, AppleKeyStoreState, RamBlock, VerifiedRoot, GopFramebuffer, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/kerrinz/UniXNU-zorn/blob/ef13dcc71b9ca97bde15381d51fe74aeff81f854/porting.toml).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | Owner-confirmed desktop/unlock/icon taps and a retained-Data boot are reported; this does not establish all profiles or long-run reliability. Evidence: README.md; docs/evidence/dual-system-reinstall-2026-11-01.json. |
| GPU | Work in progress / incomplete | CPU-owned backing/source work is implemented, but README says hardware GPU execution/rendering/Metal remain unqualified. SOURCE ONLY, not device-verified: README.md; docs/evidence/gpu-owned-memory-integration-2026-10-30.json. |
| Display | Partial / limited | Desktop/lock-screen output and brightness register readback are reported; continuous presentation/brightness-slider behavior is not qualified. Evidence: docs/evidence/display-progress-repeat-2026-10-30.json; docs/evidence/brightness-dim-result.json. |
| Touch & Buttons | Partial / limited | Owner confirmed unlock and icon taps; multitouch/complex gestures and physical buttons are unqualified. Evidence: docs/evidence/touch-desktop-fast-qualified.json; docs/evidence/qualified-source-repeat-two-contacts.json. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | PMGR service publication/ABI source is present, but charging, battery, DVFS and sleep/wake are explicitly unqualified. SOURCE ONLY, not device-verified: native/pmgr/README.md; porting.toml [area power]. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | UFS-backed Data mount/retained marker reported on device; full Android cross-boot, power-loss integrity, endurance and stress remain unqualified. Evidence: docs/evidence/dual-system-reinstall-2026-11-01.json. |
| Stability | Partial / limited | Some bounded desktop/Data trials passed; a 900-second trial remained on the Apple logo and broad stress/long-term behavior is unqualified. Evidence: docs/evidence/cpu1-root-publication-stability-2026-10-30.json; README.md. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
