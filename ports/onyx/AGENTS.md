# Onyx source-reference notes

This folder tracks `Aymon-njz/hackios-xnu-kernel-Onyx` at the exact pin in `port.toml`. It is a **reference-only** port descriptor, not evidence that Onyx boots.

Before touching code, read the pinned `repo/README.md`, `repo/common/devices/onyx.conf`, `repo/docs/PORTING.md`, root `LICENSE`, and `repo/prebuilt/NOTICES.md` (plus any nested license/firmware notices). The repository's reported device results are for `redwood` and QEMU. Onyx has a profile, but the upstream README does not report an Onyx kernel build or device boot; `UEFI_FD` and DTB are external inputs.

Do not transfer Redwood addresses, firmware, display/touch/GPU behavior, or boot results to Onyx. Do not copy code from this source until each file and bundled component has been license-reviewed. Keep every compatibility cell Not tested unless pinned Onyx-specific evidence is added. No device operation is implied; flashing/reset still requires current explicit authorization and a verified recovery path.
