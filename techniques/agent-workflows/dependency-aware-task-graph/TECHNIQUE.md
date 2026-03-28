---
id: AOA-T-0049
name: dependency-aware-task-graph
domain: agent-workflows
status: promoted
origin:
  project: steveyegge/beads
  path: README.md
  note: Adapted from the open-source Beads project, which exposes blocker-aware ready work over an explicit dependency graph for agent task coordination.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - dependency-graph
  - blockers
  - ready-work
  - coordination
summary: Model multi-step coding work as explicit dependency nodes and edges so blocked state and ready work stay reviewable instead of hiding in chat memory.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-27
export_ready: true
relations:
  - type: complements
    target: AOA-T-0001
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# dependency-aware-task-graph

## Intent

Represent multi-step coding work as an explicit dependency graph so blocked state, ready state, and ordering decisions stay visible instead of disappearing into chat memory or ad hoc operator intuition.

## When to use

- several bounded tasks depend on one another
- the next safe slice should come from real prerequisite state, not from memory
- humans or agents need one durable working surface for ready versus blocked work
- the workflow needs coordination structure without becoming a full project-management system

## When not to use

- one bounded task can be handled without dependency modeling
- the real need is a full tracker with scheduling, estimation, staffing, or reporting policy
- the graph is being used as a memory substrate or knowledge graph rather than a work-coordination surface
- the ready view would be invented theater rather than a reflection of real execution constraints

## Inputs

- task nodes that describe reviewable work slices
- explicit dependency edges between those nodes
- current task state
- optional owner or label hints that do not replace the dependency contract

## Outputs

- a reviewable task graph
- a ready frontier derived from satisfied prerequisites
- explicit blocked reasons for work that cannot start yet
- a durable coordination surface that can be updated as state changes

## Core procedure

1. List the smallest real task nodes that matter for the current bounded workflow.
2. Record explicit dependency edges between nodes that truly block one another.
3. Derive ready work from the nodes whose prerequisites are satisfied.
4. Choose the next bounded step from that ready frontier instead of guessing from memory.
5. Update node state when real work completes or blocker state changes.
6. Recompute the ready frontier after each meaningful state change.
7. Keep the graph subordinate to implementation review, validation, and reporting rather than treating the graph itself as the final proof surface.

## Contracts

- dependency edges are explicit
- ready work is derived from graph state, not guessed from memory or inferred from narrative alone
- blocked work includes a named unmet prerequisite
- node granularity stays tied to reviewable execution steps rather than broad project themes
- the graph remains a working surface, not a memory substrate, dashboard product, or full project-management system
- implementation review and validation still happen in their own canonical surfaces

Relationship to adjacent techniques: unlike `AOA-T-0001`, this technique does not own the full change protocol of plan, diff, verify, and report. It complements that workflow by making dependency order and ready work visible before or between bounded execution slices.

## Risks

### Failure modes

- stale edges keep work blocked after the blocker is gone
- hidden cycles make the ready frontier misleading
- node scopes become so large that the graph stops helping with execution order

### Negative effects

- over-modeling can slow down simple work
- the graph can create false precision when completion signals are weak
- teams can spend more time curating the graph than finishing the bounded tasks it is supposed to coordinate

### Misuse patterns

- using the graph as a substitute for implementation review or release validation
- widening the graph into a full project-management doctrine
- treating knowledge links, memory features, or staffing policy as part of this bounded contract

### Detection signals

- many nodes have no clear completion signal
- the ready set does not match actual execution constraints
- people update the graph after the fact instead of using it to make next-step choices
- blocked tasks cannot name the specific unmet prerequisite that keeps them closed

### Mitigations

- keep node granularity small and reviewable
- name blockers explicitly instead of implying them
- re-check the ready frontier after every real state change
- split out reporting, memory, or platform features instead of widening this graph contract

## Validation

Verify the technique by confirming that:
- a known blocked node becomes ready only when its prerequisite flips
- blocked tasks can point to a real unmet prerequisite
- the ready frontier can be recomputed from the graph without relying on hidden session memory
- the graph remains smaller than a full project-management system
- implementation review and release validation still live outside the graph itself

See `checks/dependency-aware-task-graph-checklist.md`.

## Adaptation notes

What can vary across projects:
- node schema
- edge labels
- state vocabulary
- storage shape, UI, or CLI surface
- optional ownership fields

What should stay invariant:
- dependencies are explicit
- ready work is derived from current graph state
- blocked work names the unmet prerequisite
- the graph stays bounded to work coordination rather than broad platform behavior

Project-shaped details that should not be treated as invariant:
- one database or storage engine
- one task ID format or hierarchy style
- donor-specific molecule, epic, or claim semantics
- product dashboards, notifications, or dispatch features

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: explicit dependency nodes plus blocker-aware ready-work derivation for coding tasks. Persistent memory framing, tracker product semantics, graph-link taxonomy beyond blocking, auto-claim flows, hierarchy-heavy planning features, and donor runtime or storage specifics were intentionally left out of the public contract.

## Example

See `examples/minimal-dependency-aware-task-graph.md`.

## Checks

See `checks/dependency-aware-task-graph-checklist.md`.

## Promotion history

- adapted from open-source `steveyegge/beads`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-27 as a bounded external-import technique for dependency-aware work coordination

## Future evolution

- keep a ready-frontier-only sibling separate if `ready-work-from-blocker-graph` later proves independently reusable
- add a stronger second live context if another public repository uses the same explicit dependency-graph contract in practice
- add bounded graph-health checks only if they stay reviewable and do not widen into a project-management platform
