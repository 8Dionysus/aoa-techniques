# Second Context Adaptation

## Technique
- id: AOA-T-0088
- name: approval-sensitivity-check

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the skill-local checkpoint boundary was extracted into one standalone approval-sensitivity technique
- AoA-specific approval gates, repair routes, and repo names moved into adaptation notes instead of the invariant core
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- one automation candidate still gets one approval-sensitivity verdict
- hidden authority, missing rollback, and missing health checks still remain visible
- `checkpoint_required` still stays a boundary flag rather than permission
- low-risk read-only candidates still remain distinguishable from mutating ones

## Risks introduced by adaptation
- the public wording can drift into generic risk prose if one automation candidate is not kept explicit
- the bundle can widen into general change-management doctrine if checkpoint language starts sounding sovereign
- the example can understate how often the right outcome is a downgrade to repair or reviewed proposal rather than a positive automation lane

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is one workflow-side checkpoint classification rather than a governance repository or playbook
- the public wording keeps fit classification, landing choice, and approval burden separate
- the origin evidence remains strong enough to justify a promoted public bundle without importing local approval commands or runtime wrappers

## Result
- verdict: works
- note: the adapted bundle stays readable as one bounded approval-sensitivity check over an automation candidate
