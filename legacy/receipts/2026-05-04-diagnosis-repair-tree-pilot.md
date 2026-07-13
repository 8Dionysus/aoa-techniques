# Diagnosis-Repair Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the fourth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/diagnosis-repair-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0080` | `techniques/agent-workflows/session-drift-taxonomy/` | `techniques/recovery/diagnosis-repair/session-drift-taxonomy/` |
| `AOA-T-0081` | `techniques/agent-workflows/diagnosis-from-reviewed-evidence/` | `techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/` |
| `AOA-T-0082` | `techniques/agent-workflows/repair-shape-from-diagnosis/` | `techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/` |
| `AOA-T-0083` | `techniques/agent-workflows/checkpoint-bound-self-repair/` | `techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/` |

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
- Do not treat `diagnosis-repair` as global recovery canon beyond this
  validated pilot.
- Keep the four leaf bundles separate rather than merging them into one repair
  loop.
- Keep self-improvement rhetoric, hidden doctrine edits, role-law changes,
  proof-law changes, and scenario-scale rollout outside this shelf.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
