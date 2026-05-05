---
id: AOA-T-0045
name: witness-trace-as-reviewable-artifact
domain: history
kind: artifact
status: promoted
origin:
  project: aoa-memo + aoa-playbooks
  path: docs/WITNESS_TRACE_CONTRACT.md + playbooks/witness-to-compost-pilot/PLAYBOOK.md
  note: Extracted from the witness/compost pilot where a nontrivial run leaves behind a structured witness trace and human-readable summary before any memo writeback or compost promotion happens.
owners:
  - 8Dionysus
tags:
  - history
  - witness
  - trace
  - review
  - provenance
summary: Preserve a bounded witness trace as a reviewable artifact with step visibility, state-delta notes, and human-readable summary so a nontrivial run can be inspected before any writeback or promotion without creating a new memory-object kind.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0026
  - type: complements
    target: AOA-T-0044
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# witness-trace-as-reviewable-artifact

## Intent

Preserve a nontrivial run as one reviewable witness trace artifact so humans can inspect what the run tried to do, what it actually did, where risk or failure appeared, and what should be examined next before any downstream writeback, compost promotion, or canon lift happens.

## When to use

- a run is substantial enough that one reviewable trace should survive it
- reviewers need more structured visibility than a raw transcript provides, especially around step order, tool visibility, or state deltas
- the route may later feed memory writeback, compost, or canon decisions, but first needs one bounded review artifact
- failure paths or risky transitions must stay inspectable instead of disappearing into a summary-only surface
- the reusable object is the reviewable witness artifact itself, not the whole witness runtime or playbook

## When not to use

- the main need is still session capture or transcript packaging rather than a structured witness trace
- the route mainly needs memory-object writeback, principle promotion, or canon routing logic
- the artifact would introduce a new memory-object family instead of staying a trace export
- the run is too trivial to justify a bounded witness artifact
- the draft cannot explain what the witness trace adds beyond `save sessions locally` or a plain transcript export

## Inputs

- one bounded run identity and goal
- one ordered step sequence for the witnessed run
- one redaction posture for tool inputs, outputs, and state-delta notes
- one human-readable summary format
- one review path before any writeback or promotion

## Outputs

- one reviewable witness trace artifact for the run
- one compact human-readable summary that tells a reviewer what matters most
- clearer inspection of tool use, state deltas, and failure paths than a raw transcript alone
- one explicit pre-writeback artifact that can support later memo or canon decisions without becoming memory substrate

## Core procedure

1. Bound the run tightly enough to name its identity, goal, and review scope.
2. Record one run-level witness trace with bounded status, time window, ordered steps, and review notes.
3. Preserve step-level visibility for intent, observation, tool use when present, and state delta when an external effect occurred.
4. Produce one compact human-readable summary that states what the run tried to do, what it did, where risk or review flags appeared, what survived as the main result, and what a human should inspect next.
5. Redact secret-bearing payloads or hidden chain-of-thought detail before treating the trace as shareable or reusable.
6. Preserve the witness trace as the reviewable source artifact before mapping any surviving pieces into memory objects, compost notes, or canon bundles.
7. Leave writeback, promotion, eval anchors, and role choreography to sibling layers instead of widening the trace artifact contract.

## Contracts

- `WitnessTrace` remains a trace export contract rather than a memory object
- the witness trace is the reviewable source artifact for the bounded run until other layers decide what survives beyond it
- run-level identity, goal, bounded status, time window, and ordered steps remain visible
- tool visibility and state-delta visibility stay visible when they matter for review
- failure-path preservation and redaction-first posture remain part of the invariant core
- one human-readable summary travels with the trace so a reviewer can inspect the route without parsing the whole step log first
- the technique does not own runtime witness generation, memory writeback, compost promotion, canon routing, or eval policy
- [AOA-T-0026](../session-capture-as-repo-artifact/TECHNIQUE.md) remains the capture sibling, and [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md) remains the transcript-packaging sibling

