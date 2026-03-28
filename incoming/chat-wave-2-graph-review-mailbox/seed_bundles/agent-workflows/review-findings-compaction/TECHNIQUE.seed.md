---
id: AOA-T-XXXX
name: review-findings-compaction
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
summary: Compact and revalidate review findings so repeated or stale findings do not overwhelm current review surfaces.
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
# review-findings-compaction

## Intent

Turn a noisy or repeated findings set into a smaller current review surface by deduping, merging, and revalidating against the latest code.

## When to use

- repeated review runs produce overlapping findings
- stale findings need to be filtered out
- reviewers need one tighter current view

## When not to use

- the problem is issue triage rather than review findings
- findings should stay fully expanded for legal or audit reasons
- there is no way to revalidate against current code

## Inputs

- findings from one or more review passes
- current code or diff target
- optional severity or confidence signals

## Outputs

- compacted findings set
- stale findings removed or marked
- current review artifact with less duplication

## Core procedure

1. collect the current findings set
2. group likely duplicates
3. revalidate each group against the current code state
4. keep one current representative where the issue still holds
5. drop or mark stale findings explicitly

## Contracts

- compaction never invents new findings
- current code is checked before a finding survives
- stale findings do not silently persist as current truth
- the technique stays smaller than generic issue management

## Risks

### Failure modes

- real distinct findings are merged incorrectly
- stale findings survive because revalidation is weak

### Negative effects

- reviewers lose nuance from over-aggressive compaction
- current review trust drops when stale findings remain

### Misuse patterns

- using compaction to hide uncomfortable findings
- widening the technique into issue backlog policy

### Detection signals

- compacted artifacts still contain many exact duplicates
- merged findings cite mismatched code locations

### Mitigations

- keep original references during grouping
- re-check code locations before carrying findings forward
- separate compaction from prioritization

## Validation

- confirm duplicate findings collapse into one representative
- confirm invalidated findings are removed or marked stale
- verify current references still point to live code

## Adaptation notes

- duplicate grouping rules
- revalidation method
- artifact output shape
- severity preservation

## Public sanitization notes

Remove donor-specific review product behavior. Keep only the bounded compaction and revalidation contract.

## Example

See `examples/compacted_findings.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 review loop cluster

## Future evolution

- confidence-aware grouping
- stale finding tombstones
- compaction diffs
