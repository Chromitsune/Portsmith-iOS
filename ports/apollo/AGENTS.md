# Xiaomi Mi 10T family (`apollo`) port

Source is `repo/`, pinned to `aTechGeekDev/ios-apollo` main; read its README, `NOTES.md`, and `userland/README.md` for current status. The device family is Xiaomi Mi 10T / Mi 10T Pro / Redmi K30S, Qualcomm SM8250/Snapdragon 865.

Upstream's dated status reports iOS 16.7.16 to the home screen with touch, Wi-Fi, Bluetooth, some audio, and an Adreno 650 OpenGL ES path. Metal, smoother 60 fps, camera, cellular, sleep, and other services are incomplete or not started. Status is upstream-reported, not independently reproduced here.

The Mi 10T hardware, firmware and partition assumptions are not portable to Lavender or other devices. Follow the upstream backup/recovery instructions; flashing `userdata` erases Android data.
