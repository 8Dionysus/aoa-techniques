---
id: AOA-T-0055
name: requirements-design-tasks-ladder
domain: agent-workflows
kind: workflow
status: promoted
origin:
  project: gotalab/cc-sdd
  path: README.md + .kiro/specs/photo-albums-en/requirements.md + .kiro/specs/photo-albums-en/design.md + .kiro/specs/photo-albums-en/tasks.md
  note: Adapted from the open-source cc-sdd project, which keeps requirements, design, and tasks as explicit successive spec artifacts before implementation.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - planning
  - requirements
  - design
  - tasks
summary: Separate requirements, design, and task slices so implementation planning stays reviewable without importing a full spec-driven methodology stack.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
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

# requirements-design-tasks-ladder

## Intent

Keep requirements, design, and tasks as visibly separate planning layers so work can move from problem statement to solution shape to execution slices without collapsing all three into one planning blob.

## When to use

- a feature or change needs more than a one-line plan
- the next execution slice depends on a visible design seam
- tasks should be traceable back to stated requirements and design choices
- the workflow needs a small pre-execution ladder without importing a full methodology stack

## When not to use

- the work is one tiny change with no real design question
- the main need is a full methodology, template suite, or governance process
- the workflow needs intent normalization, dry-run, or contract artifacts before any action
- the ladder would become ceremony with no real boundary between layers

## Inputs

- one bounded requirement statement
- one design response to that requirement
- one bounded task set derived from the design
- optional review or approval seams that do not replace the ladder itself

## Outputs

- one visible requirement layer
- one visible design layer
- one bounded task layer for later implementation
- clearer traceability from execution slices back to the reasoning that produced them

## Core procedure

1. State the requirement in plain, bounded language before discussing implementation.
2. Write the smallest design response that explains how the requirement will be met.
3. Derive bounded tasks from that design instead of inventing tasks in isolation.
4. Keep transitions between requirement, design, and tasks explicit and reviewable.
5. Let each layer constrain the next one without silently replacing it.
6. Keep tasks small enough that later execution can happen slice by slice.
7. Stop widening the bundle when templates, approvals, research lanes, or methodology branding become the real center of gravity.

## Contracts

- requirements, design, and tasks remain distinct layers
- design responds to a visible requirement instead of standing alone
- tasks are derived from visible design choices rather than invented in isolation
- each layer may constrain the next layer, but should not silently replace it
- the ladder stays smaller than a full methodology, template ecosystem, or governance process
- implementation, validation, and runtime coordination remain outside this bounded planning contract

Relationship to adjacent techniques: unlike [AOA-T-0001](../plan-diff-apply-verify-report/TECHNIQUE.md), this technique stops before apply, verify, and report. Unlike [AOA-T-0004](../intent-plan-dry-run-contract-chain/TECHNIQUE.md), it does not normalize intent into dry-run and contract artifacts. Unlike [AOA-T-0049](../dependency-aware-task-graph/TECHNIQUE.md), it does not coordinate task dependencies through a graph; it only keeps the requirement-to-design-to-task ladder explicit before execution begins.

## Risks

### Failure modes

- design stays too vague to produce bounded tasks
- tasks are written before requirement or design is clear
- one layer quietly absorbs another and the ladder becomes decorative rather than operative
- methodology language overwhelms the reusable core

### Negative effects

- the ladder can become paperwork theater when the change is too small
- over-detailed design can delay execution unnecessarily
- teams may mistake the existence of documents for real planning clarity

### Misuse patterns

- importing a whole template system into the technique
- treating task lists as a substitute for design
- using requirements language as a disguise for process mandates unrelated to the change

### Detection signals

- task items have no visible design source
- design sections do not clearly answer any requirement
- contributors discuss template compliance more than the layer transitions themselves
- the planning surface grows faster than the bounded work it is supposed to enable

### Mitigations

- keep each layer short and bounded
- require an explicit transition from requirement to design to tasks
- trim methodology or template language that does not support the core ladder
- stop and split the work when the ladder cannot stay smaller than the wider planning framework

## Validation

Verify the technique by confirming that:
- tasks can be traced back to a visible design choice
- design responds to a visible requirement
- the three layers remain distinct in wording and purpose
- the ladder stays smaller than a full methodology import
- later execution still needs its own separate workflow surface

See `checks/requirements-design-tasks-ladder-checklist.md`.

## Adaptation notes

What can vary across projects:
- the document format used for each layer
- layer naming conventions
- how much detail lives in the design layer
- task slice granularity
- whether approvals happen between layers

What should stay invariant:
- requirements stay distinct from design
- design stays distinct from tasks
- tasks are derived from visible design
- the ladder remains a bounded pre-execution planning surface

Project-shaped details that should not be treated as invariant:
- one command suite or slash-command taxonomy
- one template pack or rules directory
- one agent roster or parallel-execution system
- donor-specific research, steering, or project-memory surfaces
- methodology branding such as SDD or AI-DLC

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: explicit requirements, design, and task layers that remain distinct before implementation. Command suites, template ecosystems, steering docs, project memory, validation commands, and wider methodology doctrine were intentionally left out of the public contract.

## Example

See `examples/minimal-requirements-design-tasks-ladder.md`.

## Checks

See `checks/requirements-design-tasks-ladder-checklist.md`.

## Promotion history

- adapted from open-source `gotalab/cc-sdd`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for explicit requirement-to-design-to-task planning ladders

## Future evolution

- keep dependency coordination separate instead of widening this bundle into task-graph management
- keep dry-run, contract, or approval machinery separate instead of folding it into the ladder
- add a stronger second live context if another public repository uses the same bounded planning ladder outside the donor methodology family
