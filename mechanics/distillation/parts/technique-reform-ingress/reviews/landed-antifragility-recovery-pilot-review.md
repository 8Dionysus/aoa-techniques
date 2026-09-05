# Landed Antifragility-Recovery Pilot Review

Source packet:
[Technique Reform Ingress](../README.md)

Migration review:
[Antifragility-Recovery Direct-Read Migration Review](antifragility-recovery-direct-read-migration-review.md)

Migration receipt:
[Antifragility-Recovery Tree Pilot Receipt](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/legacy/receipts/2026-05-05-antifragility-recovery-tree-pilot.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: pilot-validated, choose `execution/ready-work-graphs` for direct-read
migration review, not path migration, not `tree_path` frontmatter.

## Verdict

Accept the landed `antifragility-recovery` pilot as a successful fifteenth tree
migration and the second successful shelf under the `recovery` trunk.

The shelf stayed useful after landing. `AOA-T-0097`, `AOA-T-0099`,
`AOA-T-0100`, and `AOA-T-0098` now sit under one recovery-facing neighborhood
while IDs, `domain`, `kind`, status, evidence, notes, examples, checks,
relations, maturity, validation-strength metadata, and public-safety posture
stayed unchanged. The migration made the stress-to-receipt-to-recovery corridor
easy to browse without turning it into Agents-of-Abyss Antifragility doctrine,
incident response, runtime self-healing, rollback policy, proof authority, KAG
meaning, stats meaning, playbook choreography, service catalog ownership, or a
generic resilience platform.

This review does not move another shelf. It confirms that the next honest tree
slice should run a direct-read review for `execution/ready-work-graphs`. The
next review must read the three execution candidates directly before any path
movement, because blocker graphs, ready frontiers, and requirement/design/task
ladders can easily drift into project-management doctrine if the execution
trunk is accepted only from projection rows.

## Sources Read

- [AOA-T-0097 degrade-reground-recover](../../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md)
- [AOA-T-0099 isolated-service-stop-on-shared-substrate](../../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md)
- [AOA-T-0100 stress-receipt-reground-closeout](../../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md)
- [AOA-T-0098 receipt-first-failure-analysis](../../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md)
- [Recovery route card](../../../../../techniques/recovery/AGENTS.md)
- [Root legacy index](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/legacy/INDEX.md)
- [Antifragility-recovery tree pilot receipt](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/legacy/receipts/2026-05-05-antifragility-recovery-tree-pilot.md)
- [Antifragility-recovery direct-read migration review](antifragility-recovery-direct-read-migration-review.md)
- [Landed diagnosis-repair pilot review](landed-diagnosis-repair-pilot-review.md)
- [Technique tree projection rows for `antifragility-recovery` and `ready-work-graphs`](../reports/technique_tree_projection.md)
- [Technique family scout rows for `ready-work-graphs`](../reports/technique_family_scout.md)
- [Technique topology scout rows for `ready-work-graphs`](../reports/technique_topology_scout.md)
- [AOA-T-0049 dependency-aware-task-graph](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md)
- [AOA-T-0050 ready-work-from-blocker-graph](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md)
- [AOA-T-0055 requirements-design-tasks-ladder](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md)
- the release lane result recorded in the migration receipt

## Landed Shape Read

| check | result | reading |
|---|---|---|
| current path | `techniques/recovery/antifragility-recovery/` | the active path now matches the projected `recovery` trunk and `antifragility-recovery` shelf |
| frontmatter truth | unchanged | `AOA-T-0097`, `AOA-T-0099`, and `AOA-T-0100` remain `domain: system-recovery`; `AOA-T-0098` remains `domain: validation-patterns` and `kind: validation` |
| route card | present | `techniques/recovery/AGENTS.md` names the shelf while keeping recovery as a tree trunk, not a frontmatter domain |
| root legacy | receipt only | active bundles moved directly between authored homes; `legacy/` preserves accounting |
| generated surfaces | rebuilt | catalogs, capsules, manifests, reports, source-owned KAG exports, and reader surfaces point at current paths |
| link repair | complete enough for this stage | Antifragility mechanics, audit readiness, active review sources, root docs, and generated readers route to current authored paths; old paths remain only in receipts, tests, raw legacy, and migration accounting |
| validation | green | release check covered unit tests, nested AGENTS coverage, repository parity, generated parity, tree projection parity, and source-owned KAG export parity |

## What The Fifteenth Pilot Proved

- `recovery/` can hold a second shelf with a different center than
  `diagnosis-repair`: stress-aware degraded continuation and receipt-first
  recovery review rather than diagnosis-to-repair shape selection.
- Path architecture can improve browsing without erasing frontmatter truth.
  `AOA-T-0098` is easier to find beside the stress and recovery leaves, but it
  still remains a validation-shaped technique.
- A shelf may intentionally contain one cross-domain leaf when the leaf keeps
  the shelf honest. Here, receipt-first failure analysis prevents recovery
  claims from becoming folklore, dashboards, or proof theater.
- A runtime-adjacent recovery leaf can stay bounded when the target stop,
  shared substrate, evidence, and escalation posture stay explicit.
- Root `legacy/receipts/` remains sufficient for migration accounting; active
  bundles did not need to pass through legacy.

## Remaining Weaknesses

- `AOA-T-0098` will remain a watch point: future readers may over-trust the
  recovery path and forget that its canonical move shape is validation.
- `AOA-T-0099` still carries runtime-adjacent pressure, so later shelves around
  runtime truth or service lifecycle must not import its stop semantics by
  proximity.
- The generated projection still labels landed shelves as `candidate`. That is
  tolerable while projection remains a non-authoritative lens, but later
  generated status language may need its own review.
- The recovery trunk now has two precedents, not a complete recovery taxonomy.
  Any neighboring recovery shelf still needs direct reading before movement.
- `family`, `tree_path`, capability, substrate, execution-profile, and risk
  axes are still scout or projection layers, not bundle frontmatter truth.

## Sixteenth Shelf Choice

Choose `execution/ready-work-graphs` for the next direct-read migration review.

Projected shelf:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0049` | `techniques/agent-workflows/dependency-aware-task-graph/` | `techniques/execution/ready-work-graphs/dependency-aware-task-graph/` |
| `AOA-T-0050` | `techniques/agent-workflows/ready-work-from-blocker-graph/` | `techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/` |
| `AOA-T-0055` | `techniques/agent-workflows/requirements-design-tasks-ladder/` | `techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/` |

Reason:

`ready-work-graphs` is the next clean candidate because it tests the first
`execution` trunk shelf with three promoted workflow techniques that are already
bounded around pre-execution and between-slice work selection. The shelf is not
the full `agent-workflows` backbone. It is the narrow neighborhood where
dependency graphs, blocker-derived ready frontiers, and requirement/design/task
ladders make the next executable slice visible before broader execution work
continues.

Why direct-read first:

The three bundles share readiness pressure, but their boundaries differ.
`AOA-T-0049` owns explicit dependency graph authoring, `AOA-T-0050` owns a
ready queue derived from an existing blocker graph, and `AOA-T-0055` owns a
requirements -> design -> tasks ladder before implementation. The next review
must decide whether those are one shelf or whether the ladder wants a separate
planning shelf. It must also keep the shelf smaller than project-management
platform doctrine, scheduling, staffing, dispatch, memory substrate, or hidden
agent orchestration.

Why not the neighboring execution shelves first:

`intent-chain` is smaller but closer to action-contract rollout and should wait
until the execution trunk has one visible work-readiness precedent.
`agent-workflows-core` is larger and more canonical; it should not be the first
execution shelf because it would put the broad workflow backbone before the
tree proves that a small execution shelf can stay bounded.
`runtime-truth-lifecycle` carries runtime and lifecycle authority pressure and
should wait until the cleaner read-only execution shelf has been tested.

## Stop Lines

- Do not move `execution/ready-work-graphs` from this review alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not treat `antifragility-recovery` as incident response, runtime
  self-healing, runtime ownership, proof authority, rollback policy,
  deployment lifecycle law, service catalog ownership, KAG authority, stats
  meaning, playbook choreography, or a generic resilience platform.
- Do not erase `AOA-T-0098` as `domain: validation-patterns` and
  `kind: validation`.
- Do not treat `ready-work-graphs` as project management, scheduling, staffing,
  dispatch policy, memory substrate, graph database doctrine, hidden
  orchestration, or proof of execution readiness.
- Do not move `intent-chain`, `agent-workflows-core`, `runtime-truth-lifecycle`,
  governance, continuity, proof, automation, tool-use, owner-truth, or
  neighboring shelves in the same wave.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run a direct-read migration review for `execution/ready-work-graphs`.

Read `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055`; inspect their support
files, relations, external import notes, current `agent-workflows` route card,
projection rows, family scout, topology scout, and small-agent selection
pressure; decide whether the three leaves belong together under
`techniques/execution/ready-work-graphs/`; preserve graph, readiness,
planning-ladder, project-management, scheduling, staffing, dispatch, memory,
orchestration, and proof stop lines; and do not move any files until that
review lands.
