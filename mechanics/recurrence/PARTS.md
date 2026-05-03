# Recurrence Parts

This file maps current recurrence behavior to active `aoa-techniques` parts.
It is not the AoA center recurrence part map and not a raw source inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `live-observation-producers` | Names the local producer inputs that may feed technique review while keeping generated evidence advisory. | [parts/live-observation-producers](parts/live-observation-producers/README.md) | [PROVENANCE](PROVENANCE.md) |
| `review-decision-closure` | Names how recurrence-fed technique beacons can close as review decisions without changing technique status. | [parts/review-decision-closure](parts/review-decision-closure/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how recurrence pressure
was observed and closed.
