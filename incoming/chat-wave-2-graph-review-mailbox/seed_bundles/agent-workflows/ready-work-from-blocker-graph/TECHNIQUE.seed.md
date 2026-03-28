---
id: AOA-T-XXXX
name: ready-work-from-blocker-graph
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
summary: Derive the next bounded work queue from blocker-free graph state instead of hand-waving what is ready.
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
# ready-work-from-blocker-graph

## Intent

Turn an explicit blocker graph into a bounded next-work queue so operators can choose from work that is actually unblocked.

## When to use

- you already have dependency state
- multiple possible next tasks compete for attention
- you want ready work to be derived, not narrated

## When not to use

- the graph itself is missing or untrusted
- the problem is full project prioritization rather than ready-state derivation
- the work has no meaningful blocker structure

## Inputs

- dependency graph with task state
- blocker relationships
- optional priority hints

## Outputs

- ready task queue
- explicit reasons why other tasks are not ready
- stable frontier for the next bounded step

## Core procedure

1. inspect the current blocker graph
2. select tasks whose prerequisites are satisfied
3. keep blocked tasks out of the queue
4. surface why each blocked task is still waiting
5. refresh the queue after each real graph change

## Contracts

- ready work depends on blocker-free state
- blocked tasks are not silently promoted
- queue derivation stays smaller than full prioritization policy
- the queue remains explainable from graph state

## Risks

### Failure modes

- stale blocker state yields a wrong ready queue
- hidden manual overrides bypass the graph

### Negative effects

- operators trust an outdated queue
- priority language starts replacing dependency truth

### Misuse patterns

- mixing blocker-free derivation with broad PM ranking
- letting every queue tweak become manual policy

### Detection signals

- blocked tasks appear in the ready queue without explanation
- queue order cannot be explained from visible inputs

### Mitigations

- recompute the frontier after each state change
- keep blockers and overrides explicit
- separate dependency truth from later prioritization

## Validation

- verify only blocker-free nodes appear in the queue
- verify blocked reasons remain visible for excluded tasks
- confirm queue updates track graph changes

## Adaptation notes

- frontier ordering rules
- queue display format
- task state vocabulary
- local storage shape

## Public sanitization notes

Remove donor-specific workflow UI and task-management rhetoric. Keep only the blocker-derived ready queue contract.

## Example

See `examples/ready_frontier.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 graph cluster

## Future evolution

- queue aging notes
- explicit override logging
- frontier diff snapshots
