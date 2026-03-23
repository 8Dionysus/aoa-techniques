---
id: AOA-T-0038
name: one-command-service-lifecycle
domain: agent-workflows
status: promoted
origin:
  project: OpenMemory-Code
  path: README.md
  note: Adapted from the OpenMemory-Code startup manager and companion stop surfaces, which collapse local multi-service startup into one explicit operator entrypoint without forcing manual per-service coordination.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - lifecycle
  - startup
  - shutdown
  - local-stack
summary: Start and stop a bounded local service stack through one explicit lifecycle entrypoint so prerequisite checks, visible runtime status, and clean shutdown stay reviewable without widening into generic launcher or platform doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0036
  - type: complements
    target: AOA-T-0037
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

# one-command-service-lifecycle

## Intent

Keep a bounded local service stack startable and stoppable through one explicit lifecycle entrypoint so operators do not have to coordinate multiple terminals, hidden child processes, or ad hoc cleanup steps by hand.

## When to use

- local agent-supporting stacks need more than one service, but operators still want one visible entrypoint
- prerequisite checks, auto-build steps, or startup messages should happen in one bounded place before the stack goes live
- the local runtime should tell the operator what started and how to stop it
- clean shutdown matters because orphaned child processes or half-running sidecars create repeated drift
- the reusable object is local lifecycle ownership, not composition, render review, readiness verdicts, or deployment orchestration

## When not to use

- the main need is profile or preset composition rather than lifecycle control
- the main need is pre-start rendered runtime truth or selector-aware readiness checks
- the real target is remote deployment, fleet orchestration, or always-on background service management
- the entrypoint would become a generic project bootstrap or install wizard instead of a bounded runtime lifecycle surface
- the stack cannot name one clear stop path for every service it starts

## Inputs

- one explicit operator-facing lifecycle entrypoint
- one bounded local service stack with named dependent services
- one prerequisite or build policy for what must exist before startup may proceed
- one visible stop path such as terminal interrupt or a paired stop helper
- one concise status surface that can name what is running after startup

## Outputs

- one predictable local start surface for the bounded stack
- lower operator friction compared with manual multi-terminal startup
- visible runtime status and stop instructions after launch
- one explicit cleanup path that reduces orphaned local processes
- a clear handoff from composition, render review, and readiness into actual local runtime control

## Core procedure

1. Pick one operator-facing entrypoint that owns startup for the bounded local stack.
2. Run prerequisite checks or required build steps there, and fail early if the stack cannot be started safely enough.
3. Start the root service or manager that owns any dependent local services instead of requiring the operator to coordinate each service manually.
4. Print a concise status summary that names the running services or roles and the stop path.
5. Keep the lifecycle attached to the initiating terminal or another equally explicit stop surface rather than hiding it behind ambient background state.
6. On interrupt or stop, terminate the services started by the entrypoint together and report leftover cleanup if any child process does not exit cleanly.
7. Leave profile composition, rendered truth, readiness verdicts, project initialization, and integration setup to sibling techniques or docs.

## Contracts

- one explicit operator-facing entrypoint owns local stack startup
- prerequisite and build checks may sit inside that entrypoint, but remain subordinate to lifecycle ownership
- dependent services start and stop as one bounded local stack rather than as scattered manual commands
- the operator can see what started and how to stop it
- shutdown is explicit and tries to prevent orphaned local processes or half-running local services
- the technique stays local, bounded, and operator-triggered rather than widening into deployment orchestration, platform doctrine, or generic launcher behavior
- composition ownership remains with `AOA-T-0035`, rendered truth remains with `AOA-T-0036`, and readiness verdict ownership remains with `AOA-T-0037`

Relationship to adjacent techniques: unlike `AOA-T-0036`, this technique owns starting and stopping the bounded local stack after review rather than rendering the pre-start runtime view. Unlike `AOA-T-0037`, it owns lifecycle control rather than a selector-aware readiness verdict.

