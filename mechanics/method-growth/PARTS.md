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

## Part-Local Contract Packets

These JSON schema/example pairs are active Method-growth part contracts, not
root `schemas/` or root `examples/` material.

| Part | Schema | Example |
|---|---|---|
| `pattern-adoption` | [parts/pattern-adoption/schemas/technique_pattern_adoption_note_v1.json](parts/pattern-adoption/schemas/technique_pattern_adoption_note_v1.json) | [parts/pattern-adoption/examples/technique_pattern_adoption_note.example.json](parts/pattern-adoption/examples/technique_pattern_adoption_note.example.json) |
| `adoption-boundaries` | [parts/adoption-boundaries/schemas/technique_adoption_boundary_check_v1.json](parts/adoption-boundaries/schemas/technique_adoption_boundary_check_v1.json) | [parts/adoption-boundaries/examples/technique_adoption_boundary_check.example.json](parts/adoption-boundaries/examples/technique_adoption_boundary_check.example.json) |
| `technique-to-skill-handoff` | [parts/technique-to-skill-handoff/schemas/technique_to_skill_handoff_v1.json](parts/technique-to-skill-handoff/schemas/technique_to_skill_handoff_v1.json) | [parts/technique-to-skill-handoff/examples/technique_to_skill_handoff.example.json](parts/technique-to-skill-handoff/examples/technique_to_skill_handoff.example.json) |
| `retention-checks` | [parts/retention-checks/schemas/technique_retention_probe_v1.json](parts/retention-checks/schemas/technique_retention_probe_v1.json) | [parts/retention-checks/examples/technique_retention_probe.example.json](parts/retention-checks/examples/technique_retention_probe.example.json) |
| `obsolescence` | [parts/obsolescence/schemas/technique_obsolescence_notice_v1.json](parts/obsolescence/schemas/technique_obsolescence_notice_v1.json) | [parts/obsolescence/examples/technique_obsolescence_notice.example.json](parts/obsolescence/examples/technique_obsolescence_notice.example.json) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how adoption pressure
moved.
