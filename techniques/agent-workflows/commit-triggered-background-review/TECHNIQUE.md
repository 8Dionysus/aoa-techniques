---
id: AOA-T-0051
name: commit-triggered-background-review
domain: agent-workflows
status: promoted
origin:
  project: roborev-dev/roborev
  path: cmd/roborev/postcommit.go
  note: Adapted from the open-source roborev project, which enqueues a background review after a visible commit boundary and keeps findings inspectable before any later fix loop.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - review
  - commit
  - background
  - findings
summary: Trigger a bounded background review after a commit so findings survive as inspectable artifacts without widening into autonomous merge, rewrite, or CI governance.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-27
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

# commit-triggered-background-review

## Intent

Launch a bounded review pass after a visible commit boundary and preserve the result as a review artifact so findings can be inspected before any later remediation, merge, or policy action.

## When to use

- commits are the cleanest review trigger in the workflow
- review should happen asynchronously from the commit itself
- findings need to remain inspectable before any follow-up action
- the workflow wants commit-bound review coverage without turning the review surface into full CI governance

## When not to use

- the workflow expects interactive pair review rather than artifact output
- the system would auto-apply code changes, auto-merge, or auto-close policy state in the same technique
- the trigger needs to cover every repository event rather than a commit boundary
- the main reusable object is findings compaction or remediation rather than the commit-bound review run

## Inputs

- one visible commit or diff target
- one bounded review scope
- one background runner or queue surface
- optional severity or policy hints that do not replace human inspection

## Outputs

- one background review artifact tied to the triggering commit
- findings with code references or equivalent review handles
- one explicit signal that review ran after the commit boundary
- one separation between review production and any later remediation path

## Core procedure

1. Detect a new commit boundary.
2. Enqueue or launch a bounded background review against that commit or its delta.
3. Preserve the resulting findings as a read-only review artifact tied to the triggering commit.
4. Surface enough commit identity and scope information for later reviewers to understand what was reviewed.
5. Keep follow-up actions such as fixing, merging, or policy changes outside the review run itself.
6. Revalidate or rerun review later if the code has moved beyond the triggering commit.
7. Stop widening the technique when the workflow starts needing remediation loops, queue compaction, or full CI governance.

## Contracts

- review runs after a visible commit boundary
- findings remain inspectable artifacts rather than hidden transient output
- the artifact can be tied back to the commit or diff that triggered it
- the technique does not merge, rewrite, or close state automatically
- background execution stays smaller than full CI governance
- remediation and compaction remain separate sibling concerns

Relationship to adjacent techniques: unlike `AOA-T-0001`, this technique does not own the broader change protocol around planning, diff review, verification, and reporting. It owns one asynchronous post-commit review trigger plus an inspectable findings artifact.

## Risks

### Failure modes

- stale findings outlive the code they reviewed
- background timing hides the relation to the triggering commit
- the review artifact becomes detached from its scope or commit identity

### Negative effects

- operators can confuse a review artifact with final truth
- asynchronous review can create lag between commit and inspection
- teams can overtrust the background loop and neglect explicit follow-up review

### Misuse patterns

- attaching auto-fix, auto-merge, or auto-rewrite behavior to the same technique
- widening the trigger to every repository event
- treating one background review run as if it were already CI governance or policy enforcement

### Detection signals

- findings cannot be tied back to a commit or diff
- review output mutates code or policy state directly
- reviewers cannot tell whether the artifact reflects current code or an older commit
- queue behavior becomes more important than the bounded review artifact itself

### Mitigations

- keep commit references in the artifact
- separate review from remediation and merge actions
- revalidate findings before acting on them
- split queue, compaction, and policy surfaces into narrower sibling techniques

## Validation

Verify the technique by confirming that:
- the review artifact names the triggering commit or diff
- findings survive as read-only output
- no automatic merge or rewrite path is implied
- a reviewer can tell what scope was reviewed
- stale findings are detectable and can be rerun or revalidated later

See `checks/commit-triggered-background-review-checklist.md`.

## Adaptation notes

What can vary across projects:
- commit source
- background runner choice
- findings severity format
- artifact retention path
- how the artifact is surfaced to later reviewers

What should stay invariant:
- the trigger is a visible commit boundary
- review happens asynchronously from the commit itself
- findings survive as an inspectable artifact
- remediation stays separate from the review run

Project-shaped details that should not be treated as invariant:
- one daemon or queue implementation
- one TUI or dashboard surface
- one fix-loop or refine-loop workflow
- provider-specific prompt or agent wiring

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: post-commit background review that emits an inspectable findings artifact. Auto-fix loops, refine iterations, queue UI, alerting hooks, broader event automation, and donor runtime specifics were intentionally left out of the public contract.

## Example

See `examples/minimal-commit-triggered-background-review.md`.

## Checks

See `checks/commit-triggered-background-review-checklist.md`.

## Promotion history

- adapted from open-source `roborev-dev/roborev`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-27 as a bounded external-import technique for commit-bound asynchronous review artifacts

## Future evolution

- keep findings compaction as a separate sibling instead of widening this bundle into stale-finding cleanup
- keep remediation loops separate instead of collapsing review and fix into one technique
- add a stronger second live context if another public repository uses post-commit background review in practice
