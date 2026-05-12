# Canonical Readiness

## Technique
- id: AOA-T-0069
- name: approval-bound-durable-jobs

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around scheduler semantics, orchestration stacks, pack formats, and wider governance breadth
- second context: `aoa-techniques` now records the same durable-job-across-approval contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `pydantic/pydantic-ai` provides exact-fit public reinforcement beyond the donor family: deferred tools can end an agent run with `DeferredToolRequests`, preserve pending approval or external-call identities, let the caller gather approvals or results outside the agent process, and start a follow-up run with the original message history plus `DeferredToolResults`
- Pydantic AI's durable-execution surface reinforces the longer-running side of the same contract by preserving progress across transient failures, restarts, asynchronous work, and human-in-the-loop workflows through public durable-system adapters
- LangGraph provides supporting boundary evidence for checkpoint/thread/resume semantics: an interrupt saves graph state through a checkpointer, waits indefinitely for external input, uses a `thread_id` as the persistent cursor, and resumes through `Command(resume=...)`
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for approval-bound continuation from durable or serialized state

## Default-use rationale
- this is the right canonical default when the main problem is preserving longer-running work across an explicit approval seam without falling back to hidden memory or widening into scheduler doctrine
- it remains narrower than [AOA-T-0062](../../../../continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) because it centers durable job identity and resume-from-state rather than narrative episode structuring
- it also remains narrower than a one-shot boundary gate because it owns pause and resume continuity across longer-running work
- it is now strong enough as a canonical default because the second context repeats the key shape outside the donor family: a pending unit keeps identity, continuation waits for approval or external result, and the resumed run receives explicit state or history instead of relying on hidden memory

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable durable-job seam and excludes donor-specific scheduler posture, orchestration stacks, and platform governance
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected Pydantic AI and LangGraph sources are MIT licensed or official public docs, and no source code, private state, credentials, model outputs, job IDs, approval payloads, product setup instructions, or platform-specific backend wiring were copied into the technique

## Remaining gaps
- no blocker remains for canonical status
- future sources can reinforce the default, but they must preserve the narrow boundary: one durable or serialized unit, one approval or external-result seam, explicit continuation input, and resume from durable state or saved history, without importing full scheduler products, workflow-platform governance, queue policy, fleet operations, background autonomy doctrine, or generic human-approval gates

## Recommendation
- move `AOA-T-0069` to `canonical`
- add an adverse-effects review to preserve the boundary between approval-bound durable jobs, one-shot fail-closed gates, episode loops, generic queues, scheduler platforms, and full orchestration products
