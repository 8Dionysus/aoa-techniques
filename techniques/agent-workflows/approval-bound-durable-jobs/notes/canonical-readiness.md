# Canonical Readiness

## Technique
- id: AOA-T-0069
- name: approval-bound-durable-jobs

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around scheduler semantics, orchestration stacks, pack formats, and wider governance breadth
- second context: `aoa-techniques` now records the same durable-job-across-approval contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor family

## Default-use rationale
- this is the right promoted default when the main problem is preserving longer-running work across an explicit approval seam without falling back to hidden memory or widening into scheduler doctrine
- it remains narrower than [AOA-T-0062](../episode-bounded-agent-loop/TECHNIQUE.md) because it centers durable job identity and resume-from-state rather than narrative episode structuring
- it also remains narrower than a one-shot boundary gate because it owns pause and resume continuity across longer-running work

## Fresh public-safety check
- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable durable-job seam and excludes donor-specific scheduler posture, orchestration stacks, and platform governance
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses durable approval-bound jobs without widening into scheduler or orchestration-platform doctrine

## Recommendation
- keep `AOA-T-0069` `promoted`
- defer canonical promotion until another live adopter confirms that the durable-job contract survives outside the donor family
