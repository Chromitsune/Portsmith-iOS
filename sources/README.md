# Pinned source projects

The projects below are Git submodules to the owner's forks, pinned by the superproject's gitlink. They are **separate codebases**, not merged source. Use `git submodule status` to see exact revisions and `git submodule update --init --recursive` to materialize them. Keep nested source licenses and histories intact.

Forking is for a stable, attributable workspace and does not imply endorsement or that upstream maintainers contribute to Portsmith. When adapting code, preserve its license and record the source path and commit.

Initial set:

- `sources/iOSPlus10` — akshaynexus; OnePlus 10 Pro/Negroni, tools and multi-agent workflow. Portsmith points at the `lavender-panic-recovery` branch in the Chromitsune fork.
- `sources/UniXNU` — UniXNU contributors; shared UEFI/driver/build framework.
- `sources/ios-sweet` — dipa-studio; foundational iOS 16/XNU bring-up on Redmi Note 10 Pro.
- `sources/ios-flame` — NWylynko; Pixel 4/SM8150 bring-up and GPU/Metal-through-Vulkan work.
- `sources/ios-s9` — syncmodz (based on ios-sweet); Snapdragon Galaxy S9 port and persistent-log tooling.
- `sources/UniXNU-Lavender` — Chromitsune; Lavender/SDM660 board port and its current recovery experiments.

See `manifest.toml` and `../CREDITS.md` for URLs, upstream owners, and license notes. Do not commit firmware, IPSWs, device backups, generated payloads, identifiers, or calibration data from any source.
