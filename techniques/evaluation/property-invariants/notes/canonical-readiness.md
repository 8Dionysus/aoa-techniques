# Canonical Readiness

## Technique
- id: AOA-T-0017
- name: property-invariants

## Verdict
- approved for canonical promotion

## Evidence summary
- consumer evidence: `aoa-skills/skills/aoa-property-invariants/SKILL.md` remains a real, evaluated invariant-first consumer, and committed `aoa-skills@ad60e3c` now carries `skills/aoa-invariant-coverage-audit/SKILL.md` as a second focused consumer whose singular pinned dependency is `AOA-T-0017`
- reuse shape: the first skill executes invariant-oriented checks directly, while the new audit skill reviews whether an existing validation surface really constrains the stable invariant instead of only repeating examples
- validation strength: the second consumer is supported by a committed review record at `aoa-skills/docs/reviews/status-promotions/aoa-invariant-coverage-audit.md`, an example, and evaluation fixtures, so the technique now has two bounded downstream consumers rather than one
- boundary separation: the two consumers still keep `AOA-T-0017` distinct from `AOA-T-0015` boundary-contract design and from `AOA-T-0007` signal-promotion discipline

## Default-use rationale
- this is now the default bounded choice when the main validation problem is broader coverage around one stable domain truth that should hold across many cases
- it remains narrower than adjacent techniques: `AOA-T-0015` is still the clearer default when a consumer-visible boundary must be defined explicitly, and `AOA-T-0007` still governs staged promotion of an already-observed signal rather than invariant design
- the two committed downstream consumers now show that invariant-oriented coverage is not just publishable, but selected as a natural first-class move in more than one bounded validation workflow

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the published bundle keeps the reusable invariant-first pattern and does not depend on ATM10-specific data shapes, tool choices, or hidden operational context
- public reuse check: the current examples, checklist, adaptation notes, and committed skill consumers remain understandable without origin-project access and stay bounded to technique-level meaning

## Remaining gaps
- no blocking gap remains for canonical use as long as the technique stays centered on meaningful invariants rather than broad generic "stronger tests" language
- future reuse in another non-skill corpus would strengthen breadth further, but the current cross-context evidence is already enough for default-use approval

## Recommendation
- promote `AOA-T-0017` to `canonical`
- use it as the default invariant-oriented coverage technique while keeping contract-boundary work and staged signal-promotion work routed back to their narrower companions
