# QEMU generic-menu renderer fixture

This folder contains a Portsmith-authored bare-metal rendering fixture used only by `boot-menu/qemu-preview.py`. It reads a generated `scene.h` from profile data, draws to QEMU guest RAM and never emulates a target bootloader, panel, keys, touch, storage or boot executor. Do not add device registers, UFS/GPT writes, firmware or upstream menu code. Keep the fixed QEMU framebuffer contract separate from any future real platform backend.
