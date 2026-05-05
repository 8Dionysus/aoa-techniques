---
id: AOA-T-0026
name: session-capture-as-repo-artifact
domain: history
kind: artifact
status: promoted
origin:
  project: getspecstory
  path: README.md
  note: Adapted from the open-source SpecStory CLI, which saves AI coding sessions locally into project-scoped `.specstory/history/` artifacts instead of treating them as transient chat only.
owners:
  - 8Dionysus
tags:
  - history
  - sessions
  - artifacts
  - local-first
  - transcripts
summary: Capture AI coding sessions as versioned repo artifacts so project history stays searchable, reviewable, and reusable without turning session logs into memory or instruction policy.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0002
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

# session-capture-as-repo-artifact

## Intent

Preserve AI coding sessions as explicit project-scoped history artifacts so useful reasoning, decisions, and traces stay reviewable after the session ends instead of disappearing into a transient chat window.

## When to use

- repositories that want local-first session history to remain searchable and shareable as project artifacts
- workflows that need an inspectable record of AI-assisted development sessions across tools or terminals
- teams that want session capture to support audit, replay, reuse, or later distillation without requiring cloud sync
- cases where session history should be stored as versioned artifacts rather than as hidden product memory

## When not to use

- systems whose main reusable object is long-term memory retrieval, recall ranking, or memory-object storage
- workflows that want session transcripts to become the canonical source of truth for instructions or policy
- repositories where the real need is intent/progress summaries rather than raw or near-raw session capture
- cases where captured history cannot be sanitized or safely persisted as public-facing artifacts

## Inputs

- one project-scoped location for saved session artifacts
- one capture path that writes sessions as files or equivalent repo-visible artifacts
- one local-first retention policy
- one review path for later summarization, reuse, or selective sharing
- one boundary that keeps session history separate from memory or instruction authority

## Outputs

- one persistent session-history artifact layer inside the project
- one more reviewable trail of AI-assisted work across sessions and tools
- lower risk that useful session context disappears once a terminal or editor tab closes
- a bounded history surface that can later feed summaries, audits, or reuse without becoming memory substrate

## Core procedure

1. Choose one project-scoped home for session artifacts before broadening capture behavior.
2. Save each session into that local history area as a versioned artifact instead of leaving it only in transient UI state.
3. Keep the capture path local-first so project history exists even without optional cloud or external indexing services.
4. Preserve enough structure that a later reader can inspect, summarize, or share the session without reconstructing it from memory.
5. Treat the captured session as a history artifact, not as the new source of truth for instructions, rules, or memory recall behavior.
6. Layer summaries, insights, or sharing paths on top of the artifacts only after the artifact contract itself is stable.
7. Split out separate techniques if memory retrieval, history-to-instructions generation, or cloud sync becomes the real reusable object.

## Contracts

- session history stays project-scoped and artifact-based
- local persistence remains available without requiring cloud sync
- captured sessions stay reviewable as history, not as hidden runtime memory
- the artifact layer can support later audit, replay, summary, or selective sharing
- the technique does not own memory recall semantics, vector retrieval, or universal instruction authority
- the captured history does not become the canonical source of truth for repository policy or active instructions

## Risks

### Failure modes

- session artifacts quietly become the de facto instruction source because no stronger authored source stays visible
- local history capture becomes too noisy or too raw to review safely, so teams stop trusting it
- repositories keep sensitive or over-project-shaped session data without enough sanitization discipline

### Negative effects

- persistent session capture can create review overhead when teams really only need short summaries or decisions
- keeping rich transcripts locally can increase storage and hygiene burden
- a strong history layer can tempt teams to treat session archives like memory substrate or policy logs

### Misuse patterns

- widening the technique into vector memory, search ranking, or recall orchestration
- using session captures as universal instructions for future agents without distillation or review
- equating optional cloud sync or analytics with the core reusable contract

### Detection signals

- project rules start pointing to session history instead of maintained authored docs
- teams cannot explain which parts of captured history are safe to share or reuse
- local-first history is no longer usable without cloud services or other external systems

### Mitigations

- keep one explicit boundary between session artifacts, authored instructions, and any later memory systems
- sanitize or selectively share history artifacts instead of treating every raw session as portable by default
- keep cloud sync, analytics, and history-to-instructions generation as separate layers outside this technique
- route memory-object or recall behavior into `aoa-memo` or later sibling techniques instead of widening this contract

## Validation

Verify the technique by confirming that:
- session history is saved as project-scoped artifacts
- the local artifact path remains useful even without cloud sync
- a reviewer can inspect or summarize the artifact later without hidden runtime state
- the artifact layer does not replace authored instructions or decision docs
- memory recall, retrieval, and instruction-policy behavior remain outside this bounded contract

See `checks/session-capture-as-repo-artifact-checklist.md`.

## Adaptation notes

What can vary across projects:
- the folder name used for history artifacts
- the session file format
- whether artifacts are captured from one tool or several
- the retention, pruning, or sharing workflow

What should stay invariant:
- sessions are persisted as project-scoped artifacts
- local-first history remains available without requiring cloud sync
- history stays a reviewable artifact layer rather than memory substrate
- the technique remains about capture and artifact discipline, not retrieval or instruction authority

Project-shaped details that should not be treated as invariant:
- cloud sync product behavior
- search UI or web dashboards
- history-derived skills or summaries
- provider-specific wrapper commands

## Public sanitization notes

This import narrows the donor repository to one history pattern: local-first session capture into project-scoped repo artifacts. Cloud sync, search UX, history-derived skills, history-to-instructions generation, and cross-session memory semantics were intentionally left out of the public technique contract.

## Example

See `examples/minimal-session-capture-as-repo-artifact.md` and `examples/concrete-local-first-session-history.md`.

## Checks

See `checks/session-capture-as-repo-artifact-checklist.md`.

## Promotion history

- adapted from open-source `getspecstory`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique for local-first session history artifacts

## Future evolution

- split out a dedicated history-to-summary sibling if reusable summarization flows prove stable beyond raw artifact capture
- split out a dedicated history-to-instructions sibling if distilled instruction generation becomes reusable without widening memory semantics
- add a stronger second live context if another public repository adopts the same local-first session-artifact contract
