# UniXNU device catalog snapshot

This is a machine-readable snapshot of the entries listed on [unixnu.com/devices](https://unixnu.com/devices/), copied from `UniXNU/devices.toml` at commit `e2fdae4312d0acc3d8a52bc457101e7918095e6a`. It preserves all 265 repository records, URLs (stored upstream as `owner/repository`), revision pins, board/SoC metadata, component lists, and record states. The 79 records marked `available` have 73 reachable pinned source references: 72 optional Git submodules under top-level `ports/<name>/repo` and one matching sheng record that reuses the curated `ports/sheng/repo`. Six inaccessible revisions remain metadata-only. These are submodule pointers to original repositories, not code copied into the Portsmith superproject, and they are **not** Portsmith verification.

## Snapshot size and identity

- **265 records**: 150 legacy format 1 and 115 format 2.
- **79** marked `available`, **25** `invalid`, **11** `missing`, and **150** with no `record_state` (all format 1).
- **52 named SoC strings**; one record has no SoC value. The SoC field also contains non-chip labels such as `build tree` and `crosvm-gunyah`.
- **265 distinct owner/repository URLs** and GitHub repository IDs, but only **159 distinct short repository names** across **239 owners**. There are no exact duplicate repository identities; 41 short names recur under different owners, covering 147 records.
- **122 board/codename values**: 48 values occur in multiple records, covering 179 entries. Examples include `sheng` (26 records), `fuxi` (13), `picasso` (7), `nabu` (6), and `alioth` (5). These are alternate repositories/maintainers for boards, not that many distinct hardware devices.
- 12 records omit the `board` field. Three groups share exact commit SHAs (7 records total): `sheng` (3 entries), `raphael` (2), and another `sheng` pair (2). Compare commit IDs before treating them as distinct source trees.
- The catalog does not retain GitHub `isFork`/parent metadata, so repeated board names and repo basenames are signals for alternate maintainers, not proof of direct fork ancestry.

## Meaning of upstream record states

For format 2 entries, UniXNU's sync process fetches `board.toml` and `porting.toml` from the repository's default branch, validates the porting record, and marks it `available` if that record validates. `missing` means no record was found; `invalid` means validation failed. Format 1 entries do not receive these states.

Therefore, **`available` means a valid UniXNU porting-record snapshot was present at sync time**. It does not mean the code builds, the device boots, any feature is complete, or the reported hardware evidence was independently verified. Record completion levels can range from `planned` to `device-verified`; record validation is not device verification. See the pinned UniXNU [porting-record guide](https://github.com/UniXNU/UniXNU/blob/e2fdae4312d0acc3d8a52bc457101e7918095e6a/docs/porting/records.md).

Repository metadata does not establish license permission for each linked source tree. UniXNU's framework license does **not** automatically apply to every listed project or nested dependency. Review the selected repository's exact license and notices before source import or reuse.

## Query the snapshot

```sh
python3 tools/portsmith.py device-catalog --summary
python3 tools/portsmith.py device-catalog --state available
python3 tools/portsmith.py device-catalog --soc SM8550 --search sheng --all
```

Each reachable `available` record has an external, pinned source submodule under `ports/<name>/repo`, with generated Portsmith metadata/compatibility notes. The 12 manually curated ports remain distinguished by `catalog_record` being absent; catalog-derived wrappers do not imply independent validation. `portsmith.py ports --group-by <vendor|soc|storage|gpu|bootloader>` lists both sets. The six unavailable pins have generated metadata-only wrappers under `ports/<name>/` (no source repo or compatibility evidence). Additional full code copies/adapters should only be made after source, duplicate identity, safety and per-file license review.

To review the import plan, run `python3 tools/import-unixnu-available-sources.py --dry-run`; `--apply` refreshes the audited submodule pointers and their manifest records. Do not use a newer catalog revision with this audit map until the repositories, exact commits, licenses, and notices have been reviewed again.

The catalog snapshot's BSD-2-Clause-Patent license and source pin are recorded in `LICENSE` and `UPSTREAM.toml`. The catalog submodule checkouts retain their own repositories/notices; no code is flattened into Portsmith. No device was built, flashed, or reset to create this snapshot.
