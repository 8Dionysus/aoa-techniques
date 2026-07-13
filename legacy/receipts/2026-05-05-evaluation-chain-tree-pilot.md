# Evaluation-Chain Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Scope

This receipt preserves the twelfth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/evaluation-chain-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0003` | `techniques/evaluation/contract-first-smoke-summary/` | `techniques/proof/evaluation-chain/contract-first-smoke-summary/` |
| `AOA-T-0007` | `techniques/evaluation/signal-first-gate-promotion/` | `techniques/proof/evaluation-chain/signal-first-gate-promotion/` |
| `AOA-T-0032` | `techniques/evaluation/context-report-for-ci/` | `techniques/proof/evaluation-chain/context-report-for-ci/` |

## Preservation Rule

Active technique bundles moved directly from old authored homes to new authored
homes. They did not pass through root `legacy/`.

Root legacy preserves only this migration accounting.

## Invariants

- Keep bundle IDs unchanged.
- Keep `domain`, `kind`, `status`, owners, evidence, relations, checklists,
  examples, notes, maturity, validation-strength metadata, and public-safety
  posture unchanged.
- Do not add `tree_path` frontmatter.
- Do not move any other shelf in this wave.
- Do not treat `evaluation-chain` as CI ownership, release policy, eval-suite
  authority, proof verdict law, mandatory testing doctrine, generic quality
  gate doctrine, or owner acceptance.
- Keep summary-contract generation, staged signal promotion, and CI context
  reporting as separate leaf bundles rather than merging them into one gate
  framework bundle.
- Keep `AOA-T-0032` promoted; path placement does not promote it to
  canonical.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
