# Xiaomi 15 (`dada`) port notes

The full source snapshot is in [`repo/`](repo/), including its original `README.md`, `README.zh-CN.md`, `NOTICE.md`, and `LICENSES/`. It was compared against upstream commit `f1ae906fcc43ba8f763663257724ba938fb820ab` of [`superboyyy/hakios-arm64e-dada`](https://github.com/superboyyy/hakios-arm64e-dada) and matches after restoring the upstream root `.gitignore`. Do not edit or remove the upstream notices.

The source README reports an experimental iOS 26 arm64e/XNU port on Xiaomi 15 (`dada`, SM8750/Snapdragon 8 Elite): home screen, touch, Adreno 830 GPU via Metal → metal2vulkan → Turnip, and Bluetooth; Wi-Fi is unreliable, audio is partial, and camera/HDR/modem are not started. These are upstream claims, not independently verified by Portsmith.

This is a vendored source snapshot, not a Git submodule; `port.toml` records the upstream URL and commit. To refresh it, compare the upstream commit and review its `README.md`, `NOTICE.md`, `LICENSES/`, `.gitignore`, and the publishability scan before replacing the snapshot.

The upstream `tools/check-publishable.sh` flags two contributor email addresses embedded in patch provenance. These are legitimate upstream attributions, not credentials; do not strip them. Its scan found no firmware/private image artifacts. Re-run it and inspect warnings before future updates.

Do not copy this SM8750/arm64e/PAC, UEFI, memory, display, storage, or Adreno 830 code into Lavender (SDM660) without a separate hardware audit. Never commit IPSWs, firmware, device dumps, generated images, or per-device calibration data. No flash without explicit authorization.
