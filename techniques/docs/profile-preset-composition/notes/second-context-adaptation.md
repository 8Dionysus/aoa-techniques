# Second Context Adaptation

## Technique
- id: AOA-T-0035
- name: profile-preset-composition

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable, reviewable technique bundles

## What changed
- donor-specific compose layout and local service naming were rewritten as a reusable module-profile-preset contract
- ports, host-facing endpoints, and local roots were generalized or removed
- the donor scripts became public-safe inspection language instead of repo-specific command requirements
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- atomic units remain separate from profile groupings and preset groupings
- preset-expanded profiles still resolve before direct profile additions
- duplicate profiles and modules still stay at first appearance
- a read-only inspection path still exists before launch

## Risks introduced by adaptation
- the public wording can drift into generic configuration composition if the layer ownership is not restated clearly
- the bundle can widen into render or lifecycle semantics if inspection-before-run is confused with startup control
- a minimal example can feel too toy-like if it does not show both a base profile and an additive profile

## Evidence
- the public technique stays in `docs` because the reusable object is a reviewable composition contract rather than a launcher or runtime manager
- the bundle now has explicit neighboring seams for rendered truth, readiness, and lifecycle so this technique can stay narrow
- the donor evidence remains strong enough to support a bounded promoted bundle without importing donor-specific operational detail

## Result
- verdict: works
- note: the adapted bundle stays readable as a public docs technique for layered runtime composition
