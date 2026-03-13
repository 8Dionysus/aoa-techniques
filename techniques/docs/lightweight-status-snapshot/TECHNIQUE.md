---
id: AOA-T-0009
name: lightweight-status-snapshot
domain: docs
status: promoted
origin:
  project: atm10-agent
  path: docs/DECISIONS.md
  note: Derived from a real doc-hygiene transition where README and MANIFEST were reduced to short snapshots that linked to canonical execution, history, decision, and runbook documents instead of duplicating long status blocks.
owners:
  - 8Dionysus
tags:
  - docs
  - snapshots
  - anti-drift
  - status
summary: Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes.
---

# lightweight-status-snapshot

## Intent

Keep repository entrypoint status easy to scan by turning top-level status docs into short snapshots that summarize the current state and link to canonical detail instead of duplicating long chronology.

## When to use

- the repository already has a source-of-truth layout for plans, runbooks, decisions, and history
- `README` needs to stay readable for humans landing on the repo
- a compact machine or human snapshot such as `MANIFEST` is useful for fast orientation
- long-running projects keep accumulating metrics, run IDs, or session details that would otherwise spread into entrypoint docs

## When not to use

- the repository is small enough that one short `README` is already sufficient
- there is no canonical home for detailed status, history, or operator detail
- the team expects the top-level docs to hold full chronology rather than serve as snapshots

## Inputs

- one source-of-truth document map such as `AOA-T-0002`
- one short human-facing entrypoint doc
- one short machine or mixed snapshot doc when the repository needs it
- canonical detailed docs for active work, goals, decisions, runbooks, and history

## Outputs

- a concise `README` that points to canonical docs
- a concise `MANIFEST` or equivalent repository snapshot
- reduced duplication of run history and changing status counters
- clearer separation between summary state and detailed operational truth

## Core procedure

1. Choose which top-level docs should stay lightweight, typically `README` and optionally `MANIFEST`.
2. Keep those docs focused on current orientation: purpose, quick links, active capabilities, and short status bullets.
3. Move detailed execution state to `TODO`, goals to `PLANS`, commands to `RUNBOOK`, decisions to `DECISIONS`, and long chronology to `SESSION_*`.
4. Replace copied detail with short references to the canonical documents that already hold it.
5. Treat CI and the latest session snapshot as the source of detailed current-state evidence rather than copying counters into every top-level doc.
6. Re-trim entrypoint docs whenever they begin to accumulate long run lists, metric history, or duplicated troubleshooting notes.

## Contracts

- `README` stays a short human-facing entrypoint
- `MANIFEST`, when present, stays a short machine or mixed snapshot
- long run IDs, long metric history, and detailed chronology do not live in snapshot docs
- detailed current-state evidence lives in CI and the latest session or equivalent canonical history doc
- snapshot docs link outward instead of restating canonical detail
- this technique complements `AOA-T-0002` by constraining how summary docs stay lightweight; it does not replace the broader document-role layout

## Risks

- making the snapshot so short that it stops being useful for orientation
- keeping stale links after the canonical doc map evolves
- allowing new summary prose to drift back into `README` and `MANIFEST`
- confusing lightweight summaries with a complete operational record

## Validation

Verify the technique by confirming that:
- `README` remains short and human-facing
- `MANIFEST`, when used, remains a compact snapshot rather than a long log
- detailed run history and changing counters are absent from snapshot docs
- canonical links point to the current `TODO`, `PLANS`, `RUNBOOK`, `DECISIONS`, and latest session detail
- a reader can understand the current state quickly and then navigate to the right detailed document

See `checks/lightweight-snapshot-checklist.md`.

## Adaptation notes

What can vary across projects:
- whether a separate `MANIFEST` exists
- the exact snapshot sections such as current status, active capabilities, or quick links
- whether the detailed history doc is daily, weekly, or milestone-based
- whether CI links are explicit URLs or just canonical doc references

What should stay invariant:
- snapshot docs stay short
- canonical detail is linked rather than duplicated
- current-state evidence is anchored in one detailed location
- top-level docs remain orientation surfaces rather than archives

## Public sanitization notes

ATM10-specific capabilities, workflow names, local paths, and session-specific status numbers were removed. The public version keeps only the reusable snapshot discipline: short top-level status docs with outward links to canonical detail.

## Example

See `examples/minimal-lightweight-snapshot.md`.

## Checks

See `checks/lightweight-snapshot-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through a doc-hygiene transition where `README.md` and `MANIFEST.md` were trimmed to snapshot form while detailed state stayed in `TODO`, `PLANS`, `RUNBOOK`, `DECISIONS`, and `SESSION_*`
- promoted to `aoa-techniques` on 2026-03-14

## Future evolution

- add a companion example for repositories without `MANIFEST`
- add optional guidance for snapshot freshness checks
- add a relationship note for weekly summary templates and release notes
