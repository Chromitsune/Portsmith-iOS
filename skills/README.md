# Shared skills

Skills are short, repeatable playbooks for recurring work. They should be device-agnostic unless stored under a port-specific directory. Each skill should state inputs, read-only/host tests, destructive actions requiring authorization, outputs to record, and evidence level.

- `device-state-check/SKILL.md` — read-only check of a phone before any reset.
- `host-validation/SKILL.md` — run host tests and report exactly what they prove.
- `source-port-audit/SKILL.md` — compare a port, check hardware boundaries and license/provenance before reuse.

- `new-port-intake/SKILL.md` — add a pinned port/reference with license, duplicate, and catalog boundaries.
- `compatibility-evidence/SKILL.md` — map exact-revision evidence to matrix statuses conservatively.
- `device-log-triage/SKILL.md` — retrieve and interpret logs without causing an unnecessary reset/write.
