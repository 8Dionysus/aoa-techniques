# Skill-Discovery Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Scope

This receipt preserves the tenth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/skill-discovery-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0041` | `techniques/docs/skill-marketplace-curation/` | `techniques/instruction/skill-discovery/skill-marketplace-curation/` |
| `AOA-T-0042` | `techniques/evaluation/upstream-skill-health-checking/` | `techniques/instruction/skill-discovery/upstream-skill-health-checking/` |

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
- Do not treat `skill-discovery` as installer behavior, sync substrate,
  registry product doctrine, registry governance, access control, routing
  policy, recommendation ranking, trust scoring, security scanning, compliance
  review, generic monitoring, capability ownership, command doctrine, runtime
  law, or agent-role authority.
- Keep curated marketplace discoverability and upstream source-readiness as
  separate leaf bundles rather than merging them into one framework bundle.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- `python scripts/release_check.py` passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
