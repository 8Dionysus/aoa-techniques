# Adverse Effects Review

## Technique
- id: AOA-T-0016
- name: bounded-context-map

## Review focus
- current role: default docs and scoping pattern for naming neighboring responsibilities and visible handoff surfaces
- current watch seam: keep the technique tied to real semantic ambiguity instead of letting it drift into generic architecture formalism, ceremony, or false architectural confidence

## Failure modes
- too many contexts are invented for a small problem
- the map renames concepts without reducing ambiguity or scoping the next change more safely
- interfaces remain muddy even after the map is drawn, so the artifact looks cleaner than the work actually feels

## Negative effects
- over-structuring can slow small projects if no real confusion exists
- premature context formalization can freeze evolving vocabulary too early
- a polished map can create false architectural confidence even while handoffs, ownership, or translation points remain implicit
- the map can become generic architecture formalism if it stops being tied to one concrete scoping problem

## Misuse patterns
- using context mapping as a substitute for real interface cleanup
- declaring a DDD-style map without changing how reviews or changes are scoped
- treating every folder boundary as a bounded context automatically
- using the technique to justify architecture theater instead of one bounded ambiguity reduction pass
- using context mapping as a durable architecture program when the real need is one immediate scoping decision

## Detection signals
- contributors still confuse neighboring areas after the map is written
- the context names overlap, feel interchangeable, or only repeat folder names
- handoff points are still implicit or undocumented
- reviewers start discussing taxonomy or diagram shape more than the actual scope boundary being protected
- the first question after reading the map is still "what stays out of scope for this change?"

## Mitigations
- collapse weak or ceremonial contexts
- tighten the vocabulary around observable responsibilities
- add or clarify the interface notes between contexts
- re-anchor the map in one concrete scoping decision instead of a broader architecture program
- delete or reduce the map when one sharper scoping note would do more work than a permanent taxonomy surface

## Recommendation
- keep current `canonical` status and use this note as the watch surface for over-structuring, false architectural confidence, vocabulary freeze, and architecture-formalism drift
