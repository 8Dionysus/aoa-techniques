# Capability-Boundary Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the ninth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/capability-boundary-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0040` | `techniques/docs/skill-vs-command-boundary/` | `techniques/instruction/capability-boundary/skill-vs-command-boundary/` |
| `AOA-T-0043` | `techniques/docs/multi-source-primary-input-provenance/` | `techniques/instruction/capability-boundary/multi-source-primary-input-provenance/` |
| `AOA-T-0093` | `techniques/agent-workflows/recommendation-truth-vs-host-actionability/` | `techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/` |

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
- Do not treat `capability-boundary` as skill marketplace curation, upstream
  health validation, routing policy, recommendation ranking, KAG graph
  semantics, runtime execution doctrine, host inventory policy, command
  product design, shell doctrine, registry product doctrine, or agent-role
  authority.
- Keep skill-command ownership, primary source priority, and
  recommendation/actionability as separate guardrail leaves rather than
  merging them into one framework bundle.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
