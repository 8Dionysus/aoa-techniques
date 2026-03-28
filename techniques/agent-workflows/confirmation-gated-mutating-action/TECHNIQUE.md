---
id: AOA-T-0028
name: confirmation-gated-mutating-action
domain: agent-workflows
status: canonical
origin:
  project: qqqa
  path: README.md
  note: Adapted from the open-source qqqa project, which separates read-only shell-side work from one explicit confirmed mutating step.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - confirmation
  - mutation
  - shell
  - bounded
summary: Require one explicit confirmation seam before a read or plan flow crosses into a mutating action so the action stays reviewable without widening into a multi-step autonomous loop.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-28
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
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
---

# confirmation-gated-mutating-action

## Intent

Keep the boundary between read or plan work and mutating work explicit so a confirmed action stays reviewable, bounded, and easy to stop before it crosses into hidden autonomy.

## When to use

- a read or plan flow is enough until one specific mutating step is ready
- a mutating step should be visible, acknowledged, and easy to review before it runs
- a repository or operator workflow needs a clear seam between advice and action
- the task should stay bounded even when the action itself is small and routine

## When not to use

- the task is already a full multi-step workflow that needs planning, diff review, validation, and reporting
- the main goal is a stateless shell fast path rather than a confirmation boundary
- the action should happen implicitly or through a weak approval signal
- the task depends on a broader autonomous loop or hidden continuation behavior

## Inputs

- one explicit read or plan result
- one proposed mutating action
- one visible confirmation decision
- one bounded target for the mutation

## Outputs

- one confirmed mutation or one explicit refusal
- one auditable checkpoint between read or plan and write
- one clear handoff point when the task should widen into a broader workflow

## Core procedure

1. Read or plan only until the mutating step is concrete.
2. State the proposed mutation in bounded terms.
3. Require a visible confirmation before any write or execution that changes state.
4. Execute only the confirmed mutation and keep it scoped to the stated target.
5. Stop after the confirmed action instead of chaining an unbounded follow-on loop.
6. Escalate to a broader workflow technique when the task now needs multiple coordinated steps.

## Contracts

- read or plan work stays distinct from mutating work
- the confirmation seam is the center of the contract
- implicit approvals do not count as confirmation
- the technique does not depend on stateless shell invocation as an invariant
- the technique stays bounded and reviewable even when the underlying action is simple
- when the task widens beyond one confirmed mutation, hand off to a broader workflow technique instead of stretching this contract

Relationship to adjacent techniques: unlike `AOA-T-0023`, this technique centers the explicit confirmation boundary itself rather than the broader stateless single-shot shell fast path. Unlike `AOA-T-0001`, it does not own multi-step planning, diff review, or verification across a larger repository workflow.

## Risks

### Failure modes

- the confirmation step becomes so weak that it no longer feels like a real gate
- the workflow quietly expands into a multi-step loop after the first confirmation
- the action target gets broader than the confirmation text actually described

### Negative effects

- a confirmation gate can add friction to small safe actions
- teams may overuse the technique when a fuller workflow would be more honest
- a visible gate can still hide risk if the described mutation is too vague

### Misuse patterns

- treating a generic caution prompt as if it were a real confirmation gate
- bundling several writes behind one vague approval
- using the technique as a substitute for planning or diff review when the task is already broad

### Detection signals

- the workflow starts asking for approval after the mutation is already underway
- the action text does not match the actual change being made
- the same run begins chaining additional steps without a new explicit gate

### Mitigations

- keep the proposed mutation specific and visible before execution
- require a fresh confirmation when the action changes scope
- route broader work into `AOA-T-0001` or another multi-step technique instead of extending this one

## Validation

Verify the technique by confirming that:
- a read or plan flow can pause before mutation
- the mutation is named explicitly before it runs
- the confirmation is visible and reviewable
- the workflow stops after the confirmed mutation instead of becoming a hidden loop
- broader work cleanly hands off to a more complete workflow technique

See `checks/confirmation-gated-mutating-action-checklist.md`.

## Adaptation notes

What can vary across projects:
- the confirmation UI or terminal prompt
- the shape of the proposed mutation text
- the command runner or automation wrapper behind the action
- the repository or tool surface being mutated

What should stay invariant:
- the confirmation seam stays explicit
- read or plan and mutation remain distinct
- a fresh confirmation is required when the action changes scope
- the technique remains a bounded action gate, not a hidden autonomous loop

Project-shaped details that should not be treated as invariant:
- provider-specific shell behavior
- install or onboarding scripts
- generic approval phrasing that does not name the mutation
- multi-step orchestration details

## Public sanitization notes

This import narrows the donor repository to one bounded agent-workflow pattern: an explicit confirmation gate before a mutating action. Shell invocation details, provider-specific behavior, onboarding steps, and broader orchestration breadth were intentionally left out of the public technique contract.

## Example

See `examples/minimal-confirmation-gated-mutating-action.md` and `examples/concrete-confirmed-mutating-action.md`.

## Checks

See `checks/confirmation-gated-mutating-action-checklist.md`.

## Promotion history

- adapted from open-source `qqqa`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique focused on confirmation before mutation
- strengthened on 2026-03-28 by GitHub Copilot's public coding-agent approval surfaces, which keep command or tool execution behind explicit operator confirmation in both interactive CLI and agent-mode IDE workflows
- promoted to `canonical` on 2026-03-28 after second-context review confirmed that the explicit confirmation-before-mutation seam survives beyond the donor lineage

## Future evolution

- split out a tighter read-only advisory sibling if the confirmation gate proves reusable with no mutating step
- split out a broader workflow sibling if confirmation plus mutation later needs a richer planning or verification chain
- add a stronger second live context if another public repository adopts the same confirmation-gated mutation boundary
