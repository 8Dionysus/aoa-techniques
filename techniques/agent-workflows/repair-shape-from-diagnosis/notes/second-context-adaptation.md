# Second Context Adaptation

## Technique
- id: AOA-T-0082
- name: repair-shape-from-diagnosis

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the skill-local repair packet became one bounded repair-shaping technique
- AoA repo names and local rollout mechanics moved into adaptation notes instead of the invariant core
- checkpoint posture stayed separate as the sibling `checkpoint-bound-self-repair` technique instead of remaining fused into one broad bundle
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- repair shaping still starts only after diagnosis
- the chosen repair still stays bounded
- owner target and validation still remain explicit
- escalation still remains available when widening is honest

## Risks introduced by adaptation
- public wording can drift into generic improvement advice if bounded repair shape is not kept explicit
- the bundle can widen into checkpoint doctrine if approval or rollback posture replaces the core seam
- a minimal example can understate when escalation should happen

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is one bounded post-session workflow for repair shaping
- the public wording still preserves the seam between diagnosis, repair shape, and checkpoint posture
- the origin evidence remains strong enough to justify a promoted public bundle without importing local skill wrappers

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded repair-shape-from-diagnosis technique
