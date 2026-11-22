# Shared Portsmith host tools

This folder contains repository-owned inventory, source checkout, catalog materialization, compatibility generation, upstream watching, QEMU preview and evidence-ingestion tools. Before copying an upstream utility here, read `docs/tool-reuse-audit.md`, inspect its exact source/license and side effects, and keep hardware-specific adapters out of shared code.

- `portsmith.py`: read-only inventories/checks; `check` must remain non-device-probing.
- `checkout-sources.py`: explicit pinned submodule initialization; never recurse by default.
- `materialize-unixnu-available-ports.py`, `generate-unixnu-component-index.py`, `build-compatibility-matrix.py`: update generated files from pinned inputs; regenerate instead of hand-editing outputs.
- `watch-upstreams.py`: reports drift/lookup failure; never changes status to working automatically.
- `device-log-capture.py`: packages already-acquired local files/stdin only; no device access.
- `qemu-guacamole-menu-preview.py`: compile/render fixture with mocked hardware, not a shim/boot test.
- `portsmith-image-tools/`: reviewed Rust subset with its own source notices; see its local instructions.
- `jobs/`: host background job/notification helpers.

Run scripts from the repository root. Tests must state their evidence level and avoid device write/reset commands unless explicitly authorized. Keep outputs in ignored locations and run `python3 tools/portsmith.py check` plus relevant syntax/tests after edits.
