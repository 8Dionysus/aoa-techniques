# Second Context Adaptation

## Technique

- id: AOA-T-0050
- name: ready-work-from-blocker-graph

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where existing staged dependency surfaces can be used to derive the next honest landing step without shipping the donor ready-work command itself

## What changed

- paths: donor CLI and storage paths were replaced by markdown seed bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a tracker runtime, queue API, or claim workflow surface
- dependencies: the queue now derives next landing work from existing blocker notes or graph surfaces rather than from the donor tracker implementation
- operating assumptions: the queue is treated as a bounded coordination seam inside repo work, not as a product-facing task board

## What stayed invariant

- contract: only blocker-free eligible work enters the ready queue
- validation logic: blocked exclusions stay visible and the frontier updates when blocker state changes
- safety rules: dependency truth stays separate from later prioritization and from the broader execution workflow

## Risks introduced by adaptation

- a documentation-first queue can drift if the underlying blocker state is not updated
- very small repo tasks may not need a separate ready-frontier surface at all

## Evidence

- source paths: `incoming/chat-wave-2-graph-review-mailbox/seed_bundles/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.seed.md`, `incoming/chat-wave-2-graph-review-mailbox/docs/CHAT_WAVE_2_PLANTING_ORDER.md`, and `techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing

## Result

- works as a documentation-first second context and preserves the blocker-aware ready-frontier contract without importing the donor tracker runtime or broader prioritization doctrine
