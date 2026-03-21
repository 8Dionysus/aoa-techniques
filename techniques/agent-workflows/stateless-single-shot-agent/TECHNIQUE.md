---
id: AOA-T-0023
name: stateless-single-shot-agent
domain: agent-workflows
status: promoted
origin:
  project: qqqa
  path: README.md
  note: Adapted from the open-source qqqa project, which keeps shell-side LLM runs mostly stateless and limits tool-using agent execution to one confirmed step per invocation.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - stateless
  - shell
  - single-shot
  - confirmation
summary: Keep shell-side agent work mostly stateless and bounded to one confirmed step per invocation so runs stay composable, reviewable, and low-memory by default.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0001
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

# stateless-single-shot-agent

## Intent

Keep quick shell-side agent work bounded to one mostly independent invocation so the fast path stays composable, inspectable, and safe to abandon instead of silently turning into a hidden long-running session.

## When to use

- ad hoc shell assistance where one answer or one bounded tool-using step is enough
- workflows that value pipes, files, or explicit terminal context more than hidden conversational memory
- cases where command execution or file mutation should require a visible confirmation gate
- operator flows that need a small, low-ceremony fast path before escalating to a broader repository workflow

## When not to use

- multi-step repository changes that need planning, diff review, verification, and reporting across several actions
- tasks that depend on long-lived hidden memory or an iterative autonomous loop
- workflows where one invocation must safely coordinate many tool calls or background state transitions
- cases where the real need is a richer intent chain or test-first implementation slice instead of a shell fast path

## Inputs

- one explicit question or one explicit action request
- optional transient context such as stdin, recent commands, or a named file path
- one bounded tool allowance for the current invocation
- one visible confirmation step before any mutating action runs

## Outputs

- one answer or one confirmed action result for the current invocation
- one shell-friendly interaction that can be repeated without hidden session coupling
- lower risk of accidental multi-step drift during quick operator work
- a clear handoff point when the task has outgrown the single-shot contract

## Core procedure

1. Treat the run as one bounded invocation with one explicit question or one explicit action request.
2. Attach only the transient context needed for that invocation, such as stdin, recent terminal commands, or one named file path.
3. Keep read-only question flows tool-free by default.
4. If tools are needed, allow at most one bounded tool-using step for that invocation.
5. Require an explicit confirmation gate before any file-writing or command-executing action runs.
6. End the invocation after the answer or confirmed action result instead of stretching the same run into a hidden loop.
7. Escalate to a broader workflow technique when the task now needs planning, multiple steps, or stronger verification.

## Contracts

- each invocation stays mostly independent and reproducible by default
- transient context is an input to one run, not a hidden long-lived memory layer
- read-only question flows stay tool-free unless the contract explicitly changes
- tool use is optional and bounded to one step per invocation
- mutating actions require an explicit confirmation gate
- when the task widens beyond one step, the workflow should hand off to a broader technique such as `AOA-T-0001` instead of stretching this fast path

## Risks

### Failure modes

- a supposedly single-shot invocation quietly expands into a multi-step loop with hidden state
- confirmation is bypassed or phrased so weakly that mutating actions no longer feel reviewable
- transient context grows into an implicit memory layer that changes behavior across runs

### Negative effects

- a strong fast path can tempt teams to keep using one-shot invocations after the task already needs a broader workflow
- strict one-step bounds can add friction when a repository really does need a richer plan or verification loop
- shell convenience can hide that the underlying action still carries non-trivial operational risk

### Misuse patterns

- treating repeated single-shot invocations as a substitute for explicit planning or diff review
- widening the technique into a general autonomous agent loop while still calling it stateless
- letting provider profiles, runtime integrations, or memory toggles become the real center of gravity instead of the bounded invocation contract

### Detection signals

- one invocation starts chaining several tools or mutating steps before reporting back
- operators stop distinguishing between read-only question mode and confirmed action mode
- task success now depends on hidden prior runs or implicit session context

### Mitigations

- re-narrow the workflow so each invocation answers one question or performs one confirmed step only
- keep mutating actions behind an explicit confirmation gate that is easy to audit
- route broader work into `AOA-T-0001` or another multi-step workflow instead of stretching this fast path
- treat optional history or provider-specific features as out-of-scope adjuncts unless a later sibling technique proves them reusable

## Validation

Verify the technique by confirming that:
- one invocation handles one explicit question or one explicit action request
- read-only question flows do not silently gain tool access
- tool-using action flows require explicit confirmation before mutation
- the invocation ends after one confirmed step instead of looping into hidden autonomy
- the same task can be rerun with fresh transient context and without hidden session dependence

See `checks/stateless-single-shot-agent-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact shell wrapper or CLI command name
- the source of transient context, such as stdin, recent commands, or one named file path
- the form of the confirmation gate before mutating tools run
- the provider/runtime behind the answer or tool call

What should stay invariant:
- one invocation remains mostly independent and reproducible
- read-only question flows stay distinct from confirmed action flows
- tool-using agent behavior stays single-step and confirmation-gated
- the technique remains a fast path rather than a disguised multi-step loop

Project-shaped details that should not be treated as invariant:
- provider/profile matrices
- model-selection or configuration file details
- optional history flags
- donor-specific ANSI formatting or install flows

## Public sanitization notes

This import narrows the donor repository to one agent-workflow pattern: stateless single-shot shell assistance with explicit confirmation before mutation. Provider matrices, install steps, configuration format, optional history toggles, formatting behavior, and broader product integration details were intentionally left out of the public technique contract.

## Example

See `examples/minimal-stateless-single-shot-agent.md` and `examples/confirmed-single-step-action.md`.

## Checks

See `checks/stateless-single-shot-agent-checklist.md`.

## Promotion history

- adapted from open-source `qqqa`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique focused on stateless single-shot shell assistance

## Future evolution

- split out a dedicated read-only question-only sibling if that narrower mode proves reusable on its own
- split out a dedicated confirmation-gated command execution sibling if tool-action posture becomes strong enough to stand without the rest of the fast-path contract
- add a stronger second live context if another public repository adopts the same single-shot bounded invocation model
