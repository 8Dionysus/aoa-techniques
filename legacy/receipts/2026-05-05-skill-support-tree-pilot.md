# Skill-Support Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Scope

This receipt preserves the eleventh authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/skill-support-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0016` | `techniques/docs/bounded-context-map/` | `techniques/proof/skill-support/bounded-context-map/` |
| `AOA-T-0015` | `techniques/evaluation/contract-test-design/` | `techniques/proof/skill-support/contract-test-design/` |
| `AOA-T-0017` | `techniques/evaluation/property-invariants/` | `techniques/proof/skill-support/property-invariants/` |

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
- Do not treat `skill-support` as proof authority, eval-suite ownership,
  mandatory testing doctrine, DDD formalism, architecture taxonomy, runtime
  readiness, owner-truth law, or policy enforcement.
- Keep bounded context vocabulary, contract-boundary validation, and invariant
  coverage as separate leaf bundles rather than merging them into one proof
  framework bundle.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
