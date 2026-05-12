# Second Context Adaptation

## Technique

- id: AOA-T-0050
- name: ready-work-from-blocker-graph

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where existing staged dependency surfaces can be used to derive the next honest landing step without shipping the donor ready-work command itself
- external reinforcement:
  - name: Taskwarrior
  - repository: `GothenburgBitFactory/taskwarrior`
  - observed revision: `88697406f78c363595667c270430439f304acd40`
  - public surfaces: `doc/man/task.1.in`, `test/dependencies.test.py`, `test/blocked.test.py`

## What changed

- paths: donor CLI and storage paths were replaced by markdown candidate bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a tracker runtime, queue API, or claim workflow surface
- dependencies: the queue now derives next landing work from existing blocker notes or graph surfaces rather than from the donor tracker implementation
- operating assumptions: the queue is treated as a bounded coordination seam inside repo work, not as a product-facing task board
- the external Taskwarrior reinforcement proves the same ready-frontier seam in a public task workflow: blocked tasks are visibly excluded, unblocked tasks can be reported, and completing a prerequisite removes `BLOCKED` state from downstream work

## What stayed invariant

- contract: only blocker-free eligible work enters the ready queue
- validation logic: blocked exclusions stay visible and the frontier updates when blocker state changes
- safety rules: dependency truth stays separate from later prioritization and from the broader execution workflow
- boundary: the external evidence is the blocker-free frontier, not Taskwarrior's urgency scoring, scheduling, sync, context, or broader task-management product surface

## Risks introduced by adaptation

- a documentation-first queue can drift if the underlying blocker state is not updated
- very small repo tasks may not need a separate ready-frontier surface at all
- a public task manager can make blocker-free derivation look like full prioritization unless secondary ranking and report behavior stay outside the invariant

## Evidence

- source paths: `incoming/chat-graph-review-mailbox/candidate_bundles/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.candidate.md`, `incoming/chat-graph-review-mailbox/docs/CHAT_GRAPH_REVIEW_MAILBOX_PLANTING_ORDER.md`, and `techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing
- Taskwarrior's public man page exposes `blocked`, `blocking`, and `unblocked` reports, giving a visible distinction between blocked work and blocker-free work.
- Taskwarrior's dependency tests verify that completing a dependency removes the `BLOCKED` state from the waiting task.
- Taskwarrior's blocked report test verifies that the blocking task appears while the blocked downstream task does not appear in the blocking report.

## Result

- works across donor, documentation-first, and Taskwarrior blocker-frontier contexts while preserving the blocker-aware ready-frontier contract without importing tracker runtime, urgency ranking, sync, scheduling, or broader prioritization doctrine
