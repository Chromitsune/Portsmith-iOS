# Compatibility checklist workflow

`ports.json` is the source of truth for the per-feature checklist. The generated [`MATRIX.md`](MATRIX.md) works in GitHub's Markdown view; [`../docs/compatibility-matrix.html`](../docs/compatibility-matrix.html) is a dependency-free interactive view with editable dropdowns. The HTML stores edits in that browser's local storage and can export them, but it does not write to GitHub or alter the checked-in source data. Open the HTML file in a browser, or serve the repository with `python3 -m http.server` and visit `/docs/compatibility-matrix.html`.

## Status vocabulary

- **Reported working** — the pinned upstream project explicitly reports the feature. This is not Portsmith verification.
- **Partial / limited** — upstream reports partial behavior, limitations, or a development path with important gaps.
- **Work in progress / incomplete** — upstream says work is ongoing, incomplete, or not started.
- **Reported unavailable** — upstream explicitly says the feature is unavailable or absent.
- **Not tested / no evidence** — Portsmith's current source notes do not provide a comparable result. It does not mean broken.
- **Not applicable** — only when the capability genuinely does not apply to that device.

Each port row includes its source URL and exact pinned revision. Filled cells include a short evidence note; the source link resolves to the pinned README/NOTES/porting record. Avoid inferring storage, CPU, power, or stability support from a successful UI alone. Do not mark a capability “working” from a compile or source implementation alone.

## Sweet source distinction

The canonical `sweet` port remains pinned to the MIT-licensed `dipa-studio/ios-sweet` baseline. The requested [DC28088/ios-sweet](https://github.com/DC28088/ios-sweet) repository is already tracked separately as `sweet-native-metal`, pinned to its `codex/native-adreno-metal` development branch. The two branches/repos have diverged; the DC28088 fork has no recognized root license. Keeping them separate avoids silently replacing the licensed baseline with an unlicensed fork or implying branch equivalence. Its current matrix row points to the requested repository and commit.

## Updating the checklist

1. Review the pinned source's README, NOTES, porting/status record, and exact commit. Record whether the claim is upstream-reported or actually verified by Portsmith.
2. Edit `ports.json`; add a concise `detail` to every non-`not_tested` cell. Keep `repo_revision` current only after the source pin has been deliberately reviewed.
3. Render/check views: `python3 tools/build-compatibility-matrix.py` and `python3 tools/build-compatibility-matrix.py --check`.
4. Run `python3 tools/portsmith.py check` and submit the data/evidence change as a reviewed pull request.

## Upstream monitoring automation

The scheduled GitHub workflow runs `tools/watch-upstreams.py`. It compares direct port/framework repository pins with their configured branch heads and, on change, opens a pull request that updates `upstream-watch.json` with compare links and any changed README/NOTES/porting/status files found by GitHub's compare API. The first run found a newer sheng Bluetooth report; its review is recorded in [`review-notes.md`](review-notes.md).

**It never changes a compatibility cell to “working.”** A commit may contain a refactor, a regression, or no hardware work at all, so source activity is not evidence of hardware compatibility. The review PR is a prompt to inspect new evidence and manually update `ports.json`. If an upstream later publishes a versioned machine-readable compatibility report, Portsmith could import that report with a separate schema and keep its source/evidence attribution; no such common contract exists across these projects today.

The workflow needs repository Actions enabled and permission for `GITHUB_TOKEN` to create pull requests. It can also be run locally with `python3 tools/watch-upstreams.py --output compatibility/upstream-watch.json`.

For example, the current watcher flags new sheng Bluetooth documentation. Even though the newer upstream `porting.toml` labels that area device-verified, the cited positive evidence is from older local builds and the current report records startup failures and pending device checks. Portsmith therefore does not flip the pinned matrix status. See [`review-notes.md`](review-notes.md).
