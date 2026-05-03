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

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how Experience pressure
moved.

Use `technique-candidate-bridge` before drafting from Experience pressure. It
keeps candidate classification separate from promotion and from stronger-owner
authority.
