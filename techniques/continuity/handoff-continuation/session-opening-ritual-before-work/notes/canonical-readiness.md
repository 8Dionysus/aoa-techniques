# Canonical Readiness

## Technique
- id: AOA-T-0060
- name: session-opening-ritual-before-work

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around mission loops, state-file families, startup test doctrine, task routing, handoff authoring, and broader orchestration semantics
- second context: `aoa-techniques` now records the same session-opening seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `anthropics/cwc-long-running-agents` provides exact-fit public reinforcement beyond the donor family: its long-running convention says to read `PROGRESS.md` before doing anything else, create it if missing, then run `git log --oneline -10` and a project smoke/build/test check so the session starts from a visible baseline instead of a broken or stale handoff
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for the same pre-mutation read-and-verify ritual

## Default-use rationale

- this is the right canonical default when the main problem is how a resumed session should re-read current context and verify baseline state before the first edit
- it remains narrower than [AOA-T-0057](../../structured-handoff-before-compaction/TECHNIQUE.md), [AOA-T-0059](../../git-verified-handoff-claims/TECHNIQUE.md), and [AOA-T-0001](../../../../agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) because it owns only the pre-mutation opening ritual
- it also remains smaller than total startup doctrine because it does not choose tasks, define baseline test policy, or ship an orchestrator contract
- it is now strong enough as a canonical default because the external reinforcement repeats the same "read first, check baseline, then work" shape without requiring task picking, episode loops, evaluator harnesses, or startup-test doctrine to become part of the bundle

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable session-opening seam and excludes donor runtime stacks, state-file contracts, task governance, and startup test mandates
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `cwc-long-running-agents` convention carries file-level Apache-2.0 SPDX metadata and no source code, private data, credentials, or restricted workflow details were copied into the technique

## Remaining gaps

- no blocker remains for canonical status
- future work can add another session-opening implementation, but it must preserve the narrow boundary: read a current context surface, check one visible baseline before mutation, record mismatches, and route task selection, detailed git-claim verification, baseline test doctrine, and orchestrator loops elsewhere

## Recommendation

- move `AOA-T-0060` to `canonical`
- add an adverse-effects review to preserve the boundary between the opening ritual, handoff packet authoring, git-claim verification, baseline testing, task routing, and full long-running-agent harnesses
