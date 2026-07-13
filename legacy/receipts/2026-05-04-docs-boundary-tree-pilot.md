# Docs-Boundary Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the seventh authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/docs-boundary-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0002` | `techniques/docs/source-of-truth-layout/` | `techniques/instruction/docs-boundary/source-of-truth-layout/` |
| `AOA-T-0009` | `techniques/docs/lightweight-status-snapshot/` | `techniques/instruction/docs-boundary/lightweight-status-snapshot/` |
| `AOA-T-0034` | `techniques/docs/public-safe-artifact-sanitization/` | `techniques/instruction/docs-boundary/public-safe-artifact-sanitization/` |
| `AOA-T-0033` | `techniques/docs/decision-rationale-recording/` | `techniques/instruction/docs-boundary/decision-rationale-recording/` |

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
- Do not treat `docs-boundary` as source-of-truth governance, AoA
  constitutional law, approval policy, skill acceptance, proof authority,
  runtime role law, or architecture taxonomy.
- Keep the four leaf bundles separate rather than merging them into one
  documentation-governance framework bundle.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
