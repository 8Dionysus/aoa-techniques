# History-Artifacts Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Scope

This receipt preserves the fourteenth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/history-artifacts-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0044` | `techniques/history/versionable-session-transcripts/` | `techniques/history/history-artifacts/versionable-session-transcripts/` |
| `AOA-T-0053` | `techniques/history/local-first-session-index/` | `techniques/history/history-artifacts/local-first-session-index/` |
| `AOA-T-0026` | `techniques/history/session-capture-as-repo-artifact/` | `techniques/history/history-artifacts/session-capture-as-repo-artifact/` |
| `AOA-T-0045` | `techniques/history/witness-trace-as-reviewable-artifact/` | `techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/` |
| `AOA-T-0066` | `techniques/history/transcript-replay-artifact/` | `techniques/history/history-artifacts/transcript-replay-artifact/` |
| `AOA-T-0067` | `techniques/history/transcript-linked-code-lineage/` | `techniques/history/history-artifacts/transcript-linked-code-lineage/` |

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
- Keep capture, transcript packaging, derivative local indexing, witness trace
  review, transcript replay, and code-lineage links as six separate leaf
  bundles under one history shelf.
- Do not treat `history-artifacts` as memory doctrine, instruction authority,
  private transcript publication, hidden capture policy, hosted viewer product
  doctrine, repo analytics, retention policy, recall substrate, proof
  authority, or a generic history platform.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- `python scripts/release_check.py` passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
