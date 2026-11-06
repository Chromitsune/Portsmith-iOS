# Negroni port agent notes

Canonical device/build source: `ports/negroni/repo`; read its `CLAUDE.md`, `docs/notes.md`, `docs/plan.md`, and `config/negroni-ne2211.toml` before touching device code.

This is the OnePlus 10 Pro (`negroni`, SM8450/Snapdragon 8 Gen 1, UFS, Mu-Silicium/UniXNU) port. Its `negroni_*` kernel patches, UFS log window, PMIC reboot path, GPU addresses, and Mu DXEs are device-specific.

Portsmith keeps the original iOSPlus10 repository as a pinned submodule at `ports/negroni/repo`; do not change its source through an unreviewed flattened copy. Lavender comparison notes are in `lavender-integration.md`. Preserve upstream licensing.
