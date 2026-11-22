# Portsmith workspace agent instructions

## Mission and state

Portsmith is a research and coordination workspace for XNU/iOS bring-up on non-Apple ARM64 hardware. It is **not** a merged operating system, universal firmware image, or blanket compatibility claim.

The repository currently indexes 95 port profiles, 118 pinned source references, and the 265 records in its pinned UniXNU device-catalog snapshot. The root compatibility table is generated from `compatibility/ports.json`. It distinguishes upstream reports from Portsmith host/device evidence. Counts can change; `README.md` and the manifests are the live inventory.

## Repository map

- `.github/`: repository CI/workflow configuration; workflows should remain host-only unless an explicitly reviewed test says otherwise.
- `boot-menu/`: Portsmith-owned, declarative menu looks/options/schemas plus a host-only selection model, keyboard-driven terminal UI and SVG/QEMU previews. It is **not** bootable firmware or a platform backend.
- `compatibility/`: editable feature/status inputs (`ports.json`) and upstream-watch report. `docs/compatibility-matrix.html` and the marked README table are generated outputs.
- `components/`: source snapshots and compatibility notes. Read the component README, `component.toml`, `UPSTREAM.toml`, source license and family matrix before reuse; the manifest is not portability proof.
- `docs/`: architecture, research/audit notes, evidence conventions and screenshots. Screenshots must say whether they are device, full emulator, or renderer/mock output.
- `logs/`: git-ignored runtime output only. Keep device logs and sensitive data out of Git.
- `ports/`: separate device/source profiles. Port-specific `AGENTS.md`, `port.toml` and README describe each hardware/boot contract. `repo/` is commonly a pinned external repository; Dada is a vendored snapshot. `ports/catalog/` is the separate UniXNU catalog and generated wrapper data.
- `skills/`: reusable task playbooks. Load the relevant `SKILL.md` before port intake, evidence changes, host validation or log triage.
- `sources/`: shared UniXNU framework and optional reference source submodules, indexed in `sources/manifest.toml`.
- `tools/`: Portsmith inventory/validation, source checkout, catalog/matrix generation, upstream monitoring, QEMU renderer preview and reviewed host utilities. Read `tools/README.md` and the local `tools/AGENTS.md` before changing a utility.

## First steps for every task

1. Read this file and the root `README.md`; check `git status --short` and current source pins before editing.
2. Load the matching skill from `skills/README.md`.
3. Use `python3 tools/portsmith.py ports --group-by soc|vendor|storage|gpu|bootloader` and `python3 tools/portsmith.py components` to find related profiles/components. Read the specific port's `AGENTS.md`, its `port.toml`, source project's own guidance and current status/evidence notes.
4. Preserve each source pin and license boundary. Submodule pointers are not a license grant. Do not recursively initialize submodules without path-specific review.
5. Prefer host-only inspection/tests. Record exact commands, revisions, hashes and what the test does **not** prove.
6. Before finishing, update any generated outputs through their source/generator, run the checks below, review `git diff --check`, and summarize outstanding questions.

## Canonical device-log workflow

There is no universal on-device log transport: ADB, recovery, serial/USB CDC, retained RAM, persistent log partitions and QEMU each have different prerequisites and side effects. Use [`docs/device-log-method.md`](docs/device-log-method.md) and [`skills/device-log-triage/SKILL.md`](skills/device-log-triage/SKILL.md).

1. Prefer existing host artifacts/logs. Inspect the phone's present state and identify the exact port, model, source/image revision and transport before acquisition.
2. Choose the least disruptive, port-documented path that covers the relevant boot stage. Read only the documented file/range with the matching reader/decoder; do not guess offsets or dump whole partitions as a shortcut.
3. Do not reboot to recovery, boot a reader image, use a console reset command, clear logs, change slots or issue other state-changing commands merely to make logs available. Any reset/boot/write needs current explicit authorization and an exact target/effects summary.
4. Keep raw bytes separate from decoded/symbolized copies. Record transport, sanitized command, state-before, source commit, image SHA-256, range/format, raw length/hash, and evidence level. Do not put serials, ECIDs, credentials, firmware, user data or private captures in the manifest or Git.
5. After a separately reviewed read-only acquisition, normalize a local file with `python3 tools/device-log-capture.py`. That helper reads only a local path/stdin and writes the raw capture plus a provenance manifest under ignored `logs/<port>/<run-id>/`; **it does not connect to or control a device**. Use `--evidence-level host` for QEMU, and `device` only for a real device capture.
6. Use existing source-specific tools only after reading their defaults. Some scripts named “read log” perform a reboot/reset after capture (for example, the Sheng reader); do not run such defaults without current authorization.

