# Shared tools

## Workspace inventory and preflight

`python3 tools/portsmith.py ports` lists ports; add `--group-by vendor|soc|storage|gpu|bootloader` to group them. `components` lists shared families and compatibility notes; `sources` prints commit pins and upstream URLs; `check` validates port/source/component metadata and flags dirty or uninitialized checkouts; `doctor` reports host tools without probing or controlling a phone. These commands are read-only.

## Jobs

`tools/jobs/bg.sh NAME COMMAND...` starts a long command in a detached `tmux` session, saves output to ignored `logs/NAME.log`, records the exit code, and sends a best-effort desktop notification. `tools/jobs/bg.sh -s NAME` reports status; `tools/jobs/bg.sh -l` lists sessions. This is adapted from iOSPlus10's MIT-licensed `scripts/bg.sh` and `scripts/lib/notify.sh` (see file headers / upstream credit).

## Device log evidence

`python3 tools/device-log-capture.py` packages an already-acquired local file or stdin stream under ignored `logs/<port>/<run-id>/` and writes a manifest with UTC time, transport, evidence level, source/image pins, byte count, SHA-256, and optional source range/decoder format. It never runs ADB, fastboot, serial commands or any device action. Acquisition itself must use the documented, read-only port-specific path in [`docs/device-log-method.md`](../docs/device-log-method.md).

## Boot-menu staging

`boot-menu/` contains neutral look/options/profile data and a host-only selection/SVG preview prototype. It has no device backend or boot executor. The Guacamole QEMU preview is explicitly a mocked renderer fixture, not a universal boot menu or device test. Read [`docs/tool-reuse-audit.md`](../docs/tool-reuse-audit.md) before moving code from a port into shared tools.

## Image and firmware CLI

`portsmith-image-tools/` is an initial Rust CLI adapted from iOSPlus10's MIT-licensed `tools/op10tool`:

- `img2simg`, `simg2img`, `hfs-size`
- `ipsw-get` (remote ZIP range download, resumable chunks, CRC check)
- `im4p` (Apple IM4P payload extraction; does not download or distribute Apple files)
- `uefi-unpack` (UEFI firmware-volume/FFS inspection)

Build with `cargo build --release --manifest-path tools/portsmith-image-tools/Cargo.toml`; see `--help` for arguments. These functions are source-level tools, not permission to write to a device. `ctl`, `bootlog`, and OnePlus/R0Q UEFI patching are deliberately not called universal and remain only in the iOSPlus10 submodule.

Before adding a universal tool, check if it contains board-specific addresses, reset semantics, partition offsets, firmware, or a hardcoded network protocol. Keep those in a port backend.
