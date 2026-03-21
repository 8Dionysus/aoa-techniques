# Second Context Adaptation

## Technique
- id: AOA-T-0023
- name: stateless-single-shot-agent

## Target project
- name: aoa-techniques
- environment: public library repository with reusable technique bundles, generated catalog surfaces, and documentation-first validation
- runtime: documentation-first repository that records the fast-path workflow rather than shipping the donor CLI itself

## What changed
- paths: the donor exposes `qq` and `qa`; this adaptation presents a generic shell-side fast-path pattern without depending on exact binary names
- services: provider profiles, HTTP clients, and CLI integrations are removed from the reusable contract
- dependencies: the adaptation depends on bounded single-shot invocation and confirmation posture, not on the donor runtime stack
- operating assumptions: contributors should read the technique as a workflow contract for shell-side agent work, not as an installation guide for the donor tool

## What stayed invariant
- contract: one invocation stays mostly independent, tool use stays single-step, and mutation stays confirmation-gated
- validation logic: read-only and tool-using modes stay distinct, and the fast path should end after one invocation instead of becoming a hidden loop
- safety rules: transient context remains input-only and mutating actions require explicit confirmation

## Risks introduced by adaptation
- the pattern can become vague if a project copies the "stateless" label but quietly adds hidden continuity or multi-step autonomy
- some repositories may keep the shell fast path but drop the explicit confirmation gate before mutating commands

## Evidence
- the donor `README.md` describes `qqqa` as a stateless shell tool where `qq` answers a single question and `qa` performs one tool-using step with confirmation
- the donor philosophy section keeps runs mostly independent, shell-friendly, and safe by default instead of relying on long hidden sessions
- this imported technique narrows those behaviors into one reusable fast-path contract for shell-side agent work

## Result
- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific runtime breadth
