---
name: host-validation
description: Validate code and artifacts without touching a physical phone.
---

# Host-only validation

1. Inspect the working tree and record source commits/submodule pins.
2. Prefer unit/contract tests, static checks, reproducible builds, and temporary copies.
3. Never pass a device handle to a test unless the user explicitly authorized that hardware action.
4. Record exact commands, exit status, and artifacts/hashes. State what the test does not prove.
5. Label results `host-verified`; do not infer hardware behavior, reset/DRAM retention, bootloader semantics, or device success from compilation.
