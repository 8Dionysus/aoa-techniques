---
id: AOA-T-0017
name: property-invariants
domain: evaluation
status: canonical
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
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-20
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
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
---

# property-invariants

## Intent

Reduce weak example-only validation by expressing stable system or domain truths as invariant-oriented checks that should hold across many cases.

## When to use

- rules that should hold across a wide input or state space
- situations where example-based tests feel too narrow
- systems with conservation, monotonicity, idempotency, structural, or safety invariants
- agent-assisted validation work where the invariant can act as a compact spec
- cases where the main problem is broader coverage around one known domain truth rather than making a consumer-visible boundary explicit

## When not to use

- presentation-only behavior where concrete examples are clearer
- situations where no meaningful invariant is yet understood
- systems where the main problem is unknown requirements rather than coverage breadth
- named API, file, or summary boundaries where `AOA-T-0015 contract-test-design` is the clearer fit

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

- the chosen invariant is too weak or too generic to constrain real behavior
- the generator range never reaches meaningful stress points or becomes too broad to review honestly
- the checks look sophisticated and wide, but the protected domain truth is still underspecified

### Negative effects

- overly complex generator logic can hide the domain truth behind tooling complexity
- large noisy failing cases can make debugging slower if the invariant was poorly chosen
- a polished property suite can create false confidence while teams still cannot explain what stable truth is being protected

### Misuse patterns

- writing vague properties like “should not fail” and calling them invariants
- confusing random data generation with meaningful property testing
- using property checks where a few concrete examples would communicate better
- using invariant language to avoid defining the actual boundary or rule that matters

### Detection signals

- the property could pass for many broken implementations
- reviewers can explain the generator or harness more easily than why the invariant matters to the domain
- the generated space grows, but the signal gained is small or obvious boundary regressions still surface elsewhere first
- failing cases are noisy, but the report cannot say which stable truth was violated

### Mitigations

- rewrite the property around a stronger domain truth
- narrow the generator to meaningful ranges first
- combine property checks with a few clear examples for readability
- route consumer-boundary questions back to `AOA-T-0015` instead of stretching this technique

## Validation

Verify the technique by confirming that:
- the property expresses a meaningful invariant rather than a vague expectation
- the resulting check broadens coverage beyond a small fixed example set
- generator or input assumptions are understandable enough to review
- the final report states what the invariant actually constrains
- the final report can name which stable truth was violated or protected, not only that generated inputs produced a failure

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

Relationship to adjacent techniques:
- unlike `AOA-T-0015 contract-test-design`, this technique is about constraining one meaningful invariant across many cases after the boundary is already understood, not about defining a consumer-visible contract
- unlike `AOA-T-0007 signal-first-gate-promotion`, this technique strengthens the check surface itself rather than governing how an observed signal becomes strict

## Public sanitization notes

This public version removes project-specific data shapes and tool details while preserving the reusable invariant-oriented validation pattern.

## Example

See `examples/minimal-invariant-check.md` for a small flow where one stable rule is expressed as an invariant instead of a tiny fixed example list.
See `examples/concrete-config-invariant-check.md` for a more concrete public-safe config-validation example where one meaningful invariant is checked across bounded configuration cases.

## Checks

See `checks/property-invariants-checklist.md` for a minimal review pass covering invariant strength, bounded input assumptions, and honest reporting.

## Promotion history

- shaped from invariant-driven testing needs around `atm10-agent`
- extracted into first public reusable form in `aoa-techniques` on 2026-03-18

## Future evolution

- strengthen guidance on choosing strong invariants
- connect more explicitly to signal-first promotion of checks
