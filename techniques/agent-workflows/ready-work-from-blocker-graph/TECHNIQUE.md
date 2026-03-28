---
id: AOA-T-0050
name: ready-work-from-blocker-graph
domain: agent-workflows
status: promoted
origin:
  project: steveyegge/beads
  path: cmd/bd/ready.go
  note: Adapted from the open-source Beads project, which derives ready work from blocker-aware graph state instead of treating open work as automatically claimable.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - ready-work
  - blockers
  - queue
  - frontier
summary: Derive the next bounded work queue from blocker-free graph state so operators choose from what is truly ready instead of narrating readiness from memory.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-27
export_ready: true
relations:
  - type: complements
    target: AOA-T-0049
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

# ready-work-from-blocker-graph

## Intent

Turn an existing blocker graph into a bounded next-work queue so the next step comes from visible dependency truth rather than from memory, narrative, or broad prioritization debate.

## When to use

- you already have explicit dependency or blocker state
- multiple possible next tasks compete for attention
- you want ready work to be derived rather than narrated
- the workflow needs a stable frontier for the next bounded step without bringing in a full tracker policy stack

## When not to use

- the graph itself is missing, stale, or untrusted
- the real need is broad prioritization, scheduling, staffing, or backlog policy
- the work has no meaningful blocker structure
- the main gap is graph authoring rather than ready-frontier derivation

## Inputs

- an explicit dependency or blocker graph
- current task state
- blocker relationships
- optional bounded ordering hints that remain subordinate to blocker truth

## Outputs

- a ready work queue or frontier
- explicit reasons why excluded tasks are still blocked
- a stable next-step surface derived from visible graph state
- a narrower decision seam between dependency truth and later prioritization choices

## Core procedure

1. Inspect the current blocker graph and the current task state.
2. Select only the nodes whose prerequisites are satisfied and whose state still makes them eligible.
3. Keep blocked tasks out of the ready queue instead of treating all open tasks as equally claimable.
4. Surface why each excluded task is still waiting.
5. Apply any secondary ordering hints only after blocker-free eligibility is established.
6. Refresh the ready queue after each real graph or state change.
7. Hand off to a broader execution workflow once the next bounded task has been chosen.

## Contracts

- ready work depends on blocker-free state
- blocked tasks are not silently promoted into the queue
- the queue remains explainable from visible graph inputs
- any secondary ordering hints come after dependency truth and do not replace it
- the technique stays smaller than full prioritization policy or project-management doctrine
- the technique assumes a graph exists, but it does not own graph authoring itself

Relationship to adjacent techniques: unlike `AOA-T-0049`, this technique does not own the explicit graph as the working surface; it owns the derived ready queue that sits on top of an existing blocker graph. Unlike `AOA-T-0001`, it does not own planning, diff review, verification, or reporting after a task has been selected.

## Risks

### Failure modes

- stale blocker state yields a wrong ready queue
- hidden manual overrides bypass the graph without being visible
- secondary sort rules quietly replace dependency truth

### Negative effects

- operators may trust an outdated queue too much
- narrow queue derivation can look like full prioritization even when it is not
- teams may debate ordering policy inside a surface that should stay blocker-first

### Misuse patterns

- mixing blocker-free derivation with broad PM ranking doctrine
- letting every queue tweak become implicit manual policy
- using this queue as if it were the graph-authoring technique itself

### Detection signals

- blocked tasks appear in the ready queue without explanation
- queue order cannot be explained from visible inputs
- open tasks are treated as ready even when blockers still exist
- teams argue about ranking policy more than blocker truth

### Mitigations

- recompute the frontier after each state change
- keep blockers and overrides explicit
- separate dependency truth from later prioritization or staffing policy
- route graph authoring concerns back to `AOA-T-0049` instead of widening this queue contract

## Validation

Verify the technique by confirming that:
- only blocker-free eligible nodes appear in the queue
- blocked reasons remain visible for excluded tasks
- queue updates track graph changes
- open-but-blocked work does not leak into the frontier
- any secondary ordering remains explainable after blocker-free eligibility is established

See `checks/ready-work-from-blocker-graph-checklist.md`.

## Adaptation notes

What can vary across projects:
- frontier ordering rules
- queue display format
- task state vocabulary
- storage shape or query surface
- optional priority hints once readiness is already established

What should stay invariant:
- ready work is derived from blocker-free state
- blocked tasks stay out of the queue until their prerequisites are satisfied
- excluded tasks keep visible blocked reasons
- dependency truth remains separate from later prioritization policy

Project-shaped details that should not be treated as invariant:
- one CLI or dashboard view
- donor-specific molecule or claim semantics
- one database or query engine
- broad ranking, triage, or staffing behavior

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: derive a ready work queue from blocker-aware graph state. Tracker product semantics, broad sort policy, gate-resume dispatch, hierarchy-heavy planning, claim workflow behavior, and donor runtime/storage specifics were intentionally left out of the public contract.

## Example

See `examples/minimal-ready-work-from-blocker-graph.md`.

## Checks

See `checks/ready-work-from-blocker-graph-checklist.md`.

## Promotion history

- adapted from open-source `steveyegge/beads`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-27 as a bounded external-import technique for blocker-aware next-work derivation

## Future evolution

- keep graph-authoring and ready-frontier derivation as separate siblings instead of collapsing them into one broad graph doctrine
- keep queue aging, ranking, and override governance separate unless a much narrower reusable contract appears
- add a stronger second live context if another public repository uses blocker-aware ready-work derivation in practice
