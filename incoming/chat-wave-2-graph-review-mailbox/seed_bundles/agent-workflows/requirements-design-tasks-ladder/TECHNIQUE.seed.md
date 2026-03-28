---
id: AOA-T-XXXX
name: requirements-design-tasks-ladder
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
summary: Separate requirements, design, and task slices so implementation ladders stay reviewable without importing a full methodology stack.
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
# requirements-design-tasks-ladder

## Intent

Keep requirements, design, and task slices visibly distinct so work can move down the ladder without collapsing intent, solution, and execution into one blob.

## When to use

- the implementation path needs explicit requirement, design, and task layers
- the team needs a small planning ladder instead of one large methodology import
- the next execution slice depends on a visible design seam

## When not to use

- the work is one tiny change with no design question
- the goal is to import a full methodology or template ecosystem
- the ladder would become ceremony with no real boundary

## Inputs

- bounded requirement statement
- design response to that requirement
- task slices derived from the design

## Outputs

- visible requirement layer
- visible design layer
- bounded task layer for implementation

## Core procedure

1. state the requirement in plain language
2. write the smallest design response that explains the approach
3. split work into bounded task slices
4. keep transitions between layers visible
5. avoid letting one layer silently replace another

## Contracts

- requirements, design, and tasks stay distinct
- each layer is allowed to constrain the next layer
- the ladder stays smaller than a full planning doctrine
- tasks are derived from design rather than invented in isolation

## Risks

### Failure modes

- design stays too vague to generate bounded tasks
- tasks are written before the requirement or design is clear

### Negative effects

- the ladder becomes paperwork theater
- methodology language overwhelms the reusable core

### Misuse patterns

- importing a whole template system into the technique
- treating task lists as a substitute for design

### Detection signals

- task items have no visible design source
- design language starts carrying unrelated project process rules

### Mitigations

- keep each layer short and bounded
- require an explicit transition between layers
- stop if the ladder cannot stay smaller than the methodology

## Validation

- confirm tasks can be traced back to a design choice
- confirm design responds to a visible requirement
- verify the seed stays smaller than a full planning framework

## Adaptation notes

- document format
- layer naming
- task slice granularity
- approval seams

## Public sanitization notes

Remove donor-specific framework naming and template ecosystems. Keep only the bounded three-layer ladder contract.

## Example

See `examples/ladder_slice.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 planning ladder cluster

## Future evolution

- layer transition checklists
- bounded review gates
- cross-link helpers
