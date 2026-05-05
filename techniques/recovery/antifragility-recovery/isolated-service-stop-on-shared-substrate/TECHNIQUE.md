---
id: AOA-T-0099
name: isolated-service-stop-on-shared-substrate
domain: system-recovery
kind: recovery
status: promoted
origin:
  project: abyss-stack
  path: docs/TOS_GRAPH_CURATION.md
  note: Generalized from a bounded local-stack closeout where one helper service had to be stopped after live verification while the shared substrate remained intentionally alive for continued validation and follow-through.
owners:
  - 8Dionysus
tags:
  - system-recovery
  - bounded-stop
  - shared-substrate
  - runtime
  - closeout
summary: Stop one bounded service while keeping shared substrate services alive, then verify both target absence and substrate continuity so closeout does not widen into unnecessary teardown.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-08
export_ready: true
relations:
  - type: complements
    target: AOA-T-0097
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# isolated-service-stop-on-shared-substrate

## Intent

Stop one bounded service in a shared local stack without needlessly tearing down the substrate that other verification, recovery, or follow-through work still needs.

The technique keeps the stop smaller than a full profile shutdown and makes both halves of the result explicit:
the target service is really down, and the shared substrate is really still alive.

## When to use

- one helper, UI, worker, or edge service needs to stop while shared data services should stay available
- the route is closing a bounded helper lane rather than ending the whole environment
- follow-up verification still needs the shared substrate after the target service is gone
- the safe alternative to full teardown is small enough to verify explicitly

## When not to use

- the target service owns exclusive mutable state that must be quiesced together with its dependencies
- the shared substrate is itself the unstable surface and needs broader recovery or rollback
- operators cannot name the exact target service and the exact services that should remain alive
- the route really needs full profile shutdown, cutover, or incident recovery rather than bounded stop

## Inputs

- one named target service
- one named shared substrate set that should remain alive
- one stop handle for the target service
- one bounded verification path for target absence and substrate continuity

## Outputs

- one stopped target service
- one explicit continuity check for the shared substrate
- one bounded closeout or recovery note that says what was stopped and what intentionally stayed alive
- one escalation point if the stop reveals wider instability than expected

## Core procedure

1. Name the exact target service that should stop and the exact shared substrate that should remain alive.
2. Confirm that the route really needs a bounded service stop rather than full-stack teardown.
3. Stop only the target service through the narrowest runtime handle available.
4. Verify that the target service is actually down instead of assuming the stop succeeded.
5. Verify that the shared substrate is still healthy enough for the next bounded step.
6. Record the result as a bounded closeout or recovery fact: target stopped, substrate still alive, wider rollback not currently required.
7. Escalate to broader recovery or rollback only if the stop breaks the shared substrate or exposes hidden coupling.

## Contracts

- the target stop stays singular and named
- the shared substrate set is explicit before the stop happens
- target absence and substrate continuity both need evidence
- the bounded stop must remain smaller than full-stack teardown
- wider rollback or incident posture must be re-opened explicitly if the stop exposes hidden coupling

## Risks

### Failure modes

- operators stop more than the named target service and silently widen the route
- the target looks stopped from one surface while another runtime handle still keeps it alive
- shared substrate health is assumed instead of checked after the stop

### Negative effects

- keeping the substrate alive can preserve cost or background noise longer than a full teardown would
- a narrow stop can create false confidence that the whole environment is healthy
- teams may delay a needed broader rollback because the first bounded stop appeared clean

### Misuse patterns

- treating a narrow service stop as a substitute for incident recovery
- using ambiguous labels like "the helper stack" instead of naming the exact target and substrate set
- declaring closeout after the stop without proving the shared substrate still supports the next step

### Detection signals

- reviewers cannot tell which service was intentionally stopped
- substrate continuity is described narratively but not checked
- later follow-up fails because hidden coupling was ignored during the bounded stop

### Mitigations

- name target and substrate explicitly before mutation
- verify both absence and continuity after the stop
- keep a visible escalation seam to broader rollback when hidden coupling appears
- prefer full-stack teardown when the substrate itself is unstable

## Validation

Verify the technique by confirming that:
- the target service and shared substrate were named before the stop
- the stop affected only the target service
- one post-stop check showed the target was down
- one post-stop check showed the shared substrate was still usable
- the route kept an explicit escalation seam if the bounded stop was not enough

See `checks/isolated-service-stop-on-shared-substrate-checklist.md`.

## Adaptation notes

What can vary across projects:
- container runtime or supervisor tooling
- the names and count of shared substrate services
- which continuity signals count as healthy enough for the next step
- whether the closeout note lives in a runbook, receipt, or reviewed summary

What should stay invariant:
- one named target stop
- one named substrate continuity set
- explicit verification of both target absence and substrate health
- escalation to broader recovery when the bounded stop is no longer honest

## Public sanitization notes

This public bundle removes machine-local paths, secret-bearing env surfaces, and project-specific runtime names while preserving the reusable bounded-stop contract: stop only the named service, prove it is down, and prove the shared substrate still supports the next honest step.

## Example

See `examples/minimal-isolated-service-stop.md`.

## Checks

See `checks/isolated-service-stop-on-shared-substrate-checklist.md`.

## Promotion history

- born from a bounded `abyss-stack` local-stack closeout for `tos-graph`
- promoted into `aoa-techniques` on 2026-04-08 as a reusable shared-substrate stop pattern

## Future evolution

- add a second context where the same bounded-stop seam appears outside the current local-stack family
- clarify when this pattern should yield to explicit cutover or incident-recovery playbooks
- connect it more directly to receipt publication once a second public context exists
