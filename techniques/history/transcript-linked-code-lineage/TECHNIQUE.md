---
id: AOA-T-0067
name: transcript-linked-code-lineage
domain: history
kind: artifact
status: promoted
origin:
  project: git-ai-project/git-ai
  path: README.md + specs/git_ai_standard_v3.0.0.md + skills/ask/SKILL.md
  note: Adapted from the open-source git-ai project, which links AI-written code back to session evidence so reviewers can reopen the originating conversation or rationale instead of treating code provenance as invisible.
owners:
  - 8Dionysus
tags:
  - history
  - lineage
  - transcripts
  - code
  - provenance
summary: Link code history back to saved session evidence so reviewers can reopen the originating transcript or rationale without widening the bundle into generic repo analytics or memory doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0045
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

# transcript-linked-code-lineage

## Intent

Link code history back to saved session evidence so reviewers can reopen the originating transcript or rationale without widening the bundle into generic repo analytics, repository mining, or memory doctrine.

## When to use

- saved agent sessions or transcript evidence already exist alongside code changes
- reviewers need to trace which saved session or conversation produced a code change
- one code-review or blame surface should reopen bounded provenance instead of relying on memory
- the reusable object is a code-to-session lineage seam, not a broad analytics or search platform

## When not to use

- there is no saved session evidence to link back to
- the main need is generic git analytics, productivity scoring, or repository mining
- the workflow wants a full retrieval or Q and A product rather than a lineage link
- the bundle would become authorship governance, policy enforcement, or memory substrate
- one witness trace or one handoff check is the actually smaller object

## Inputs

- one saved session, transcript, or equivalent evidence artifact
- one code anchor such as file, line range, diff hunk, or commit
- one stable reference that links the code anchor back to the saved evidence
- one review or blame surface that can expose the link

## Outputs

- one explicit lineage record from code history back to saved session evidence
- one reviewable path to reopen the originating transcript or rationale
- lower pressure to treat provenance as hidden memory or oral history
- one bounded seam between code review and deeper retrieval or analytics systems

## Core procedure

1. Start from saved session evidence that is already stable enough to reference.
2. Choose the code anchor that needs provenance, such as a file, line range, diff hunk, or commit.
3. Record one stable link from that code anchor back to the saved evidence artifact.
4. Surface the link in one blame, review, or inspection path so a later reader can reopen the evidence.
5. Keep the lineage surface bounded to provenance lookup rather than broad analytics or interactive retrieval products.
6. Preserve the saved evidence artifact as the authoritative source for what the session said or did.
7. Split out telemetry, retrieval UX, or governance layers if they become the real center of gravity.

## Contracts

- code anchors link back to already-saved evidence artifacts
- the lineage link is stable enough that another reviewer can reopen the source evidence later
- saved session evidence stays authoritative when lineage is inspected
- the technique stays smaller than generic repo analytics, hosted search, or memory-product doctrine
- the technique does not own performance telemetry, authorship scoring, or free-form Q and A products

Relationship to adjacent techniques: unlike [AOA-T-0045](../witness-trace-as-reviewable-artifact/TECHNIQUE.md), this technique does not preserve a fuller run artifact with ordered steps and state deltas; it links code anchors back to evidence that already exists. Unlike [AOA-T-0059](../../agent-workflows/git-verified-handoff-claims/TECHNIQUE.md), it does not verify present-tense handoff claims against git state; it preserves lineage from code history back to prior evidence. It also stays smaller than generic blame analytics because the center of gravity is the stable code-to-evidence link itself.

## Risks

### Failure modes

- lineage links break because code anchors or evidence references are unstable
- reviewers treat the lineage pointer as if it were the evidence itself
- the bundle widens into productivity telemetry or generic code analytics
- provenance links quietly become a memory or retrieval platform without bounded review surfaces

### Negative effects

- maintaining lineage links adds overhead compared with plain code review
- line-range granularity can be brittle if refactors are frequent
- provenance cues can be overtrusted even when the saved evidence is incomplete or noisy

### Misuse patterns

- treating code lineage as a scorecard for agent quality or contributor ranking
- widening the bundle into hosted search, dashboards, or repository mining
- using lineage links as a substitute for keeping the saved evidence artifact readable and accessible
- collapsing lineage into generic why-search or Q and A product behavior

### Detection signals

- reviewers cannot reopen the saved evidence from the lineage surface
- dashboards or ranking metrics become more prominent than the provenance link
- saved evidence artifacts become harder to inspect than the lineage pointers themselves
- teams talk about repository intelligence or analytics more than one bounded code-to-evidence seam

### Mitigations

- keep the lineage link stable and reviewable
- preserve saved evidence artifacts as the authoritative source layer
- split telemetry, ranking, or retrieval UX into sibling techniques instead of widening this contract
- use broader witness or transcript artifacts when the actual need is fuller run context rather than lineage lookup

## Validation

Verify the technique by confirming that:
- code anchors can be linked back to already-saved evidence artifacts
- another reviewer can reopen the source evidence from the lineage surface
- the explanation still makes sense without analytics dashboards or retrieval-product features
- the saved evidence remains authoritative after the link is created
- the bundle stays distinct from handoff verification, telemetry, and hosted search platforms

See `checks/transcript-linked-code-lineage-checklist.md`.

## Adaptation notes

What can vary across projects:
- the code anchor type such as file, line range, commit, or diff hunk
- where the lineage record lives
- whether lineage is surfaced through blame, review comments, or another bounded inspection path
- how evidence artifacts are named or stored

What should stay invariant:
- lineage begins from already-saved evidence artifacts
- code anchors keep stable pointers back to source evidence
- provenance lookup remains the center of gravity
- analytics, dashboards, and free-form retrieval stay outside the invariant core

Project-shaped details that should not be treated as invariant:
- one blame command or CLI name
- one Git Notes layout or storage backend
- repo-wide analytics dashboards or deployment metrics
- interactive assistant commands beyond the bounded lineage lookup seam

## Public sanitization notes

This public bundle keeps only the reusable lineage seam: link code anchors back to saved session evidence so later reviewers can reopen provenance. Donor-specific Git Notes layouts, productivity metrics, dashboards, deployment telemetry, and broader retrieval-product behavior were intentionally removed or generalized.

## Example

See `examples/minimal-transcript-linked-code-lineage.md`.

## Checks

See `checks/transcript-linked-code-lineage-checklist.md`.

## Promotion history

- adapted from open-source `git-ai-project/git-ai`
- landed from the Wave 1C history-lineage-governed-actions shard inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for code-to-session provenance links

## Future evolution

- keep [AOA-T-0045](../witness-trace-as-reviewable-artifact/TECHNIQUE.md) as the fuller run-artifact sibling rather than widening this bundle into witness export
- reopen a narrower retrieval sibling only if it survives without collapsing back into lineage plus search product behavior
- keep telemetry and scoring separate rather than turning lineage into contributor or model analytics
