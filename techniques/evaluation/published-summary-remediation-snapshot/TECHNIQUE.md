---
id: AOA-T-0008
name: published-summary-remediation-snapshot
domain: evaluation
status: promoted
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real nightly remediation helper that read already-published summaries and turned them into a bounded, reviewable backlog without recomputing source history or widening product surface area.
owners:
  - 8Dionysus
tags:
  - evaluation
  - remediation
  - summaries
  - bounded
summary: Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior.
---

# published-summary-remediation-snapshot

## Intent

Create one reviewable remediation snapshot from already-published latest summaries, so operators, dashboards, and agents can see what needs follow-up without rerunning upstream checks or rebuilding historical state.

## When to use

- nightly or scheduled checks already publish stable machine-readable latest summaries
- operators need a compact remediation backlog instead of reading many separate summaries
- the project wants deterministic follow-up buckets with explicit caps
- the project needs a read-only helper that can support humans, UIs, and agents from the same published artifacts

## When not to use

- source checks do not publish stable latest summaries yet
- the workflow must actively execute remediation instead of producing a review surface
- historical replay is required to answer the question, rather than the latest published state
- the bucket policy is still unstable enough that snapshot output would drift from run to run

## Inputs

- a fixed set of latest published summary aliases
- one deterministic bucket policy
- one explicit candidate cap per bucket
- optional freshness rules for stale or missing source summaries

## Outputs

- one remediation snapshot
- one bounded bucketed backlog of candidate items
- explicit references to the source summaries used for each candidate
- explicit reporting for missing, stale, or truncated inputs

## Core procedure

1. Define the small fixed set of latest published summary aliases the snapshot is allowed to read.
2. Read only those latest aliases and do not scan historical runs.
3. Apply one deterministic bucket policy to the observed latest state.
4. Place candidate items into a fixed bucket set such as `failing_now`, `stale_inputs`, and `follow_up_needed`.
5. Cap each bucket explicitly so the remediation surface stays reviewable.
6. Preserve source references for every emitted candidate item.
7. Report missing or stale sources explicitly in the snapshot instead of silently skipping them.
8. Publish the remediation snapshot as a read-only downstream view over existing summaries.

## Contracts

- the helper reads latest published summaries only
- the helper does not replay history or recompute trend state
- the bucket set is fixed and deterministic for a given snapshot version
- each bucket has an explicit candidate cap
- candidate ordering and truncation policy are explicit rather than incidental
- missing or stale source summaries are surfaced explicitly
- emitted items retain traceable references to their source summary paths
- source summaries and upstream runtime behavior are not mutated by snapshot generation
- this technique consumes published summary patterns such as `AOA-T-0006` and can support promoted gate outputs such as `AOA-T-0007`, but it is neither a dual-write layout pattern nor a gate-promotion pattern itself

## Risks

- letting the bucket policy grow ad hoc until the snapshot stops being reviewable
- hiding missing or stale sources, which can make the backlog look healthier than reality
- accidentally reintroducing history replay and turning a snapshot into a second evaluator
- dropping source references and making remediation items harder to audit or verify

## Validation

Verify the technique by confirming that:
- only latest published summary aliases are read
- no history replay or trend recomputation is required
- the bucket set is fixed and documented
- each bucket has a documented cap
- missing or stale sources are reported explicitly
- emitted candidates retain source references
- snapshot generation is read-only with respect to source artifacts

See `checks/remediation-snapshot-checklist.md`.

## Adaptation notes

What can vary across projects:
- summary filenames and alias paths
- bucket names and ordering rules
- freshness windows for stale inputs
- candidate ranking fields inside each bucket
- output format details such as plain JSON, artifact bundles, or UI adapters

What should stay invariant:
- the helper reads latest published summaries rather than historical runs
- the bucket set is deterministic
- per-bucket caps are explicit
- source references stay attached to emitted candidates
- the snapshot remains a read-only downstream view

## Public sanitization notes

ATM10-specific gateway names, workflow names, thresholds, run roots, and remediation scripts were removed. The public version keeps only the reusable pattern: bounded read-only aggregation from latest published summaries into a deterministic remediation snapshot.

## Example

See `examples/minimal-remediation-snapshot.md`.

## Checks

See `checks/remediation-snapshot-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through a nightly remediation helper that consumed already-published summaries and emitted a bounded review surface
- promoted to `aoa-techniques` on 2026-03-14

## Future evolution

- add a companion technique for telemetry-integrity snapshots over published summary layouts
- add an adaptation example for object-store-backed summary aliases
- add guidance for versioning bucket policy without breaking snapshot consumers
