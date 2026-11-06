# Portsmith architecture

Portsmith separates three layers:

1. **Workspace layer** — shared agent instructions, skills, source catalog, provenance, host-only tools and tests.
2. **Port layer** — one directory per physical device/board, with its own `AGENTS.md`, manifest, status, boot safety notes, evidence, and adapters.
3. **Source layer** — pinned Git submodules under `sources/`. Each stays a real upstream-derived repository with its own history and license; Portsmith records what it is useful for without flattening its code into a universal kernel tree.

## Why keep ports separate?

Two phones can share ARM64/XNU concepts yet differ in bootloader behavior, SoC generation, GIC/timer setup, page size, memory map, DRAM carve-outs, storage type, display path, reset reasons, and GPU submission ABI. Similar-looking code is not proof of portability. Portsmith should expose common interfaces/tools while leaving board-specific code isolated and explicitly selected.

## Evidence model

Every status entry should use one of these labels:

- `host-verified`: unit/contract test or build ran on a host; says nothing by itself about the device.
- `device-verified`: exact behavior observed on the named device/firmware, with logs or other reproducible evidence.
- `inferred`: reasoned from source or another port, not yet reproduced on target hardware.
- `unknown`: not established.

Record device model/variant, firmware, source commit, command, result, and limitations. A screenshot, successful compilation, or reset invocation alone does not establish a full boot or retained logs.

## Source and license rules

- Update a submodule pin deliberately; review and document the commit before changing it.
- Use adapters/submodules for upstream components. Avoid a copied multi-kernel monolith.
- Before copying code, check its exact license, keep required notices, and record origin path and commit in `CREDITS.md` or the component's `UPSTREAM.md`.
- Keep vendor firmware, Apple restore files, generated images, and per-device calibration/private data out of the repository.
