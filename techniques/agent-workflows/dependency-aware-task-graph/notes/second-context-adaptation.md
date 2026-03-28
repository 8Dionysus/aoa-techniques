# Second Context Adaptation

## Technique

- id: AOA-T-0049
- name: dependency-aware-task-graph

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where the graph contract is recorded and used to coordinate bounded landing work rather than shipped as a live tracker product

## What changed

- paths: donor CLI and storage paths were replaced by markdown seed bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a tracker runtime, memory store, or ready-work command surface
- dependencies: the graph now coordinates bounded landing tasks and shared-surface updates rather than issues inside the donor tracker
- operating assumptions: the graph is kept as a reviewable working surface for staging and landing work, not as a product-facing issue system

## What stayed invariant

- contract: explicit dependency edges determine which work is blocked and which work is ready
- validation logic: the ready frontier can be recomputed after each blocker or state change
- safety rules: the graph remains subordinate to implementation review, source markdown, and `python scripts/release_check.py`

## Risks introduced by adaptation

- a documentation-first graph can drift if it is not updated when work state changes
- very small repo tasks may not need this much coordination structure

## Evidence

- source paths: `incoming/chat-wave-2-graph-review-mailbox/seed_bundles/agent-workflows/dependency-aware-task-graph/TECHNIQUE.seed.md`, `incoming/chat-wave-2-graph-review-mailbox/docs/CHAT_WAVE_2_PLANTING_ORDER.md`, and `techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing

## Result

- works as a documentation-first second context and preserves the bounded dependency-graph contract without importing the donor tracker runtime or memory breadth
