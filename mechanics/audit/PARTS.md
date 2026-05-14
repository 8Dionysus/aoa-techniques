# Audit Parts

| part | role | active surface | provenance |
|---|---|---|---|
| `promotion-readiness-matrix` | Maintains the promoted-corpus readiness queue and lane counts. | [README](parts/promotion-readiness-matrix/README.md) | [PROVENANCE](PROVENANCE.md) |
| `promotion-evidence-runbook` | Describes the current bounded evidence-prep wave for leading promoted candidates. | [README](parts/promotion-evidence-runbook/README.md) | [PROVENANCE](PROVENANCE.md) |
| `external-evidence-sprint-runbook` | Defines live external-proof search execution without repeating stale lanes. | [README](parts/external-evidence-sprint-runbook/README.md) | [PROVENANCE](PROVENANCE.md) |
| `external-evidence-ledger` | Preserves searched-lane memory and closure precedents. | [README](parts/external-evidence-ledger/README.md) | [PROVENANCE](PROVENANCE.md) |
| `canonical-retro-audit` | Checks already-canonical rows for metadata/evidence/verdict coherence without reopening proof verdicts by queue pressure. | [README](parts/canonical-retro-audit/README.md) | [PROVENANCE](PROVENANCE.md) |

These parts route promotion and evidence work. They do not replace
bundle-local evidence notes or generated status surfaces.
