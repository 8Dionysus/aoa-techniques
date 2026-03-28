---
id: AOA-T-0053
name: local-first-session-index
domain: history
status: promoted
origin:
  project: wesm/agentsview
  path: README.md + internal/db/search.go + internal/db/sessions.go
  note: Adapted from the open-source agentsview project, which discovers already-saved AI session artifacts locally, syncs them into a local SQLite index, and exposes searchable lookup without turning that index into memory or hosted-dashboard authority.
owners:
  - 8Dionysus
tags:
  - history
  - sessions
  - index
  - search
  - local-first
summary: Build a local searchable index over already-saved session artifacts so teams can browse or query saved history without reopening capture semantics or turning the index into memory or dashboard doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0026
  - type: complements
    target: AOA-T-0044
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

# local-first-session-index

## Intent

Build a local searchable index over already-saved session artifacts so operators can find and reopen useful history quickly while keeping the saved artifacts, not the index, as the authoritative source.

## When to use

- session artifacts are already being saved locally
- the history layer has become large enough that browse and search matter
- operators need a faster lookup surface that still points back to original artifacts
- the reusable object is a local-first index over saved history, not capture, export, or hosted analytics

## When not to use

- the real problem is still capturing or persisting session history in the first place
- the workflow mainly needs transcript packaging, redaction, or export for review
- the index would become cloud memory, recall ranking, or instruction authority
- the contract depends on a hosted dashboard, multi-machine sync, or remote database service

## Inputs

- one already-saved session artifact layer
- one local discovery or refresh path over those artifacts
- one bounded metadata set such as session ID, source path, timestamps, agent name, or display title
- one local index store or equivalent lookup surface
- one query or browse path that can return references back to source artifacts

## Outputs

- one local searchable or browsable index over saved session artifacts
- faster lookup by text, metadata, or bounded filters
- one stable reference back to the original saved artifact for every useful hit
- one clearer separation between history lookup and any later memory, dashboard, or transcript-export layer

## Core procedure

1. Start from already-saved local session artifacts rather than from transient chat state.
2. Extract a bounded metadata and searchable-content slice into one local index.
3. Keep stable references from each index entry back to the source artifact path or identity.
4. Refresh the index from local artifacts instead of treating the index as the place where history originates.
5. Use the index to locate relevant sessions, then reopen the source artifact when review or reuse matters.
6. Keep transcript export, analytics, hosted sync, and memory recall as sibling layers outside the core contract.
7. Split out a different technique if hosted dashboards, central databases, or instruction recall become the true reusable object.

## Contracts

- the index remains derivative and rebuildable from local source artifacts
- source artifacts stay authoritative even when the index is easier to search
- results keep stable references back to the saved artifact they summarize or match
- local-first storage remains the default posture
- the technique does not own capture, transcript packaging, memory recall, or hosted dashboard doctrine
- searchable lookup stays smaller than analytics, publishing, or multi-machine sync systems

Relationship to adjacent techniques: unlike [AOA-T-0026](../session-capture-as-repo-artifact/TECHNIQUE.md), this technique assumes session artifacts already exist and only owns read-only indexing and lookup over them. Unlike [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md), it helps find artifacts but does not package selected history into a new transcript artifact. Unlike [AOA-T-0045](../witness-trace-as-reviewable-artifact/TECHNIQUE.md), it does not add step-level witness or state-delta semantics.

## Risks

### Failure modes

- the index drifts away from current source artifacts
- search hits cannot reliably reopen the original artifact
- a fast lookup surface gets mistaken for the authoritative history layer
- the bundle widens into dashboard, analytics, or remote-sync product behavior

### Negative effects

- operators may skim the index instead of opening the source artifact when nuance matters
- indexed metadata can flatten session context too aggressively
- an index database can look more authoritative than the files it was derived from

### Misuse patterns

- mixing capture, indexing, and transcript export into one technique
- turning the index into memory recall, ranking, or instruction policy
- treating hosted dashboards, PostgreSQL sync, or publish flows as part of the invariant core

### Detection signals

- results no longer include stable source paths or session IDs
- the index cannot be rebuilt from the local artifact layer alone
- design discussion drifts toward analytics dashboards, central sync, or memory features
- users act on index summaries without reopening the underlying artifact

### Mitigations

- keep stable source references in every useful hit
- make rebuild-from-local-artifacts part of the validation story
- preserve an explicit habit of reopening source artifacts for real review
- split hosted analytics, remote sync, and recall behavior into narrower sibling techniques

## Validation

Verify the technique by confirming that:
- session artifacts already exist before indexing starts
- the index can be rebuilt from local artifacts without hidden memory state
- search results or browse hits point back to the original saved artifact
- the source artifact remains readable and authoritative after lookup
- the explanation does not require capture, hosted sync, or memory doctrine to make sense

See `checks/local-first-session-index-checklist.md`.

## Adaptation notes

What can vary across projects:
- the artifact format such as JSONL, Markdown, or another saved-session shape
- the local index backend such as SQLite, a flat manifest, or another local search store
- which fields get indexed or exposed for filtering
- refresh cadence and how index rebuilds are triggered
- whether the lookup surface is CLI, TUI, or web UI

What should stay invariant:
- indexing starts from already-saved local artifacts
- the index stays derivative and rebuildable
- results keep references back to source artifacts
- local-first posture stays intact

Project-shaped details that should not be treated as invariant:
- one specific web dashboard or desktop shell
- analytics heatmaps, usage metrics, or live SSE updates
- PostgreSQL push sync or shared-team viewer features
- export, publish, or reverse-proxy configuration flows

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: local searchable indexing over already-saved session artifacts with references back to the source files. Hosted dashboards, analytics surfaces, live-update UX, export or publish flows, PostgreSQL sync, reverse-proxy configuration, and wider product semantics were intentionally left out of the public contract.

## Example

See `examples/minimal-local-first-session-index.md`.

## Checks

See `checks/local-first-session-index-checklist.md`.

## Promotion history

- adapted from open-source `wesm/agentsview`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for local searchable indexing over saved session artifacts

## Future evolution

- keep transcript packaging as a separate sibling instead of widening this bundle into export or redaction flows
- keep analytics, dashboarding, and multi-machine sync outside the core contract unless a smaller reusable sibling appears
- add a stronger second live context if another public repository uses a local-first session-history index in practice
