# Questbook Parts

This file maps current questbook pressure to active `aoa-techniques` parts. It
is not the AoA center Questbook part map and not a quest source inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `source-index-anchors` | Maps the local human index, source quest files, schemas, and generated quest projections without moving source truth into mechanics. | [parts/source-index-anchors](parts/source-index-anchors/README.md) | [PROVENANCE](PROVENANCE.md) |
| `technique-obligation-anchors` | Maps canon hardening, donor follow-through, generated/source drift, promotion-readiness, and feat-reflection obligations. | [parts/technique-obligation-anchors](parts/technique-obligation-anchors/README.md) | [PROVENANCE](PROVENANCE.md) |
| `harvest-promotion-anchors` | Maps harvest and promotion-review technique anchors without treating quest pressure as canon. | [parts/harvest-promotion-anchors](parts/harvest-promotion-anchors/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how Questbook pressure
moved.
