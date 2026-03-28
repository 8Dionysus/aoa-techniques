---
id: AOA-T-XXXX
name: commit-triggered-background-review
domain: agent-workflows
status: draft-seed
origin: chat-wave-2-graph-review-mailbox
note: seed bundle staged for operator-guided chat wave 2 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - graph-review-mailbox
summary: Trigger a bounded background review after commits so review findings stay artifact-based and inspectable.
maturity_score: 1
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: donor_soil
export_ready: false
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.seed.md
---
# commit-triggered-background-review

## Intent

Launch a bounded review pass after a commit and publish findings as a review artifact without widening into autonomous merge or unsupervised rewriting.

## When to use

- commits are the clean review trigger
- review should happen asynchronously
- findings need to remain inspectable before any follow-up action

## When not to use

- the workflow expects interactive pair review instead of artifact output
- the system would auto-apply changes without human review
- the trigger is broader than a commit boundary

## Inputs

- recent commit or diff target
- review scope
- optional policy or severity thresholds

## Outputs

- background review artifact
- findings with code references
- explicit signal that review ran after the commit boundary

## Core procedure

1. detect a new commit boundary
2. launch a bounded review pass against that delta
3. emit findings as an artifact
4. keep follow-up separate from the review run itself
5. require a later human or bounded workflow step for any action

## Contracts

- review runs after a visible commit boundary
- findings remain reviewable artifacts
- the technique does not merge or rewrite code automatically
- background execution stays smaller than full CI governance

## Risks

### Failure modes

- stale findings outlive the code they reviewed
- background timing hides the relation to the triggering commit

### Negative effects

- operators confuse review artifacts with verdict-final truth
- unsupervised follow-up sneaks in behind the review surface

### Misuse patterns

- attaching auto-fix behavior to the same technique
- widening the trigger to every repository event

### Detection signals

- findings cannot be tied back to a commit or diff
- review output mutates code or policy state directly

### Mitigations

- keep commit references in the artifact
- separate review from remediation
- revalidate findings before acting on them

## Validation

- confirm the review artifact names the triggering commit
- confirm findings survive as read-only output
- verify no automatic merge or rewrite path is implied

## Adaptation notes

- commit source
- background runner choice
- finding severity format
- artifact retention path

## Public sanitization notes

Remove donor-specific deployment and product UX. Keep only the commit-bound review artifact contract.

## Example

See `examples/review_artifact.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 review loop cluster

## Future evolution

- retry rules
- artifact expiration notes
- bounded revalidation hooks
