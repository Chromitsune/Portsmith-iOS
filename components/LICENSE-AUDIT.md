# Component source license and provenance audit

This audit is based on the exact source revisions in `sources/UniXNU/components.toml` at UniXNU commit `e2fdae4312d0acc3d8a52bc457101e7918095e6a`. The individual source archives and root license files were checked at those pins; the UniXNU parent license was **not** applied automatically to component repositories. This is a source inventory, not legal advice and not a full audit of transitive dependencies, vendor firmware, or generated files.

## Vendored snapshots

The following 25 UniXNU component repositories were snapshot-eligible: each pinned tree had a root `LICENSE` with a clear license. Every original source tree, including its license, README, copyright headers, and `NOTICE` where present, is retained under `components/<scope>/<name>/source/`. `source/UPSTREAM.toml` records the exact upstream URL, full commit, and license. `components/CREDITS.md` gives the per-repository links and pin table.

- **BSD-2-Clause-Patent:** ArmCpu, ArmDTPlatform, ArmVirtPlatform, DarwinBoot, ShengHidInput, QcomGeniSpi, GopFramebuffer, SoftwareAES, AppleKeyStoreState, RamBlock, VirtioMmioBlock, VirtioMmioConsole, XnuPrelink, AdrenoFirmware, VerifiedRoot, Sm8550Platform, ShengPreflight.
- **BSD 2-Clause:** ShengUfs and QcomBaseband.
- **MIT:** Adreno740, AdrenoMetal, AdrenoPM4, ArmSmmu4K, AirNir.
- **Apache-2.0:** ShengNovatekTouch. Both its `LICENSE` and `NOTICE` are retained; the notice records its implementation provenance and Linux protocol research.
- **Community eMMC reference:** mouseos/NativeMsdc, BSD-2-Clause-Patent at `e718d5d7bde7f6986cd9a7b425c82c50a4dcc3b8`. Its own README/credits are retained. It targets MT8167 MSDC0, not Lavender/SDM660; the current NativeMsdc driver is reported by its README as not yet booted.

The snapshot retains source files and notices but not Git history. Full origin links and commit IDs are retained, and original README/credit sections remain in each snapshot. We do not claim those upstream authors contributed to Portsmith.

## Catalog-only; code deliberately not copied

- **Ath12kWifi**, `28de7b91d7a880682b777e0e3564245a99dbc3f5`: no root `LICENSE`, `COPYING`, or `NOTICE` was found. Some individual files carry GPL-2.0 headers, but that does not establish a license for the full tree. Keep the URL/pin in the catalog and request a clear scoped license from maintainers before copying.
- **QcaBluetooth**, `22ff97f93416452335bb61badb14c762da653487`: file-level licenses are mixed (`GPL-2.0-only`, `APSL-2.0`, `BSD-2-Clause-Patent`, `BSD-3-Clause`) and the root `NOTICE` attributes the different portions. A blanket repository copy would require per-file attribution/license handling and compatibility review. Keep only its source URL/pin until that work is done.

Neither reference-only component has code under `/components`; their catalog metadata makes the license limitation explicit. Do not treat the entire UniXNU repository's license as permission to reuse their code.

## Verification

- License and source checks were performed against the pinned component revisions, not current default branches.
- No code was imported from the two reference-only repositories.
- The imported source trees were checked for nested Git submodules and large firmware/image archive files before snapshotting; none were found in the 25 licensed UniXNU component trees or NativeMsdc.
- This import did not run a device build, fetch proprietary firmware, flash, or reset a device.
