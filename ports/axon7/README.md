# ZTE Axon 7 A2017G (`axon7`) — reference-only port

**Pinned source:** [devilAPI/zte-axon7](repo/) at `60ccb0edcd32d1518f504548a0ae257d15ff9863`.

The parent repository describes a ZTE Axon 7 A2017G (`ailsa_ii`/`axon7`) multi-boot project, including iOS 16.7.16. Its README reports an on-device lock/home-screen result with touch, Adreno 530 GPU acceleration, sound, and Wi-Fi. These are **upstream reports**, not Portsmith verification. The iOS implementation is a nested `devilAPI/ios-sailfish` submodule pinned by the parent at `aae05df53f4b6913b5aa3abb2ac763b7aeaf7295`; it is not recursively initialized here.

The parent README declares APSL-2.0 for project sources, but no root LICENSE file is present. Its nested kernel/source and third-party assets have separate provenance and licenses. This Portsmith entry is a source pointer; no code was copied. Review each nested project and file before reuse.

## Compatibility at the pinned source

| Feature | Status | Upstream evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | README reports iOS 16.7.16 reaches lock/home on A2017G through ZTE LK and a shim; no Portsmith test. |
| GPU | Partial / limited | Adreno 530 GLES through Mesa/freedreno is reported; Metal for apps remains in progress (293/456 shaders in README). |
| Display | Reported working (upstream) | README reports lock/home UI on the 1440x2560 split-DSI panel. |
| Touch & Buttons | Reported working (upstream) | README reports Synaptics multitouch and physical keys; Volume Down provides Home. |
| Audio | Reported working (upstream) | README reports speakers and the main microphone. |
| Bluetooth | Reported unavailable (upstream) | README lists Bluetooth as not working yet. |
| Wi-Fi | Partial / limited | Parent README reports Wi-Fi/rejoin working, but pinned nested [ios/PORTING-AXON7.md](https://github.com/devilAPI/ios-sailfish/blob/aae05df53f4b6913b5aa3abb2ac763b7aeaf7295/PORTING-AXON7.md) records rejoin-after-disconnect DHCP failure; conflicting upstream evidence, conservatively Partial. |
| Cellular | Reported unavailable (upstream) | README lists cellular as not working yet. |
| Power & Sleep | Partial / limited | README says the phone discharges under the kernel; sleep/resume behavior is not reported. |
| Camera & Sensors | Partial / limited | Camera preview/photos are reported; other sensors are not established. |
| USB | Not tested | The loader USB link is not evidence for iOS USB support. |
| Storage | Reported working (upstream) | README reports a writable journaled HFS+ iOS root on UFS and data surviving reboot. |
| Stability | Partial / limited | Experimental, time-bounded sessions; no long-duration or thermal qualification is reported. |

See the [Portsmith compatibility matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
