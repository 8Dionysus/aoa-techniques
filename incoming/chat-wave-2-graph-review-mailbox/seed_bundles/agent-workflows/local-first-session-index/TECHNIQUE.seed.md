---
id: AOA-T-XXXX
name: local-first-session-index
domain: agent-workflows
status: draft-seed
origin: chat-wave-2-graph-review-mailbox
note: seed bundle staged for operator-guided chat wave 2 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - graph-review-mailbox
summary: Build a local searchable index over already-saved session artifacts without turning the index into capture or memory doctrine.
maturity_score: 1
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: donor_soil
export_ready: false
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.seed.md
---
# local-first-session-index

## Intent

Provide a searchable local index over existing session artifacts so operators can browse saved history without reopening capture semantics or memory-system claims.

## When to use

- session artifacts already exist locally
- you need search or browse over saved history
- the artifact layer should stay local-first

## When not to use

- the real problem is capturing sessions in the first place
- the surface would become cloud history or memory recall doctrine
- the source artifacts are not stable enough to index

## Inputs

- saved session artifacts
- local metadata or path references
- optional indexing fields such as title, time, or agent name

## Outputs

- local index entries
- searchable or browsable lookup surface
- references back to original session artifacts

## Core procedure

1. read already-saved session artifacts
2. extract a bounded local metadata set
3. build or refresh the local index
4. return references to the source artifact, not a replacement for it
5. keep the index separate from memory or instruction authority

## Contracts

- the index points back to source artifacts
- capture remains outside this technique
- local-first storage stays the default posture
- the technique stays smaller than a memory or dashboard product

## Risks

### Failure modes

- the index drifts away from the source artifacts
- search fields flatten too much session context

### Negative effects

- operators trust the index more than the source artifact
- the surface drifts into memory or recall claims

### Misuse patterns

- letting the index become a new source of truth
- mixing capture or cloud sync into the same technique

### Detection signals

- results cannot link back to saved artifacts
- index refresh depends on hidden runtime state

### Mitigations

- keep stable source references
- refresh from local artifacts only
- separate indexing from capture and recall policy

## Validation

- confirm results point back to existing artifacts
- confirm the index can be rebuilt from local sources
- verify no memory or capture claims are needed to explain the flow

## Adaptation notes

- artifact formats
- index storage shape
- searchable fields
- refresh cadence

## Public sanitization notes

Remove donor-specific product dashboards and hosted sync assumptions. Keep only the bounded local index contract.

## Example

See `examples/index_entry.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 session-index cluster

## Future evolution

- filter presets
- artifact freshness notes
- bounded index rebuild commands
