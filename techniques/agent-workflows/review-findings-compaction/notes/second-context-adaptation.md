# Second Context Adaptation

## Technique

- id: AOA-T-0052
- name: review-findings-compaction

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where multiple review findings can be compacted into a cleaner current surface without shipping the donor daemon or synthesis runtime

## What changed

- paths: donor daemon, compact job, and synthesis paths were replaced by markdown seed bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a compact command, daemon worker, or fix loop
- dependencies: the compaction pass now exists as a documentation-first reusable contract rather than as a donor runtime feature
- operating assumptions: the technique is read as one bounded findings-hygiene pass, not as a full review platform

## What stayed invariant

- contract: duplicate or stale findings are revalidated and compacted against current code before they survive as the active review surface
- validation logic: grouped findings remain traceable and invalidated findings do not silently persist
- safety rules: compaction remains separate from review triggering, remediation, and backlog policy

## Risks introduced by adaptation

- a documentation-first compaction pass can look stronger than the live runtime evidence if readers forget that this repo is recording the pattern, not running it
- some repositories may widen the contract into issue triage if they ignore the boundary from prioritization

## Evidence

- source paths: `incoming/chat-wave-2-graph-review-mailbox/seed_bundles/agent-workflows/review-findings-compaction/TECHNIQUE.seed.md`, `incoming/chat-wave-2-graph-review-mailbox/docs/CHAT_WAVE_2_PLANTING_ORDER.md`, and `techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing

## Result

- works as a documentation-first second context and preserves the findings-compaction contract without importing the donor compact runtime or remediation breadth
