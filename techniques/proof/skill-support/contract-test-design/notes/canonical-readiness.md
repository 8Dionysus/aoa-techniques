# Canonical Readiness

## Technique
- id: AOA-T-0015
- name: contract-test-design

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: the source notes describe a repeated boundary-validation need where consumer-visible contracts mattered more than hidden implementation details
- second context: the public adaptation keeps the same boundary-first contract while rewriting project-shaped service and workflow edges into repo-agnostic contract framing
- validation strength: the bundle already has a checklist, two concrete examples, a semantic review, and clear adaptation notes that keep the consumer boundary explicit
- semantic separation: the `Skill-Support Semantic Review` keeps `AOA-T-0015` distinct from `AOA-T-0017`, which helps confirm that contract design is not just broader invariant coverage

## Default-use rationale
- this reads as the default when a team needs to make one consumer-visible boundary explicit and reviewable without freezing unrelated internals
- it stays narrower than `AOA-T-0017`, which is the better choice when the main problem is broadening coverage with stable invariants rather than designing the boundary contract itself
- it also remains narrower than `AOA-T-0003`, which focuses on runnable smoke summary production rather than contract framing at the consumer boundary

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the public bundle removes project-specific endpoints, service names, and local operational topology while keeping the reusable boundary-design pattern
- public reuse check: the example, checklist, and adaptation notes remain understandable without origin-project access

## Remaining gaps
- a future third live context would add more proof surface, but it is not required before canonical promotion for this bounded evaluation discipline

## Recommendation
- approve `AOA-T-0015` for `promoted -> canonical` in this wave; it now reads as the default boundary-contract evaluation discipline within its bounded scope
