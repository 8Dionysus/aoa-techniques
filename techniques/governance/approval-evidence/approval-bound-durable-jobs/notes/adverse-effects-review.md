# Adverse Effects Review

## Technique
- id: AOA-T-0069
- name: approval-bound-durable-jobs

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `pydantic/pydantic-ai`, with LangGraph used only as supporting checkpoint/thread/resume boundary evidence
- confirm that the bundle remains one approval-bound durable-job contract, not a scheduler, queue platform, workflow product, human-approval doctrine, or total long-running-agent lifecycle

## Failure modes
- a job appears paused for approval, but continuation can still happen without an explicit approval or result input
- resume depends on hidden memory, current process state, or reconstructed narration instead of durable state, saved history, or a persisted checkpoint
- approval payloads lose the pending job or tool-call identity needed to match the later decision back to the paused work
- side effects before the approval seam are replayed on resume because the durable state does not record completed work or idempotency boundaries

## Negative effects
- durable jobs add persistence, identity, and status overhead that is unnecessary for short one-shot actions
- approval seams can stall legitimate work if the waiting state is hard to inspect or unblock
- platform examples can tempt contributors to import scheduler, queue, worker-fleet, or dashboard semantics into a technique that only needs one durable pause/resume seam

## Misuse patterns
- using this bundle as a substitute for [fail-closed-evidence-gate](../../fail-closed-evidence-gate/TECHNIQUE.md) when the actual need is one immediate non-allow verdict before a side effect
- using this bundle as a substitute for [AOA-T-0062](../../../../continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) when the actual need is step-bounded episode structure and re-planning
- using this bundle as a substitute for [AOA-T-0028](../../../../execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) when the actual need is simple human confirmation before a single mutation
- importing durable-execution frameworks, queue brokers, workflow histories, cloud workers, retry policies, dashboards, or product-specific commands as invariant requirements

## Detection signals
- reviewers cannot tell which job, tool call, or pending unit the approval belongs to
- examples say "resume" but do not show durable state, saved history, checkpoint, pending-call ID, or equivalent continuity anchor
- the explanation centers workers, schedules, retries, queues, deployments, observability, or fleet policy more than the approval-bound pause/resume contract
- denial, timeout, missing approval, or stale approval outcomes are not represented as visible terminal or waiting states

## Mitigations
- keep a stable job, checkpoint, thread, pending-call, or message-history identity across pause and resume
- require explicit approval, denial, or external result before continuation and record how it maps back to the pending unit
- make waiting, denied, resumed, canceled, and completed states inspectable enough for a reviewer to distinguish them
- route scheduler, queue, orchestration, retry, fleet, dashboard, and broad policy behavior to sibling techniques or owning systems instead of widening this bundle

## Recommendation
- safe to promote as a canonical agent-workflow handoff when the job or pending call keeps stable identity, waits at an explicit approval seam, and resumes from durable state, saved history, or checkpointed context rather than hidden memory
- keep future revisions narrow: do not absorb fail-closed side-effect gates, generic confirmation prompts, episode planning, workflow-platform governance, queue semantics, retry doctrine, worker-fleet control, or total durable-execution product behavior into this bundle
