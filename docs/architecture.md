# Portsmith architecture

Portsmith separates three layers:

1. **Workspace layer** — shared agent instructions, skills, source catalog, provenance, host-only tools and tests.
2. **Port layer** — one directory per physical device/board, with its own `AGENTS.md`, manifest, status, boot safety notes, evidence, and adapters.
3. **Source layer** — complete pinned device repositories under `ports/<port>/repo/`, shared framework submodules under `sources/`, and license-audited, exact-commit component snapshots under `components/<scope>/<name>/source/`. Component snapshots keep their original README/LICENSE/NOTICE and `UPSTREAM.toml` provenance; unresolved or mixed-license trees remain catalog-only. This is a source index, not a universal kernel tree.

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
- Keep hardware ports as their original pinned repositories; do not flatten them together.
- Vendor shared component code only after an exact-revision license/provenance audit. Preserve each original license/NOTICE and record origin URL and full commit in `source/UPSTREAM.toml` and `components/CREDITS.md`. Keep unresolved mixed/unlicensed projects as references only.
- Keep vendor firmware, Apple restore files, generated images, and per-device calibration/private data out of the repository.
