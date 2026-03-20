---
id: AOA-T-0014
name: tdd-slice
domain: agent-workflows
status: canonical
origin:
  project: atm10-agent
  path: planning-layer
  note: Extracted from bounded feature-slice needs around agent-friendly testing discipline and prepared for first public reusable form.
owners:
  - 8Dionysus
tags:
  - testing
  - tdd
  - bounded-change
  - agent-friendly
summary: Implement a bounded behavior slice through test-first discipline, minimal implementation, and explicit refactor limits.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-20
export_ready: true
relations:
  - type: complements
    target: AOA-T-0001
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
---

# tdd-slice

## Intent

Reduce ambiguity and regression risk by expressing one bounded behavior slice as tests before implementation, then keeping the implementation and any refactor inside that slice.

## When to use

- small or medium feature slices with clearly describable behavior
- logic changes that benefit from explicit behavioral framing
- refactors where a bounded test surface should constrain change
- agent-assisted implementation where the main risk is scope drift inside one already understood behavior slice
- work that needs a compact executable specification for the slice itself, not a wider boundary or contract redesign

## When not to use

- exploratory work where the behavior is still too vague to test meaningfully
- large structural rewrites where test-first on one slice would hide the real scope
- boundary-definition work where the primary question is contract shape rather than slice execution
- purely mechanical or wording-only changes with no meaningful behavior surface

## Inputs

- desired behavior or rule change
- bounded module or slice under change
- constraints and non-goals
- available test surface

## Outputs

- new or updated tests
- minimal implementation satisfying the tests
- bounded refactor if needed
- concise validation result

## Core procedure

1. state the behavior in bounded, reviewable language
2. write or update tests before implementation where the task shape allows it
3. make the smallest implementation change that satisfies the tests
4. refactor only inside the declared slice
5. run the relevant tests and record the result
6. report what behavior is now specified and what remains out of scope

## Contracts

- tests should express behavior rather than incidental implementation detail
- the implementation should stay bounded to the declared slice
- unrelated cleanup should not be smuggled into the change
- boundary or contract questions should stay out of the slice unless the slice itself is the contract surface
- the final result should make future regressions easier to detect

## Risks

### Failure modes

- tests mirror the implementation instead of constraining it
- the slice is too broad and hides an architectural rewrite
- the chosen test surface is too weak to catch real regressions

### Negative effects

- ritualized TDD can slow work when the problem is still undefined
- narrow tests can create false confidence if the slice was chosen poorly

### Misuse patterns

- writing tests after the code and labeling it test-first
- forcing TDD on glue code or one-off scripts with no stable behavioral core
- using the test suite as permission to widen scope without naming it

### Detection signals

- tests mention internal implementation details more than behavior
- the diff grows far beyond the declared slice
- the post-change explanation cannot clearly state what behavior is now specified

### Mitigations

- narrow the slice before continuing
- rewrite tests around behavior and observable outcomes
- split architectural cleanup into a separate change

## Validation

Verify the technique by confirming that:
- tests were added or updated before implementation when the task was suitable for TDD
- the implementation stayed inside the declared slice
- the relevant test surface passed after the change
- the final report names both the covered behavior and the remaining out-of-scope behavior

## Adaptation notes

What can vary across projects:
- testing framework and command surface
- module boundaries
- naming for behavior slices versus acceptance slices
- whether the tests are unit, contract, or smoke tests

What should stay invariant:
- explicit behavior framing before implementation
- bounded slice discipline
- minimal implementation before refactor expansion
- visible verification at the end
- clear separation from `AOA-T-0015 contract-test-design`, which starts from a consumer-visible boundary contract rather than from one bounded implementation slice
- tests used as execution discipline for the slice, not as a substitute for defining the contract surface itself

## Public sanitization notes

This first public version generalizes the technique into a repository-agnostic bounded TDD workflow and strips project-specific tool commands and local paths.

## Example

See `examples/minimal-tdd-slice.md` for a small bounded flow where one behavior rule is expressed first in tests and then implemented with a minimal diff.
See `examples/concrete-application-handler-slice.md` for a more concrete public-safe application-handler change where one observable behavior slice is fixed tests-first without widening into boundary redesign.

## Checks

See `checks/tdd-slice-checklist.md` for a minimal review pass covering bounded scope, behavior-shaped tests, and explicit final verification.

## Promotion history

- shaped from recurring bounded-testing needs observed around `atm10-agent`
- extracted into first public reusable form in `aoa-techniques` on 2026-03-18
- promoted to canonical after second-context validation, semantic separation from contract-design techniques, and a fresh public-safety recheck on 2026-03-20

## Future evolution

- add a stronger note on when not to use TDD ritualistically
- connect to skill-level guidance in `aoa-skills`
