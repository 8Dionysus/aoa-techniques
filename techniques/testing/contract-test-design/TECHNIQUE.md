---
id: AOA-T-0015
name: contract-test-design
domain: testing
status: promoted
origin:
  project: abyss-stack
  path: planning-layer
  note: Extracted from repeated need to make service and workflow boundaries explicit and reviewable for agents and humans.
owners:
  - 8Dionysus
tags:
  - testing
  - contracts
  - boundaries
  - agent-friendly
summary: Make a boundary explicit by defining expected inputs, outputs, and verification around the contract rather than around hidden internals.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: bounded_checklist
public_safety_reviewed_at: 2026-03-18
export_ready: true
relations:
  - type: complements
    target: AOA-T-0003
  - type: complements
    target: AOA-T-0001
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# contract-test-design

## Intent

Reduce breakage at boundaries by expressing the expected interface behavior explicitly and verifying it at the contract surface rather than only through internal tests.

## When to use

- service or module boundaries with downstream consumers
- smoke paths that should emit stable summaries or structured output
- interface changes where downstream drift is a risk
- refactors that keep internals moving while the boundary must remain stable

## When not to use

- purely local logic with no meaningful boundary
- situations where the real problem is that the boundary itself is still undefined
- very small changes where a boundary contract would add ceremony without value

## Inputs

- boundary under review
- expected inputs and outputs
- known downstream expectations
- current validation surface

## Outputs

- explicit contract assumptions
- contract-oriented tests or checks
- downstream impact notes
- concise validation result

## Core procedure

1. identify the boundary and its consumers
2. describe the expected inputs, outputs, and failure behavior in bounded terms
3. express the contract through tests, smoke summaries, or structured checks
4. avoid overfitting to internals that consumers never observe
5. run the contract checks and record what they do and do not prove
6. report the contract surface that is now explicit and any remaining weak edges

## Contracts

- the contract should be visible and reviewable by another human or agent
- validation should target the boundary surface, not only hidden internals
- downstream assumptions should be named when they matter
- interface changes should not be smuggled in without explicit note

## Risks

### Failure modes

- the contract is too vague to constrain behavior
- validation covers a summary artifact but not the real consumer boundary
- downstream compatibility assumptions remain implicit

### Negative effects

- an oversized contract can freeze useful internal evolution unnecessarily
- weak contract definitions can create false confidence

### Misuse patterns

- calling any smoke test a contract test without boundary discipline
- encoding internal implementation details into the boundary contract
- widening the contract surface simply because a tool makes it easy

### Detection signals

- the supposed contract mostly references internals rather than observable inputs/outputs
- downstream consumers are still surprised after the contract change
- the validation surface does not actually exercise the real boundary

### Mitigations

- narrow the contract to what the consumer really observes
- separate internal correctness tests from boundary stability tests
- add downstream impact notes before changing the boundary

## Validation

Verify the technique by confirming that:
- the boundary and consumers were named explicitly
- tests or checks target observable contract behavior
- downstream impact was considered where relevant
- the result states what the contract guarantees and what it does not

## Adaptation notes

What can vary across projects:
- the shape of the boundary (API, file contract, summary artifact, message queue, service wrapper)
- the validation mechanism (unit, smoke, structured summary, contract suite)
- how downstream consumers are documented

What should stay invariant:
- explicit contract framing
- boundary-first validation discipline
- visibility of downstream assumptions when relevant
- concise statement of what is guaranteed

## Public sanitization notes

This public version removes project-specific endpoints, service names, and operational topology while keeping the reusable boundary-design pattern.

## Example

A later revision should include one public example where an interface contract is expressed explicitly and then used to constrain a refactor.

## Checks

A minimal review pass should confirm that the boundary is real, observable, and not merely an internal surrogate.

## Promotion history

- shaped from boundary-validation needs around `abyss-stack`
- extracted into first public reusable form in `aoa-techniques` on 2026-03-18

## Future evolution

- connect more explicitly to structured smoke-summary techniques
- add a second-context example from an application-code repository
- strengthen guidance on keeping contracts narrow
