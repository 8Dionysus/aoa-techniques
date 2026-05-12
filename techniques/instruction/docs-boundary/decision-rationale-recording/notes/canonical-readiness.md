# Canonical Readiness

## Technique
- id: AOA-T-0033
- name: decision-rationale-recording

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the second context adaptation kept the practice bounded and public-safe
- MADR provides exact-fit public reinforcement: its template and own decision records preserve one decision with context/problem, considered options, chosen outcome with justification, and accepted consequences
- the bundle now has a checklist, a public-safe example, origin evidence, second-context adaptation, and external decision-record reinforcement beyond the `aoa-skills` source lineage

## Default-use rationale
- this is useful when a meaningful decision needs a reviewable rationale record
- it is strongest when the missing object is the decision tradeoff itself, not a source-of-truth map or a generic changelog entry
- it is now the natural default when a project needs one bounded record that preserves context, alternatives, rationale, and consequences for later review
- ADR tooling and decision-log management remain neighboring or downstream concerns rather than the technique's core contract

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the published technique keeps only the reusable decision-recording contract and strips origin-project identifiers, local discussion detail, and private context
- public reuse check: the external reinforcement is from public MADR docs and decision records, not private internal decision logs or hidden discussion threads

## Remaining gaps
- future work can add more examples for non-architecture decisions, but no blocker remains for canonical status
- the line between one decision record, ADR tooling, decision-log governance, source-of-truth layout, and architecture taxonomy should stay guarded in future adaptations

## Recommendation
- move `AOA-T-0033` to `canonical`
- add an adverse-effects review to preserve the caution boundary after promotion
