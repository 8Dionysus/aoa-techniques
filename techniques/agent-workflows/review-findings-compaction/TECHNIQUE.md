---
id: AOA-T-0052
name: review-findings-compaction
domain: agent-workflows
kind: handoff
status: promoted
origin:
  project: roborev-dev/roborev
  path: cmd/roborev/compact.go
  note: Adapted from the open-source roborev project, which verifies and consolidates open review findings against the current codebase before later fix loops act on them.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - review
  - findings
  - compaction
  - revalidation
summary: Compact and revalidate review findings against current code so repeated or stale findings do not overwhelm the current review surface.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-27
export_ready: true
relations:
  - type: complements
    target: AOA-T-0051
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

# review-findings-compaction

## Intent

Turn a noisy or repeated findings set into a smaller current review surface by deduping, merging, and revalidating findings against the latest code instead of treating every historical finding as still current.

## When to use

- repeated review runs produce overlapping findings
- stale findings need to be filtered out before acting on them
- reviewers need one tighter current view instead of several partially duplicated review artifacts
- the workflow wants a quality layer between review production and remediation

## When not to use

- the main problem is issue triage or backlog policy rather than review findings
- findings must remain fully expanded for legal, audit, or forensics reasons
- there is no way to revalidate against current code
- the real reusable object is the post-commit trigger rather than the consolidation pass

## Inputs

- findings from one or more review passes
- current code or diff target
- original review references
- optional severity or confidence signals that do not replace revalidation

## Outputs

- one compacted findings set
- stale findings removed or explicitly marked
- one current review artifact with less duplication
- one cleaner handoff surface for later remediation or human review

## Core procedure

1. Collect the current findings set from one or more review artifacts.
2. Group likely duplicates or closely related findings.
3. Revalidate each group against the current code state.
4. Keep one current representative where the issue still holds.
5. Drop or mark findings that no longer reproduce against the current code.
6. Preserve enough original references for a reviewer to understand where grouped findings came from.
7. Stop widening the technique when the workflow starts needing backlog policy, remediation automation, or generic issue management.

## Contracts

- compaction never invents new findings
- current code is checked before a finding survives as current truth
- stale findings do not silently persist as current truth
- duplicate grouping stays explainable and reviewable
- original finding references remain traceable even after grouping
- the technique stays smaller than generic issue management or remediation workflow design

Relationship to adjacent techniques: unlike `AOA-T-0051`, this technique does not own the commit-triggered background review run that produced the findings. It owns the later verification-and-consolidation pass that reduces duplicate or stale findings before human action or remediation.

## Risks

### Failure modes

- real distinct findings are merged incorrectly
- stale findings survive because revalidation is weak
- important nuance disappears in over-aggressive grouping

### Negative effects

- reviewers can lose context if compaction becomes too aggressive
- trust drops when a compacted surface still carries stale findings
- the compacted artifact can look more authoritative than the revalidation process really was

### Misuse patterns

- using compaction to hide uncomfortable findings
- widening the technique into issue backlog policy
- treating compaction as if it were already remediation or policy enforcement

### Detection signals

- compacted artifacts still contain many exact duplicates
- merged findings cite mismatched code locations
- reviewers cannot trace a representative finding back to its source findings
- grouped findings mix issues that do not share one underlying defect

### Mitigations

- keep original references during grouping
- re-check code locations before carrying findings forward
- separate compaction from prioritization and remediation
- keep false-positive or stale markers explicit when a finding drops out

## Validation

Verify the technique by confirming that:
- duplicate findings collapse into one representative
- invalidated findings are removed or marked stale
- current references still point to live code
- grouped findings remain traceable back to their source findings
- the compacted artifact stays a review surface, not a remediation or issue-management system

See `checks/review-findings-compaction-checklist.md`.

## Adaptation notes

What can vary across projects:
- duplicate grouping rules
- revalidation method
- artifact output shape
- severity preservation
- stale-finding marker format

What should stay invariant:
- revalidation happens against current code before a finding survives
- compaction reduces duplication rather than inventing new findings
- stale findings are removed or marked explicitly
- traceability back to original findings remains possible

Project-shaped details that should not be treated as invariant:
- one daemon or queue implementation
- one synthesis prompt or model
- one review dashboard or comment format
- backlog or issue-triage behavior

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: verify and consolidate open review findings against the current codebase so the active review surface stays smaller and fresher. Post-commit triggers, fix loops, queue UI, broader issue management, and donor runtime specifics were intentionally left out of the public contract.

## Example

See `examples/minimal-review-findings-compaction.md`.

## Checks

See `checks/review-findings-compaction-checklist.md`.

## Promotion history

- adapted from open-source `roborev-dev/roborev`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-27 as a bounded external-import technique for findings verification and consolidation

## Future evolution

- keep the trigger-and-artifact loop in `AOA-T-0051` instead of folding it into this bundle
- keep remediation or fix loops separate instead of letting compaction become action policy
- add a stronger second live context if another public repository uses findings compaction and revalidation in practice
