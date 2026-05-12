# Canonical Readiness

## Technique
- id: AOA-T-0062
- name: episode-bounded-agent-loop

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around mission runtimes, supervision stacks, budget policies, task integrity systems, and broader autonomous-platform semantics
- second context: `aoa-techniques` now records the same episode-loop seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `cloudflare/cloudflare-docs` provides exact-fit public reinforcement beyond the donor family: its long-running Agents guide persists a plan with current step state, runs one step at a time, schedules the next step after completion, marks failed steps without silently continuing, uses checkpoints for recovery, and names re-planning plus human oversight as the review boundary before proceeding
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for the same bounded episode or step loop

## Default-use rationale

- this is the right canonical default when the main problem is how to segment longer work into checkpointed episodes or equivalent durable steps with explicit continue, stop, or escalate decisions
- it remains narrower than [AOA-T-0057](../../structured-handoff-before-compaction/TECHNIQUE.md), [AOA-T-0060](../../session-opening-ritual-before-work/TECHNIQUE.md), and [AOA-T-0001](../../../../agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) because it owns only the longer-run segmentation seam
- it also remains smaller than total autonomous-agent doctrine because it does not define supervision, budgets, immutable task governance, or one orchestrator runtime
- it is now strong enough as a canonical default because the external reinforcement repeats the same "bounded slice, checkpoint state, explicit next decision, later slice starts from durable state" shape without requiring the bundle to absorb the Cloudflare platform, sub-agent model, workflow engine, schedule API, or Durable Objects lifecycle

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable episode-loop seam and excludes donor runtime stacks, budget policies, supervision systems, and platform lifecycle machinery
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `cloudflare/cloudflare-docs` source is CC-BY-4.0 licensed and no source code, credentials, private state, platform configuration, or Cloudflare-specific runtime setup was copied into the technique

## Remaining gaps

- no blocker remains for canonical status
- future work can add another episode-loop implementation, but it must preserve the narrow boundary: one bounded work slice, one visible checkpoint or stop state, one explicit continue / stop / escalate decision, and a later slice that starts from durable checkpoint state rather than hidden memory

## Recommendation

- move `AOA-T-0062` to `canonical`
- add an adverse-effects review to preserve the boundary between the episode loop, session-opening rituals, handoff packet structure, git-claim verification, proof gates, durable-job platforms, and full autonomous-agent lifecycle governance
