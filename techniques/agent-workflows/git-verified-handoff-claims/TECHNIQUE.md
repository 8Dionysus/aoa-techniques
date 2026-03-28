---
id: AOA-T-0059
name: git-verified-handoff-claims
domain: agent-workflows
status: promoted
origin:
  project: thebasedcapital/nightcrawler + jeremiah-k/agor
  path: README.md + skills/nightcrawler-episode.md + docs/snapshots.md
  note: Adapted from Nightcrawler's mandatory git cross-check before continuing from handoff, reinforced by AGOR's snapshot-receiver verification posture, to keep handoff trust anchored to visible repo state.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - handoff
  - git
  - verification
  - continuation
summary: Verify concrete handoff claims against visible git state before continuation so the next session trusts repo evidence rather than memory or summary prose alone.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0057
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

# git-verified-handoff-claims

## Intent

Verify concrete handoff claims against visible git state before continuation so the next session trusts reviewable repo evidence rather than memory, optimism, or summary prose alone.

## When to use

- a handoff packet claims that code, files, or commits changed and the next session will rely on that claim
- the receiving side can inspect local git evidence such as recent commits, diffs, or branch state
- continuation should start from what the repo actually shows rather than what the handoff merely says
- the reusable object is one bounded handoff-verification seam, not general code review or provenance infrastructure

## When not to use

- there is no git-backed worktree or the relevant change is not represented in visible repo state
- the handoff is purely conceptual and makes no concrete code or commit claims
- the workflow needs a fuller witness artifact, review loop, or provenance framework rather than one handoff check
- packet authoring or receipt confirmation are the real missing seams

## Inputs

- one handoff packet with concrete claims, references, or file anchors
- one visible local git state such as recent commits, current diff, or branch head
- one continuation boundary where trust in the handoff should be checked before work resumes

## Outputs

- one explicit verification result for the concrete handoff claims
- one visible set of matches, mismatches, or unverifiable claims anchored to git evidence
- lower risk that the next session continues from hallucinated or stale progress claims

## Core procedure

1. Read the handoff packet and isolate the claims that describe concrete repo changes or current code state.
2. Inspect visible git evidence such as recent commits, current diff, branch head, or file status relevant to those claims.
3. Compare each concrete claim against the repo evidence instead of trusting the handoff summary on its own.
4. Record which claims are verified, which mismatch the repo, and which remain unverifiable from the available git state.
5. Continue from the verified repo-backed understanding rather than from the original handoff wording alone.
6. Keep the verification seam narrow enough that it remains one handoff-truth check rather than a full review workflow, witness trace, or provenance framework.
7. Route packet authoring, receipt semantics, baseline testing, and broader review policy to sibling techniques when they become the real center of gravity.

## Contracts

- concrete handoff claims are checked against visible git evidence before continuation
- the verification output distinguishes verified, mismatched, and unverifiable claims explicitly
- the git evidence used for the check stays reviewable enough that another reader can understand the verdict
- continuation trusts repo-backed state over handoff narration when they diverge
- the technique stays smaller than generic code review, witness artifacts, and broad provenance doctrine

Relationship to adjacent techniques: unlike [AOA-T-0057](../structured-handoff-before-compaction/TECHNIQUE.md), this technique does not create the handoff packet; it verifies packet claims after the packet already exists. Unlike [AOA-T-0058](../receipt-confirmed-handoff-packet/TECHNIQUE.md), it does not record that a receiver accepted the handoff; it checks whether the handoff's concrete repo claims are true. Unlike [AOA-T-0045](../../history/witness-trace-as-reviewable-artifact/TECHNIQUE.md), it does not preserve a fuller run artifact with ordered steps and state deltas. It also stays smaller than a generic code-review workflow because it only verifies handoff claims that matter for immediate continuation.

## Risks

### Failure modes

- stale local git state produces a false sense of verification
- the handoff claims are too vague to compare meaningfully against repo evidence
- verification checks only one commit or file and misses the claim that actually matters

### Negative effects

- the workflow can gain extra ceremony when the handoff is simple enough that direct file inspection would suffice
- teams may overtrust the verification note and skip broader testing or review that the change still needs
- the seam can drift toward a generic review workflow if every code change is routed through it

### Misuse patterns

- treating git verification as a substitute for writing a real handoff packet
- treating any recent commit activity as proof that the specific handoff claim is true
- widening the bundle into generic code review, provenance logging, or full review-policy doctrine

### Detection signals

- handoff claims mention progress but do not name files, commits, or other repo anchors
- the verification output cannot say which git evidence was checked
- mismatches are silently ignored and continuation still follows the original handoff narrative
- discussions shift toward total review coverage instead of the bounded trust check before continuation

### Mitigations

- require concrete file, commit, or diff anchors in claims that need verification
- record the exact git evidence used for each verdict
- keep mismatches and unverifiable claims explicit
- separate this seam from packet authoring, receipt confirmation, baseline testing, and broader review policy

## Validation

Verify the technique by confirming that:
- at least one concrete handoff claim can be tied to visible git evidence
- the verification result names the evidence used and the verdict reached
- mismatches or unverifiable claims remain explicit instead of being silently treated as true
- continuation can be explained from the verification output without appealing to hidden memory
- the explanation still makes sense without a full review framework or witness-artifact doctrine

See `checks/git-verified-handoff-claims-checklist.md`.

## Adaptation notes

What can vary across projects:
- which git evidence is primary, such as `git log`, `git diff`, status, or file-by-file inspection
- how many recent commits or diffs are checked
- whether the verification result is appended to the handoff, written separately, or logged in another reviewable surface
- whether unverifiable claims block continuation or simply stay flagged
- whether the same agent or a later agent performs the check

What should stay invariant:
- the check happens before continuation trusts the handoff claims
- concrete claims are compared against visible repo state
- mismatches and unverifiable claims stay explicit
- verified understanding is anchored to the repo, not to memory

Project-shaped details that should not be treated as invariant:
- one fixed command like `git log --oneline -5`
- one handoff file path or orchestrator runtime
- one snapshot log such as `.agor/agentconvo.md`
- one branch naming scheme, review queue, or CI gate
- broader provenance tracking or review-policy layers

## Public sanitization notes

This import narrows the donors to one bounded pattern: before continuing from a handoff, compare its concrete repo claims against visible git state and carry mismatches forward explicitly. Orchestrator loops, snapshot tooling, coordination logs, broader review workflows, and provenance or policy systems were intentionally left out of the public contract.

## Example

See `examples/minimal-git-verified-handoff-claims.md`.

## Checks

See `checks/git-verified-handoff-claims-checklist.md`.

## Promotion history

- adapted from open-source `thebasedcapital/nightcrawler` with supporting snapshot-receiver verification posture from `jeremiah-k/agor`
- staged through the chat wave 3 handoff-bounded-continuation lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for repo-backed verification of handoff claims before continuation

## Future evolution

- keep packet authoring separate instead of widening this bundle back into handoff-writing doctrine
- keep receipt semantics separate instead of treating verification as proof that the handoff was accepted
- keep broader review and provenance layers separate instead of turning this seam into generic code-review governance
