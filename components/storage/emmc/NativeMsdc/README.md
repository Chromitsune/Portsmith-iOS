# NativeMsdc eMMC component reference

The source snapshot is in [`source/`](source/) at `e718d5d7bde7f6986cd9a7b425c82c50a4dcc3b8`. It retains its BSD-2-Clause-Patent license and upstream README/credits. Upstream credits include mouseos/edk2-mtk, mouseos/xnu_kernel_benesse_a04br3, and UniXNU.

This driver targets MediaTek MT8167 MSDC0, not Qualcomm SDM660 or generic eMMC/SDHCI. Its upstream README reports host compilation/tests but says the current NativeMsdc driver has not yet been booted. Do not transplant or treat this as Lavender verification.

Host-only results and the macOS compiler-flag caveat are recorded in [`TESTING.md`](TESTING.md).
