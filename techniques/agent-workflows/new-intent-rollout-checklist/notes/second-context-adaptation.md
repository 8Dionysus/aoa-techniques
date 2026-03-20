# Second Context Adaptation

## Technique
- id: AOA-T-0005
- name: new-intent-rollout-checklist

## Target project
- name: aoa-techniques
- environment: public technique canon with markdown-first contracts, generated selection surfaces, and explicit repo-local examples and checks
- runtime: documentation-first repository where the rollout checklist survives as a bounded extension pattern even without the origin project’s live automation chain

## What changed
- adaptation path: the origin rollout policy is reused here as a public checklist for adding one new intent type to an already-existing dry-run chain, rather than as a donor-specific CI script or workflow rewrite
- downstream surface: the visible reuse point is the technique bundle, its checklist, examples, and rollout-failure triage note instead of a full operational automation implementation
- linkage form: the repo-local example and checklist keep the shared-chain contract explicit, with `AOA-T-0004` as the underlying chain and `AOA-T-0001` as the change workflow for editing the rollout itself

## What stayed invariant
- extension boundary: one new intent type is added to an existing shared chain, not to a new one-off path
- safety discipline: dry-run remains the gate before any real action path
- review discipline: the new intent must stay visible on the same artifact and review surfaces as the existing intent set

## Risks introduced by adaptation
- the repo-local example can look like proof of live reuse even though it is still a bounded sketch rather than a second production context
- the checklist can drift toward generic rollout advice if it stops naming fixtures, routing checks, and artifact alignment explicitly
- future readers could mistake a readable public example for the stronger evidence needed for canonical promotion

## Evidence
- `examples/minimal-intent-rollout.md` shows the checklist as a generic bounded rollout for one new intent path, including fixture, smoke, contract-check, review surface, and regression discipline.
- `examples/concrete-non-ui-intent-rollout.md` grounds the same contract in a public-safe non-UI example, `refresh_skill_index`, which keeps the reusable shape but not the origin project’s exact automation details.
- `checks/intent-rollout-checklist.md` keeps the bounded review shape explicit by checking fixture, smoke, contract-check, artifact, and regression coverage in one list.
- `notes/rollout-failure-triage.md` shows that the checklist remains tied to concrete failure repair paths rather than general rollout philosophy.

## Result
- works as a bounded repo-local second context for the public checklist shape, but it is still not enough on its own to justify canonical promotion
