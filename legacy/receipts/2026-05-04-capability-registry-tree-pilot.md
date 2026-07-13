# Capability-Registry Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the eighth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/capability-registry-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0025` | `techniques/docs/capability-spec-versioning/` | `techniques/instruction/capability-registry/capability-spec-versioning/` |
| `AOA-T-0063` | `techniques/docs/versioned-agent-registry-contract/` | `techniques/instruction/capability-registry/versioned-agent-registry-contract/` |
| `AOA-T-0064` | `techniques/docs/capability-discovery/` | `techniques/instruction/capability-registry/capability-discovery/` |

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
- Do not treat `capability-registry` as registry product doctrine, discovery
  ranking, marketplace curation, trust policy, graph semantics, runtime
  resolution, skill acceptance, or agent-role authority.
- Keep capability specs, registry-facing entries, and discovery queries as
  separate leaf bundles rather than merging them into one registry framework
  bundle.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
