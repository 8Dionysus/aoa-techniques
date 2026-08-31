# AGENTS.md

## Applies to

This card applies to `techniques/continuity/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`continuity/` stores technique bundles whose primary placement question is how
working context, review truth, handoff state, donor material, or capability
availability survives a state boundary.

Current `continuity` trunk: shared placement applies; local role and shelves are the delta.
## Current Shelves

Current shelves:

- `review-compaction/`: preserves or restores review and capability context
  across commit, compaction, or repeated-review boundaries
- `handoff-continuation/`: carries handoff, receipt, verification, startup,
  resource-map, mailbox, and episode-checkpoint seams across session, agent,
  repo, or episode boundaries
- `donor-harvest/`: carries reviewed-session donor packs, harvest-packet
  contracts, progression evidence deltas, and adjunct quest overlays across
  session closeout without granting memory, playbook, or progression authority

## Read before editing

Use shared order in [techniques/AGENTS.md](../AGENTS.md#read-before-editing); inspect `continuity` role and its target bundle.
## Trunk Rules

Placement contract: [techniques/AGENTS.md](../AGENTS.md#closeout); local `continuity` shelf and boundary delta follows.
## Boundaries

Keep the continuity object explicit:

- what state crosses the boundary
- what evidence or capability must remain inspectable
- what stale, noisy, or missing context is being reduced
- what the technique refuses to reconstruct or govern

Do not turn a continuity technique into a live skill, phase system, memory
policy, or review verdict contract.

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

`continuity` path placement follows the parent contract; renames need its reviewed projection and bounded receipt.
## Validation

Inherit [techniques/AGENTS.md](../AGENTS.md#validation): `source-fast`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `techniques/continuity/AGENTS.md`.
## Closeout

Local delta `techniques/continuity/AGENTS.md`: state placement/frontmatter/generated-reader changes or route-only guidance.
