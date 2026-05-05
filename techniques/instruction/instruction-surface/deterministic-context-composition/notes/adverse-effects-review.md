# Adverse Effects Review

## Technique
- id: AOA-T-0012
- name: deterministic-context-composition

## Review focus
- current role: default many-fragment composition pattern for one deterministic generated context artifact
- current watch seam: keep source cardinality and one-output composition explicit so the pattern does not blur into generic multi-target instruction management

## Failure modes
- ordering and precedence rules become implicit and stop being explainable from the fragment set
- contributors edit the generated artifact directly and break the fragment-first source-of-truth contract
- the output stays stable enough to look authoritative even after precedence becomes too opaque for normal contributors to reason about

## Negative effects
- deterministic composition can add hidden review overhead when maintainers must reconstruct precedence from tribal knowledge
- a stable generated artifact can create false confidence even while fragment authority and ownership become harder to explain
- once the output looks settled, teams can delay simplifying the precedence model because determinism starts to masquerade as clarity

## Misuse patterns
- widening the technique into a general documentation build system instead of one bounded generated-context pattern
- adding more precedence or routing layers instead of simplifying fragment authority
- letting a one-output composition technique drift toward multi-target management because the generated artifact already looks like a control surface

## Detection signals
- reviewers cannot explain output ordering or ownership without consulting implementation detail outside the fragments
- direct generated-artifact edits start showing up in normal maintenance diffs
- the output looks stable, but contributors still cannot say why this precedence model should remain the current default

## Mitigations
- simplify precedence until ordering is explainable from fragments plus one small deterministic rule set
- reassert fragment-first authority by routing fixes back through source fragments and regeneration
- stop the current pattern at one generated output and route multi-target propagation needs to a narrower sibling technique instead of widening this one

## Recommendation
- keep current `canonical` status and use this note as the watch surface for false determinism, opaque precedence, and drift from one-output composition into multi-target management
