# Canonical Readiness

## Technique
- id: AOA-T-0017
- name: property-invariants

## Verdict
- defer for now

## Evidence summary
- origin evidence: `atm10-agent` already shows repeated need for invariant-oriented checks where broader behavioral coverage mattered more than a few fixed examples
- second context: the public adaptation note keeps the technique distinct inside `aoa-techniques` as an invariant-first validation pattern rather than generic "stronger tests" language
- semantic reinforcement: `docs/SKILL_SUPPORT_SEMANTIC_REVIEW.md` keeps `AOA-T-0015` versus `AOA-T-0017` readable as contract-surface validation versus invariant-oriented coverage broadening, while also naming that seam as the main watch point
- support surfaces: the bundle already has a checklist plus two public-safe examples that keep the center of gravity on invariant strength, bounded input assumptions, and honest reporting

## Default-use rationale
- this is the right bounded choice when the main validation problem is broader coverage around one known domain truth that should hold across many cases
- it remains narrower than adjacent techniques: `AOA-T-0015` is still the clearer default when a consumer-visible boundary must be defined explicitly, and `AOA-T-0007` still governs staged promotion of an already-observed signal rather than invariant design

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the published bundle keeps the reusable invariant-first pattern and does not depend on ATM10-specific data shapes, tool choices, or hidden operational context
- public reuse check: the current examples, checklist, and adaptation notes remain understandable without origin-project access and stay bounded to technique-level meaning

## Remaining gaps
- the main remaining gap is stronger live reuse evidence that the technique becomes the natural default across more than one bounded validation domain without drifting back toward generic contract-testing language

## Recommendation
- keep `AOA-T-0017` as `promoted` in this wave; the technique is strong and distinct, but one more reinforcement step around live default-use evidence would make a later `promoted -> canonical` decision easier and cleaner
