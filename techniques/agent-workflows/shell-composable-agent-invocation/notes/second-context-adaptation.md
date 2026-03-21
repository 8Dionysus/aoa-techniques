# Second Context Adaptation

## Technique
- id: AOA-T-0031
- name: shell-composable-agent-invocation

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit provenance-note discipline
- runtime: documentation-first repository that records the shell-composable invocation pattern rather than shipping the donor CLI itself

## What changed

- paths: the donor exposes shell-friendly one-shot commands; this adaptation presents the pattern as a generic shell-visible invocation contract that can fit other repositories
- services: no provider profile matrix, install flow, or interactive wrapper behavior is required in this repository
- dependencies: the adaptation depends on explicit stdin, stdout, file, and pipe boundaries rather than on one donor command name
- operating assumptions: contributors should keep invocation inputs and outputs shell-visible and route confirmation or broader orchestration into separate sibling techniques

## What stayed invariant

- contract: one agent run stays one-shot and shell-composable
- validation logic: stdin, stdout, files, or pipes still define the observable composition boundary
- safety rules: the run ends after the current result instead of drifting into a hidden session

## Risks introduced by adaptation

- the pattern can become vague if a project keeps one-shot commands but loses the explicit shell I/O boundaries that make the technique reviewable
- some repositories may quietly fold confirmation or long-lived session behavior into the same command and blur the contract

## Evidence

- the donor README describes shell-first one-shot invocations that compose through existing terminal flows
- the donor surface keeps the commands small and composable rather than requiring a hidden long-lived session
- this imported technique narrows those behaviors into one reusable agent-workflow pattern for shell-side composition

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific CLI breadth
