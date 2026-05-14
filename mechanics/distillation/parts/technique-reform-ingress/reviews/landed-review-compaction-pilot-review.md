# Landed Review-Compaction Pilot Review

Source packet:
[Technique Reform Ingress](../README.md)

Migration review:
[Review-Compaction Direct-Read Migration Review](review-compaction-direct-read-migration-review.md)

Migration receipt:
[Review-Compaction Tree Pilot Receipt](../../../../../legacy/receipts/2026-05-04-review-compaction-tree-pilot.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: pilot-validated, choose `handoff-continuation` for direct-read migration
review, not path migration, not `tree_path` frontmatter.

## Verdict

Accept the landed `review-compaction` pilot as a successful first tree
migration.

The pilot improved browsability without changing bundle meaning. The three
bundles now live where the generated projection says they should live, while
their IDs, `domain`, `kind`, status, evidence, notes, checklists, examples, and
public-safety posture stayed unchanged.

This review does not move more files. It confirms that the next honest tree
slice may be a direct-read migration review for `handoff-continuation`, because
that shelf is the nearest continuity sibling and will test whether
`continuity/` is a real trunk rather than a one-shelf exception.

## Sources Read

- [AOA-T-0051 commit-triggered-background-review](../../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md)
- [AOA-T-0052 review-findings-compaction](../../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md)
- [AOA-T-0054 compaction-resilient-skill-loading](../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md)
- [Continuity route card](../../../../../techniques/continuity/AGENTS.md)
- [Root legacy index](../../../../../legacy/INDEX.md)
- [Review-compaction tree pilot receipt](../../../../../legacy/receipts/2026-05-04-review-compaction-tree-pilot.md)
- [Technique tree projection rows for `review-compaction` and
  `handoff-continuation`](../reports/technique_tree_projection.md)
- `python scripts/release_check.py` result recorded in the migration receipt

## Landed Shape Read

| check | result | reading |
|---|---|---|
| current path | `techniques/continuity/review-compaction/` | the active path now matches the projected trunk and shelf |
| frontmatter truth | unchanged | `domain` still carries owner lane; `kind` still carries move shape |
| route card | present | `techniques/continuity/AGENTS.md` names the trunk boundary without pretending to be a new domain |
| root legacy | receipt only | active bundles moved directly between authored homes; `legacy/` preserves accounting |
| generated surfaces | rebuilt | catalogs, capsules, sections, examples, checklists, evidence notes, and projection surfaces point at current paths |
| validation | green | release check covered unit tests, nested AGENTS coverage, and repository parity |

## What The Pilot Proved

- A tree trunk can organize techniques by placement question without replacing
  `domain`.
- A shelf can hold different `kind` values when the shared browse question is
  real: two workflows and one recovery technique can still belong together.
- Root `legacy/receipts/` is the right accounting surface for path migration
  history, while active bundles remain in `techniques/`.
- The validator can support both the old domain layout and the new tree layout
  during the reform period.
- Generated projection can remain a review aid even after one shelf lands,
  because current paths and proposed paths are now equal for the landed shelf.

## Remaining Weaknesses

- `review-compaction` alone does not prove that `continuity/` is a stable trunk.
- `techniques/continuity/AGENTS.md` still names only the first accepted pilot
  shelf; it should be updated when another continuity shelf lands.
- No `boundary-watch` or `split-review-needed` shelf has been moved, so the
  current success applies only to clear pilot candidates.
- The corpus still has many broad-domain folders; this pilot proves the route,
  not the full tree.

## Next Shelf Choice

Choose `handoff-continuation` for the next direct-read migration review.

Projected shelf:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0056` | `techniques/agent-workflows/channelized-agent-mailbox/` | `techniques/continuity/handoff-continuation/channelized-agent-mailbox/` |
| `AOA-T-0057` | `techniques/agent-workflows/structured-handoff-before-compaction/` | `techniques/continuity/handoff-continuation/structured-handoff-before-compaction/` |
| `AOA-T-0058` | `techniques/agent-workflows/receipt-confirmed-handoff-packet/` | `techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/` |
| `AOA-T-0059` | `techniques/agent-workflows/git-verified-handoff-claims/` | `techniques/continuity/handoff-continuation/git-verified-handoff-claims/` |
| `AOA-T-0060` | `techniques/agent-workflows/session-opening-ritual-before-work/` | `techniques/continuity/handoff-continuation/session-opening-ritual-before-work/` |
| `AOA-T-0061` | `techniques/agent-workflows/cross-repo-resource-map-bootstrap/` | `techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/` |
| `AOA-T-0062` | `techniques/agent-workflows/episode-bounded-agent-loop/` | `techniques/continuity/handoff-continuation/episode-bounded-agent-loop/` |

Reason:

`handoff-continuation` is the closest real pressure test after
`review-compaction`. It stays inside `continuity`, but it shifts the central
object from review/capability context after compression to handoff state,
resume posture, and continuation packets across session or agent boundaries.

## Stop Lines

- Do not move `handoff-continuation` from this review alone.
- Do not add `tree_path`, `family`, or scout topology axes to frontmatter.
- Do not move `media-ingest`, `diagnosis-repair`, `instruction-surface`, or
  `kag-source-lift` in the same wave.
- Do not treat `continuity` as final trunk truth for all future shelves until
  at least one more continuity shelf lands cleanly.
- Do not move `boundary-watch`, `split-review-needed`, or `singleton-hold`
  shelves without a separate direct-read review.

## Next Honest Move

Run a direct-read migration review for `handoff-continuation`.

Read `AOA-T-0056` through `AOA-T-0062`, decide whether the shelf is clearer
than the broad `agent-workflows` folder, and only then choose whether to move
those exact bundles into `techniques/continuity/handoff-continuation/`.