Useful distinctions: `adb logcat -d` is Android userspace, not XNU kernel logging; a missing ramoops/persistent ring can reflect configuration or overwrite, not a specific failure; QEMU output is host evidence, never a phone result.

## Port and source boundaries

- Treat every `ports/<id>` as a distinct hardware, boot, firmware and evidence contract. Similar SoCs/codenames do not justify copying addresses, memory maps, reset flows, storage offsets, display/touch timings, drivers or boot assumptions.
- Preserve the current pin and upstream documentation. If the live source advanced, document drift; do not silently move a pin.
- Before adapting code, inspect the exact repository/file license and provenance. Record origin path and commit in `CREDITS.md` or component `UPSTREAM.md`; preserve notices and third-party carve-outs.
- Catalog `available`, source compilation, mock UI rendering and upstream “device-verified” records do not become Portsmith device verification. Use the evidence level that the exact source supports.
- Shared components are scoped experiments, not universal drivers. Do not mark an implementation compatible without board/SoC/controller-level review.
- `boot-menu/` contains only neutral profile data and UI contracts. Keep entry display/model, rendering, input, timer, target dispatch and optional preference storage separate. The Guacamole QEMU preview is renderer-only with mocked I/O; the generic `boot-menu/qemu-preview.py` renders profile looks in a toy guest. Neither runs a real boot chain or accesses a device. Do not copy menu code/art or use its UFS/boot-slot behavior generically without the documented audit and license review.

## Folder-level `AGENTS.md` policy

Each Portsmith-owned folder should have a concise local `AGENTS.md` describing its purpose, owned files, safe workflows, and the next folder/source to read. Existing per-port instructions are authoritative for their own profile; parent instructions add shared rules.

Do **not** add or edit Portsmith instructions inside external `ports/*/repo` or `sources/*` submodules, vendored/component source snapshots, generated record trees, build outputs, `__pycache__`, or ignored log/artifact directories merely to make the count exhaustive. Those folders have their own provenance/owners or are disposable. Put local guidance at the nearest Portsmith-owned wrapper/category boundary. Generated wrapper changes belong in their generator/templates and must be regenerated, not hand-edited.

## Safety

- Never flash, reset, reboot, change slots, alter GPT/partitions, or write device storage without explicit, **current** user authorization. Earlier authorization does not carry forward.
- Before any proposed device action, identify the exact physical target, present state, expected effect, recovery path and exact command; ask if any identity or effect is uncertain.
- No LOGFS writes, guessed register/partition addresses, or DRAM-retention claims from PSCI reset alone.
- Keep backups, serials, ECIDs, calibration data, private keys, IPSWs, vendor firmware, root filesystems and raw sensitive logs out of Git.

## Common commands

- `python3 tools/portsmith.py ports --group-by soc` — inventory/group profiles.
- `python3 tools/portsmith.py components` — inspect scoped shared-component candidates.
- `python3 tools/portsmith.py check` — validate manifests and source pins without probing hardware.
- `python3 tools/build-compatibility-matrix.py` after editing `compatibility/ports.json`; `--check` validates generated outputs.
- `python3 tools/checkout-sources.py --curated`, `--name <record>`, `--available`, or `--reference <source>` initializes explicit pinned submodules. Do not add `--recursive`.
- `python3 tools/watch-upstreams.py --no-compare-api --output compatibility/upstream-watch.json` refreshes the review report; lookup failures remain review items.
- `python3 tools/qemu-guacamole-menu-preview.py` creates a renderer fixture only; it is not a boot test. `python3 tools/portsmith.py check` does not cover the menu schema: run `python3 boot-menu/check-configs.py` and `python3 -m unittest discover -s boot-menu/tests -v`.
- `python3 tools/device-log-capture.py --help` documents offline log ingestion/metadata.
- `python3 tools/import-unixnu-available-sources.py --dry-run` previews catalog imports.
- Build/test only the nearest relevant host target. Do not run hardware steps unless separately authorized.

Run `python3 tools/portsmith.py check`, the relevant host/schema/unit checks, `python3 tools/build-compatibility-matrix.py --check` when applicable, and `git diff --check` before committing.
