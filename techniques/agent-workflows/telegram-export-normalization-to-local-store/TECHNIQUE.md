---
id: AOA-T-0074
name: telegram-export-normalization-to-local-store
domain: agent-workflows
kind: ingest
status: promoted
origin:
  project: Telethon + TDLib + opentele + Chatistics + tg-archive + telegram-mcp
  path: README.md
  note: Adapted from open-source Telegram client, archive, analytics, and MCP surfaces that expose message retrieval, export, media references, and local persistence, while this bundle keeps only the bounded normalization contract.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - telegram
  - normalization
  - local-store
  - provenance
summary: Normalize Telegram messages and media into a resumable local store with visible provenance so later workflows can inspect, route, or distill the data without collapsing auth, session, or memory doctrine into the storage contract.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations: []
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

# telegram-export-normalization-to-local-store

## Intent

Turn Telegram export or sync output into a bounded, provenance-preserving local store so later workflows can inspect, route, or distill message history without importing auth bootstrap, session conversion, or memory-writeback doctrine.

## When to use

- Telegram messages or Saved Messages need to become a local structured store
- media references and reply edges matter
- sync or export should resume without rewriting the whole store
- downstream workflows need message-level provenance instead of a flat text dump
- the reusable seam is Telegram-source normalization, not auth, control-plane behavior, or memory policy

## When not to use

- the real problem is account auth, session conversion, or bootstrap
- the workflow needs a live agent-control surface rather than a local normalized store
- the intent is to auto-promote everything into memory or canon
- one project-specific archive app or dashboard owns the whole workflow end to end

## Inputs

- one Telegram export, API-derived message stream, or equivalent source batch
- media download paths or media source references
- one local storage target
- optional resume markers or checkpoint state

## Outputs

- one normalized message object surface
- one media reference map
- one resumable local store
- explicit source references back to export chunks, API batches, or file paths

## Core procedure

1. Take export or synced messages as the source input.
2. Normalize message ids, timestamps, sender identity, reply edges, and media references into one stable object shape.
3. Preserve source references so downstream review can trace where a record came from.
4. Write into a resumable local store that supports partial progress and later continuation.
5. Keep auth secrets, session conversion, and bootstrap procedures outside the normalized object contract.
6. Keep curation, summarization, memory writeback, and downstream routing outside the invariant core.
7. Split out a sibling technique if the real reusable object becomes auth handoff, memory ingestion, or general history-artifact doctrine.

## Contracts

- auth posture stays separate from normalization
- message provenance remains visible
- the local store is resumable
- normalized objects preserve reply edges and media references
- the technique does not auto-promote content into memory, canon, or downstream action policy
- downstream systems consume one stable local object contract rather than donor-specific API or export internals

Relationship to adjacent techniques: unlike [AOA-T-0026](../../history/session-capture-as-repo-artifact/TECHNIQUE.md), this bundle does not claim general project-scoped history capture ownership; it owns Telegram-source normalization into a resumable local store. Unlike `telegram-account-auth-and-session-bridge`, it does not handle credentials, session conversion, or bootstrap approval. It also stays smaller than transcript packaging, recall, or memory-ingestion surfaces because it stops at normalized storage.

## Risks

### Failure modes

- media references lose source linkage
- reply edges disappear during normalization
- the local store collapses export and live sync semantics into one ambiguous state
- resume markers skip or duplicate messages

### Negative effects

- operators can confuse storage with curation
- session handling can leak into the normalization contract
- normalized stores can look authoritative even when source provenance is missing

### Misuse patterns

- treating the local store as memory truth
- burying secret or session files beside normalized outputs
- widening the technique into Telegram ops doctrine or bot-control behavior

### Detection signals

- untraceable media files
- messages with missing source ids or reply links
- mixed auth or session artifacts inside the normalized store
- resume after interruption produces duplicate or missing records

### Mitigations

- keep auth and session paths separate
- preserve explicit source fields
- define one stable local object contract
- keep resume markers visible and bounded

## Validation

Verify the technique by confirming that:
- a sample export with replies and media retains source ids and media references
- resume after interruption preserves progress without losing or duplicating records
- export and sync provenance remain distinguishable
- normalized objects stay readable without donor-specific runtime code
- auth, session, and memory doctrine remain outside the technique

See `checks/telegram-export-normalization-to-local-store-checklist.md`.

## Adaptation notes

What can vary across projects:
- local store backend
- export versus live sync route
- media storage paths
- message-family extensions
- checkpoint format for resume behavior

What should stay invariant:
- auth remains separate
- normalized message objects preserve provenance
- the store remains resumable
- downstream systems read one stable local object contract

Project-shaped details that should not be treated as invariant:
- session-secret storage policy
- auth bootstrap procedure
- agent-control rhetoric
- automatic memory writeback

## Public sanitization notes

This public bundle keeps only the reusable normalization seam: Telegram messages and media become stable local objects with visible provenance and resumable storage, while auth, session handling, and memory policy remain separate. Secret handling, operator auth procedure, and live-control doctrine were intentionally removed or generalized.

## Example

See `examples/minimal-telegram-export-normalization-to-local-store.md`.

## Checks

See `checks/telegram-export-normalization-to-local-store-checklist.md`.

## Promotion history

- adapted from open-source `Telethon`, `TDLib`, `opentele`, `Chatistics`, `tg-archive`, and `telegram-mcp`
- landed from `personal-ingest-wave-2`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for Telegram-source normalization into a local resumable store

## Future evolution

- keep auth/session bridging separate unless a narrower approved seam proves reusable
- split out thread reconstruction or media-routing helpers only if those contracts survive independently
- add a stronger second live context if another public workflow keeps Telegram normalization explicit before later routing, recall, or memory actions
