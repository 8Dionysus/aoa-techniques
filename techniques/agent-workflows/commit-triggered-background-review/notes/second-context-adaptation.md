# Second Context Adaptation

## Technique

- id: AOA-T-0051
- name: commit-triggered-background-review

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where a commit-triggered background review can be described as a bounded artifact loop without shipping the donor review daemon itself

## What changed

- paths: donor daemon, hook, and queue paths were replaced by markdown seed bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a background review service, TUI, or fix loop
- dependencies: the review artifact now exists as a documentation-first reusable contract rather than as a donor runtime feature
- operating assumptions: the technique is read as one bounded post-commit review artifact pattern, not as a full review platform

## What stayed invariant

- contract: a visible commit boundary triggers background review and yields an inspectable findings artifact
- validation logic: the artifact names the reviewed commit or scope and stays distinct from any later remediation step
- safety rules: review, remediation, and policy enforcement remain separate surfaces

## Risks introduced by adaptation

- a documentation-first artifact loop can look stronger than the live runtime evidence if readers forget that this repo is recording the pattern, not running it
- some repositories may widen the contract into full CI governance if they ignore the remediation boundary

## Evidence

- source paths: `incoming/chat-wave-2-graph-review-mailbox/seed_bundles/agent-workflows/commit-triggered-background-review/TECHNIQUE.seed.md`, `incoming/chat-wave-2-graph-review-mailbox/docs/CHAT_WAVE_2_PLANTING_ORDER.md`, and `techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing

## Result

- works as a documentation-first second context and preserves the commit-bound review artifact contract without importing the donor review daemon or remediation breadth
