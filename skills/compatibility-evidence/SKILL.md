---
name: compatibility-evidence
description: Audit a pinned device source and maintain Portsmith's per-feature evidence without overclaiming.
---

# Compatibility evidence audit

1. Read the exact pinned repository revision and the specific README, porting record, diagnostics, test, or report that supports each claim. Never cite only the default branch.
2. Separate host/source evidence from device evidence. Compilation, CI, QEMU, fixture runs, and configuration validation do not prove a phone boot or feature works.
3. Map evidence to Portsmith's feature taxonomy conservatively. If no direct, comparable evidence exists, use `not_tested`; do not infer from a catalog state, same-SoC port, fork, or adjacent component.
4. Use `reported_working`, `partial`, `in_progress`, or `reported_unavailable` only with an evidence detail and exact source link. A report is upstream-reported unless Portsmith itself performed and recorded the test.
5. Keep board- and generation-specific scope explicit (storage controller/media, GPU generation, display, USB, reset path). Do not transfer a driver claim between devices merely because the vendor or SoC family matches.
6. For inaccessible or missing source revisions, keep the record metadata-only and features `not_tested`; link the catalog page if useful but do not promote unreviewed cached claims.
7. After edits, regenerate the README/HTML matrix and run the manifest/matrix checks. Record open questions and preserve existing evidence rather than silently replacing it.
