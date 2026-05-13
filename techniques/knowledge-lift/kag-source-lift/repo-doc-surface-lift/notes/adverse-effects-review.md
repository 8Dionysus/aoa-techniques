# Adverse Effects Review

## Technique
- id: AOA-T-0046
- name: repo-doc-surface-lift
- current role: canonical default for lifting one bounded public repo-doc or status set into a subordinate route reader or manifest

## Review focus
- current watch seam: keep the generated route surface derived, bounded, and source-pointing without letting it become docs taxonomy, policy authority, or sibling-owner truth

## Failure modes
- the generated route map or reader starts replacing the authored docs it points to
- maintainers widen the source set until planning docs, deeper guides, review docs, or local status notes become part of the same route class
- route-map consumers treat linked owner repos, release semantics, or public support posture as if the generated reader owns them
- generated outputs are edited by hand instead of being rebuilt from the bounded source docs

## Negative effects
- a clean route surface can make sparse or stale docs look more complete than they are
- external users may overread an orientation manifest as a policy engine or support promise
- sibling repositories can lose owner clarity if route refs are treated as authority transfer instead of navigation

## Misuse patterns
- adding every useful markdown file to the repo-doc route surface because it is discoverable
- using the reader to answer "what is the policy?" instead of "which authored doc should I open?"
- promoting framework-specific docs conversion, LLM-ready exports, or full docs search as if they were the same bounded repo-doc lift
- importing owner-route doctrine, release validation, or semantic-review findings into the technique body

## Detection signals
- the source set includes `TODO.md`, `PLANS.md`, broad roadmap debt, implementation paths, or review surfaces
- a reviewer fixes meaning by changing generated JSON or text instead of editing source markdown and rebuilding
- route entries point at low-context implementation files when public docs/status refs would answer the route question
- readers stop opening the authored docs even when the question needs meaning, policy, or current owner truth

## Mitigations
- keep the source set explicit and small, tied to a concrete public docs/status routing need
- regenerate and validate the route surface from authored markdown rather than hand-editing outputs
- route authority questions back to the owning docs and repositories immediately
- split a new bounded source class when deeper guides, review surfaces, release policy, or docs taxonomy becomes the real object

## Recommendation
- keep current `canonical` status and use this note as the watch surface for route-reader overreach, generated-output authority drift, source-set widening, and sibling-owner authority import
