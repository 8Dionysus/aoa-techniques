# Published-Summary Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Scope

This receipt preserves the thirteenth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/published-summary-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0006` | `techniques/evaluation/latest-alias-plus-history-copy/` | `techniques/proof/published-summary/latest-alias-plus-history-copy/` |
| `AOA-T-0008` | `techniques/evaluation/published-summary-remediation-snapshot/` | `techniques/proof/published-summary/published-summary-remediation-snapshot/` |
| `AOA-T-0010` | `techniques/evaluation/telemetry-integrity-snapshot/` | `techniques/proof/published-summary/telemetry-integrity-snapshot/` |
| `AOA-T-0011` | `techniques/evaluation/required-vs-optional-source-rendering/` | `techniques/proof/published-summary/required-vs-optional-source-rendering/` |

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
- Do not treat `published-summary` as telemetry owner doctrine, dashboard
  ownership, runtime storage policy, archive governance, remediation
  execution, integrity verdict law, release policy, proof verdict law, or a
  generic reporting platform.
- Keep latest alias storage, remediation snapshot, integrity diagnosis, and
  required-versus-optional rendering as separate leaf bundles rather than
  merging them into one published-summary package technique.
- Keep `AOA-T-0011` readable as reusable consumer policy, not only a package
  appendix.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- `python scripts/release_check.py` passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
