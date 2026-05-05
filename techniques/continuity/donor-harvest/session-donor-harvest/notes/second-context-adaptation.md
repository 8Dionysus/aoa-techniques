# Second Context Adaptation

## Technique
- id: AOA-T-0075
- name: session-donor-harvest

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the donor skill wrapper was reduced to a reusable technique contract for post-session donor extraction
- AoA repo names and local routing details moved into adaptation notes instead of the invariant core
- owner placement was split into the sibling `owner-layer-triage` technique instead of staying fused into one broad skill-shaped bundle
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- the workflow still starts only after the session artifact is reviewed
- reusable units are still extracted as bounded candidates rather than broad topics
- evidence anchors still remain visible for later review
- defer or hold posture remains available instead of forcing promotion

## Risks introduced by adaptation
- the public wording can drift into generic summarization if candidate extraction and evidence-anchor posture are not kept explicit
- the bundle can drift back into ecosystem-specific routing if adaptation notes start replacing the technique contract
- a minimal example can understate the need to split merged candidates before later placement

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is a bounded post-session workflow, not a docs taxonomy or memory surface
- the public wording still preserves the seam between donor extraction and later owner placement
- the donor evidence remains strong enough to justify a promoted public bundle without importing local runtime invocation details

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded workflow for extracting donor candidates from reviewed session artifacts
