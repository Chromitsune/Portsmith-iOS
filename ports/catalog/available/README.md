# UniXNU available device source references

The pinned UniXNU device catalog has **79** records marked `available`; exact revision fetches succeeded for **73** and **6** remain metadata-only because the recorded repository/revision was inaccessible during the pinned-source audit.

There are **72** pinned Git submodule refs under `ports/catalog/available/<name>/repo`; the `sheng` record reuses the curated source at `ports/sheng/repo`. The parent repository does not vendor these device source files. After a plain clone, initialize one source with `python3 tools/checkout-sources.py --name <record-name>` or initialize the accessible set with `python3 tools/checkout-sources.py --available` (no recursive submodule initialization).

Root-license inventory: 54 repositories have an identifiable root license (some with scoped/third-party terms), 16 have no root license/notice, 3 have mixed or unclear scope, and 6 pins were inaccessible. A source pointer is not permission to reuse code. Review per-file, nested-submodule, firmware and transitive terms before adapting code.

`available` describes UniXNU port-record validation, not a successful build or boot. Source checkouts are discovery references; license status is recorded per repository below and in `sources/manifest.toml`. These catalog-only sources are not counted as Portsmith-managed `ports/*/port.toml` ports.

See [`LICENSE-AUDIT.md`](LICENSE-AUDIT.md) for all pinned root-license and reachability findings.
