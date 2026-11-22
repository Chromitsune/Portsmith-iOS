# Samsung Galaxy S20 LTE `SM-G980F` (`x1slte`) — full upstream port reference

**Pinned source:** [jesvi-eulah/Jesvi-iOS](repo/) at [`3d7b07ad64fbb6edf3e4b96cdce0312215992a20`](https://github.com/jesvi-eulah/Jesvi-iOS/commit/3d7b07ad64fbb6edf3e4b96cdce0312215992a20), branch `main`.

## This is a full port (upstream claim)

This project is an unusually complete, device-targeted iOS 16.5 port—not just XNU entry, a UI screenshot or a boot-menu demonstration. The upstream README describes a full system tree with kernel, loader, drivers, user-space glue and release tooling, and reports a broad set of working subsystems on the **Galaxy S20 LTE SM-G980F / Exynos 990**:

- display modes through FHD+/QHD/FHD up to 120 Hz, True Tone, brightness and AOD; multitouch and hardware buttons;
- Mali-G77 Metal acceleration and OpenGL ES through Mesa;
- 4G/LTE data, VoLTE calls and SMS; 2.4/5 GHz Wi-Fi, Bluetooth/audio and hotspot;
- front and three rear camera lenses, photo/video and main-lens autofocus; speaker, earpiece and microphone;
- motion, compass, proximity, gyro and light sensors; GPS, fingerprint features, battery/charging, thermal management and haptics;
- persistent UFS storage, microSD exFAT read/write, USB networking, Finder file access and serial console.

These are **upstream reports**, not Portsmith tests. The upstream project calls this a full port, but labels the release **Beta**, notes known bugs, and lists unfinished items such as Touch ID unlock, App Store, iMessage/FaceTime, standalone Apple ID and full GPS. Its docs identify VoLTE as AP-side VoIP-style calling, not the modem's native voice path. The project says only the SM-G980F with bootloader `G980FXXSNHYB7` boots; S20+ and S20 Ultra kernels build but have not booted. “Full port” here means a broad end-to-end implementation for this one device—not production-complete, independently certified or supported across the S20 family.

## Compatibility reported at this pin

| Feature | Status | Upstream evidence / limitation |
|---|---|---|
| Boot | Reported working (upstream) | README describes native iOS 16.5 on SM-G980F through its loader/XNU stack; exact-model report only. |
| GPU | Reported working (upstream) | Mali-G77 Metal acceleration and Mesa/OpenGL ES are reported. |
| Display | Reported working (upstream) | Multiple display modes up to 120 Hz, True Tone, brightness and AOD are reported. |
| Touch & Buttons | Reported working (upstream) | Multitouch, lock-screen pocket rejection and power/volume controls are reported. |
| Audio | Reported working (upstream) | Speaker, earpiece, microphone, video and call sound are reported. |
| Bluetooth | Reported working (upstream) | Bluetooth and A2DP audio are reported. |
| Wi-Fi | Reported working (upstream) | 2.4 and 5 GHz Wi-Fi are reported. |
| Cellular | Reported working (upstream) | LTE data, VoLTE calls and SMS are reported; calls are AP-side VoIP-style, not modem voice. |
| Camera & Sensors | Partial / limited | Cameras and several sensors are reported; GPS is partial and fingerprint matching/unlock is incomplete. |
| Power & Sleep | Partial / limited | Charging, battery gauge and thermal management are reported; sleep/wake is not established by this README. |
| USB | Reported working (upstream) | USB networking, Finder file access and serial console are reported. |
| Storage | Reported working (upstream) | Persistent UFS and microSD exFAT read/write are reported. |
| Stability | Partial / limited | Beta release, known bugs and no Portsmith long-run qualification. |

## Safety and license boundary

The documented fresh TWRP install erases Android userdata; restoring Android wipes the iOS data. Its install guide restricts support to the exact model/bootloader and has several confirmation/recovery steps. **Do not run installer, TWRP, Odin, Download Mode, flash, reboot or partition commands** without current explicit authorization. The upstream installer documentation itself contains historical qualification notes that should be reconciled before any end-user safety claim.

The root `LICENSE` grants MIT to project-authored non-XNU code; `xnu/hakios.patch` and `xnu/files/` are APSL-2.0. `NOTICE` and third-party compliance docs list separate origins, including vendor-derived files with unresolved/review-needed terms. The iOS 16.5 IPSW and phone firmware are fetched from the owner's sources/device and are not included or licensed by the repository. Portsmith stores only a pinned source pointer; no code, IPSW, firmware or release image was copied.