## Risks

### Failure modes

- the supposed one-command entrypoint still depends on hidden manual prep in other terminals
- startup messages look reassuring, but the operator still cannot tell what is actually running or how to stop it
- shutdown only kills the parent process and leaves child services behind
- the lifecycle script accumulates unrelated install, configuration, or platform policy until the bounded contract disappears

### Negative effects

- a unified entrypoint can hide useful detail if the status surface is too vague
- automated prerequisite checks can slow small local runs when they are not kept proportional
- a convenience lifecycle wrapper can create false confidence that render review or readiness checks already happened
- contributors may start treating the entrypoint as the place to put every local operation

### Misuse patterns

- widening the bundle into generic project bootstrap, installer, or environment-doctor doctrine
- using one-command lifecycle as a substitute for render review, readiness, smoke, or deployment workflows
- silently backgrounding services so the operator loses the real stop path
- mixing unrelated logging, registry, OAuth, or memory-system breadth into what should stay a bounded local stack lifecycle

### Detection signals

- operators still need a setup note with several manual terminal commands before the lifecycle entrypoint works
- reviewers cannot list which services the entrypoint owns
- stop instructions are missing, unreliable, or known to leave leftovers
- discussions about the bundle drift toward platform integration, remote deployment, or global install behavior

### Mitigations

- keep the entrypoint narrow and lifecycle-centered
- print a short runtime summary and stop path every time the stack starts
- treat leftover child processes as a lifecycle defect instead of normal operator cleanup
- route composition, rendered truth, readiness, smoke, and installation concerns into sibling techniques or separate docs
- split out donor-specific platform extensions instead of widening the core lifecycle contract

## Validation

Verify the technique by confirming that:
- one explicit operator-facing entrypoint starts the bounded local stack
- prerequisite or build checks fail early or are reported clearly before startup continues
- the startup output identifies what is running and how to stop it
- interrupt or a paired stop surface shuts down the started services together
- the bundle stays distinct from composition, rendered truth, readiness verdicts, project bootstrap, and deployment orchestration

See `checks/one-command-service-lifecycle-checklist.md`.

## Adaptation notes

What can vary across projects:
- the command name or wrapper script
- whether the lifecycle surface supports a development and production mode
- the exact prerequisite or build checks
- the exact number of dependent services in the bounded stack
- whether stop happens through terminal interrupt, a companion stop helper, or both

What should stay invariant:
- one explicit entrypoint owns local stack startup
- the started services form one bounded local lifecycle surface
- the operator can see what started and how to stop it
- shutdown is treated as part of the contract rather than as manual cleanup

Project-shaped details that should not be treated as invariant:
- exact ports, host paths, or log locations
- global install locations or desktop shortcut flows
- logging API, OAuth connector, or dashboard side programs
- donor-specific memory, enforcement, registry, or compliance systems

## Public sanitization notes

This public bundle keeps only the reusable local-lifecycle contract: one explicit entrypoint starts a bounded stack, prints a visible runtime summary, and owns clean shutdown. Donor-specific ports, global-install paths, desktop integration, logging extras, OAuth surfaces, and memory-system behavior were intentionally removed or generalized.

## Example

See `examples/minimal-one-command-service-lifecycle.md`.

## Checks

See `checks/one-command-service-lifecycle-checklist.md`.

## Promotion history

- adapted from open-source `OpenMemory-Code`
- promoted into `aoa-techniques` on 2026-03-23 as a bounded external-import technique for local service lifecycle ownership

## Future evolution

- keep `AOA-T-0035` as the composition sibling rather than widening this bundle into profile or preset doctrine
- keep `AOA-T-0036` as the rendered-truth sibling rather than absorbing pre-start review into startup control
- keep `AOA-T-0037` as the readiness sibling rather than making launch control look like a health verdict
- keep `baseline-first-additive-profile-benchmarks` as the comparison sibling rather than turning local lifecycle convenience into performance scoring
