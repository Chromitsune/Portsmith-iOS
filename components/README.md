# Portsmith component workspace

Components are grouped by their upstream scope (for example, `storage/`, `gpu/`, `graphics/`, `controller/`, `display/`, `soc/`, and `board/`). License-cleared source repositories are **vendored as exact commit snapshots** under each component's `source/` directory so agents can inspect the code directly without initializing a separate submodule. Each snapshot includes its original README, LICENSE, copyright headers, and NOTICE when present; `source/UPSTREAM.toml` records the origin, commit, and license. The snapshot does not retain upstream Git history, so the URL and full commit are part of the provenance record.

Read each component's `README.md`, `component.toml`, `source/UPSTREAM.toml`, and original license before reuse. `components/manifest.toml` is the cross-port family catalog; `components/imported.toml` and `catalog/unixnu-components.toml` preserve the source component metadata. Board-specific modules, including several sheng/SM8550 components, are not generic drivers. A component's upstream use or verification does not imply Portsmith compatibility.

`Ath12kWifi` and `QcaBluetooth` remain catalog-only because their source trees need file-level license/provenance handling; their code has not been copied. Do not infer the parent UniXNU license applies to them. Keep eMMC, UFS, GPU, Wi-Fi, Bluetooth, display, and Metal/graphics sources distinct and check hardware scope before adapting.

Run `python3 tools/portsmith.py components` for the compatibility index and `python3 tools/portsmith.py check` for host-side manifest/pin validation. These commands do not probe a device.
