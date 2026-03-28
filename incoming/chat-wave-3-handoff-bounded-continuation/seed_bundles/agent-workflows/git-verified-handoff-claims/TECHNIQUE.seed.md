---
id: AOA-T-XXXX
name: git-verified-handoff-claims
domain: agent-workflows
status: draft-seed
origin: chat-wave-3-handoff-bounded-continuation
note: seed bundle staged for operator-guided chat wave 3 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - handoff-bounded-continuation
summary: Verify handoff claims against recent git evidence so continuation relies on reviewable repo state rather than memory alone.
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
# git-verified-handoff-claims

## Intent

Check handoff claims against recent git evidence so the receiving side can verify what actually changed before continuing work.

## When to use

- a handoff packet references code or commit state
- continuation depends on trusting recent repo changes
- git evidence is available locally

## When not to use

- there is no git-backed worktree to verify against
- the handoff is purely conceptual with no code claims
- the flow would collapse into generic code review doctrine

## Inputs

- handoff claim set
- recent commits or diffs
- target repository state

## Outputs

- verified or rejected handoff claims
- explicit mismatch notes
- continuation decision with repo-backed evidence

## Core procedure

1. read the handoff claims
2. inspect recent commits or diffs
3. compare claims against repo evidence
4. record matches and mismatches explicitly
5. continue only with the verified understanding

## Contracts

- repo evidence is checked before continuation
- mismatches stay visible
- the technique stays smaller than generic code review
- handoff trust is anchored to visible git state

## Risks

### Failure modes

- stale local git state leads to false verification
- vague claims cannot be checked meaningfully

### Negative effects

- operators over-trust unverified summaries
- the technique drifts into general review workflow doctrine

### Misuse patterns

- using git verification as a replacement for the handoff packet
- marking unverifiable claims as implicitly true

### Detection signals

- claims lack commit or file anchors
- verification output cannot name the evidence used

### Mitigations

- require concrete claim anchors
- record the exact repo evidence checked
- separate handoff verification from broad review policy

## Validation

- confirm claims can be tied to visible git evidence
- confirm mismatches are reported explicitly
- verify continuation logic is explainable from the verification output

## Adaptation notes

- git range choice
- mismatch reporting
- repo state assumptions
- handoff packet format

## Public sanitization notes

Remove donor-specific workflow or platform language. Keep only the bounded git-backed claim verification contract.

## Example

See `examples/git_verification.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 3 verification cluster

## Future evolution

- verification receipts
- mismatch severity notes
- bounded retry rules
