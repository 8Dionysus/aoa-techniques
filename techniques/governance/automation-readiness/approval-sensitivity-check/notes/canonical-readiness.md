# Canonical Readiness

## Technique
- id: AOA-T-0088
- name: approval-sensitivity-check

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the downstream automation scan declares `AOA-T-0088` as a technique dependency
- it marks checkpoint requirements when a route crosses self-change, hidden authority, or important mutation
- approval sensitivity stays visible as a blocker or narrowing signal rather than a hidden policy override


## Default-use rationale
- Use this as the default check when automation pressure may cross approval, rollback, secret, or self-change boundaries.
- the second context proves the same move outside the original extraction packet while preserving portability and owner boundaries
- It is not approval itself, mutation permission, or a proof verdict.

## Fresh public-safety check
- review date: 2026-05-13
- result: pass
- sanitization still holds: public wording keeps the reusable technique atom while stripping local command wrappers, private session detail, and neighboring owner authority

## Remaining gaps
- no canonical blocker remains for this promotion wave; future non-AoA external adoption can widen evidence but is not required for this bounded canonical review
- downstream evidence ref: `repo:aoa-skills/skills/core/session-growth/aoa-automation-opportunity-scan/SKILL.md` hash `133aba96a21474c1a455ab66f9689e43ca0b8f06`
- boundary preserved: approval sensitivity classifies the burden and stop line only
- boundary preserved: downstream consumers are evidence and adaptation references, not hidden runtime dependencies for standalone reuse

## Recommendation
- move `AOA-T-0088` to `canonical`
