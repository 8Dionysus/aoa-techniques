# Ready-Work-Graphs Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Preceding landed review:
[Landed Antifragility-Recovery Pilot Review](landed-antifragility-recovery-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-sixteenth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `execution/ready-work-graphs` as the sixteenth bounded tree migration
pilot.

Direct reading confirms that `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055`
form one execution shelf around visible readiness before or between bounded
work slices. The shelf is not project management and not the whole
`agent-workflows` backbone. It is the portable corridor where dependency
state, blocker-free frontier selection, and requirement -> design -> task
layering make the next executable step visible without relying on chat memory,
hidden prioritization, or full tracker doctrine.

The shelf is accepted with one watch line. `AOA-T-0055` is not graph-derived in
the same way as `AOA-T-0049` and `AOA-T-0050`; it is a planning ladder. Direct
reading still supports the move because the ladder's invariant is
pre-execution readiness: tasks are derived from visible design, design answers
visible requirements, and later execution still belongs to a separate
workflow. That makes it a companion readiness leaf, not a methodology import.

This review does not move files. It only authorizes a later migration wave to
move exactly these three bundles into `techniques/execution/ready-work-graphs/`
if that wave also creates or updates the execution route card, preserves
frontmatter, adds root legacy accounting, repairs links, rebuilds generated
surfaces, and validates the repository.

## Sources Read

- [AOA-T-0049 dependency-aware-task-graph](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md)
- [AOA-T-0049 checklist](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/checks/dependency-aware-task-graph-checklist.md)
- [AOA-T-0049 minimal example](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/examples/minimal-dependency-aware-task-graph.md)
- [AOA-T-0049 external origin](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/notes/external-origin.md)
- [AOA-T-0049 second context adaptation](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/notes/second-context-adaptation.md)
- [AOA-T-0049 external import review](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/notes/external-import-review.md)
- [AOA-T-0049 canonical readiness](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/notes/canonical-readiness.md)
- [AOA-T-0050 ready-work-from-blocker-graph](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md)
- [AOA-T-0050 checklist](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/checks/ready-work-from-blocker-graph-checklist.md)
- [AOA-T-0050 minimal example](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/examples/minimal-ready-work-from-blocker-graph.md)
- [AOA-T-0050 external origin](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/notes/external-origin.md)
- [AOA-T-0050 second context adaptation](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/notes/second-context-adaptation.md)
- [AOA-T-0050 external import review](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/notes/external-import-review.md)
- [AOA-T-0050 canonical readiness](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/notes/canonical-readiness.md)
- [AOA-T-0055 requirements-design-tasks-ladder](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md)
- [AOA-T-0055 checklist](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/checks/requirements-design-tasks-ladder-checklist.md)
- [AOA-T-0055 minimal example](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/examples/minimal-requirements-design-tasks-ladder.md)
- [AOA-T-0055 external origin](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/notes/external-origin.md)
- [AOA-T-0055 second context adaptation](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/notes/second-context-adaptation.md)
- [AOA-T-0055 external import review](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/notes/external-import-review.md)
- [AOA-T-0055 canonical readiness](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/notes/canonical-readiness.md)
- [Agent-workflows route card](../../../../../techniques/agent-workflows/AGENTS.md)
- [Technique tree projection rows for `ready-work-graphs`](../../../../../reports/technique_tree_projection.md)
- [Technique family scout rows for `ready-work-graphs`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `ready-work-graphs`](../../../../../reports/technique_topology_scout.md)
- [Landed antifragility-recovery pilot review](landed-antifragility-recovery-pilot-review.md)

## Direct Bundle Read

| technique | current path | domain | kind | status | direct-read result |
|---|---|---|---|---|---|
| `AOA-T-0049` | `techniques/agent-workflows/dependency-aware-task-graph/` | `agent-workflows` | `workflow` | `promoted` | owns explicit dependency nodes, blocker edges, and ready work derived from graph state rather than memory |
| `AOA-T-0050` | `techniques/agent-workflows/ready-work-from-blocker-graph/` | `agent-workflows` | `workflow` | `promoted` | owns the derived ready queue over an existing blocker graph, keeping blocked exclusions visible and ranking policy outside |
| `AOA-T-0055` | `techniques/agent-workflows/requirements-design-tasks-ladder/` | `agent-workflows` | `workflow` | `promoted` | owns a requirements -> design -> tasks ladder before implementation, keeping task slices traceable without importing a full methodology stack |

The first two leaves are graph/queue siblings. The third leaf is accepted
because it prepares a ready task layer before execution starts. It should stay
near the graph leaves only while the shelf is framed as ready-work visibility,
not as graph data modeling.

## Why The Shelf Holds

- `AOA-T-0049` supplies the explicit graph surface: tasks become nodes, blockers
  become edges, and the ready frontier can be recomputed.
- `AOA-T-0050` supplies the frontier view over that graph: open work is not
  automatically ready, and blocked exclusions remain visible.
- `AOA-T-0055` supplies the pre-graph planning ladder: tasks should be derived
  from a visible design response to a visible requirement before later
  dependency modeling or execution selection begins.
- All three leaves keep readiness weaker than execution proof. They prepare the
  next honest work slice; they do not implement, verify, dispatch, schedule, or
  prove the work themselves.

## Watch Line For `AOA-T-0055`

Do not split before the sixteenth migration, but preserve the watch.

`AOA-T-0055` is not a blocker-graph technique. Its fit is that it creates a
bounded task layer that can later be coordinated, sequenced, or executed. The
support files keep that boundary explicit: the checklist says later execution
still needs its own workflow technique, the external import review excludes
template ecosystems and methodology doctrine, and the canonical readiness note
keeps it promoted until another live context proves the ladder beyond the donor
family.

The migration should not rename the shelf to `dependency-graphs` or the ladder
would look misplaced. `ready-work-graphs` remains acceptable because it names
the browsing problem: make ready work visible before action.

## Execution Trunk Fit

`execution/` is the right trunk because the shelf prepares bounded work to be
done. The leaves are still read-only or planning-shaped, but their purpose is
execution readiness: what can be worked, why it is ready, what remains blocked,
and what task layer the later executor should consume.

This shelf also gives the execution trunk a safe first precedent. It is smaller
than `agent-workflows-core`, less action-contract-heavy than `intent-chain`,
and less runtime-authority-sensitive than `runtime-truth-lifecycle`.

## Boundary Watch Accepted

The projection marks `ready-work-graphs` as `candidate`, but direct reading
confirms several authority pressures:

- `AOA-T-0049` can drift into project management, memory substrate, graph
  database doctrine, or tracker product behavior if blocker edges become
  broad relation semantics.
- `AOA-T-0050` can drift into prioritization, ranking, staffing, dispatch, or
  hidden override policy if blocker-free eligibility stops being the first
  gate.
- `AOA-T-0055` can drift into a full methodology, template suite, command
  system, steering surface, project memory doctrine, or execution workflow if
  the layer transitions stop being the center.

The shelf is accepted because those pressures are explicit in the bundle
contracts, checklists, examples, external-origin notes, import reviews, and
canonical-readiness notes.

## Proposed Move

Move exactly these three bundles in the migration wave:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0049` | `techniques/agent-workflows/dependency-aware-task-graph/` | `techniques/execution/ready-work-graphs/dependency-aware-task-graph/` |
| `AOA-T-0050` | `techniques/agent-workflows/ready-work-from-blocker-graph/` | `techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/` |
| `AOA-T-0055` | `techniques/agent-workflows/requirements-design-tasks-ladder/` | `techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/` |

Keep `domain`, `kind`, status, IDs, evidence, relations, maturity,
validation-strength metadata, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- a new or updated `techniques/execution/AGENTS.md`, because `execution/` does
  not yet have a trunk route card in the current tree
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- authored links from adjacent workflow techniques, generated selection docs,
  review packets, and external-import references
- generated catalogs, capsules, manifests, reports, KAG exports, docs readers,
  and source-lift surfaces after the path move
- tests that still assert the old broad `agent-workflows/` paths as current

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Why Not Neighbor Shelves In This Wave

`intent-chain` should wait because it carries action-contract and rollout
pressure rather than work-readiness graph pressure.

`agent-workflows-core` should wait because it is larger, more canonical, and
closer to the generic execution backbone. Moving it first would make the
execution trunk too broad before a smaller shelf proves the shape.

`runtime-truth-lifecycle` should wait because it touches runtime composition,
host readiness, lifecycle, and service posture.

`donor-harvest`, `decision-routing`, `automation-governance`,
`review-evidence`, and `owner-truth-closeout` should wait because they carry
continuity, governance, automation, proof, or owner-acceptance pressure rather
than ready-work visibility.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not change `domain` or `kind`; this pilot tests path architecture, not
  frontmatter remap.
- Do not treat `ready-work-graphs` as project-management doctrine, scheduling,
  staffing, dispatch policy, backlog governance, graph database doctrine,
  memory substrate, hidden orchestration, proof of readiness, or execution
  validation.
- Do not collapse graph authoring, ready-frontier derivation, and
  requirement/design/task layering into one mega-technique.
- Do not move `intent-chain`, `agent-workflows-core`,
  `runtime-truth-lifecycle`, continuity, governance, proof, automation,
  tool-use, owner-truth, or neighboring shelves in the same wave.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the sixteenth pilot migration.

Move exactly `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055` into
`techniques/execution/ready-work-graphs/` after creating the execution trunk
route card and preserving the watch line that `AOA-T-0055` is a readiness
ladder, not a graph database, methodology, or execution workflow.
