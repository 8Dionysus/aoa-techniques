# Second Context Adaptation

## Technique
- id: AOA-T-0036
- name: render-truth-before-startup

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over reviewable technique bundles

## What changed
- donor-specific service names, deployment paths, and command examples were rewritten into a portable pre-start render-review contract
- the donor's compose-specific runtime details were reduced to the more general idea of rendering the actual composed view before launch
- secret-bearing output handling was kept as a public caution without carrying over donor-local file locations
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- the render step still happens before startup
- the render view still comes from the actual composed runtime rather than from declared profiles alone
- service-list render remains the lighter pass and full config render remains the deeper local pass
- full rendered config still stays local and potentially sensitive

## Risks introduced by adaptation
- the public wording can drift into generic configuration export if the pre-start review seam is not restated clearly
- the bundle can widen into readiness or lifecycle semantics if it starts describing what should happen after the render step
- a generic example can hide the distinction between declared composition and actual rendered truth if it is too abstract

## Evidence
- the public technique stays in `agent-workflows` because the reusable object is a pre-start operator step rather than a docs-only structure or an evaluation report
- the donor already treats rendered truth as a separate layer from docs, composition introspection, and post-start validation
- the adapted bundle preserves the strongest bounded caution from the donor: full rendered config may be secret-bearing and should stay local

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded workflow technique for pre-start rendered runtime review
