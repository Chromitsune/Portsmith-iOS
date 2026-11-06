# Redmi Note 12 Turbo / POCO F5 (marble), Qualcomm SM7475 (Snapdragon 7+ Gen 2) (MiLacy) (`marble-milacy`)

**Upstream source:** [https://github.com/MiLacy/UniXNU-marble@`78f4e7bf00e88129f8b6ef5680d81770d386832d`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `marble`
- **SoC:** `SM7475`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, ShengUfs, GopFramebuffer, XnuPrelink, DarwinBoot, QcomGeniSpi, VirtioMmioBlock, RamBlock
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** Keep the separate drivers/ShengUfs/LICENSE and review component provenance.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/MiLacy/UniXNU-marble/blob/78f4e7bf00e88129f8b6ef5680d81770d386832d/docs/REAL-DEVICE-TESTS.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Device boots XNU to the expected missing-root stop; a further device run reached launchd but /sbin/mount exited 66. See docs/REAL-DEVICE-TESTS.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Partial / limited | Device console output is visible through the XNU missing-root checkpoint; userland display is not established. See docs/REAL-DEVICE-TESTS.md. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Partial / limited | Device UFS/GCC/SMMU takeover and GPT read are recorded; root/launchd run then fails at missing boot-manifest-hash. See docs/REAL-DEVICE-TESTS.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
