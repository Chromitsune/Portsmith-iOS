# UniXNU component catalog snapshot

`unixnu-components.toml` is copied from the UniXNU framework repository pinned at `sources/UniXNU` revision `e2fdae4312d0acc3d8a52bc457101e7918095e6a`. Its 27 entries record upstream component IDs, exact source URLs/revisions, hardware scopes, OS ABIs, board dependencies, and component dependencies.

For license-cleared components, Portsmith contains the original repository tree as a vendored snapshot under `/components/<scope>/<name>/source/`, with `source/UPSTREAM.toml` recording its exact origin and revision. The original `LICENSE`, `NOTICE`, README, copyright headers, and license notices are retained. The source snapshots do not include Git history; the original URL and full commit identify provenance. The parent UniXNU license does not replace any component's terms.

`Ath12kWifi` and `QcaBluetooth` are catalog-only: their complete source trees were not copied pending license/provenance handling. This catalog describes upstream choices. It does not qualify a component for another port or independently verify it. Board clocks, resets, PHYs, MMIO ranges, SMMU/DMA rules, firmware, memory ownership, and OS ABI remain device-specific.
