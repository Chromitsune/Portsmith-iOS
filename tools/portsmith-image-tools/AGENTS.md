# Portsmith image/IPSW host CLI

This Rust crate contains a reviewed, MIT-licensed subset adapted from iOSPlus10's generic image/IPSW tools. Read `UPSTREAM.md`, `UPSTREAM-LICENSE`, the crate README/CLI help and root `CREDITS.md` before changing it. Keep scope to host-side parsing/packaging; the current CLI does not authorize downloads or writes to a device. Do not reintroduce excluded Negroni-only `ctl`/`bootlog` tools or board-specific firmware/partition logic as generic commands without a separate audit.
