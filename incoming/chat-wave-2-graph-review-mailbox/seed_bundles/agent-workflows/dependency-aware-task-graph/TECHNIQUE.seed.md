---
id: AOA-T-XXXX
name: dependency-aware-task-graph
domain: agent-workflows
status: draft-seed
origin: chat-wave-2-graph-review-mailbox
note: seed bundle staged for operator-guided chat wave 2 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - graph-review-mailbox
summary: Model coding work as explicit dependency nodes and edges so blocked and ready work stays reviewable.
maturity_score: 1
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: donor_soil
export_ready: false
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.seed.md
---
# dependency-aware-task-graph

## Intent

Represent multi-step coding work as an explicit dependency graph so blocked state, ready state, and ordering decisions stay visible instead of hiding in chat memory.

## When to use

- multiple tasks block each other
- the next safe slice depends on upstream completion
- you need a durable working surface for ready versus blocked work

## When not to use

- one bounded task can be handled without dependency modeling
- the work is really a full project-management system
- the graph would be invented theater rather than real execution structure

## Inputs

- task nodes
- explicit dependency edges
- optional task state and owner hints

## Outputs

- reviewable task graph
- ready frontier derived from unmet dependencies
- explicit blocked reasons per task

## Core procedure

1. list the smallest real task nodes
2. record explicit dependency edges
3. derive ready work from nodes with satisfied prerequisites
4. update node state after each bounded step
5. keep the graph as a working surface, not a hidden memory layer

## Contracts

- dependency edges are explicit
- ready work is derived from graph state, not guessed
- blocked work includes a named blocker
- the technique stays smaller than a full PM platform

## Risks

### Failure modes

- stale edges keep work blocked after the blocker is gone
- fake precision creates a graph that no one trusts

### Negative effects

- over-modeling slows down simple work
- hidden cycles make the ready frontier misleading

### Misuse patterns

- using the graph as a substitute for implementation review
- letting the graph become a product taxonomy

### Detection signals

- many nodes have no real completion signal
- the ready set does not match actual execution constraints

### Mitigations

- keep node granularity small and reviewable
- name blockers explicitly
- re-check the ready frontier after every real state change

## Validation

- confirm the ready frontier changes when dependencies flip
- confirm blocked tasks point to real unmet prerequisites
- verify the graph remains smaller than a full PM system

## Adaptation notes

- node schema
- edge labeling
- status vocabulary
- local storage shape

## Public sanitization notes

Remove donor-specific product UX and persistent platform semantics. Keep only the bounded graph contract.

## Example

See `examples/minimal_graph.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 graph cluster

## Future evolution

- ready frontier views
- blocker aging notes
- bounded graph validation helpers
