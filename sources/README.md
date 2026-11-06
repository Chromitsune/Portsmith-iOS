# Shared source frameworks

Device repositories live in `ports/<port>/repo/` as complete, pinned Git submodules with their original READMEs and histories. This folder holds shared framework references used by more than one port; currently that is the common [UniXNU](UniXNU) framework.

Use `git clone --recurse-submodules` (or `git submodule update --init --recursive`) to materialize the full trees. `sources/manifest.toml` is the workspace-wide catalog of both shared frameworks and port repositories.

Do not commit Apple/vendor firmware, IPSWs, device dumps, keys, calibration data, generated images, or private build artifacts from any checkout. Preserve the source repository's license and history.
