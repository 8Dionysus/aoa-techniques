---
id: AOA-T-0033
name: decision-rationale-recording
domain: docs
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-adr-write/SKILL.md
  note: Extracted from a bounded decision-recording practice that keeps meaningful choices reviewable without expanding into source-of-truth governance or architecture taxonomy.
owners:
  - 8Dionysus
tags:
  - docs
  - decision
  - rationale
  - reviewable
summary: Keep one meaningful decision in a reviewable note with context, options, rationale, and consequences while staying out of source-of-truth governance and architecture taxonomy.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-22
export_ready: true
relations: []
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# decision-rationale-recording

## Intent

Record one meaningful decision in a compact, reviewable note that preserves context, options, rationale, and consequences without widening into source-of-truth governance or architecture taxonomy.

## When to use

- a real choice has been made and the reason needs to stay reviewable
- multiple viable options were considered and the tradeoff matters
- the decision should be understandable without recreating the full discussion
- the note needs to be public-safe, bounded, and easy to audit later

## When not to use

- trivial obvious edits that do not deserve a decision note
- tasks whose real need is source-of-truth clarification
- boundary mapping, document-role assignment, or architecture taxonomy work
- cases where no decision exists yet and the next step is still discovery
- changes that only need a short status update or implementation comment

## Inputs

- one bounded decision subject
- the viable options considered
- the constraints that shaped the choice
- the intended consequence or follow-up of the chosen path
- any context that future reviewers would need to understand the rationale

## Outputs

- one concise decision note
- an explicit decision statement
- the context that led to the decision
- the alternatives considered and why they were not chosen
- the consequences, tradeoffs, or guardrails that follow from the decision

## Core procedure

1. Name the decision in one sentence before expanding into detail.
2. Capture the minimum context needed to understand why the choice was necessary.
3. List the real alternatives that were considered.
4. State the chosen option and the rationale for selecting it.
5. Record the expected consequences, follow-up work, or limits of the decision.
6. Sanitize the note so it stays public-safe and does not expose private detail.
7. Keep the note focused on one decision; split the content if it contains several unrelated choices.

## Contracts

- the note must preserve context, options, rationale, and consequences
- the note must stay bounded to one decision rather than a broader policy or taxonomy map
- the note must reject trivial obvious edits that do not need durable rationale
- the note must not turn into source-of-truth governance, boundary mapping, or architecture classification
- the note must remain readable as a decision record even when the reviewer does not know the origin project

## Risks

### Failure modes

- the note captures a summary but not the actual decision tradeoff
- the write-up drifts into governance language instead of decision rationale
- several unrelated choices get merged into one oversized record

### Negative effects

- extra documentation can slow very small changes if the decision was not actually meaningful
- over-recording every edit can bury the few decisions that matter
- too much taxonomy can obscure the practical reason the decision existed

### Misuse patterns

- using the technique for tiny obvious edits that do not need a rationale note
- using it to decide where truth should live instead of recording the decision itself
- turning the note into boundary mapping, schema design, or architecture classification
- writing a generic changelog entry and calling it a decision record

### Detection signals

- the note does not make clear why one option won
- reviewers still cannot tell what changed after reading the record
- the content starts naming canonical homes or repository roles instead of the decision
- the note reads like a taxonomy exercise instead of a bounded rationale

### Mitigations

- require an explicit decision statement near the top of the note
- keep options and consequences visible in plain language
- split unrelated choices into separate records
- route source-of-truth and boundary questions to a different technique

## Validation

Verify the technique by confirming that:
- one real decision is named clearly
- context, options, rationale, and consequences are all visible
- the note does not drift into source-of-truth clarification or boundary mapping
- trivial obvious edits are rejected as out of scope
- a reviewer could understand the tradeoff without reopening the entire discussion

See `checks/decision-rationale-recording-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact note format
- whether consequences are framed as risks, follow-ups, or commitments
- the amount of context needed for a future reviewer
- whether the decision is documented in a dedicated file or a section of a larger review surface

What should stay invariant:
- one meaningful decision is captured per record
- context, options, rationale, and consequences stay explicit
- the note remains bounded and reviewable
- the technique stays out of source-of-truth governance and architecture taxonomy

## Public sanitization notes

This public version keeps only the reusable decision-recording pattern. Project-specific identifiers, local planning details, and private discussion threads were removed so the bundle can be reviewed and reused without origin-project access.

## Example

See `examples/minimal-decision-rationale-note.md`.

## Checks

See `checks/decision-rationale-recording-checklist.md`.

## Promotion history

- extracted from `aoa-skills`
- promoted to `aoa-techniques` on 2026-03-22 as a bounded docs technique

## Future evolution

- add a sibling technique if decision records need stronger linkage to follow-up action tracking
- add a compact template for multi-option decisions if the single-decision pattern is not enough
