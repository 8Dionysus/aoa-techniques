# Canonical Readiness

## Technique
- id: AOA-T-0096
- name: pinned-validation-matrix-before-generated-publish

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the split-wave run required sibling bridge publication before downstream consumers validated against live updated surfaces
- the downstream validation pack reran repo-native validators, live workspace contract checks, and compatibility checks after bridge publication
- the residual risk explicitly warns that generated-surface repos can false-green if workflow-pinned sibling refs are not reproduced before publish


## Default-use rationale
- Use this as the default pre-publish move when generated or derived surfaces depend on sibling refs, workflow pins, or bridge publication order.
- the second context proves the same move outside the original extraction packet while preserving portability and owner boundaries
- It is not a general release checklist or proof that generated output is semantically correct.

## Fresh public-safety check
- review date: 2026-05-13
- result: pass
- sanitization still holds: public wording keeps the reusable technique atom while stripping local command wrappers, private session detail, and neighboring owner authority

## Remaining gaps
- no canonical blocker remains for this promotion wave; future non-AoA external adoption can widen evidence but is not required for this bounded canonical review
- downstream evidence ref: `repo:aoa-playbooks/docs/real-runs/2026-04-07.split-wave-cross-repo-rollout.md` hash `7ba4f12069ec67336a1fd893593e0159b9d6a7d8`
- boundary preserved: validation pins must match the generated publish surface before publication trust grows
- boundary preserved: downstream consumers are evidence and adaptation references, not hidden runtime dependencies for standalone reuse

## Recommendation
- move `AOA-T-0096` to `canonical`
