# Lavender port agent notes

Canonical device source: `sources/UniXNU-Lavender` (Git submodule). Read its `AGENTS.md`, `README.md`, `docs/panic-recovery-status.md`, and `board.toml` before touching device code.

Hardware contract recorded from the device: Xiaomi Redmi Note 7 (`lavender`), Qualcomm SDM660, 4 GB DRAM, eMMC (not UFS), Xiaomi ABL and a custom EDK2 package derived from its XBL, 1080x2340 NT36672A panel, SMC PSCI. This port is not the OnePlus 10 Pro/SM8450 configuration.

Current safety/status reminders:
- The earlier authorized test flash is complete; this is not authorization to flash again.
- The prior panic-recovery device run was inconclusive. Inspect the phone's current state before any reset.
- The PSCI reset/DRAM retention path and BCB/ABL-to-OrangeFox behavior remain unverified.
- Never write `LOGFS` or guess hardware register addresses.
- Keep build outputs and payload images ignored; do not commit them.

The `iOSPlus10` source is a reference for its agent workflow, logging and generic tools, not a drop-in SDM660 driver set. See `sources/README.md` and `docs/` for the integration boundary.
