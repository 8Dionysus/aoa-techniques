# Boundary Bridge Parts

This file maps current boundary-bridge pressure to active `aoa-techniques`
parts. It is not the AoA center boundary-bridge part map and not a raw source
inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `owner-boundary-anchors` | Maps owner placement, nearest-wrong-target rejection, bounded context, and validated-mirror technique anchors without claiming owner acceptance. | [parts/owner-boundary-anchors](parts/owner-boundary-anchors/README.md) | [PROVENANCE](PROVENANCE.md) |
| `derived-projection-anchors` | Maps source-lift, KAG, relation, provenance, repo-doc, and generated reader surfaces that stay downstream of authored bundles. | [parts/derived-projection-anchors](parts/derived-projection-anchors/README.md) | [PROVENANCE](PROVENANCE.md) |
| `proof-claim-anchors` | Maps proof and public-claim practice anchors without issuing proof verdicts from mechanics. | [parts/proof-claim-anchors](parts/proof-claim-anchors/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how boundary-bridge
pressure moved.
