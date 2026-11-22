# Device profile workspace

Each `ports/<id>/` is an independent hardware/source contract. Read its local `AGENTS.md`, `port.toml`, README and exact source repository notes before work. Keep duplicate codenames, forks, boot chains, hardware assumptions and evidence separate. Most `repo/` paths are external submodules; Dada is a vendored snapshot. Never recursively initialize submodules without review. Do not edit generated wrappers by hand; use `ports/catalog/AGENTS.md` and the generator.
