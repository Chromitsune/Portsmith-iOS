# Boot-menu host tests

Tests here exercise only the platform-neutral profile loader, selection state machine and SVG preview using fixtures. They must never invoke ADB, fastboot, QEMU firmware, a boot executor, storage, reset or any device interface. Keep target selection opaque and assert that confirmation returns an ID without executing it.
