# Instruction-Surface Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the fifth authored path migration for the technique tree
pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/instruction-surface-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0012` | `techniques/docs/deterministic-context-composition/` | `techniques/instruction/instruction-surface/deterministic-context-composition/` |
| `AOA-T-0013` | `techniques/docs/single-source-rule-distribution/` | `techniques/instruction/instruction-surface/single-source-rule-distribution/` |
| `AOA-T-0024` | `techniques/docs/upstream-mirroring-with-provenance/` | `techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/` |
| `AOA-T-0027` | `techniques/docs/cross-agent-skill-propagation/` | `techniques/instruction/instruction-surface/cross-agent-skill-propagation/` |
| `AOA-T-0029` | `techniques/docs/nested-rule-loading/` | `techniques/instruction/instruction-surface/nested-rule-loading/` |
| `AOA-T-0030` | `techniques/docs/fragmented-agent-context/` | `techniques/instruction/instruction-surface/fragmented-agent-context/` |
| `AOA-T-0035` | `techniques/docs/profile-preset-composition/` | `techniques/instruction/instruction-surface/profile-preset-composition/` |

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
- Do not treat `instruction-surface` as AoA constitutional law, skill
  acceptance policy, runtime role law, generated context authority, or a public
  source-of-truth replacement.
- Keep the seven leaf bundles separate rather than merging them into one
  instruction framework bundle.
- Keep `profile-preset-composition` bounded to reviewable surface definition
  and out of render truth, lifecycle control, deployment roots, host details,
  and one-command service behavior.

## Validation

- `python scripts/release_check.py` passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
