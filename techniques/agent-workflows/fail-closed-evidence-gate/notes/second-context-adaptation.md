# Second Context Adaptation

## Technique
- id: AOA-T-0068
- name: fail-closed-evidence-gate

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded fail-closed execution seam rather than shipping the donor enforcement platform

## What changed

- paths: the donor ships concrete verify, proxy, and bridge surfaces; this adaptation keeps the generic verdict-before-side-effects contract without requiring one runtime package
- services: broader policy constitutions, pack formats, CI regression loops, and trust-platform features were removed from the reusable contract
- dependencies: the adaptation depends on one execution-boundary verdict seam plus one evidence artifact, not on the donor's wider policy product
- operating assumptions: contributors should read the technique as one bounded execution gate, not as a complete governance framework

## What stayed invariant

- contract: non-allow blocks side effects at the execution boundary
- validation logic: explicit allow is required and one evidence artifact survives for review
- safety rules: the technique remains separate from human confirmation doctrine, durable jobs, and broader policy-platform semantics

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0028](../confirmation-gated-mutating-action/TECHNIQUE.md) if teams stop distinguishing machine or contract verdicts from human confirmation seams
- the public bundle could drift into durable orchestration if pause, checkpoint, and resume semantics become central
- contributors may over-associate the technique with broad governance platforms because the donor bundles the gate with larger policy surfaces

## Evidence

- the donor README describes fail-closed posture around tool execution and preserved evidence
- `docs/agent_integration_boundary.md` says enforcement must happen before tool execution and that non-allow must be non-executing
- `docs/mcp_capability_matrix.md` shows explicit verify and proxy surfaces where verdicts guard execution and where non-allow prevents side effects
- together these sources show that one bounded fail-closed evidence seam can be extracted without importing the whole donor platform

## Result

- works as a documentation-first second context and preserves one bounded execution-gate contract without carrying over the donor's broader governance or trust-product breadth
