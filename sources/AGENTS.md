# Shared frameworks and reference sources

`manifest.toml` records exact source pins, licenses and source roles. Read it and `sources/README.md` before initializing anything. Use `tools/checkout-sources.py` with an explicit selector (`--curated`, `--name`, `--available`, or `--reference`); never initialize recursively by default. Nested submodules and upstream source trees have their own licenses and may be unavailable. Do not copy code based solely on a gitlink.
