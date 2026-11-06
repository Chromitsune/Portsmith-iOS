# Samsung Galaxy S7 Exynos (`herolte`) port

Source is `repo/`, pinned to `wardevsa/ios-a5xelte` branch `herolte`; read its README, `HEROLTE_PROGRESS.md`, `A5XELTE_PROGRESS.md`, `NOTES.md`, and `NOTICE/LICENSE` material before making changes. The repository name is inherited from its Galaxy A5 project, but the **`herolte` branch is a Galaxy S7 Exynos 8890 port**; it also contains separate early A5XELTE work.

Upstream reports iOS 16.7.16 reaching the S7 home screen with Mali-T880 GPU drawing through an OpenGL ES/Panfrost path, touch, and buttons. Wi-Fi, cellular, Bluetooth, audio, cameras, sensors, and sleep remain unavailable. The A5XELTE track is earlier: XNU/storage bring-up, not iOS userland. These are upstream-reported statuses.

The S7 is Exynos (not the Snapdragon Galaxy S9) and is unrelated at the hardware-driver level to Lavender. The fork has no recognized GitHub license metadata; preserve its original notices and do not copy/redistribute its additions without license clarification.
