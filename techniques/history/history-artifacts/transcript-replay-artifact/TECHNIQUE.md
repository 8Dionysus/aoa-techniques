---
id: AOA-T-0066
name: transcript-replay-artifact
domain: history
kind: artifact
status: promoted
origin:
  project: es617/claude-replay + wesm/agentsview
  path: README.md from es617/claude-replay + README.md from wesm/agentsview
  note: Adapted from the open-source claude-replay project, with supporting second context from agentsview, to keep post-capture session history replayable as a bounded review artifact without importing the donor replay products or hosted viewer semantics.
owners:
  - 8Dionysus
tags:
  - history
  - transcript
  - replay
  - review
  - sessions
summary: Turn already-saved session history into a replayable artifact so reviewers can inspect message flow and timeline without reopening capture semantics or widening into hosted replay-platform doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0044
  - type: complements
    target: AOA-T-0053
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

# transcript-replay-artifact

## Intent

Turn already-saved session history into a replayable artifact so reviewers can inspect message flow and timeline without reopening capture semantics or widening into hosted replay-platform doctrine.

## When to use

- session artifacts already exist and reviewers need more temporal flow than a plain transcript file conveys
- demos, bug reports, audits, or teaching flows benefit from replaying the sequence of a saved session
- one bounded artifact should preserve the order and pace of a session without requiring the original runtime
- the reusable object is post-capture replay, not first-save capture, indexing, or hosted viewer product semantics

## When not to use

- the real problem is still saving session history in the first place
- a plain readable transcript is enough and replay adds no real value
- the artifact would become a hosted collaboration product, editor, or dashboard
- the workflow really needs witness-level state deltas, review flags, or broader run forensics
- replay semantics depend on product accounts, cloud sync, or a persistent hosted viewer

## Inputs

- one already-saved session or transcript artifact
- one replay renderer or equivalent transformation path
- one bounded time or message-order surface that should survive into replay
- optional redaction or sanitization posture before sharing
- one review or presentation context where replay is actually useful

## Outputs

- one replayable artifact over saved session history
- preserved message order and flow cues that are easier to inspect than raw saved files alone
- one post-capture review or demo object that remains derivative from the saved source artifacts
- one explicit separation between replay and broader hosted viewer product semantics

## Core procedure

1. Start from an already-saved session artifact rather than from live capture.
2. Transform that saved session into one replayable artifact or replay package.
3. Preserve message order and other bounded flow cues that make the session reviewable as a replay.
4. Keep references back to the underlying saved artifact or source session identity.
5. Redact or sanitize the replay package before wider sharing when the saved session is too project-shaped.
6. Treat replay as a derivative post-capture review surface rather than as the new authoritative history layer.
7. Split out transcript packaging, history indexing, witness tracing, or hosted viewer semantics when those become the real center of gravity.

## Contracts

- replay begins after session capture and does not own first-save persistence
- one replayable artifact is derivative from one or more already-saved session artifacts
- message order and bounded flow cues survive into the replay surface
- saved source artifacts remain authoritative even when replay is easier to consume
- the technique stays smaller than transcript packaging, witness trace export, local indexing, and hosted replay products
- replay does not become memory substrate, instruction authority, or collaboration-platform doctrine

Relationship to adjacent techniques: unlike [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md), this technique preserves replayable flow rather than packaging saved sessions into readable Markdown transcripts. Unlike [AOA-T-0053](../local-first-session-index/TECHNIQUE.md), it does not build a searchable lookup layer over many sessions; it turns a saved session into a replay object. Unlike [AOA-T-0045](../witness-trace-as-reviewable-artifact/TECHNIQUE.md), it does not add state deltas, review flags, or broader run-forensics semantics.

## Risks

### Failure modes

- the replay artifact quietly re-owns capture because the saved source seam disappears
- replay becomes a hosted product surface with accounts, publish flows, or shared dashboards
- reviewers confuse replay with stronger witness or proof artifacts
- the replay package drops stable links back to the saved source artifact

### Negative effects

- replay can add packaging work when a simple transcript would have been enough
- visual replay surfaces can tempt teams to prioritize polish over reviewable history
- a replay artifact can overstate fidelity if important context was removed during sanitization

### Misuse patterns

- relabeling a hosted viewer or editor product as the whole technique
- treating replay artifacts as the canonical source of truth for repo decisions or instructions
- widening the bundle into search, publishing, analytics, or hosted collaboration
- using replay where witness artifacts or plain transcripts are the actually smaller objects

### Detection signals

- the replay package cannot identify the saved source artifact it came from
- product sharing, viewer accounts, or publishing modes dominate the explanation
- reviewers expect state-delta or policy-proof semantics that the replay object does not actually provide
- teams cannot explain what replay adds beyond plain transcript text

### Mitigations

- keep one explicit seam between saved source artifacts and replay derivatives
- preserve source references in the replay package
- use transcript packaging or witness tracing when those are the real reusable objects
- split out hosted viewer or publishing behaviors instead of widening the replay contract

## Validation

Verify the technique by confirming that:
- replay starts from an already-saved session artifact
- message order or equivalent flow cues survive into the replay surface
- the replay artifact keeps stable references back to the saved source artifact
- the explanation still makes sense without hosted sharing, dashboards, or editor semantics
- the bundle stays distinct from transcript packaging, history indexing, and witness trace export

See `checks/transcript-replay-artifact-checklist.md`.

## Adaptation notes

What can vary across projects:
- the replay container format such as HTML, JSON plus assets, or another self-contained artifact
- whether timing cues are preserved exactly or as bounded step order only
- how much UI chrome is present around the replay
- whether the replay is shared locally, attached to review, or kept internal

What should stay invariant:
- replay begins after capture
- replay remains derivative from saved source artifacts
- flow cues survive well enough to make the artifact replayable
- hosted platform doctrine stays outside the invariant core

Project-shaped details that should not be treated as invariant:
- one viewer implementation
- one publish command or shared URL flow
- embedded editors, dashboards, or analytics panes
- product-specific replay controls beyond the fact that replay remains inspectable

## Public sanitization notes

This public bundle keeps only the reusable post-capture replay contract: take a saved session artifact, preserve bounded flow cues, and expose it as a replayable review object. Hosted sharing, replay editors, dashboards, publish flows, live monitoring, and wider product packaging were intentionally removed or generalized.

## Example

See `examples/minimal-transcript-replay-artifact.md`.

## Checks

See `checks/transcript-replay-artifact-checklist.md`.

## Promotion history

- adapted from open-source `es617/claude-replay` with supporting second context from `wesm/agentsview`
- landed from the Wave 1C history-lineage-governed-actions shard inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for post-capture session replay artifacts

## Future evolution

- keep [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md) as the transcript-packaging sibling rather than widening replay into text-export doctrine
- keep [AOA-T-0053](../local-first-session-index/TECHNIQUE.md) as the lookup sibling rather than turning replay into history browsing or search
- reopen a hosted replay or collaboration sibling only if it survives without dragging product-platform semantics back into this bundle
