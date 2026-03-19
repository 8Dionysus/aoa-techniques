---
id: AOA-T-0017
name: property-invariants
domain: evaluation
status: promoted
origin:
  project: atm10-agent
  path: planning-layer
  note: Extracted from repeated need to turn system truths into invariant-oriented checks that cover more than a few fixed examples.
owners:
  - 8Dionysus
tags:
  - testing
  - properties
  - invariants
  - agent-friendly
summary: Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-18
export_ready: true
relations:
  - type: complements
    target: AOA-T-0007
  - type: complements
    target: AOA-T-0001
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
---

# property-invariants

## Intent

Reduce weak example-only validation by expressing stable system or domain truths as invariant-oriented checks that should hold across many cases.

## When to use

- rules that should hold across a wide input or state space
- situations where example-based tests feel too narrow
- systems with conservation, monotonicity, idempotency, structural, or safety invariants
- agent-assisted validation work where the invariant can act as a compact spec

## When not to use

- presentation-only behavior where concrete examples are clearer
- situations where no meaningful invariant is yet understood
- systems where the main problem is unknown requirements rather than coverage breadth

## Inputs

- target rule or system truth
- current examples or tests
- candidate input space or generators
- known edge cases

## Outputs

- explicit invariant statements
- property-oriented tests or checks
- notes on assumptions behind the generators or input space
- concise validation result

## Core procedure

1. identify what must remain true across many cases
2. separate strong invariants from weak hopes or vague expectations
3. express those invariants as property-oriented tests or repeated checks
4. keep the generator or input strategy bounded and reviewable
5. run the checks and record what properties now constrain behavior
6. report what the properties do and do not prove

## Contracts

- each property should express a meaningful invariant
- the technique should broaden coverage beyond a tiny fixed example set
- generator assumptions should remain understandable
- the resulting checks should help future regressions surface earlier

## Risks

### Failure modes

- the property is too weak to constrain real behavior
- the generator range never reaches meaningful stress points
- the checks are random-looking but semantically shallow

### Negative effects

- overly complex generator logic can hide rather than clarify the domain truth
- large noisy failing cases can make debugging slower if the invariant was poorly chosen

### Misuse patterns

- writing vague properties like “should not fail” and calling them invariants
- confusing random data generation with meaningful property testing
- using property checks where a few concrete examples would communicate better

### Detection signals

- the property could pass for many broken implementations
- no one can explain why the invariant matters to the domain
- the generated space is large but the signal gained is small

### Mitigations

- rewrite the property around a stronger domain truth
- narrow the generator to meaningful ranges first
- combine property checks with a few clear examples for readability

## Validation

Verify the technique by confirming that:
- the property expresses a meaningful invariant rather than a vague expectation
- the resulting check broadens coverage beyond a small fixed example set
- generator or input assumptions are understandable enough to review
- the final report states what the invariant actually constrains

## Adaptation notes

What can vary across projects:
- test framework and generator tooling
- the shape of the input space
- whether the invariant is implemented as a formal property test or a repeated structured check
- the strength of shrinking or failure reporting tools

What should stay invariant:
- meaningful invariant framing
- broader coverage than handpicked examples alone
- explicit generator or input assumptions
- honest statement of what the property proves

## Public sanitization notes

This public version removes project-specific data shapes and tool details while preserving the reusable invariant-oriented validation pattern.

## Example

See `examples/minimal-invariant-check.md` for a small flow where one stable rule is expressed as an invariant instead of a tiny fixed example list.

## Checks

See `checks/property-invariants-checklist.md` for a minimal review pass covering invariant strength, bounded input assumptions, and honest reporting.

## Promotion history

- shaped from invariant-driven testing needs around `atm10-agent`
- extracted into first public reusable form in `aoa-techniques` on 2026-03-18

## Future evolution

- add a second-context example from an infra or config validation setting
- strengthen guidance on choosing strong invariants
- connect more explicitly to signal-first promotion of checks
