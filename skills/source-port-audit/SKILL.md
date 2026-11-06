---
name: source-port-audit
description: Decide whether code from one Android-device XNU port can be reused on another.
---

# Source and port audit

1. Identify exact device variants, SoC, CPU/GIC/timer, memory map/page size, bootloader/UEFI, storage, display/touch, reset method, and firmware dependencies.
2. Compare those facts with the target; mark each component shared, adaptable, board-specific, or unknown.
3. Read the source file's license and provenance before copying or patching. Preserve history/notice and upstream attribution.
4. Prefer pinned references/submodules and small adapters to flattening whole repositories.
5. Check existing target implementations first; do not duplicate a stronger persistent log or reset path without showing a missing requirement.
6. Report host and device evidence separately.
