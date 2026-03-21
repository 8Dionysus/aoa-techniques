---
id: AOA-T-0031
name: shell-composable-agent-invocation
domain: agent-workflows
status: promoted
origin:
  project: qqqa
  path: README.md
  note: Adapted from the open-source qqqa project, which treats agent runs as shell-friendly one-shot tools that compose through stdin, stdout, files, and pipes.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - shell
  - composability
  - pipes
  - one-shot
summary: Make agent runs composable as shell-side one-shot tools through explicit stdin, stdout, files, and pipes without widening into generic shell advice or autonomous loops.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0023
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# shell-composable-agent-invocation

## Intent

Keep agent invocations composable as shell tools so one-shot runs can read from stdin, write to stdout, work with files, and fit into pipes without turning into hidden long-lived sessions.

## When to use

- shell-side workflows where an agent should behave like one more composable command
- cases where files, pipes, and explicit terminal inputs are a better boundary than hidden conversational memory
- repositories that want agent output to slot into existing command-line workflows
- one-shot runs where the main reusable value is shell composability rather than confirmation or multi-step orchestration

## When not to use

- workflows where the real need is a visible confirmation seam before mutation
- tasks that need multi-step planning, verification, and reporting across several dependent actions
- repositories looking for generic shell best practices rather than one agent-specific invocation contract
- cases where a hidden long-lived session or autonomous loop is the real execution model

## Inputs

- one explicit one-shot question or action request
- one shell-visible input path such as stdin, stdout, a file path, or a pipe
- one invocation boundary that ends after the current command finishes
- one optional lightweight wrapper that still preserves shell composability

## Outputs

- one shell-friendly agent invocation that works in pipelines and file-based flows
- lower friction when combining agent output with existing command-line tools
- one explicit boundary between this run and the next run
- lower pressure to turn the agent into a hidden long-running shell session

## Core procedure

1. Treat the agent run as one shell-visible invocation, not as a hidden background conversation.
2. Pass inputs through explicit shell channels such as stdin, stdout, file paths, or pipes.
3. Keep the invocation output composable so another shell command or review step can consume it directly.
4. End the invocation after the current answer or action result instead of stretching it into a hidden loop.
5. Use a different sibling technique when the real need is confirmation-gated mutation or a broader workflow backbone.

## Contracts

- the agent run stays one-shot and shell-visible
- stdin, stdout, files, or pipes remain the primary composition boundary
- the technique stays focused on composability, not on generic shell guidance
- confirmation logic may exist nearby, but it is not the core invariant here
- the invocation does not become a hidden autonomous loop or long-lived memory layer
- shell composability remains distinct from broader workflow orchestration

Relationship to adjacent techniques: unlike `AOA-T-0023`, this technique is centered on shell composability through explicit stdin, stdout, files, and pipes rather than on the broader stateless fast-path posture. Unlike `AOA-T-0028`, it is not centered on the confirmation seam before mutation.

## Risks

### Failure modes

- the invocation stops behaving like a shell tool and starts depending on hidden session state
- output stops being easy to pipe or capture because the run accumulates interactive or product-shaped behavior
- shell wrappers become so elaborate that the composable boundary is no longer visible

### Negative effects

- shell composability can make an agent feel simpler than it is, even when the underlying action still needs careful review
- one-shot command ergonomics can tempt teams to force every task into a pipe-friendly shape
- wrapper churn can create portability problems if the technique depends too much on one CLI surface

### Misuse patterns

- widening the bundle into generic shell best practices
- treating confirmation or broader workflow safety as if shell composability alone already provides it
- turning a composable one-shot invocation into a disguised long-lived agent session

### Detection signals

- reviewers can no longer explain how stdin, stdout, or files delimit the invocation
- the command only works through hidden local state or interactive side channels
- the output is not usable in a pipe, file handoff, or explicit shell review step
- the team debates autonomous loop behavior more than the one-shot composition boundary

### Mitigations

- keep the invocation one-shot and centered on explicit shell I/O
- route mutation safety into `AOA-T-0028` and broader workflow orchestration into `AOA-T-0001` when those become the main concern
- narrow wrappers until the underlying composable command boundary is easy to explain
- split out product-shaped session features instead of widening this shell contract

## Validation

Verify the technique by confirming that:
- the run behaves like one shell-visible invocation
- inputs and outputs can move through stdin, stdout, files, or pipes
- the invocation ends cleanly after one result
- shell composability stays visible without relying on hidden session state
- confirmation or broader workflow safety is not falsely implied by the shell boundary alone

See `checks/shell-composable-agent-invocation-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact wrapper command
- whether the invocation prefers stdin, file paths, or pipes
- the shape of the output consumed downstream
- the shell environment around the run

What should stay invariant:
- the agent run is one-shot and shell-visible
- stdin, stdout, files, or pipes define the composition boundary
- the invocation remains composable with other shell steps
- the technique stays distinct from confirmation logic and broader workflow orchestration

Project-shaped details that should not be treated as invariant:
- exact install flows
- provider or profile matrices
- product-specific formatting behavior
- hidden session features or history toggles

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: shell-composable one-shot agent invocation through explicit stdin, stdout, files, and pipes. Generic shell advice, confirmation-as-core behavior, provider matrices, and broader autonomous loop breadth were intentionally left out of the public technique contract.

## Example

See `examples/minimal-shell-composable-agent-invocation.md` and `examples/concrete-pipe-first-agent-invocation.md`.

## Checks

See `checks/shell-composable-agent-invocation-checklist.md`.

## Promotion history

- adapted from open-source `qqqa`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique for shell-composable one-shot agent invocation

## Future evolution

- keep `AOA-T-0023` as the broader stateless-fast-path sibling rather than widening this bundle into general single-shot workflow posture
- keep `AOA-T-0028` as the confirmation-boundary sibling rather than making mutation gating part of this contract
- add a stronger second live context if another public repository adopts the same shell-composable invocation pattern
