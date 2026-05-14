# Release Support Parts

This file maps current release-support behavior to active `aoa-techniques`
parts. It is not the AoA center release-support part map and not a raw source
inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `installation-techniques` | Names staged landing, migration safety, smoke gates, rollback, and replay-audit practice without owning activation authority. | [parts/installation-techniques](parts/installation-techniques/README.md) | [PROVENANCE](PROVENANCE.md) |
| `sovereign-release-techniques` | Names release ritual, decision sealing, rollback rehearsal, and post-release watch practice without sealing authority. | [parts/sovereign-release-techniques](parts/sovereign-release-techniques/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part-Local Contract Packets

These JSON schema/example pairs are active release-support part contracts, not
root `schemas/` or root `examples/` material.

| Part | Schema | Example |
|---|---|---|
| `installation-techniques` | [parts/installation-techniques/schemas/installation_technique_note_v1.json](parts/installation-techniques/schemas/installation_technique_note_v1.json) | [parts/installation-techniques/examples/installation_technique_note_v1.example.json](parts/installation-techniques/examples/installation_technique_note_v1.example.json) |
| `sovereign-release-techniques` | [parts/sovereign-release-techniques/schemas/sovereign_release_technique_note_v1.json](parts/sovereign-release-techniques/schemas/sovereign_release_technique_note_v1.json) | [parts/sovereign-release-techniques/examples/sovereign_release_technique_note_v1.example.json](parts/sovereign-release-techniques/examples/sovereign_release_technique_note_v1.example.json) |

## Part Rule

If a part starts carrying a stable reusable practice with inputs, outputs,
risks, examples, and validation, route the practice bundle into `techniques/`.
Leave this package as the mechanics layer that explains how release-support
pressure moved.
