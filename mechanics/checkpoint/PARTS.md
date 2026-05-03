# Checkpoint Parts

This file maps current checkpoint pressure to active `aoa-techniques` parts.
It is not the AoA center checkpoint part map and not a raw source inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `phase-handoff-candidate` | Keeps the active `phase_sync_for_agents` narrowing lane visible without creating a premature `phase-synchronized-agent-handoff` bundle. | [parts/phase-handoff-candidate](parts/phase-handoff-candidate/README.md) | [PROVENANCE](PROVENANCE.md) |
| `technique-anchors` | Maps existing checkpoint-adjacent technique bundles and their limits without changing technique status. | [parts/technique-anchors](parts/technique-anchors/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how checkpoint pressure
moved.
