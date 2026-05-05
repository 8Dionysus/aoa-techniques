# Adverse Effects Review

## Technique
- id: AOA-T-0015
- name: contract-test-design

## Review focus
- current role: default boundary-contract evaluation discipline for consumer-visible interfaces
- current watch seam: keep the contract narrow enough that it protects the live consumer boundary without collapsing into helpers, hidden internals, or broad invariant coverage

## Failure modes
- the contract is too vague or fixture-shaped to constrain the actual consumer boundary
- validation ends up covering a summary artifact, helper wrapper, or fixture while the real consumer boundary remains untested
- downstream compatibility assumptions stay implicit until a later break forces the issue

## Negative effects
- an oversized contract can freeze useful internal evolution around details the consumer never observes
- a surrogate contract can create false confidence that the real boundary is protected because the suite still passes on the wrong surface
- review energy can shift into contract ceremony while the real boundary remains unnamed or weakly scoped

## Misuse patterns
- calling any smoke test a contract test without boundary discipline
- encoding internal implementation details into the boundary contract
- widening the contract surface simply because a tool makes it easy
- treating a helper artifact or fixture format as if it were the live boundary contract

## Detection signals
- the supposed contract mostly references helpers, summaries, or internals rather than observable inputs or outputs at the live boundary
- downstream consumers are still surprised after the contract change
- the suite stays green through refactor, but reviewers still cannot say which consumer promise it protects
- boundary drift bugs keep surfacing first in downstream or integration contexts instead of inside the contract checks

## Mitigations
- replace surrogate assertions with at least one check on the real consumer-visible boundary
- narrow the contract to what the consumer really observes
- separate internal correctness tests from boundary stability tests
- add downstream impact notes before changing the boundary

## Recommendation
- keep the canonical bundle and use this note as the watch surface for surrogate-boundary drift, over-wide contracts, and invariant creep, while keeping `AOA-T-0017` as the separate home for invariant-broadening validation
