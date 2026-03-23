---
id: AOA-T-0009
name: lightweight-status-snapshot
domain: docs
status: canonical
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
maturity_score: 5
rigor_level: light
reversibility: easy
review_required: false
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations:
  - type: complements
    target: AOA-T-0002
evidence:
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
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

### Failure modes

- the snapshot becomes so thin that it no longer gives enough orientation to send readers to the right canonical detail
- outward links go stale after the canonical doc map evolves, so the snapshot keeps pointing to the wrong current-state surfaces
- the top-level docs stay short and tidy, but they quietly stop acting as reliable entrypoints because the routing aliases no longer reflect where current truth actually lives

### Negative effects

- excessive trimming can make operational truth harder to find even while the entrypoint docs look cleaner
- the snapshot can hide active gaps in status hygiene by removing detail faster than the repository learns where that detail should live
- false cleanliness can make a repo feel better maintained than it is while new readers still cannot find the active state without asking around

### Misuse patterns

- using the technique as a reason to delete detail instead of routing it to canonical homes
- treating `README` or `MANIFEST` cleanliness as the goal by itself, even when navigability and current-state orientation get worse
- preserving stale outward links or summary aliases because the entrypoint still "looks short enough"

### Detection signals

- new readers can tell that the entrypoint docs are short, but still cannot find the current detailed status quickly
- links from the snapshot stop resolving to the latest `TODO`, `PLANS`, `RUNBOOK`, `DECISIONS`, or session detail
- teams keep re-adding summary prose to `README` or `MANIFEST` because the snapshot no longer feels sufficient for orientation
- the entrypoint docs look clean, but operators still need to ask around to learn where real operational truth now lives
- a repo review praises top-level neatness even though the first question from a newcomer is still "where is the real current state?"

### Mitigations

- restore just enough orientation context to make the snapshot navigable before adding back long chronology
- fix or rotate canonical links whenever the doc map changes
- move removed detail into explicit canonical homes instead of dropping it entirely
- treat repeated confusion about where current truth lives as a signal to strengthen routing, not to turn the snapshot back into a log
- treat stale routing aliases as a breakage in the entrypoint contract, not as cosmetic drift

## Validation

Verify the technique by confirming that:
- `README` remains short and human-facing
- `MANIFEST`, when used, remains a compact snapshot rather than a long log
- detailed run history and changing counters are absent from snapshot docs
- canonical links point to the current `TODO`, `PLANS`, `RUNBOOK`, `DECISIONS`, and latest session detail
- a reader can understand the current state quickly and then navigate to the right detailed document

See `checks/lightweight-snapshot-checklist.md`.
For source-backed evidence, see `notes/origin-evidence.md` and `notes/second-context-adaptation.md`.

## Adaptation notes

What can vary across projects:
- whether a separate `MANIFEST` exists
- the exact snapshot sections such as current status, active capabilities, or quick links
- whether the detailed history doc is daily, weekly, or milestone-based
- whether CI links are explicit URLs or just canonical doc references
- whether one snapshot doc is enough or both `README` and `MANIFEST` stay lightweight

What should stay invariant:
- snapshot docs stay short
- canonical detail is linked rather than duplicated
- current-state evidence is anchored in one detailed location
- top-level docs remain orientation surfaces rather than archives

Project-shaped details that should not be treated as invariant:
- the exact status bullets shown in the snapshot
- whether capabilities are listed in `README`, `MANIFEST`, or both
- the exact session file date linked from the current snapshot
- whether current-state evidence comes from CI, session docs, or a similar published summary surface

See `notes/second-context-adaptation.md` for a compact public-repository variant.

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
- approved for `canonical` in `aoa-techniques` on 2026-03-16 after cross-context evidence, a clean docs-boundary semantic review, and a fresh public-safety recheck

## Future evolution

- add a companion example for repositories without `MANIFEST`
- add optional guidance for snapshot freshness checks
