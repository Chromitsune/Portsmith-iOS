# Storage families: eMMC, UFS, and RAM-backed roots

“Storage driver” is not one interchangeable module. Keep the host/controller driver separate from common block-device, partition, and filesystem layers.

| Family | What may be shared | What stays board/SoC-specific | Portsmith examples |
|---|---|---|---|
| eMMC / SDHCI | Block I/O contract, GPT parsing, upper filesystem layer | SDHCI controller registers, clocks, regulators, tuning/voltage modes, DMA/SMMU | Lavender (eMMC, SDM660; its XNU block driver is not device-verified); separate A5XELTE experiment nested in the Herolte repo |
| UFS | UFS protocol/LUN concepts and the block interface | UFSHCI revision, PHY/clock/reset sequence, SMMU/DMA, firmware and bootloader state | Sweet, Flame, Snapdragon S9, Apollo, Negroni, Dada, and others; implementations remain in their pinned port repos |
| RAM / virtio block | Block-device and test interfaces | Memory ownership, DMA mapping, UEFI/virtio transport, lifetime | UniXNU `RamBlock` and `VirtioMmioBlock`; per-board selection still matters |

The catalog is informational. Do not transplant a UFS or SDHCI implementation just because two phones use the same media type. Verify the exact controller, SoC generation, DMA/IOMMU contract, and bootloader state first. No unmeasured physical addresses are recorded here.

## Concrete eMMC reference

`components/storage/emmc/NativeMsdc/source/` contains mouseos's BSD-2-Clause-Patent MT8167 MSDC0 eMMC driver snapshot, pinned to `e718d5d7bde7f6986cd9a7b425c82c50a4dcc3b8`. Its original `LICENSE`, README and upstream credits are retained. It is MediaTek MT8167-specific; it is not a generic SDHCI driver and is not compatible with Lavender's Qualcomm SDM660 by implication. Its README reports host tests/compilation but says this NativeMsdc implementation has not yet been booted. The earlier a04br3 eMMC observations do not qualify this driver or another board.
