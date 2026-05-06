# Second Context Adaptation

## Technique
- id: AOA-T-0094
- name: canonical-owner-with-validated-mirror

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the live receipt-envelope seam was reduced to one bounded law about canonical ownership and validated mirrors
- repository-specific schema field names, file paths, and migration chatter were moved into adaptation notes instead of the invariant core
- the public bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- exactly one repository owns the shared contract
- local mirrors stay legal only when they remain subordinate and parity-checked
- consumer intake rejects unknown contract tokens early
- migrations move through the canonical owner before mirrors

## Risks introduced by adaptation
- the public wording can drift back into generic source-of-truth doctrine if mirror legality stops being the center
- the bundle can drift into rollout policy if owner ordering and publisher recovery become the focus
- a tiny example can understate how important consumer-side fail-fast validation is for catching drift

## Evidence
- the adapted bundle stays in `docs` because the surviving object is a contract-ownership law, not a runtime workflow or proof doctrine
- the public wording keeps adjacent techniques for distribution, mirroring, and rollout explicit rather than blending them
- the origin evidence remains strong enough for a promoted public bundle without importing session-local detail as invariant contract language

## Result
- verdict: works
- note: the adapted bundle stays readable as one bounded rule for canonical cross-repo contract ownership with validated mirrors
