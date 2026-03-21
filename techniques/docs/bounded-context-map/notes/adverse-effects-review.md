# Adverse Effects Review

## Technique
- id: AOA-T-0016
- name: bounded-context-map

## Review focus
- current role: default docs and scoping pattern for naming neighboring responsibilities and visible handoff surfaces
- current watch seam: keep the technique tied to real semantic ambiguity instead of letting it drift into generic architecture formalism or ceremony

## Failure modes
- too many contexts are invented for a small problem
- the map renames concepts without reducing ambiguity
- interfaces remain muddy even after the map is drawn

## Negative effects
- over-structuring can slow small projects if no real confusion exists
- premature context formalization can freeze evolving vocabulary too early
- the map can become generic architecture formalism if it stops being tied to one concrete scoping problem

## Misuse patterns
- using context mapping as a substitute for real interface cleanup
- declaring a DDD-style map without changing how reviews or changes are scoped
- treating every folder boundary as a bounded context automatically
- using the technique to justify architecture theater instead of one bounded ambiguity reduction pass

## Detection signals
- contributors still confuse neighboring areas after the map is written
- the context names overlap or feel interchangeable
- handoff points are still implicit or undocumented
- reviewers start discussing taxonomy or diagram shape more than the actual scope boundary being protected

## Mitigations
- collapse weak or ceremonial contexts
- tighten the vocabulary around observable responsibilities
- add or clarify the interface notes between contexts
- re-anchor the map in one concrete scoping decision instead of a broader architecture program

## Recommendation
- keep current `canonical` status and use this note as the watch surface for over-structuring, vocabulary freeze, and architecture-formalism drift
