# Canonical Readiness

## Technique
- id: AOA-T-0060
- name: session-opening-ritual-before-work

## Verdict
- bounded defer for now

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around mission loops, state-file families, startup test doctrine, task routing, handoff authoring, and broader orchestration semantics
- second context: `aoa-techniques` now records the same session-opening seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the current donor family

## Default-use rationale

- this is the right promoted default when the main problem is how a resumed session should re-read current context and verify baseline state before the first edit
- it remains narrower than [AOA-T-0057](../../structured-handoff-before-compaction/TECHNIQUE.md), [AOA-T-0059](../../git-verified-handoff-claims/TECHNIQUE.md), and [AOA-T-0001](../../plan-diff-apply-verify-report/TECHNIQUE.md) because it owns only the pre-mutation opening ritual
- it also remains smaller than total startup doctrine because it does not choose tasks, define baseline test policy, or ship an orchestrator contract

## Fresh public-safety check

- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable session-opening seam and excludes donor runtime stacks, state-file contracts, task governance, and startup test mandates
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor family and documentation-first adaptation
- specifically, the bundle still needs another public workflow surface where resumed sessions visibly re-read and verify baseline state before the first mutation without widening into task routing, startup test doctrine, or orchestration stacks

## Recommendation

- keep `AOA-T-0060` `promoted`
- defer canonical promotion until another live adopter confirms that the session-opening contract survives outside the current donor family
