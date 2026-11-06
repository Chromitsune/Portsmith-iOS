# Shared source frameworks

Device repositories live in `ports/<port>/repo/` as complete source trees: most are pinned Git submodules to original maintainer repositories; Dada is a vendored snapshot pinned by commit in `manifest.toml`. This folder holds shared framework references used by more than one port; currently that is the common [UniXNU](UniXNU) framework.

Use a plain clone and `git submodule update --init` to initialize direct Portsmith sources. Avoid `--recursive`: at the pinned UniXNU revision `e2fdae4312d0acc3d8a52bc457101e7918095e6a`, a nested `drivers/ArmCpu` gitlink references `2e11cda72740b985dedde3e32ba72b0fd64eb475`, which the upstream repository rejected as unavailable (`upload-pack: not our ref`). Portsmith does not need that nested checkout: the license-cleared component snapshots are organized under `components/` at their own catalog pins. To inspect only the framework source, use `git submodule update --init sources/UniXNU` (without `--recursive`). `sources/manifest.toml` is the workspace-wide catalog of framework, port, and vendored component sources.

Do not commit Apple/vendor firmware, IPSWs, device dumps, keys, calibration data, generated images, or private build artifacts from any checkout. Preserve source licenses and notices. Vendored component snapshots include their exact source commit, URL, and original license but not the source Git history.
