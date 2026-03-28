---
id: AOA-T-0069
name: approval-bound-durable-jobs
domain: agent-workflows
status: promoted
origin:
  project: Clyra-AI/gait
  path: docs/durable_jobs.md + README.md
  note: Adapted from the open-source gait project, which keeps longer-running work durable across pause, checkpoint, approval, and resume boundaries without collapsing the whole contract into a generic scheduler platform.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - durable-jobs
  - approval
  - checkpoint
  - resume
summary: Keep longer-running work durable across one explicit approval seam so checkpoint, pause, and resume remain reviewable without widening into a scheduler or orchestration platform.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0062
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# approval-bound-durable-jobs

## Intent

Keep longer-running work durable across one explicit approval seam so checkpoint, pause, and resume remain reviewable without widening into a scheduler, fleet manager, or generic orchestration platform.

## When to use

- work can span longer than one immediate interactive step
- execution must pause at a visible approval seam before continuing
- job state should survive across pause, checkpoint, and resume
- the reusable object is one approval-bound durable job contract, not a whole workflow engine or queue platform

## When not to use

- the work is short enough that a simple fail-closed gate or confirmation seam is enough
- the main need is a generic background task queue, cron system, or scheduler platform
- the workflow needs broad orchestration policy, retries, and fleet governance to make sense
- the durable object would become a general project-management or mission-control product
- no explicit approval seam actually exists in the job lifecycle

## Inputs

- one job identity that can survive beyond one immediate interactive step
- one durable checkpoint or persisted state surface
- one explicit approval seam that must be crossed before continuation
- one bounded resume path after approval
- optional pause, stop, cancel, or inspect actions that remain subordinate to the durable job contract

## Outputs

- one durable job record that survives across pause and resume
- one explicit approval checkpoint before continuation
- one reviewable path to inspect status or checkpoint state
- lower pressure to treat longer-running work as hidden background autonomy

## Core procedure

1. Create one durable job identity for work that may outlive the current immediate step.
2. Persist enough checkpoint or status state that the job can later be inspected or resumed.
3. Run until the first explicit approval seam and stop there instead of continuing implicitly.
4. Expose the pending state so a reviewer can tell the job is waiting on approval rather than silently progressing.
5. Resume only after approval is explicit and the job can continue from durable state rather than from hidden memory.
6. Keep pause, inspect, stop, and resume semantics reviewable and attached to the same bounded job identity.
7. Split out broad scheduling, fleet orchestration, or policy-platform behavior if those become the real center of gravity.

## Contracts

- the job has a stable identity across pause and resume
- checkpoint or status state survives the approval seam
- continuation does not happen until approval is explicit
- resume depends on durable state rather than on hidden memory or silent background continuity
- the technique stays smaller than scheduler platforms, queue products, and broad orchestration doctrine
- the durable job surface remains reviewable enough that another reader can tell whether it is running, paused, waiting for approval, or completed

Relationship to adjacent techniques: unlike `fail-closed-evidence-gate`, this technique does not own the immediate execution verdict at one side-effect boundary; it owns longer-running continuity across an approval seam. Unlike [AOA-T-0062](../episode-bounded-agent-loop/TECHNIQUE.md), it does not divide work into narrative episodes with continue, stop, or escalate decisions; it keeps one durable job identity stable across pause and resume. Unlike [AOA-T-0058](../receipt-confirmed-handoff-packet/TECHNIQUE.md), it does not record receipt of a handoff packet; it preserves durable work state until approval allows continuation.

## Risks

### Failure modes

- job state is not durable enough to support safe resume
- approval is ambiguous and jobs continue anyway
- pause and resume semantics grow until they require a full orchestration platform
- review surfaces cannot explain whether the job is blocked, paused, or failed

### Negative effects

- durable jobs add state-management overhead compared with short-lived actions
- explicit approval seams can slow legitimate longer-running work
- contributors may overgeneralize the pattern into a total background-work doctrine

### Misuse patterns

- relabeling a generic task queue or scheduler platform as if it were one bounded durable-job technique
- treating pause and resume as implicit background behavior instead of visible state transitions
- widening the bundle into orchestration policy, fleet coordination, or mission-control semantics
- using durable jobs where the actual need is only one boundary gate or one episode checkpoint

### Detection signals

- a reviewer cannot tell where the approval seam sits in the job lifecycle
- resuming the job depends on reconstructing context from memory rather than durable state
- dashboards or orchestration controls dominate the bundle explanation
- the same durable-job contract starts absorbing unrelated scheduling or governance semantics

### Mitigations

- keep job identity and checkpoint state explicit
- make approval waiting state visible before continuation
- keep resume tied to durable state rather than narration
- split out scheduler, queue, and orchestration semantics instead of widening this contract

## Validation

Verify the technique by confirming that:
- a stable job identity survives across pause and resume
- checkpoint or status state remains inspectable at the approval seam
- continuation does not happen until approval is explicit
- resume can happen from durable state rather than from hidden memory
- the explanation still makes sense without a scheduler or orchestration platform

See `checks/approval-bound-durable-jobs-checklist.md`.

## Adaptation notes

What can vary across projects:
- the job status model
- the checkpoint storage mechanism
- whether pause, inspect, stop, or cancel surfaces are all present
- how approval is recorded
- how resume is triggered after approval

What should stay invariant:
- job identity is durable
- approval is explicit before continuation
- resume depends on durable state
- scheduler and orchestration platform breadth stay outside the invariant core

Project-shaped details that should not be treated as invariant:
- one CLI or MCP command family
- donor runtime names
- queue brokers, fleet managers, or deployment-specific job systems
- broader mission-control, trust, or governance stacks

## Public sanitization notes

This public bundle keeps only the reusable durable-job seam: one job identity survives pause and resume, waits at an explicit approval boundary, and continues from durable state rather than hidden memory. Donor-specific scheduler posture, pack formats, platform governance, and wider orchestration product behavior were intentionally removed or generalized.

## Example

See `examples/minimal-approval-bound-durable-jobs.md`.

## Checks

See `checks/approval-bound-durable-jobs-checklist.md`.

## Promotion history

- adapted from open-source `Clyra-AI/gait`
- landed from the Wave 1C history-lineage-governed-actions shard inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for durable jobs that pause and resume across an explicit approval seam

## Future evolution

- keep `fail-closed-evidence-gate` as the immediate boundary-gate sibling rather than widening this bundle back into one-shot execution verdicts
- keep [AOA-T-0062](../episode-bounded-agent-loop/TECHNIQUE.md) as the episode-structuring sibling rather than folding all continuation doctrine into durable jobs
- reopen signed or portable evidence as a separate sibling only if it survives without widening into broad orchestration or governance systems
