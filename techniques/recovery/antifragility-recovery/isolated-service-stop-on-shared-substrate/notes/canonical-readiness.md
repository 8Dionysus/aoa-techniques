# Canonical Readiness

## Technique
- id: AOA-T-0099
- name: isolated-service-stop-on-shared-substrate

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the reviewed `tos-graph` run hardened a bounded helper service on shared substrate and later stopped only that helper service
- shared substrate services stayed alive, so stop scope remained route-specific instead of widening into full-stack teardown
- the residual risk names the exact misuse: a narrow helper-service stop can be mistaken for broader rollback when the substrate itself failed


## Default-use rationale
- Use this as the default stop move when a bounded helper or route service must stop without tearing down the shared substrate it depends on.
- the second context proves the same move outside the original extraction packet while preserving portability and owner boundaries
- It is not full rollback, incident recovery, or permission to ignore substrate health.

## Fresh public-safety check
- review date: 2026-05-13
- result: pass
- sanitization still holds: public wording keeps the reusable technique atom while stripping local command wrappers, private session detail, and neighboring owner authority

## Remaining gaps
- no canonical blocker remains for this promotion wave; future non-AoA external adoption can widen evidence but is not required for this bounded canonical review
- downstream evidence ref: `repo:aoa-playbooks/docs/real-runs/2026-04-08.owner-first-capability-landing.tos-graph-curation.md` hash `2528b8424e16e76af0f15e5343a44bea7ad6ac29`
- boundary preserved: stop the isolated service only when shared-substrate integrity is not the failing object
- boundary preserved: downstream consumers are evidence and adaptation references, not hidden runtime dependencies for standalone reuse

## Recommendation
- move `AOA-T-0099` to `canonical`
