# Upstream provenance

The Rust modules in this directory are adapted from `tools/op10tool/src/` in
[iOSPlus10](https://github.com/akshaynexus/iOSPlus10), pinned in Portsmith at
`505ae76ba72f82c336e2a194b47a3145cdbbcf17` (`Chromitsune/iOSPlus10`, branch
`lavender-panic-recovery`). The copied modules are `img2simg.rs`, `ipsw.rs`,
`im4p.rs`, and `uefi.rs`; the CLI has been reduced to those cross-port
operations.

The original repository's `ctl`, `bootlog`, and `uefi-portpatch` commands are
not exposed here: the first two speak Negroni-specific protocols/layouts and
the latter contains a OnePlus/R0Q porting strategy. A target-specific backend
must be reviewed before adding any of those capabilities.

The upstream MIT license is preserved in `UPSTREAM-LICENSE`. Each later edit
must retain this provenance and must not accidentally carry over iOSPlus10's
phone-specific addresses, firmware, or partition assumptions.
