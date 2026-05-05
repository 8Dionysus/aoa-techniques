# Kag-Source-Lift Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the sixth authored path migration for the technique tree
pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/kag-source-lift-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0018` | `techniques/docs/markdown-technique-section-lift/` | `techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/` |
| `AOA-T-0019` | `techniques/docs/frontmatter-metadata-spine/` | `techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/` |
| `AOA-T-0020` | `techniques/docs/evidence-note-provenance-lift/` | `techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/` |
| `AOA-T-0021` | `techniques/docs/bounded-relation-lift-for-kag/` | `techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/` |
| `AOA-T-0022` | `techniques/docs/risk-and-negative-effect-lift/` | `techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/` |
| `AOA-T-0046` | `techniques/docs/repo-doc-surface-lift/` | `techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/` |
| `AOA-T-0047` | `techniques/docs/github-review-template-lift/` | `techniques/knowledge-lift/kag-source-lift/github-review-template-lift/` |
| `AOA-T-0048` | `techniques/docs/semantic-review-surface-lift/` | `techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/` |

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
- Do not treat `knowledge-lift` as KAG owner doctrine, graph semantics,
  generated source of truth, retrieval policy, scoring, or automatic verdict
  authority.
- Keep the eight leaf bundles separate rather than merging them into one
  source-lift framework bundle.
- Keep authored markdown, frontmatter, notes, templates, and review docs
  stronger than generated manifests, catalogs, graphs, exports, or reader
  surfaces.

## Validation

- `python scripts/release_check.py` passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
