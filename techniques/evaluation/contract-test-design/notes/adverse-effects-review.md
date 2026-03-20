# Adverse Effects Review

## Technique
- id: AOA-T-0015
- name: contract-test-design

## Review focus
- current role: default boundary-contract evaluation discipline for consumer-visible interfaces
- current watch seam: keep the contract narrow enough that it does not collapse into either hidden internals or broad invariant coverage

## Failure modes
- the contract is too vague to constrain behavior
- validation ends up covering a summary artifact while the real consumer boundary remains untested
- downstream compatibility assumptions stay implicit until a later break forces the issue

## Negative effects
- an oversized contract can freeze useful internal evolution unnecessarily
- weak contract definitions can create false confidence that the real boundary is protected

## Misuse patterns
- calling any smoke test a contract test without boundary discipline
- encoding internal implementation details into the boundary contract
- widening the contract surface simply because a tool makes it easy

## Detection signals
- the supposed contract mostly references internals rather than observable inputs or outputs
- downstream consumers are still surprised after the contract change
- the validation surface does not actually exercise the real boundary

## Mitigations
- narrow the contract to what the consumer really observes
- separate internal correctness tests from boundary stability tests
- add downstream impact notes before changing the boundary

## Recommendation
- keep the canonical bundle and use this note as the watch surface for boundary drift, while keeping `AOA-T-0017` as the separate home for invariant-broadening validation
