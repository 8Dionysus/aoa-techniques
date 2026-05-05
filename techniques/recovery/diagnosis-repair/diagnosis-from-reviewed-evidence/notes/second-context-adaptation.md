# Second Context Adaptation

## Technique
- id: AOA-T-0081
- name: diagnosis-from-reviewed-evidence

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the skill-local diagnosis packet became one public read-only diagnosis technique
- AoA repo names and local remediation habits moved into adaptation notes instead of the invariant core
- drift taxonomy stayed separate as the sibling `session-drift-taxonomy` technique instead of remaining fused into one broader bundle
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- diagnosis still starts only after review
- symptoms and probable causes still remain distinct
- owner hints still remain non-sovereign
- mutation still stays out of the diagnosis pass

## Risks introduced by adaptation
- the public wording can drift into generic retrospectives if evidence-backed diagnosis is not kept explicit
- the bundle can widen into repair doctrine if suggested repair shapes start replacing the later repair seam
- a minimal example can understate the need for explicit unknowns

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is one bounded post-session workflow for diagnosis
- the public wording still preserves the seam between diagnosis, taxonomy, and repair planning
- the origin evidence remains strong enough to justify a promoted public bundle without importing local skill wrappers

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded diagnosis-from-reviewed-evidence technique
