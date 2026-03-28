---
id: AOA-T-XXXX
name: session-opening-ritual-before-work
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
summary: Start a new session by reading current state and verifying the baseline before changing code.
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
# session-opening-ritual-before-work

## Intent

Require a bounded read-and-verify ritual at session start so new work begins from visible state instead of stale assumptions.

## When to use

- work crosses session boundaries
- the current repo state may have changed since the last handoff
- a new operator needs a quick baseline check before editing

## When not to use

- the work is a continuous uninterrupted session
- there is no meaningful state to verify
- the ritual would become broad workflow religion

## Inputs

- current repo state
- handoff note or recent work summary
- baseline files or status signals

## Outputs

- explicit baseline understanding
- verified current starting point
- decision to proceed or pause

## Core procedure

1. read the current handoff or recent summary
2. inspect the visible repo state
3. confirm the baseline still matches reality
4. note any mismatch before editing
5. start work only after the baseline is trusted

## Contracts

- the session starts with a visible read step
- baseline verification happens before mutation
- mismatch detection is explicit
- the technique stays smaller than a full workflow doctrine

## Risks

### Failure modes

- the ritual becomes a box-check with no real verification
- stale assumptions survive because the baseline is too vague

### Negative effects

- operators skip the read step under time pressure
- the ritual expands into general methodology language

### Misuse patterns

- treating any opening checklist as the same technique
- folding design or planning doctrine into the session start ritual

### Detection signals

- edits begin before any baseline check
- no mismatch can be named when reality changed

### Mitigations

- keep the read step short and concrete
- require one visible baseline check
- separate the ritual from broader workflow policy

## Validation

- confirm the opening ritual names a baseline before edits
- confirm mismatches can stop or redirect work
- verify the seed stays smaller than a full workflow framework

## Adaptation notes

- baseline signals
- repo state commands
- mismatch handling
- session handoff sources

## Public sanitization notes

Remove donor-specific workflow branding. Keep only the bounded read-and-verify start ritual.

## Example

See `examples/opening_ritual.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 3 opening ritual cluster

## Future evolution

- bounded mismatch templates
- startup checklists
- receipt links to the opening read
