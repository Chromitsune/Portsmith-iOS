# Negroni port agent notes

Canonical device/build source: `sources/iOSPlus10`; read its `CLAUDE.md`, `docs/notes.md`, `docs/plan.md`, and `config/negroni-ne2211.toml` before touching device code.

This is the OnePlus 10 Pro (`negroni`, SM8450/Snapdragon 8 Gen 1, UFS, Mu-Silicium/UniXNU) port. Its `negroni_*` kernel patches, UFS log window, PMIC reboot path, GPU addresses, and Mu DXEs are device-specific.

Portsmith is initially an index/workbench. Do not change the OnePlus source through an unreviewed flattened copy; use its pinned fork/submodule and preserve upstream licensing.
