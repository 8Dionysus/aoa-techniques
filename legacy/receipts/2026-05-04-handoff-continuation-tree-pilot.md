# Handoff-Continuation Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the second authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/handoff-continuation-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0056` | `techniques/agent-workflows/channelized-agent-mailbox/` | `techniques/continuity/handoff-continuation/channelized-agent-mailbox/` |
| `AOA-T-0057` | `techniques/agent-workflows/structured-handoff-before-compaction/` | `techniques/continuity/handoff-continuation/structured-handoff-before-compaction/` |
| `AOA-T-0058` | `techniques/agent-workflows/receipt-confirmed-handoff-packet/` | `techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/` |
| `AOA-T-0059` | `techniques/agent-workflows/git-verified-handoff-claims/` | `techniques/continuity/handoff-continuation/git-verified-handoff-claims/` |
| `AOA-T-0060` | `techniques/agent-workflows/session-opening-ritual-before-work/` | `techniques/continuity/handoff-continuation/session-opening-ritual-before-work/` |
| `AOA-T-0061` | `techniques/agent-workflows/cross-repo-resource-map-bootstrap/` | `techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/` |
| `AOA-T-0062` | `techniques/agent-workflows/episode-bounded-agent-loop/` | `techniques/continuity/handoff-continuation/episode-bounded-agent-loop/` |

## Preservation Rule

Active technique bundles moved directly from old authored homes to new authored
homes. They did not pass through root `legacy/`.

Root legacy preserves only this migration accounting.

## Invariants

- Keep bundle IDs unchanged.
- Keep `domain`, `kind`, `status`, owners, evidence, relations, checklists,
  examples, notes, and public-safety posture unchanged.
- Do not add `tree_path` frontmatter.
- Do not move any other shelf in this wave.
- Do not treat `handoff-continuation` as global shelf canon beyond this
  validated pilot.
- Keep the seven leaf bundles separate rather than merging them into one
  handoff framework.

## Validation

- `python scripts/release_check.py` passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
