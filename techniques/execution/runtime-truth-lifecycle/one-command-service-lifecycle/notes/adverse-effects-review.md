# Adverse Effects Review

## Technique

- id: AOA-T-0038
- name: one-command-service-lifecycle

## Review focus

- current role: canonical default for one-entrypoint local stack lifecycle ownership
- current watch seam: keep startup, visible follow-through, and teardown centered on one bounded local stack rather than absorbing install, platform, deployment, readiness, render, smoke, benchmark, or monitoring authority

## Failure modes

- a convenience entrypoint becomes a hidden install wizard or platform launcher
- the entrypoint starts services but leaves stop or cleanup outside the visible contract
- backgrounded children survive after the operator believes the stack is stopped
- lifecycle output implies render review, readiness, smoke, or benchmark confidence that did not actually happen

## Negative effects

- one-command startup can hide useful service boundaries if status output is too vague
- prerequisite checks or first-run setup can slow small local runs if they are not proportional
- a canonical lifecycle wrapper can attract unrelated local operations because it is the most visible command
- teardown can be too destructive if it removes shared local substrate that the bounded stack did not own

## Misuse patterns

- using the lifecycle entrypoint as a generic project bootstrap, installer, deployment tool, or platform dashboard
- treating `up` success as proof that selected runtime truth, host readiness, smoke, or benchmarks are valid
- starting remote or fleet resources while still describing the surface as local stack lifecycle
- adding unrelated OAuth, logging, registry, memory, or monitoring breadth to the core lifecycle command

## Detection signals

- reviewers cannot name the services owned by the entrypoint
- stop instructions are absent, unreliable, or known to leave child services behind
- users need several manual terminal commands before the supposed one-command lifecycle works
- route discussion focuses more on deployment, platform policy, or product launchers than on bounded local startup and teardown

## Mitigations

- keep the entrypoint narrow and tied to a named local stack
- print what started and how to stop it every time the stack starts
- treat leftover child processes or shared-substrate teardown as lifecycle defects
- route composition, render truth, readiness, smoke, benchmark, deployment, and monitoring concerns to sibling techniques or owner repos
- document first-run tooling only as subordinate prerequisite handling, not as the reusable move

## Recommendation

- keep current `canonical` status and use this note as the watch surface for launcher drift, hidden cleanup debt, false readiness, and expansion into platform or deployment authority
