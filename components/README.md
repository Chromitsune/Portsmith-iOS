# Shared component catalog

Ports can be browsed by vendor, SoC, storage, GPU, or boot family with `python3 tools/portsmith.py ports --group-by <field>`. Candidate reusable components are indexed in [`manifest.toml`](manifest.toml) and can be listed with `python3 tools/portsmith.py components`.

This is a **catalog of compatibility and code locations**, not a place to copy board drivers prematurely. Share stable interfaces and protocol-level code where demonstrated; keep MMIO addresses, clocks, regulators, SMMU setup, DMA constraints, firmware, and boot/reset behavior in the matching SoC/board port. A shared media type (eMMC/UFS) does not mean controllers are interchangeable.
