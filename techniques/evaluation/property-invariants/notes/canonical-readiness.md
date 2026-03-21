# Canonical Readiness

## Technique
- id: AOA-T-0017
- name: property-invariants

## Verdict
- keep `promoted`; defer canonical promotion

## Evidence summary
- consumer evidence: `aoa-skills/skills/aoa-property-invariants/SKILL.md` and its committed `techniques.yaml` both wire `AOA-T-0017` into a real, evaluated consumer surface rather than a hypothetical fit
- reuse shape: the skill frames `AOA-T-0017` as a core, explicit-preferred technique for broad invariant-oriented checks, and its committed example stays centered on bounded invariant coverage instead of generic exploratory testing
- boundary separation: the consumer surface keeps `AOA-T-0017` distinct from `AOA-T-0007`, which supports the invariant-vs-signal-promotion split but does not by itself prove default-use status
- consumer-side review signal: the committed promotion review in `aoa-skills` still says `canonical` is deferred because this pass does not establish the technique as the default public reference for property-oriented testing

## Default-use rationale
- this remains the right bounded choice when the main validation problem is broader coverage around one known domain truth that should hold across many cases
- it remains narrower than adjacent techniques: `AOA-T-0015` is still the clearer default when a consumer-visible boundary must be defined explicitly, and `AOA-T-0007` still governs staged promotion of an already-observed signal rather than invariant design
- the evidence is enough to justify reuse and explicit skill wiring, but not enough to call this the default public reference across validation domains

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the published bundle keeps the reusable invariant-first pattern and does not depend on ATM10-specific data shapes, tool choices, or hidden operational context
- public reuse check: the current examples, checklist, and adaptation notes remain understandable without origin-project access and stay bounded to technique-level meaning

## Remaining gaps
- the smallest remaining gap is a second committed consumer surface that treats this technique as the natural first choice for property-oriented coverage, not just a supported dependency
- until that appears, the bundle should stay promoted rather than claim canonical default-use approval

## Recommendation
- keep `AOA-T-0017` as `promoted` in this wave; the technique is strong, distinct, and reusable, but the committed consumer evidence still falls short of canonical default-use approval
