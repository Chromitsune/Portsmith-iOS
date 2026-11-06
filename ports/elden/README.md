# Lenovo Legion Y700 Gen 4 (elden) (`elden`)

**Upstream source:** [https://github.com/jerry-2009/UNIXNU_elden@`33b55083a0b61630f71478230f648606163115eb`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record.

- **Board:** `elden`
- **SoC:** `SM8750P`
- **OS profile:** `ipados-17.7.11-21H461`
- **Catalog-listed components:** ArmDTPlatform, ArmCpu, SoftwareAES, XnuPrelink, DarwinBoot
- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).
- **License review:** No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted.

## Compatibility at the pinned revision

These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file](https://github.com/jerry-2009/UNIXNU_elden/blob/33b55083a0b61630f71478230f648606163115eb/docs/PHASE1-HANDOFF.md).

| Feature | Status | Evidence / limitation |
|---|---|---|
| Boot | Partial / limited | Owner-reported device runs reached the visible, operable UniXNU menu and returned to Android; XNU boot is not evidenced. See docs/PHASE1-HANDOFF.md and docs/PHASE2-STATUS.md. |
| GPU | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Display | Reported working (upstream) | The device menu was visible and operable in the reported RAM cold boots; see docs/PHASE2-STATUS.md. |
| Touch & Buttons | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Audio | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Bluetooth | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Wi-Fi | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Cellular | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Power & Sleep | Work in progress / incomplete | Sleep-related evidence is a host-side ADT decode, not a device suspend test. See docs/PHASE2.1-STATUS.md. |
| Camera & Sensors | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| USB | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |
| Storage | Work in progress / incomplete | Only host-side DTS/ADT work is reported; this is not a device storage test. See docs/PHASE3-STORAGE.md. |
| Stability | Not tested / no comparable evidence | No comparable evidence recorded in the pinned project files. |

See the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).
