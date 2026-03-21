# Second Context Adaptation

## Technique
- id: AOA-T-0028
- name: confirmation-gated-mutating-action

## Target project
- name: aoa-techniques
- environment: public library repository with reusable technique bundles, generated catalog surfaces, and documentation-first validation
- runtime: documentation-first repository that records the confirmation boundary rather than shipping the donor CLI itself

## What changed
- paths: the donor uses a shell-side fast path; this adaptation presents a generic confirmation-gated mutation pattern without depending on the donor's invocation model
- services: provider profiles and wider CLI orchestration are removed from the reusable contract
- dependencies: the adaptation depends on a visible confirmation seam, not on stateless-shell behavior as an invariant
- operating assumptions: contributors should read the technique as a workflow contract for crossing from read or plan into mutation, not as a shell convenience wrapper

## What stayed invariant
- contract: one explicit confirmation is required before a bounded mutation runs
- validation logic: read or plan work and mutation stay distinct, and the workflow should stop after the confirmed action
- safety rules: the confirmation must name the mutation clearly and should not collapse into a weak or implicit approval

## Risks introduced by adaptation
- the pattern can become vague if a project keeps the confirmation wording but does not name the actual mutation
- some repositories may turn the confirmation gate into generic caution prose instead of a real action boundary

## Evidence
- the donor `README.md` describes `qqqa` as a stateless shell tool where `qq` answers a single question and `qa` performs one tool-using step with confirmation
- this imported technique narrows that behavior into one reusable mutation-gating contract and makes confirmation the center of the pattern

## Result
- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific shell fast-path breadth
