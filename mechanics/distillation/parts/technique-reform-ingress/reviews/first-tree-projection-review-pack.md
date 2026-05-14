# First Tree Projection Review Pack

Source packet:
[Technique Reform Ingress](../README.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)
and
[Technique Tree Projection JSON](../reports/technique_tree_projection.json)

Upstream review:
[First Family Shelf Review Pack](first-family-shelf-review-pack.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: review-pack-landed, not path migration, not `tree_path` frontmatter.

## Verdict

The first tree projection is useful enough to choose a direct-read pilot review,
but not strong enough to move any bundle directory.

It covers all `107` current bundles and proposes a future
`techniques/<trunk>/<shelf>/<technique-slug>/TECHNIQUE.md` placement for each
one. The projection keeps `domain` and `kind` as current frontmatter truth,
keeps `family` scout-only, and records review statuses before any migration:
`34` `pilot-candidate`, `41` `candidate`, `22` `boundary-watch`, `9`
`split-review-needed`, and `1` `singleton-hold`.

This review accepts the projection as a review surface only. It does not move
files, does not add `tree_path` frontmatter, does not make family authoritative,
and does not claim the draft trunks are final.

## Projection Readout

| signal | count | reading |
|---|---:|---|
| `pilot-candidate` | `34` | enough clean shelf pressure exists to choose one direct-read pilot review |
| `candidate` | `41` | many shelves are plausible but should wait behind a smaller pilot |
| `boundary-watch` | `22` | proof, governance, runtime, capability, and owner-closeout seams need extra review |
| `split-review-needed` | `9` | `automation-governance` is too broad to migrate as one shelf yet |
| `singleton-hold` | `1` | `tool-gateway` is a useful trunk signal, not a mature shelf |

Trunk pressure is balanced enough for a first projection:

- `instruction` has `19`
- `proof` has `18`
- `continuity`, `execution`, and `governance` each have `14`
- `knowledge-lift` has `8`
- `recovery` has `8`
- `history` has `6`
- `ingest` has `5`
- `tool-use` has `1`

This means the draft trunks are plausible. It does not mean they are ready for
bulk migration.

## Pilot Choice

Choose `review-compaction` as the first direct-read migration review.

Projection entries:

| technique | current path | proposed future path |
|---|---|---|
| `AOA-T-0051` | `techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md` | `techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md` |
| `AOA-T-0052` | `techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md` | `techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md` |
| `AOA-T-0054` | `techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md` | `techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md` |

Why this shelf first:

- it is small enough to review completely in one pass
- it recently crossed the kind-audit lane, so its classification pressure is
  fresh and visible
- it tests whether `continuity` is a real trunk, not just renamed handoff
- it contains one `recovery` kind inside a continuity shelf, which is a useful
  stress case for tree-versus-facets separation
- it has low link blast radius compared with larger shelves such as
  `instruction-surface`, `handoff-continuation`, or `kag-source-lift`

## Backup Pilot

If direct reading rejects `review-compaction`, use `media-ingest` as the backup
pilot review.

Projection entries:

- `AOA-T-0070`
- `AOA-T-0071`
- `AOA-T-0072`
- `AOA-T-0073`
- `AOA-T-0074`

Reason: it is cleanly shaped, all current entries share `ingest`, and the shelf
is easy for a human reader to understand. It tests a narrow trunk, while
`review-compaction` tests a cross-kind continuity shelf.

## Hold Lines From Projection

- Keep `automation-governance` as `split-review-needed`; it should not become
  the first migration pilot.
- Keep `tool-gateway` as `singleton-hold`; one technique can signal a future
  trunk without justifying an immediate shelf move.
- Keep `runtime-truth-lifecycle`, `capability-*`, `skill-discovery`,
  `approval-evidence`, `review-evidence`, and `owner-truth-closeout` in
  `boundary-watch` until direct reading resolves owner/proof/governance
  pressure.
- Keep larger clean shelves such as `instruction-surface`,
  `handoff-continuation`, and `kag-source-lift` behind the first pilot so the
  migration machinery is tested on a smaller surface first.

## Stop Lines

- Do not move `review-compaction` from this review alone.
- Do not add `tree_path` frontmatter.
- Do not add `family` frontmatter.
- Do not rename trunks or shelves from the generated projection alone.
- Do not bulk-migrate all `pilot-candidate` shelves.
- Do not treat future paths as currently valid links.

## Next Honest Move

Run a direct-read migration review for the `review-compaction` shelf.
This has now landed as
[Review-Compaction Direct-Read Migration Review](review-compaction-direct-read-migration-review.md).

That review should open the three bundles, inspect local links, generated
surface blast radius, capsule/catalog assumptions, and docs references, then
decide whether the first pilot move is actually clearer than the current
`techniques/agent-workflows/*` placement.

That review accepted `review-compaction` for the first pilot migration. Only
the later migration wave should move files.
