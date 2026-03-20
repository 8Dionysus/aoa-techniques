# Adverse Effects Review

## Technique
- id: AOA-T-0014
- name: tdd-slice

## Review focus
- current role: default bounded execution discipline for one small behavior slice
- current watch seam: keep slice execution discipline distinct from consumer-visible contract design and from generic "always test first" ritual

## Failure modes
- the tests describe implementation details instead of the observable slice behavior
- the slice grows until it hides a broader boundary or architectural rewrite
- the behavior target is too vague, so the test-first flow never becomes a useful spec

## Negative effects
- ritualized TDD can slow work when the slice is already well understood and the real task is just execution
- narrow tests can create false confidence if the slice was chosen poorly
- the technique can distract from contract design if people use it for boundary definition work

## Misuse patterns
- writing tests after code and still describing the work as tests-first
- forcing the technique onto glue code or one-off scripts with no stable behavioral core
- using the slice discipline as a proxy for `AOA-T-0015 contract-test-design`

## Detection signals
- tests mention internal helper structure more than behavior
- the diff widens beyond the declared slice
- the final report cannot state both the covered behavior and what remains out of scope
- reviewers start asking contract questions that the slice technique cannot answer

## Mitigations
- narrow the slice before continuing
- rewrite tests around behavior and observable outcomes
- hand boundary questions to `AOA-T-0015` instead of stretching this technique into contract design

## Recommendation
- keep current `canonical` status and use this note as the watch surface for slice discipline drifting into generic TDD ritual or boundary-contract semantics
