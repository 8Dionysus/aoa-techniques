# AGENTS.md

## Applies to

This card applies to `techniques/history/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`history/` stores technique bundles whose primary placement question is how
reviewable history, witness material, session capture, transcript structure, or
lineage artifacts remain inspectable without becoming memory doctrine.

Current `history` trunk: shared placement applies; local role and shelves are the delta.
## Current Shelves

Current shelves:

- `history-artifacts/`: session capture, transcript packaging, derivative
  local indexing, witness trace review, transcript replay, and code-lineage
  links over already-saved history artifacts.

Leaf bundles stay separate: `session-capture-as-repo-artifact`,
`versionable-session-transcripts`, `local-first-session-index`,
`witness-trace-as-reviewable-artifact`, `transcript-replay-artifact`, and
`transcript-linked-code-lineage`.

## Read before editing

Use shared order in [techniques/AGENTS.md](../AGENTS.md#read-before-editing); inspect `history` role and its target bundle.
## Trunk Rules

Placement contract: [techniques/AGENTS.md](../AGENTS.md#closeout); local `history` shelf and boundary delta follows.
## Boundaries

Keep the historical object explicit: what gets captured, what stays out, and
how reviewability is preserved.
Preserve the rule that memory objects and recall surfaces still stay outside
`aoa-techniques` unless the task is about the reusable capture technique
itself.
Keep examples sanitized, and keep the line between public witness material and
private transcripts visible.

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.


If the object becomes a live memory model, a repo-local audit log, or a
project-specific retention policy, route it to the owning repository instead of
widening this technique.
If the value is mainly operational recall rather than reusable capture
structure, it does not belong here yet.

Do not:

- publish private transcripts or hidden internal notes
- treat witness capture as an excuse to dump raw logs without bounded structure
- collapse reusable capture technique into memory doctrine or repo-local retention policy
- blur public-safe history surfaces with sensitive internal chronology

`history` path placement follows the parent contract; renames need its reviewed projection and bounded receipt.
## Validation

Inherit [techniques/AGENTS.md](../AGENTS.md#validation): `source-fast`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `techniques/history/AGENTS.md`.
## Closeout

Local delta `techniques/history/AGENTS.md`: state placement/frontmatter/generated-reader changes or route-only guidance.
