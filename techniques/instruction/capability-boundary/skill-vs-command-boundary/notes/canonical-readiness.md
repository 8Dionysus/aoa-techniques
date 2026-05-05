# Canonical Readiness

## Technique
- id: AOA-T-0040
- name: skill-vs-command-boundary

## Verdict
- not approved for canonical promotion yet

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the second context adaptation keeps the contract bounded with live support from `aoa-skills` and `aoa-routing`
- the bundle now has a checklist and a public-safe example, but the pattern is still proven mainly through one donor lineage

## Default-use rationale
- this is useful when a repository has both reusable skills and explicit command entrypoints and needs a stable ownership split between them
- it is strongest when command syntax, arguments, and structured workflow should stay separate from reusable capability meaning
- it is not yet proven as the default docs technique for every capability-layer boundary problem
- the current evidence supports promotion, but not canonical status

## Fresh public-safety check
- review date: 2026-03-23
- result: pass
- sanitization still holds: the published bundle keeps only the reusable ownership split while stripping donor-specific plugin mechanics, model routing, and command catalogs

## Remaining gaps
- the bundle would benefit from a second independent donor that keeps the same skill-command split outside the current plugin-oriented lineage
- the line between reusable skill meaning and user-facing command invocation should stay tested against future Wave B siblings so it does not drift into marketplace, routing, or shell-command doctrine

## Recommendation
- keep `AOA-T-0040` as `promoted`
- revisit canonical readiness only after at least one more live context proves the same skill-command split beyond the current donor lineage
