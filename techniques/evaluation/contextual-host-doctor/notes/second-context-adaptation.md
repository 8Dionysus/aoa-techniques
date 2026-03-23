# Second Context Adaptation

## Technique
- id: AOA-T-0037
- name: contextual-host-doctor

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over reviewable technique bundles

## What changed
- donor-specific command names, runtime roots, and device paths were rewritten into a portable selector-aware readiness contract
- the donor shell script became public-safe diagnostic language rather than a repo-specific CLI requirement
- internal-only service reminders and hardware-specific checks were kept only as examples of context-aware branching, not as invariant requirements
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- the diagnostic still runs before startup
- the selected runtime still changes which checks are relevant
- item-level `ok`, `warn`, and `fail` signals still remain visible
- strict mode still remains a separate hardening seam over the same underlying diagnostic

## Risks introduced by adaptation
- the public wording can drift into generic monitoring if the pre-start boundary is not restated clearly
- the bundle can widen into render or lifecycle semantics if it starts describing what happens after the readiness verdict
- a generic example can understate the importance of context-sensitive checks if it does not show why one warning matters for one runtime choice but not another

## Evidence
- the public technique stays in `evaluation` because the reusable object is a readiness verdict rather than a composition contract or startup workflow
- the donor already treats the doctor as one bounded surface among adjacent runtime tools rather than as a universal operator platform
- the adapted bundle preserves the key donor invariant: what matters depends on the selected runtime

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded evaluation technique for selector-aware preflight readiness
