# Second Context Adaptation

## Technique
- id: AOA-T-0069
- name: approval-bound-durable-jobs

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded durable-job seam rather than shipping the donor job platform

## What changed

- paths: the donor ships concrete submit, status, checkpoint, approve, and resume surfaces; this adaptation keeps the generic durable-job-across-approval contract without requiring one runtime package
- services: scheduler semantics, broader orchestration stacks, trust-product posture, and platform governance were removed from the reusable contract
- dependencies: the adaptation depends on durable state plus one explicit approval seam, not on the donor's broader platform
- operating assumptions: contributors should read the technique as one bounded continuity seam for longer-running work, not as a generic workflow engine

## What stayed invariant

- contract: one durable job identity survives pause, approval, and resume
- validation logic: checkpoint or status state remains inspectable and resume depends on that durable state
- safety rules: continuation stays blocked until approval is explicit and the bundle remains separate from scheduler or orchestration doctrine

## Risks introduced by adaptation

- the pattern can collapse into `fail-closed-evidence-gate` if repositories stop distinguishing one-shot boundary verdicts from longer-running durable continuity
- the public bundle could drift into [AOA-T-0062](../episode-bounded-agent-loop/TECHNIQUE.md) if narrative episode structure becomes more central than durable job identity
- contributors may over-associate the technique with total workflow platforms because the donor bundles durable jobs with broader governed-execution surfaces

## Evidence

- the donor durable-jobs docs define job lifecycle surfaces such as submit, status, checkpoint, pause, stop, approve, resume, cancel, and inspect
- those same docs keep approval and resume tied to durable job state rather than to hidden memory
- the donor README frames longer-running governed work around persistent evidence and controlled continuation, which helps confirm the smaller durable-job seam while also showing why broader platform semantics should stay outside the import

## Result

- works as a documentation-first second context and preserves one bounded durable-job-across-approval contract without carrying over the donor's wider orchestration or governance breadth
