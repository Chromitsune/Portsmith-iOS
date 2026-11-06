# Redmi Note 10 Pro — DC28088 maintained Sweet source

This Portsmith entry now pins the **default `main` branch** of [DC28088/ios-sweet](repo/) at `8ba152f7132d3c25b5e2ff83b7f5455b8e01457f`, following the user's direction that this is the maintained line. Portsmith no longer tracks the old `codex/native-adreno-metal` branch.

## Evidence and caveats

- Read the pinned `repo/README.md`, `repo/NOTES.md`, and `repo/PRIVACY.md` before using any status claim. The README at this pin reports an iOS 16.7.16 home screen, native Adreno 618 Metal rendering, touch/buttons, Wi-Fi, Bluetooth pairing, USB debugging, battery state, and a writable UFS/HFS+ root.
- The same README says animation performance is not consistently smooth, audio/video/camera/cellular/sensors/sleep and production security remain incomplete, and some implementation history lives on `codex/native-adreno-metal`. Do not silently substitute that abandoned branch for the pinned `main` tree or attribute its files to this pin.
- Statuses are upstream-reported, not Portsmith verification. No device build, flash, or test was done for this update.
- The fork has no root `LICENSE` or recognized license grant at this pin. Keep it as a Git submodule reference only; do not copy or redistribute its code until the maintainer clarifies licensing.
- Its installer writes/erases `userdata`; flashing still requires explicit, current authorization.
