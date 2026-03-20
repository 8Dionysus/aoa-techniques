# Canonical Readiness

## Technique
- id: AOA-T-0014
- name: tdd-slice

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: the origin note already shows the recurring need for one bounded behavior slice, a tests-first start where appropriate, and a smallest-passing-change implementation path
- second context: the public adaptation keeps the same bounded slice contract in a repository-agnostic form with a checklist, two examples, and reviewable out-of-scope boundaries
- semantic separation: the later semantic review keeps `AOA-T-0014` distinct from `AOA-T-0015` by drawing the line between execution discipline for one slice and contract design at a consumer-visible boundary
- validation strength: the bundle already has an origin note, a second-context note, a checklist, and two concrete examples, which is stronger than the initial promotion floor

## Default-use rationale
- this is the default when the main problem is how to execute one already understood behavior slice safely, not how to define a consumer-visible boundary contract
- it is narrower than `AOA-T-0015 contract-test-design`, which should be preferred when the question is boundary shape, consumer expectations, or contract guarantees
- it complements `AOA-T-0001` because that technique governs the reviewable change process, while this one governs the test-first execution discipline inside one bounded slice

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the published technique remains free of private URLs, secrets, and project-specific operational details
- public reuse check: the checklist, examples, and adaptation note remain understandable without origin-project access

## Remaining gaps
- a future third live context would widen the proof surface further, but it is not required for a first canonical review of this bounded execution discipline

## Recommendation
- approve `AOA-T-0014` for `promoted -> canonical` in this wave; the bundle now reads as the default bounded execution discipline for small behavior slices without collapsing into boundary-contract semantics
