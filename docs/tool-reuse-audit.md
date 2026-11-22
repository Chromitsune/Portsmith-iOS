# Boot-menu and cross-port tool reuse audit

**Status:** design-stage inventory. No upstream menu, driver, transport reader, firmware, or artwork source code was copied by this audit. Device-specific implementation remains in its source port. The neutral data and newly written host-only model/preview live in [`boot-menu/`](../boot-menu/); no upstream runtime was copied.

## Boot-menu layers

| Layer | Existing references | Generalization candidate | Keep platform-specific |
|---|---|---|---|
| Entry model | Guacamole `shim/menu.h` (`396a851ef112fd34003f0b37c3270bcd6c2e8cc2`); UniXNU `Menu.c`/`Internal.h` (`e2fdae4312d0acc3d8a52bc457101e7918095e6a`) | Stable entry ID, label/detail, abstract icon ID, enabled state, opaque target token | Loader volume/file paths, initrd/DTB pointers, kernel arguments and platform descriptors |
| Selection behavior | Guacamole input loop; UniXNU `Menu.c` timer/countdown loop | Model/state machine behind abstract input events and a monotonic clock; host fixture tests for default, disabled, timeout and confirmation policy | PMIC polling, UEFI `SimpleTextIn`, touch controller, hardware timer and reset/power-off |
| Renderer/layout | Guacamole `shim/menu.c`; UniXNU `Ui.c` GOP/text/headless modes and layouts | New canvas/render contract, responsive geometry, palette/font tokens, multiple looks | Direct framebuffer pointer/format/stride, GOP protocols, display timing and panel-specific coordinates |
| Menu configuration | UniXNU `Config.c` and TOML; Guac hard-coded entry setup | Presentation-only look/options data plus a host-tested selection model (staged in `boot-menu/`) | Boot arguments, target file paths, firmware variables, storage and installation workflow |
| Integration/dispatch | UniXNU `Boot.c`, `Main.c`, `UniXNUDxe.c`; Marble `integrate-menu.py` | Adapter boundary returning a selected opaque ID | Payload loading, UEFI boot entries, `boot_b`, Android chain-loading, partition/GPT/UFS operations |
| Assets/preview | Guac `shim/art.S` and `mkmenuart.py`; Portsmith QEMU renderer preview | Asset IDs/fallback policy and a mock renderer test | Original OS icons until per-file asset provenance is confirmed; no board image/firmware bundle |

**Decision:** make only the model, behavior contract and visual configuration platform-neutral. No upstream menu implementation was copied into `tools/`. The suggested [Logopedia iOS/Versions](https://logos.fandom.com/wiki/IOS/Versions) images were checked; Fandom’s general text license does not cover images and file-level reuse rights were unclear, so none were copied. The current `boot-menu/icons/` are original generic version labels, not Apple artwork. `boot-menu/` now contains Portsmith-owned profile data, schemas, a host-tested selection-only engine, an interactive terminal UI, an SVG preview, generic version badges, and a QEMU RAM-framebuffer fixture for three looks. These are presentation/model prototypes, not bootable firmware or platform adapters. Guacamole is a compelling design reference, not a generic boot implementation: its pinned menu uses PM8150 SPMI, a specific touchscreen, fixed 1440×3120 geometry, ABL, SWEETXNU payloads, UFS, and an on-device choice-record write. UniXNU better separates model, configuration, renderer and loop but is still UEFI-bound and carries boot resource details in its menu configuration. QEMU captures are renderer fixtures with mocked/no hardware I/O, not full boots or device tests.

## Shared components worth checking before any reuse

Portsmith already catalogs candidate families in [`components/manifest.toml`](../components/manifest.toml), with exact provenance in component `README.md`/`UPSTREAM.toml` and hardware caveats in `components/README.md`. Examples of useful abstractions or interface references are `ArmDTPlatform`, `ArmCpu`, `GopFramebuffer`, `DarwinBoot`, `XnuPrelink`, `RamBlock`, `VirtioMmioBlock`, `VerifiedRoot`, `ShengUfs`, and `ShengHidInput`. These do **not** combine into universal drivers: UFSHCI/PHY, eMMC/SDHCI, GPU generation, SMMU, display, reset and firmware contracts remain per-platform.

Do not promote `Ath12kWifi`, `QcaBluetooth`, or `viva-gpu` into shared source code without their required provenance/license review. Use the component matrix to discover related work, not as compatibility proof.

## Existing tools and what not to copy blindly

- Portsmith-owned repository tools: `tools/portsmith.py`, `checkout-sources.py`, `build-compatibility-matrix.py`, `watch-upstreams.py`, and audited catalog tooling. Their schemas/pins and tests are the starting points for repository automation.
- `tools/portsmith-image-tools/` is already a narrow, MIT-licensed adaptation of generic iOSPlus10 image/IPSW functions. Keep Negroni `ctl`/`bootlog` and device writers out.
- `tools/jobs/bg.sh`/`notify.sh` are an already credited MIT adaptation. Do not import more scripts without file-level review.
- `ports/guacamole-ios27/repo/tools/mkmenuboot.py` parses Android boot-image v2 and SWEETXNU payloads; it is not a general boot-image composer.
- `ports/guacamole-ios27/repo/tools/qemu-sweet.py` boots a SWEETXNU payload in a QEMU `virt` machine; it does not execute the selector menu.
- `tools/qemu-guacamole-menu-preview.py` is a small Portsmith-owned renderer fixture: it builds the pinned menu renderer with mocked key/timer/touch inputs. It deliberately does not emulate a boot chain or access device storage.
- `ports/sheng/repo/scripts/read-sheng-log.py`, `ports/alioth-taishang1024/repo/scripts/read-sheng-log.py`, `ports/axon7/repo` pstore instructions, and J716F ramoops readers rely on different storage/retention formats. Sheng's reader can issue a reboot by default. Their common reusable part is evidence provenance/packaging, not log transport or offsets; use `tools/device-log-capture.py` after a separately reviewed, read-only port-specific capture.

Before copying any candidate into main `tools/`: verify license/attribution and assets, exact source pin, hardware assumptions, data sensitivity, side effects, CLI contract, host tests and a clean-room mock; keep platform backends separate. A submodule pointer or an upstream working result is not a reuse grant or Portsmith verification.
