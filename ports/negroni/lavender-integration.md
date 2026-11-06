# Lavender integration audit

This Portsmith note records the compatibility audit between Lavender and the upstream iOSPlus10/Negroni port. It is **not** a claim that the OnePlus 10 Pro image boots on Lavender. No device was booted or flashed while preparing this note.

## Decision: reuse the diagnostics design, not the Lavender implementation

The two targets have different board and boot contracts:

| | Lavender (Redmi Note 7) | iOSPlus10 / Negroni (OnePlus 10 Pro) |
|---|---|---|
| SoC | Qualcomm SDM660 | Qualcomm SM8450 / Snapdragon 8 Gen 1 |
| Storage | eMMC; Lavender's existing bring-up has no UFS | UFS; the current Negroni kernel/root path is UFS-based |
| RAM | about 4 GB, Lavender-specific map | 8/12 GB OnePlus map, Mu UEFI window and GPU carve-out |
| Boot | Xiaomi ABL, Lavender's carved-XBL EDK2 package; tested path flashes its boot image | OnePlus ABL -> Mu-Silicium/UniXNU, Negroni-specific DXEs and reboot-reason handling |
| Display | NT36672A 1080x2340, Lavender-specific continuous-splash mapping | Samsung 1080x2412 panel, Negroni display/GPU path |

Therefore do not copy a whole board config, MMIO address, memory layout, panel path, UEFI binary patch, UFS driver, or reset-reason implementation between them. Build Lavender as a separate board/SoC port; share only reviewed generic code and tooling.

## What the Lavender panic-recovery work contributes

The changes from `Chromitsune/UniXNU-Lavender` commits `599a6ff` and `37647e2` add:

- A kernel-image-resident 64 KiB console ring plus a locator; panic output is appended and cache-cleaned before a timed PSCI `SYSTEM_RESET`.
- DarwinBoot validation and best-effort archive to `\\EFI\\UniXNU\\bootlog.txt` on the next boot.
- A GPT `misc` Android BCB `boot-recovery` request, with read/modify/write, flush, and readback, to try to enter OrangeFox.
- Host tests for ring geometry and BCB preservation.

This is valuable evidence and an alternative for devices without a working USB log channel, but its ring depends on DRAM surviving the firmware/ABL/UEFI reset path; that remains unverified on Lavender. The device test was inconclusive. The BCB/ABL path is also unverified on Lavender.

## What iOSPlus10 already has (don't duplicate blindly)

The current Negroni source has an independent, generally stronger diagnostics path:

- XNU patch `patches/xnu/0367-negroni-bootlog.patch` writes boot records into a persistent ring in the Negroni userdata/UFS area, with a reserved log window and CRC/validation. It is designed to survive reset without relying on DRAM retention.
- `make bootlog` / `tools/op10tool bootlog` retrieves prior boot logs; `make usblog` captures the live kernel console over USB CDC-ECM.
- XNU patch `patches/xnu/0360-negroni-panic-usb.patch` keeps a panic hold loop, sends diagnostics over USB, and provides `ping`, `log`, `reboot`, `recovery`, `bootloader`, and `poweroff` commands. `negronipanic=N` enables a timed reset; zero keeps the panic display available, which is safer for diagnosis.
- `make boot-debug` turns the Negroni framebuffer console on (`negronifb_noconsole=0`). Normal builds mute text over the GUI while retaining logs.
- `scripts/kernel/test-bootlog-core.sh` host-tests the kernel log window, partition bounds, HFS+ layout, parser and CRC. This is stronger and more target-specific than transplanting Lavender's RAM-only ring tests.

On Negroni, the existing `recovery` command/reboot-reason path is the appropriate recovery mechanism to validate. Do not add Lavender's GPT `misc` BCB write to the OnePlus image unless its boot chain is separately shown to need and honor that BCB. Likewise, do not force a 20-second reset in the default profile; the existing indefinite panic hold plus optional timeout preserves time to inspect logs.

## Integration mapping

| Lavender feature | Negroni equivalent / action |
|---|---|
| Verbose panic text | Existing framebuffer panic/console and `negronifb_noconsole=0` debug profile; check readability on target. |
| Save diagnostics | Existing persistent bootlog ring plus USB live log; test that the panic record/end marker is present after panic and recovery. |
| Timed PSCI reset | Existing `negronipanic=N` path; do not duplicate with a hard-coded 20 s delay. Verify reset reason selection for any recovery test. |
| Archive old RAM ring in DarwinBoot | Not needed for Negroni's existing persistent UFS log. Only consider if logs cannot be retrieved by USB/recovery. |
| Write BCB to `misc` | Lavender/Android-specific option; not a default Negroni change. Negroni already has a reboot-reason command path. |
| Ring/BCB unit tests | Run `scripts/kernel/test-bootlog-core.sh`; add tests only for a demonstrably missing Negroni contract. |

## Safe next steps

1. Keep the Lavender-specific source repository and its device facts intact; this branch is an engineering/reference base, not a replacement for the working board repository.
2. Before attempting a Lavender port, inventory which generic `ios-sweet`/iOSPlus10 code can support SDM660 and which Negroni pieces depend on SM8450/UFS/Mu. Keep device code behind a distinct Lavender config and submodule revision.
3. For any panic/recovery change, first prove the host contract, then use a non-flashing or temporary boot path where supported. Lavender's ABL behavior and its last on-device result are not verified; inspect the phone before any new reset. No flash was authorized by this integration request.
4. Never write `LOGFS`, guess hardware addresses, or treat a PSCI reset as evidence of DRAM retention.
