# Handoff-Continuation Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Projection packet:
[First Tree Projection Review Pack](first-tree-projection-review-pack.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Prior pilot review:
[Landed Review-Compaction Pilot Review](landed-review-compaction-pilot-review.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-second-migration-pilot, not path migration, not `tree_path` frontmatter.

## Verdict

Accept `handoff-continuation` as the second migration pilot.

The move is clearer than current placement because the seven bundles share one
continuity problem: work, communication, or reviewable state must cross a
session, agent, repo, compaction, or episode boundary without depending on
hidden memory, stale narration, or a broad orchestration stack.
`agent-workflows` remains true as their current `domain`, but it is too broad
as a browsing neighborhood now that the corpus is growing toward a larger tree.

This review does not move files. It only decides that the next bounded wave may
move exactly this shelf if links, generated surfaces, validation, route cards,
and root legacy receipts move together.

## Sources Read

- [AOA-T-0056 channelized-agent-mailbox](../../../../../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md)
- [AOA-T-0057 structured-handoff-before-compaction](../../../../../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md)
- [AOA-T-0058 receipt-confirmed-handoff-packet](../../../../../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md)
- [AOA-T-0059 git-verified-handoff-claims](../../../../../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md)
- [AOA-T-0060 session-opening-ritual-before-work](../../../../../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md)
- [AOA-T-0061 cross-repo-resource-map-bootstrap](../../../../../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md)
- [AOA-T-0062 episode-bounded-agent-loop](../../../../../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md)
- supporting `checks/`, `examples/`, and `notes/` files for the seven bundles,
  scanned for invariant, adjacency, validation, and drift-pressure cues
- current references found by `rg` across the seven source bundles
- `reports/technique_tree_projection.md` rows for `AOA-T-0056` through
  `AOA-T-0062`

## Direct Read

| technique | current kind | center of gravity | pilot reading |
|---|---|---|---|
| `AOA-T-0056` `channelized-agent-mailbox` | `handoff` | durable named mailbox channels with ordered replay and explicit ack state | continuity of communication transport across session gaps, not handoff authorization |
| `AOA-T-0057` `structured-handoff-before-compaction` | `handoff` | one explicit continuation packet written before compaction or rollover | continuity of work state across context loss, not transcript packaging or phase governance |
| `AOA-T-0058` `receipt-confirmed-handoff-packet` | `handoff` | visible receipt state after a handoff packet exists and before continuation trusts delivery | continuity of receiver acceptance across the delivery/continuation boundary |
| `AOA-T-0059` `git-verified-handoff-claims` | `handoff` | concrete handoff claims checked against visible git evidence before resuming | continuity of trust from packet narration to repo-backed current state |
| `AOA-T-0060` `session-opening-ritual-before-work` | `handoff` | pre-mutation session start that rereads context and checks one visible baseline | continuity from inherited context into current reality before action |
| `AOA-T-0061` `cross-repo-resource-map-bootstrap` | `handoff` | one task-bounded map of repos and resource surfaces needed for continuation | continuity of first-look routing across repo boundaries, not a full bounded-context model |
| `AOA-T-0062` `episode-bounded-agent-loop` | `handoff` | longer work split into episodes with checkpoints and continue, stop, or escalate decisions | continuity of multi-episode work through visible checkpoint state, not a whole orchestrator |

The shared shelf is not "handoff" as a vague theme. It is the narrower
continuation seam where a later actor, later session, or later episode can
resume from visible state rather than from memory, platform magic, or broad
process doctrine.

## Boundary Read

The shelf remains useful only if the bundle boundaries stay sharp:

- `AOA-T-0056` owns mailbox transport, not continuation permission.
- `AOA-T-0057` owns the packet, not receipt, git verdict, transcript export, or
  phase policy.
- `AOA-T-0058` owns receipt state, not delivery mechanics or approval
  governance.
- `AOA-T-0059` owns repo-backed claim verification, not generic code review or
  full provenance.
- `AOA-T-0060` owns the opening ritual, not the whole change loop or startup
  doctrine.
- `AOA-T-0061` owns the task-bounded cross-repo first-look map, not bounded
  context architecture.
- `AOA-T-0062` owns episode segmentation, not runtime supervision, budgets,
  task trackers, or autonomous-agent doctrine.

Those boundaries are exactly why the shelf works. It keeps sibling techniques
near each other without merging them into one handoff framework.

## Why Not Keep This As Agent Workflows

`agent-workflows` remains true as `domain`: these are still reusable
agent-session practices, and their first review lane remains in this
repository's workflow corpus.

The directory tree is now answering a different question. It should help a
human or small agent find the nearest usable leaf. On that question,
`continuity/handoff-continuation` is tighter than the old broad folder:

- all seven bundles already describe explicit state transfer, receipt,
  verification, startup, routing, or checkpoint seams
- several bundles cite each other as adjacency boundaries, which means the
  reader benefits from local shelf proximity
- the shelf preserves atom boundaries instead of hiding a total handoff chain
  in one overgrown technique
- the path reinforces the corpus tree without changing `domain`, `kind`,
  status, owners, evidence, or bundle meaning

## Pilot Scope

Move exactly these seven bundles in the next migration wave:

| technique | current path | pilot path |
|---|---|---|
| `AOA-T-0056` | `techniques/agent-workflows/channelized-agent-mailbox/` | `techniques/continuity/handoff-continuation/channelized-agent-mailbox/` |
| `AOA-T-0057` | `techniques/agent-workflows/structured-handoff-before-compaction/` | `techniques/continuity/handoff-continuation/structured-handoff-before-compaction/` |
| `AOA-T-0058` | `techniques/agent-workflows/receipt-confirmed-handoff-packet/` | `techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/` |
| `AOA-T-0059` | `techniques/agent-workflows/git-verified-handoff-claims/` | `techniques/continuity/handoff-continuation/git-verified-handoff-claims/` |
| `AOA-T-0060` | `techniques/agent-workflows/session-opening-ritual-before-work/` | `techniques/continuity/handoff-continuation/session-opening-ritual-before-work/` |
| `AOA-T-0061` | `techniques/agent-workflows/cross-repo-resource-map-bootstrap/` | `techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/` |
| `AOA-T-0062` | `techniques/agent-workflows/episode-bounded-agent-loop/` | `techniques/continuity/handoff-continuation/episode-bounded-agent-loop/` |

Keep bundle IDs, `domain`, `kind`, `status`, owners, evidence, relations,
checklists, examples, notes, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored cross-links inside the seven moved bundles, including their
  `TECHNIQUE.md` adjacency paragraphs and `notes/second-context-adaptation.md`
  / `notes/canonical-readiness.md` references
- adjacent links from already-migrated continuity bundles, especially
  `compaction-resilient-skill-loading`
- historical mechanics review links that currently point at the old paths
- `techniques/continuity/AGENTS.md`, because the trunk would have two accepted
  shelves after the move
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- generated reader docs such as `TECHNIQUE_INDEX.md`, `docs/TECHNIQUE_*`,
  `docs/EVIDENCE_NOTE_SURFACES.md`, and generated manifests
- generated reports for family, topology, and tree projection
- release-check output touched by regenerated catalogs, capsules, sections,
  examples, checklists, evidence notes, and repo-doc surfaces

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `family` or `tree_path` frontmatter.
- Do not move other `pilot-candidate` shelves in the same wave.
- Do not rename `continuity` or `handoff-continuation` during the pilot move.
- Do not change `domain`; the pilot tests path architecture, not owner-lane
  frontmatter.
- Do not merge the seven techniques into one handoff framework.
- Do not claim `handoff-continuation` is canonical shelf truth for every future
  handoff-like technique until one actual migration validates the shape.

## Next Honest Move

Run the second pilot migration.

Move exactly `AOA-T-0056` through `AOA-T-0062` into
`techniques/continuity/handoff-continuation/`, update the continuity trunk route
card, repair authored links, preserve a root legacy receipt, rebuild generated
surfaces, and run `python scripts/release_check.py`.
