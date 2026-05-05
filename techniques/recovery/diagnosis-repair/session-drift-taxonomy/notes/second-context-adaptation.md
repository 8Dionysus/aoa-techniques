# Second Context Adaptation

## Technique
- id: AOA-T-0080
- name: session-drift-taxonomy

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the diagnosis skill's drift-label layer became one smaller taxonomy technique
- local repo blame and severity language moved into adaptation notes instead of the invariant core
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- taxonomy still starts only after review
- bounded drift labels still stay distinct from probable cause
- uncertainty still remains available
- the taxonomy still stays smaller than the full diagnosis pass

## Risks introduced by adaptation
- public wording can drift into generic friction vibes if the taxonomy seam is not kept explicit
- the bundle can widen into diagnosis doctrine if owner hints or repair shapes leak into the core
- a minimal example can understate how weak evidence should remain uncertain

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is one bounded diagnosis-step workflow rather than a docs taxonomy or routing system
- the public wording still preserves the seam between drift labels and later diagnosis verdicts
- the origin evidence remains strong enough to justify a promoted public bundle without importing local skill wrappers

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded reviewed-session drift-classification technique
