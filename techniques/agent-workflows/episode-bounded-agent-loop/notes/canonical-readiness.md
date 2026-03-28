# Canonical Readiness

## Technique
- id: AOA-T-0062
- name: episode-bounded-agent-loop

## Verdict
- bounded defer for now

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around mission runtimes, supervision stacks, budget policies, task integrity systems, and broader autonomous-platform semantics
- second context: `aoa-techniques` now records the same episode-loop seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the current donor family

## Default-use rationale

- this is the right promoted default when the main problem is how to segment longer work into checkpointed episodes with explicit continue, stop, or escalate decisions
- it remains narrower than [AOA-T-0057](../../structured-handoff-before-compaction/TECHNIQUE.md), [AOA-T-0060](../../session-opening-ritual-before-work/TECHNIQUE.md), and [AOA-T-0001](../../plan-diff-apply-verify-report/TECHNIQUE.md) because it owns only the longer-run segmentation seam
- it also remains smaller than total autonomous-agent doctrine because it does not define supervision, budgets, immutable task governance, or one orchestrator runtime

## Fresh public-safety check

- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable episode-loop seam and excludes donor runtime stacks, budget policies, and supervision systems
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor family and documentation-first adaptation
- specifically, the bundle still needs another public workflow surface where longer work is segmented into checkpointed episodes without widening into a whole autonomous platform or workflow-governance doctrine

## Recommendation

- keep `AOA-T-0062` `promoted`
- defer canonical promotion until another live adopter confirms that the episode-loop contract survives outside the current donor family
