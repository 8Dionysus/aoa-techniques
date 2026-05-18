# Second Context Adaptation

## Technique

- id: AOA-T-0049
- name: dependency-aware-task-graph

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where the graph contract is recorded and used to coordinate bounded landing work rather than shipped as a live tracker product
- external reinforcement:
  - name: Taskwarrior
  - repository: `GothenburgBitFactory/taskwarrior`
  - observed revision: `88697406f78c363595667c270430439f304acd40`
  - public surfaces: `doc/man/task.1.in`, `test/dependencies.test.py`, `src/dependency.cpp`

## What changed

- paths: donor CLI and storage paths were replaced by markdown candidate bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a tracker runtime, memory store, or ready-work command surface
- dependencies: the graph now coordinates bounded landing tasks and shared-surface updates rather than issues inside the donor tracker
- operating assumptions: the graph is kept as a reviewable working surface for staging and landing work, not as a product-facing issue system
- the external Taskwarrior reinforcement proves the same dependency graph seam in a public task workflow: tasks can depend on other tasks, circular dependencies are rejected, `BLOCKED` / `BLOCKING` status is derivable, and completing a prerequisite can unblock downstream work

## What stayed invariant

- contract: explicit dependency edges determine which work is blocked and which work is ready
- validation logic: the ready frontier can be recomputed after each blocker or state change
- safety rules: the graph remains subordinate to implementation review, source markdown, and `python scripts/release_check.py`
- boundary: the external evidence is the dependency/blocker seam, not Taskwarrior's full report, urgency, sync, context, or task-management feature set

## Risks introduced by adaptation

- a documentation-first graph can drift if it is not updated when work state changes
- very small repo tasks may not need this much coordination structure
- a mature task manager can tempt the technique to absorb reporting, urgency, context, sync, or full backlog behavior unless the blocker graph stays the invariant

## Evidence

- source paths: `mechanics/distillation/legacy/archive/closed-incoming-packets/chat-graph-review-mailbox/docs/CHAT_GRAPH_REVIEW_MAILBOX_PLANTING_ORDER.md` and `techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing
- Taskwarrior's public man page exposes `blocked`, `blocking`, and `unblocked` reports over tasks affected by dependencies.
- Taskwarrior's dependency tests reject self-dependencies and cycles, show acyclic graph support, expose `BLOCKED` / `BLOCKING` tags, and verify that completing a dependency unblocks the downstream task.
- Taskwarrior's dependency implementation explicitly walks dependency chains and handles chain repair when a blocking task is completed or deleted.

## Result

- works across donor, documentation-first, and Taskwarrior dependency-graph contexts while preserving the bounded dependency-graph contract without importing tracker runtime, memory breadth, urgency reports, sync, or full project-management doctrine
