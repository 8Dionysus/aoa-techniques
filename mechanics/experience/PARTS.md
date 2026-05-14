# Experience Parts

This file maps current Experience behavior to active parts. It is not a raw
source inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `governance-precedent` | Documents how reusable governance techniques are captured without forcing local adoption. | [parts/governance-precedent](parts/governance-precedent/README.md) | [PROVENANCE](PROVENANCE.md) |
| `authority-resolution` | Separates actor capability from governance authority. | [parts/authority-resolution](parts/authority-resolution/README.md) | [PROVENANCE](PROVENANCE.md) |
| `appeal-reasoning` | Keeps appeal and overturn reasoning evidence-bound and owner-local. | [parts/appeal-reasoning](parts/appeal-reasoning/README.md) | [PROVENANCE](PROVENANCE.md) |
| `sealed-decision` | Captures commit/reveal, hash-chain review, and tamper-detection practice. | [parts/sealed-decision](parts/sealed-decision/README.md) | [PROVENANCE](PROVENANCE.md) |
| `scope-boundary` | Keeps office/service scope below release approval, self-authority, runtime truth, and ToS write authority. | [parts/scope-boundary](parts/scope-boundary/README.md) | [PROVENANCE](PROVENANCE.md) |
| `handoff-compression` | Names office/service handoff compression practice without becoming execution workflow. | [parts/handoff-compression](parts/handoff-compression/README.md) | [PROVENANCE](PROVENANCE.md) |
| `service-clarity` | Keeps service clarity practice owner-local and bounded by upstream gates. | [parts/service-clarity](parts/service-clarity/README.md) | [PROVENANCE](PROVENANCE.md) |
| `technique-candidate-bridge` | Classifies Experience parts into extract-watch, narrow, hold, owner-route, or mechanics-only lanes before any technique promotion. | [parts/technique-candidate-bridge](parts/technique-candidate-bridge/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part-Local Contract Packets

These JSON schema/example pairs are active Experience part contracts, not root
`schemas/` or root `examples/` material.

| Part | Schema | Example |
|---|---|---|
| `appeal-reasoning` | [parts/appeal-reasoning/schemas/appeal_reasoning_step_v1.json](parts/appeal-reasoning/schemas/appeal_reasoning_step_v1.json) | [parts/appeal-reasoning/examples/appeal_reasoning_step.example.json](parts/appeal-reasoning/examples/appeal_reasoning_step.example.json) |
| `governance-precedent` | [parts/governance-precedent/schemas/technique_governance_precedent_v1.json](parts/governance-precedent/schemas/technique_governance_precedent_v1.json) | [parts/governance-precedent/examples/technique_governance_precedent.example.json](parts/governance-precedent/examples/technique_governance_precedent.example.json) |
| `sealed-decision` | [parts/sealed-decision/schemas/sealed_decision_technique_note_v1.json](parts/sealed-decision/schemas/sealed_decision_technique_note_v1.json) | [parts/sealed-decision/examples/sealed_decision_technique_note_v1.example.json](parts/sealed-decision/examples/sealed_decision_technique_note_v1.example.json) |
| `scope-boundary` | [parts/scope-boundary/schemas/scope_boundary_technique_note_v1.json](parts/scope-boundary/schemas/scope_boundary_technique_note_v1.json) | [parts/scope-boundary/examples/scope_boundary_technique_note_v1.example.json](parts/scope-boundary/examples/scope_boundary_technique_note_v1.example.json) |
| `handoff-compression` | [parts/handoff-compression/schemas/handoff_compression_technique_note_v1.json](parts/handoff-compression/schemas/handoff_compression_technique_note_v1.json) | [parts/handoff-compression/examples/handoff_compression_technique_note_v1.example.json](parts/handoff-compression/examples/handoff_compression_technique_note_v1.example.json) |
| `service-clarity` | [parts/service-clarity/schemas/service_clarity_technique_note_v1.json](parts/service-clarity/schemas/service_clarity_technique_note_v1.json) | [parts/service-clarity/examples/service_clarity_technique_note_v1.example.json](parts/service-clarity/examples/service_clarity_technique_note_v1.example.json) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how Experience pressure
moved.

Use `technique-candidate-bridge` before drafting from Experience pressure. It
keeps candidate classification separate from promotion and from stronger-owner
authority.
