# Canonical Readiness

## Technique
- id: AOA-T-0093
- name: recommendation-truth-vs-host-actionability

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the SDK note records the exact gap where router recommendations were semantically real but not directly host-executable
- it rejects both ignoring unavailable recommendations and pretending an unavailable skill was used
- it permits manual-equivalence fallback only when the same visible safety discipline is preserved


## Default-use rationale
- Use this as the default boundary check when a recommendation is true in one layer but actionability depends on the current host inventory.
- the second context proves the same move outside the original extraction packet while preserving portability and owner boundaries
- It is not skill execution, host capability proof, or permission to fake a tool invocation.

## Fresh public-safety check
- review date: 2026-05-13
- result: pass
- sanitization still holds: public wording keeps the reusable technique atom while stripping local command wrappers, private session detail, and neighboring owner authority

## Remaining gaps
- no canonical blocker remains for this promotion wave; future non-AoA external adoption can widen evidence but is not required for this bounded canonical review
- downstream evidence ref: `repo:aoa-sdk/docs/skill-runtime-recommendation-gap.md` hash `8b22f1b9e0478d8161fea494079125f315bdf90b`
- boundary preserved: semantic recommendation truth stays separate from host executability
- boundary preserved: downstream consumers are evidence and adaptation references, not hidden runtime dependencies for standalone reuse

## Recommendation
- move `AOA-T-0093` to `canonical`
