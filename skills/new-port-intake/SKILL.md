---
name: new-port-intake
description: Add a device port or source-only reference to Portsmith with exact provenance and license boundaries.
---

# New port/source intake

Use this when adding a repository, fork, device profile, or board to Portsmith.

1. **Identify and de-duplicate first.** Read the target's hardware identity (codename, model, SoC, storage, boot chain). Search `ports/`, `sources/manifest.toml`, and the pinned UniXNU catalog. If a fork resolves to the same commit/tree as an existing source, record it as an alternate URL instead of adding a duplicate checkout.
2. **Pin before reviewing.** Resolve the exact Git commit and branch. Read the README, board/profile files, agent instructions, submodule list, and relevant evidence at that commit—not at a moving branch head.
3. **Audit the license at that pin.** Record root and scoped licenses/notices. An absent or mixed grant means reference-only. A submodule pointer is not permission to copy code; do not flatten or adapt code until per-file and nested terms are reviewed.
4. **Choose the right representation.** A new device source gets `ports/<codename>/repo` plus `port.toml`, safety notes, and a README. A library/tool that is not a complete device port belongs under `sources/` or the component index. Mark reference-only work explicitly; do not create compatibility claims just because a repository exists.
5. **Keep catalog and support claims separate.** A UniXNU catalog state such as `available` validates that catalog record at sync time; it does not prove a build, boot, or working feature. Inaccessible revisions remain metadata-only.
6. **Update provenance and generated data together.** Maintain `.gitmodules`, `sources/manifest.toml`, per-port notes, and `compatibility/ports.json` as appropriate. Regenerate with `python3 tools/build-compatibility-matrix.py` and run `python3 tools/portsmith.py check` plus `python3 tools/build-compatibility-matrix.py --check`.
7. **Do not operate a device during intake.** Use host-side inspection only. Any reset, flash, partition write, or firmware operation needs current explicit authorization and a verified target/restore plan.

Record the source URL, exact SHA, evidence URL, license finding, and what was *not* tested.
