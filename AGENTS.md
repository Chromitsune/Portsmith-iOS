# Portsmith workspace instructions

## Context loading

1. Start with `README.md` and `sources/manifest.toml`.
2. For a device task, read only the relevant `ports/<device>/AGENTS.md`, the referenced source's own instructions, and its current handoff/status notes.
3. Before coding, inspect `git status`, source pins, and existing generated outputs. Keep builds/logs outside tracked source.
4. At the end, update the device status with facts, commands, hashes, tests, and unresolved questions so the next agent can resume without reconstructing the session.

## Safety

- Never flash a device or write a partition without explicit, current user authorization. An earlier one-time authorization does not carry forward.
- Before any reset, inspect the phone's current screen/connection/state. Do not reset merely to test a theory.
- Never write `LOGFS`, invent register addresses, or claim DRAM retention based only on PSCI `SYSTEM_RESET`.
- Prefer host tests, read-only inspection, and temporary copies. State exactly what a test did and did not touch.
- Keep stock backups, serials, ECIDs, calibration data, private keys, IPSWs, vendor firmware, root filesystems, and generated images out of Git.

## Port boundaries

- Treat each `ports/<device>` as a separate hardware/boot contract. Do not copy addresses, memory maps, reset paths, display timings, storage drivers, or firmware assumptions across devices without evidence.
- Source repositories are pinned submodules. Preserve their history and licensing; make port-specific changes in the correct fork/submodule, not as a flattened copy.
- Before borrowing code, check its license and record its original repository/path/commit in `CREDITS.md` or the component's `UPSTREAM.md`.
- Do not call something “working” from compilation alone. Separate `host-verified`, `device-verified`, inference, and unknown.

## Changes and verification

- Keep changes small and testable. Run the nearest host test and `git diff --check`.
- Never modify a tracked submodule pointer without explaining why and recording the tested commit.
- Before any destructive command, summarize the exact target and expected effects; get approval if not already explicit.
