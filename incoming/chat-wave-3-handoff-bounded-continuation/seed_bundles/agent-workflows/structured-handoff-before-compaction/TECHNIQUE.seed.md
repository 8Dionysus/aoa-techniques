---
id: AOA-T-XXXX
name: structured-handoff-before-compaction
domain: agent-workflows
status: draft-seed
origin: chat-wave-3-handoff-bounded-continuation
note: seed bundle staged for operator-guided chat wave 3 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - handoff-bounded-continuation
summary: Produce a structured handoff artifact before compaction or rollover so context transfer stays explicit and reviewable.
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
# structured-handoff-before-compaction

## Intent

Create one explicit handoff or checkpoint artifact before compaction or session rollover so the next operator can continue from a reviewable transfer object instead of implicit memory.

## When to use

- context compaction or rollover is likely
- unfinished work must survive the boundary
- the transfer object should be inspectable before continuation

## When not to use

- there is no real context-loss boundary
- the problem is transcript export rather than a handoff artifact
- the flow would become generic orchestration doctrine

## Inputs

- current work state
- open tasks or blockers
- compaction or rollover trigger

## Outputs

- structured handoff artifact
- status summary
- explicit next-step and blocker notes

## Core procedure

1. detect the compaction or rollover boundary
2. summarize what is done, blocked, and next
3. write one structured handoff artifact
4. make the artifact available before context is dropped
5. require later review of the artifact before continuation

## Contracts

- the handoff artifact exists before context loss
- the artifact names done, blocked, and next work
- continuation depends on the artifact, not hidden memory
- the technique stays smaller than generic orchestration

## Risks

### Failure modes

- the artifact is written too late to survive compaction
- the handoff object omits a blocker or false completion claim

### Negative effects

- reviewers trust memory over the artifact
- the artifact drifts into full transcript export

### Misuse patterns

- treating any summary as a handoff contract
- widening the technique into a full multi-agent platform

### Detection signals

- no artifact exists at the compaction boundary
- the receiving side cannot tell what remains blocked

### Mitigations

- trigger handoff generation before compaction
- keep done, blocked, and next fields explicit
- separate the handoff artifact from transcript packaging

## Validation

- confirm the artifact is created before compaction
- confirm the artifact contains done, blocked, and next fields
- verify continuation can be explained from the artifact alone

## Adaptation notes

- artifact format
- compaction trigger
- storage location
- review step ownership

## Public sanitization notes

Remove donor-specific orchestration or agent platform semantics. Keep only the pre-compaction handoff artifact contract.

## Example

See `examples/structured_handoff.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 3 handoff cluster

## Future evolution

- handoff diff notes
- receipt links
- bounded artifact validation
