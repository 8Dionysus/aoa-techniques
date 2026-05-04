# Review-Compaction Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the first authored path migration for the technique tree
pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/review-compaction-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0051` | `techniques/agent-workflows/commit-triggered-background-review/` | `techniques/continuity/review-compaction/commit-triggered-background-review/` |
| `AOA-T-0052` | `techniques/agent-workflows/review-findings-compaction/` | `techniques/continuity/review-compaction/review-findings-compaction/` |
| `AOA-T-0054` | `techniques/agent-workflows/compaction-resilient-skill-loading/` | `techniques/continuity/review-compaction/compaction-resilient-skill-loading/` |

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
- Do not treat `review-compaction` as global shelf canon beyond this validated
  pilot.

## Validation

- `python scripts/release_check.py` passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
