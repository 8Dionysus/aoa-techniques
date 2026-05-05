# Second Context Adaptation

## Technique
- id: AOA-T-0083
- name: checkpoint-bound-self-repair

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the skill-local checkpoint bridge became one bounded self-repair checkpoint technique
- AoA owner-layer names and local approval commands moved into adaptation notes instead of the invariant core
- repair shaping stayed separate as the sibling `repair-shape-from-diagnosis` technique instead of remaining fused into one broad bundle
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- self-repair still stays behind explicit checkpoint posture
- rollback and health-check cues still remain visible
- iteration limits still remain bounded
- improvement logging still stays explicit

## Risks introduced by adaptation
- the public wording can drift into generic caution prose if the self-repair checkpoint stack is not kept explicit
- the bundle can widen into general approval governance if it stops centering on bounded self-repair
- a minimal example can understate when escalation should replace retries

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is one bounded workflow-side checkpoint stack rather than a general policy system
- the public wording still preserves the seam between repair shape and checkpoint posture
- the origin evidence remains strong enough to justify a promoted public bundle without importing local skill wrappers

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded self-repair checkpoint technique
