# Second Context Adaptation

## Technique
- id: AOA-T-0096
- name: pinned-validation-matrix-before-generated-publish

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- repo-specific second-wave PR tails were reduced to one bounded publish-hygiene
  law about reproducing workflow-pinned validation inputs
- concrete sibling repo names and one-off repair details were kept in evidence
  notes instead of the invariant core
- the adapted bundle was reduced to one technique doc, one checklist, one
  example, and three evidence notes

## What stayed invariant
- generated publish confidence still depends on the same matrix that CI really
  reads
- local workspace state still cannot silently replace pinned sibling refs
- publish still waits for the pinned-matrix pass rather than for a convenient
  repo-local green check

## Risks introduced by adaptation
- the public wording can drift into generic CI advice if generated publish
  posture stops being central
- the bundle can widen into release automation or multi-repo choreography if
  the pinned matrix is not kept sharply bounded
- a tiny example can understate how much local `main` drift can mislead publish
  decisions

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is
  one bounded publish workflow law rather than an eval policy or playbook route
- the wording preserves the generated-publish seam without pulling in private
  workflow setup or broader wave doctrine
- the origin evidence remains strong enough to justify a promoted bundle from
  real cross-repo use

## Result
- verdict: works
- note: the adapted bundle stays readable as one pinned-matrix rule for
  generated publish honesty
