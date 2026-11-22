# Samsung Galaxy Tab S7+ Wi-Fi (`gts7xlwifi`) source reference

This wrapper pins `rui12366B/UniXNU-gts7xlwifi` at the exact main-branch revision in `port.toml`. The device page and `porting.toml` report iPadOS 17.7.11 on an SM-T970, SM8250 tablet. Portsmith has not built or tested it; preserve the upstream evidence level and cite logs at their own recorded run revisions.

Keep this profile distinct from [`ports/sm-t970/`](../sm-t970/), which is the separate `CakeAL/UniXNU-sm-t970` single-core bootstrap record. Same physical model does not mean same source, implementation or evidence. Do not merge assumptions or statuses across those repositories.

The upstream source documents a separate UEFI firmware tree, boot selector, ESP, native UFS root/Data, A650, drivers and proprietary-file inputs. The checked-in root `LICENSE` is BSD-2-Clause-Patent by default, with per-driver/per-kit upstream licenses, MIT-tagged files and APSL-2.0 XNU patches. Do not initialize nested submodules recursively or copy firmware, generated blobs, or source without reviewing every notice and source pin. No source code or firmware was copied into Portsmith.
