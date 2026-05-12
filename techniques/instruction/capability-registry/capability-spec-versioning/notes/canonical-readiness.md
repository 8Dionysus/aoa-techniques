# Canonical Readiness

## Technique
- id: AOA-T-0025
- name: capability-spec-versioning

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around plan-and-execute orchestration, persistence, execution-history learning, and registry breadth
- first second context: `aoa-techniques` records the same contract as a documentation-first adaptation with examples and a checklist
- exact public reinforcement: the A2A Protocol uses a discoverable Agent Card with protocol version, capabilities, supported interfaces, available skills, caching/version behavior, and capability validation rules that clients check before using optional operations
- validation strength: the bundle now carries a checklist, two examples, a clean external-origin note, one documentation-first adaptation, one exact-fit public protocol surface beyond the donor, and an adverse-effects review

## Default-use rationale
- this is the right canonical default when the main problem is keeping one agent-facing capability contract explicit and versioned instead of hiding it in provider code or runtime glue
- it remains narrower than workflow or routing techniques because it only owns the contract surface, not execution sequencing, registry lifecycle, marketplace discovery, or dispatch policy
- it also stays distinct from `AOA-T-0063`, which owns registry-facing agent records rather than the smaller capability-spec contract itself

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- source checked: A2A Protocol specification and `a2aproject/A2A` HEAD `ae6a562d5d972f2c4b184f748bb32e1fa9aa7bf2`
- sanitization still holds: the bundle keeps only the reusable capability-spec contract and excludes donor-specific runtime, CLI, persistence, learning, and protocol-platform detail
- public reuse check: the examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- no blocking promotion gap remains for the current canonical contract
- future work may still add a separate capability compatibility-matrix sibling if version transition policy becomes its own reusable object

## Recommendation
- promote `AOA-T-0025` to `canonical`
- keep `notes/adverse-effects-review.md` as the watch surface for version-number ceremony, registry drift, and implementation detail overwhelming the spec