Relationship to adjacent techniques: unlike [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md), this technique preserves structured run-level and step-level trace semantics with state deltas and review flags rather than packaging selected conversations into Markdown transcripts. Unlike [AOA-T-0026](../session-capture-as-repo-artifact/TECHNIQUE.md), it does not own whether history is captured or persisted in the first place.

## Risks

### Failure modes

- the witness artifact quietly becomes a new memory-object kind because writeback mapping is not kept separate
- the trace drops tool visibility or state deltas, leaving reviewers with a record that sounds structured but hides the important parts
- the summary gets treated as proof of correctness instead of a guide to what should be inspected next
- the bundle widens into full witness runtime choreography, role contracts, or compost routing

### Negative effects

- structured traces add review overhead compared with smaller transcript or summary artifacts
- preserving every witnessed step can create noise when the run was not actually substantial enough
- state-delta visibility can become burdensome if redaction posture is weak
- a strong witness artifact can tempt teams to treat the trace like durable memory authority

### Misuse patterns

- relabeling runtime witness capture or full playbook behavior as the technique
- using the witness trace as the canonical repository policy or instruction surface
- widening the bundle into memory-object writeback or compost-promotion doctrine
- keeping raw secret-bearing payloads or hidden chain-of-thought dumps in the trace

### Detection signals

- contributors talk about `episode`, `decision`, or other memo objects as if they were still the same artifact as the witness trace
- trace artifacts arrive without visible tool use, state deltas, or failure-path detail
- reviewers cannot tell what should be inspected next from the summary
- route discussions drift toward agent roles, deep recall, or eval enforcement rather than reviewable trace export

### Mitigations

- keep one explicit seam between witness trace export and every later writeback or promotion layer
- require visible run identity, ordered steps, and summary posture before calling the artifact a witness trace
- apply redaction-first discipline before sharing or publication
- use transcript packaging, summaries, or decision notes when those are the true smaller objects
- split out route choreography, eval anchors, or writeback policy instead of widening this artifact contract

## Validation

Verify the technique by confirming that:
- the artifact names the bounded run and its goal
- step order, tool visibility, and state deltas remain visible where they matter
- one compact human-readable summary tells a reviewer what happened and what to inspect next
- redaction-first handling removes secret-bearing payloads and hidden chain-of-thought detail
- the bundle stays distinct from capture, transcript packaging, memory objects, and promotion routes

See `checks/witness-trace-as-reviewable-artifact-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact artifact format such as JSON plus Markdown or another paired export
- the level of step granularity
- the naming convention for witness files
- whether the trace is committed directly or attached to a review surface first

What should stay invariant:
- the artifact remains a trace export, not a memory object
- the run stays bounded and reviewable
- human-readable summary travels with the trace
- later writeback or promotion layers remain separate

Project-shaped details that should not be treated as invariant:
- donor role names such as `architect`, `coder`, `reviewer`, or `memory-keeper`
- specific eval anchor names
- memo taxonomy mapping details beyond the fact that writeback is separate
- exact pilot artifact names such as `compost_note` or `canon_bundle`

## Public sanitization notes

This public bundle keeps only the reusable reviewable-trace contract: run identity, bounded steps, tool visibility, state deltas, review notes, and compact summary survive as one artifact before any later writeback. Donor-specific role choreography, deep-recall posture, eval anchors, and compost promotion behavior were intentionally removed or generalized.

## Example

See `examples/minimal-witness-trace-as-reviewable-artifact.md`.

## Checks

See `checks/witness-trace-as-reviewable-artifact-checklist.md`.

## Promotion history

- extracted from `aoa-memo` and `aoa-playbooks`
- promoted to `aoa-techniques` on 2026-03-23 as a bounded history technique for reviewable witness trace export

## Future evolution

- keep [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md) as the transcript sibling rather than widening this bundle into generic transcript packaging
- keep memory writeback policy in `aoa-memo` rather than reopening a memory-object seam here
- add a second live context if another route family uses the same reviewable witness artifact without the full witness/compost pilot
