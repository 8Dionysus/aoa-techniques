# Method-Growth Parts

This file maps current Method-growth behavior to active parts. It is not a raw
source inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `pattern-adoption` | Describes how shared patterns become reusable technique practice without automatic activation. | [parts/pattern-adoption](parts/pattern-adoption/README.md) | [PROVENANCE](PROVENANCE.md) |
| `adoption-boundaries` | Names owner consent, readiness, rollback, and no-policy-overreach stop-lines for adopting technique patterns. | [parts/adoption-boundaries](parts/adoption-boundaries/README.md) | [PROVENANCE](PROVENANCE.md) |
| `technique-to-skill-handoff` | Keeps reusable technique canon separate from bounded skill workflow proposals. | [parts/technique-to-skill-handoff](parts/technique-to-skill-handoff/README.md) | [PROVENANCE](PROVENANCE.md) |
| `retention-checks` | Keeps adoption active only while evidence, rollback, and retention posture remain reviewable. | [parts/retention-checks](parts/retention-checks/README.md) | [PROVENANCE](PROVENANCE.md) |
| `obsolescence` | Routes supersession, deprecation, and removal without erasing owner evidence or rollback routes. | [parts/obsolescence](parts/obsolescence/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how adoption pressure
moved.
