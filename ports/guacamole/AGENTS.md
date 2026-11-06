# OnePlus 7 Pro (`guacamole`) port

Source is `repo/`, pinned to `OtVaL228/ios-sweet` branch `guacamole`; read `repo/README.md` and `repo/docs/guacamole.md` before changing anything. This branch is a OnePlus 7 Pro port, despite the repository's inherited `ios-sweet` name.

Upstream reports an iOS 16 home screen and Adreno 640 GPU rendering through Mesa/freedreno + an EAGL/OpenGL ES path. This is **not native Metal**. Wi-Fi, audio, sensors, and cellular remain incomplete in the linked status. The README describes destructive `userdata` installation; treat it as lab-only and follow the upstream recovery guide.

Do not reuse Snapdragon 855 addresses, firmware, display/touch timings, or partition assumptions for Lavender/SDM660.
