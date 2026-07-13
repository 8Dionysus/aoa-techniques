# Review-Compaction Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Projection packet:
[First Tree Projection Review Pack](first-tree-projection-review-pack.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-first-migration-pilot, not path migration, not `tree_path` frontmatter.

## Verdict

Accept `review-compaction` as the first migration pilot.

The move is clearer than current placement because the three bundles share a
single continuity problem: review or capability context must survive across a
boundary where the original working surface can become stale, noisy, or
compact. `agent-workflows` still describes their current owner lane, but it no
longer helps a reader find the nearby techniques as directly as
`techniques/continuity/review-compaction/`.

This review does not move files. It only decides that the next bounded wave may
move exactly this shelf if links, generated surfaces, validation, and route
cards move together.

## Sources Read

- [AOA-T-0051 commit-triggered-background-review](../../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md)
- [AOA-T-0051 checklist](../../../../../techniques/continuity/review-compaction/commit-triggered-background-review/checks/commit-triggered-background-review-checklist.md)
- [AOA-T-0051 example](../../../../../techniques/continuity/review-compaction/commit-triggered-background-review/examples/minimal-commit-triggered-background-review.md)
- [AOA-T-0051 canonical readiness](../../../../../techniques/continuity/review-compaction/commit-triggered-background-review/notes/canonical-readiness.md)
- [AOA-T-0052 review-findings-compaction](../../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md)
- [AOA-T-0052 checklist](../../../../../techniques/continuity/review-compaction/review-findings-compaction/checks/review-findings-compaction-checklist.md)
- [AOA-T-0052 example](../../../../../techniques/continuity/review-compaction/review-findings-compaction/examples/minimal-review-findings-compaction.md)
- [AOA-T-0052 canonical readiness](../../../../../techniques/continuity/review-compaction/review-findings-compaction/notes/canonical-readiness.md)
- [AOA-T-0054 compaction-resilient-skill-loading](../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md)
- [AOA-T-0054 checklist](../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/checks/compaction-resilient-skill-loading-checklist.md)
- [AOA-T-0054 example](../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/examples/minimal-compaction-resilient-skill-loading.md)
- [AOA-T-0054 canonical readiness](../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/notes/canonical-readiness.md)
- [AOA-T-0054 Kind Destination Check](0054-kind-destination-check.md)
- current references found by `rg` across authored docs, generated docs,
  reports, mechanics reviews, and related technique bundles

## Direct Read

| technique | current kind | center of gravity | pilot reading |
|---|---|---|---|
| `AOA-T-0051` `commit-triggered-background-review` | `workflow` | commit boundary produces an inspectable review artifact that may later become stale | continuity of review evidence across commit and async review timing |
| `AOA-T-0052` `review-findings-compaction` | `workflow` | noisy or repeated findings are revalidated and compacted into one current review surface | continuity of current review truth across repeated runs and stale findings |
| `AOA-T-0054` `compaction-resilient-skill-loading` | `recovery` | compaction weakens capability context and a bounded skill-availability surface is restored | continuity of capability discoverability across context compaction |

The shared shelf is not "review" alone. It is continuity after a review,
findings, or skill-loading surface crosses a state boundary.

## Why Not Keep This As Agent Workflows

`agent-workflows` remains true as `domain`: these techniques are still reusable
agent-session practices, and their first owner lane stays in this repository's
workflow corpus.

The directory tree is now answering a different question. It should help a
reader find nearby techniques. On that question, `review-compaction` is tighter
than the current broad domain folder:

- `AOA-T-0051` and `AOA-T-0052` are already explicit siblings.
- `AOA-T-0054` is not a review technique, but the direct-read kind correction
  already proved it belongs near compaction and continuity pressure.
- keeping all three in a future continuity trunk preserves the distinction
  between `kind` and path: two workflows plus one recovery technique can share
  one shelf without falsifying frontmatter.

## Pilot Scope

Move exactly these three bundles in the next migration wave:

| technique | current path | pilot path |
|---|---|---|
| `AOA-T-0051` | `techniques/agent-workflows/commit-triggered-background-review/` | `techniques/continuity/review-compaction/commit-triggered-background-review/` |
| `AOA-T-0052` | `techniques/agent-workflows/review-findings-compaction/` | `techniques/continuity/review-compaction/review-findings-compaction/` |
| `AOA-T-0054` | `techniques/agent-workflows/compaction-resilient-skill-loading/` | `techniques/continuity/review-compaction/compaction-resilient-skill-loading/` |

Keep bundle IDs, `domain`, `kind`, `status`, owners, evidence, relations,
checklists, examples, notes, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored cross-links from sibling bundles, including
  `structured-handoff-before-compaction`, `audit-to-closeout-proof-loop`, and
  `perceptual-media-dedupe-with-threshold-review`
- historical mechanics review links that currently point at the old paths
- generated reader docs such as `TECHNIQUE_INDEX.md`, `docs/TECHNIQUE_*`,
  `docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md`, and generated manifests
- generated reports for family, topology, and tree projection
- validator expectations that derive paths from bundle discovery
- any release-check output touched by regenerated catalogs, capsules,
  sections, examples, checklists, evidence notes, and repo-doc surfaces

Create a minimal `techniques/continuity/AGENTS.md` in the migration wave so the
new trunk has local route guidance. Do not create mechanic-style `parts/`
packages or shelf READMEs for technique leaves.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `family` or `tree_path` frontmatter.
- Do not move other `pilot-candidate` shelves in the same wave.
- Do not rename `continuity` or `review-compaction` during the pilot move.
- Do not change `domain`; the pilot tests path architecture, not owner-lane
  frontmatter.
- Do not claim `review-compaction` is canonical shelf truth for the whole
  future corpus until one actual migration validates the shape.

## Next Honest Move

Run the first pilot migration.

Move exactly `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054` into
`techniques/continuity/review-compaction/`, add the minimal trunk `AGENTS.md`,
repair authored links, and rebuild generated surfaces.
Run the release lane.
