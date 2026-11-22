# UniXNU catalog and generated port wrappers

This directory contains the pinned catalog snapshot, source/license audit, and generated available-record metadata. The catalog is not Portsmith verification. `ports/catalog/available/` is generated index data; per-device wrappers live at `ports/<id>/` and are materialized by `tools/materialize-unixnu-available-ports.py`. Update catalog inputs/generator and regenerate instead of hand-editing generated metadata. Preserve exact record/source pins and separate per-source licenses.
