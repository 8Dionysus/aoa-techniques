# Second Context Adaptation

## Technique
- id: AOA-T-0042
- name: upstream-skill-health-checking

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over reviewable technique bundles

## What changed
- donor-specific registry branding, setup flows, and security features were reduced to a portable pre-surface readiness contract
- one donor's source-manifest posture and another donor's URL-plus-metadata checks were combined into one smaller evaluation technique
- broader platform features such as federation, access control, semantic search, and automated scanning were kept only as out-of-scope contrast
- the bundle was reduced to one technique doc, one checklist, one example, and four evidence notes

## What stayed invariant
- the check still runs before a source is surfaced locally
- source availability still matters separately from metadata or manifest shape
- the verdict still exists to stop silent breakage before users browse or select upstream-backed entries
- the contract still stays smaller than the surrounding marketplace or registry platform

## Risks introduced by adaptation
- the public wording can drift into generic monitoring if the pre-surface boundary is not restated clearly
- the bundle can drift into curation or sync semantics if examples start focusing on marketplace editing or import automation
- a generic example can overstate certainty if `ready` is read as trusted or secure instead of merely reachable and parseable

## Evidence
- the public technique stays in `evaluation` because the reusable object is a bounded readiness verdict, not a docs curation surface or registry control plane
- both donor contexts reinforce the same seam: upstream-backed entries need a smaller readiness check before local discovery surfaces depend on them
- the adapted bundle preserves the key invariant that availability and minimal manifest shape can be reviewed without importing broader registry doctrine

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded evaluation technique for upstream source readiness before surfacing
