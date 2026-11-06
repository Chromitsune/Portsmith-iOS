# Upstream-change review notes

## 2026-11-06 — sheng Bluetooth changes after the Portsmith pin

The automated watcher found UniXNU/UniXNU-sheng `main` advanced from Portsmith's pin `460179565a018c741b93e0b1efa07c55d4de497a` to `2d4b58b797bb03e953ed16cebe388c993d0baa5e`. Its comparison reports changes to `porting.toml`, `reports/ipados27-bluetooth-native.md`, and `reports/ipados27-bluetooth-startup.md` (among 37 files). See the [upstream compare](https://github.com/UniXNU/UniXNU-sheng/compare/460179565a018c741b93e0b1efa07c55d4de497a...2d4b58b797bb03e953ed16cebe388c993d0baa5e).

The new native-adapter report describes extensive **host tests/build checks**. It explicitly says device scanning, pairing, reconnection, BLE, audio, idle power, and Wi-Fi coexistence are pending. The companion startup report documents a fatal launchd `No service cache` path caused by a malformed/trailing-data cache input and a UART version request ending in `EILSEQ` before any bytes transmit; device verification of the fix is pending.

The new `porting.toml` labels Bluetooth `device-verified`, but its positive pairing/reconnection/A2DP evidence is from older images and local board/driver checkouts, before the current `kern.qbt_*` rename. It also records that the current submodule-resolved build and renamed sysctls have not been device-tested. The new startup evidence is for a failing/incomplete current capture. That label alone is therefore not sufficient to say the current pinned implementation works.

**Decision:** do not mark sheng Bluetooth `reported_working`. The evidence is newer than Portsmith's pin, mostly host/build-level, and includes a reported startup failure with current device tests pending. The compatibility matrix remains tied to pinned revision `4601795…`; review the source diff and licensing before changing the source pin or status. The change is surfaced in `compatibility/upstream-watch.json` for review, not silently applied.
