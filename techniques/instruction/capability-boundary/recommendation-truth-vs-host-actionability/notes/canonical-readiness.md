# Canonical Readiness

## Technique
- id: AOA-T-0093
- name: recommendation-truth-vs-host-actionability

## Verdict
- not approved for canonical promotion yet

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the adapted bundle keeps the contract narrow around recommendation truth, host actionability, and explicit inventory precedence
- the bundle now has a checklist and a public-safe example, but live evidence is still concentrated in the current `aoa-sdk` lineage

## Default-use rationale
- this is useful when control planes recommend capabilities from a larger corpus than the current host can execute
- it is strongest when operators need honest `activate_now` semantics without losing visibility into router-only relevance
- it is not yet proven as the default law for every capability selector or router outside the present skill-runtime context

## Fresh public-safety check
- review date: 2026-04-06
- result: pass
- sanitization still holds: the published bundle keeps the bounded truth split while stripping local CLI and install-root specifics from the invariant core

## Remaining gaps
- the bundle would benefit from a second live context outside `aoa-sdk`
- router-only risk-gate handling still needs another context before a stricter canonical fail-fast posture would be justified

## Recommendation
- keep `AOA-T-0093` as `promoted`
- revisit canonical readiness only after another live capability-control-plane context proves the same recommendation-versus-executability seam
