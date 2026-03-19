---
id: AOA-T-0008
name: published-summary-remediation-snapshot
domain: evaluation
status: canonical
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
maturity_score: 4
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-16
export_ready: true
relations:
  - type: requires
    target: AOA-T-0006
  - type: complements
    target: AOA-T-0010
  - type: complements
    target: AOA-T-0011
evidence:
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
---

# published-summary-remediation-snapshot

## Intent

Create one reviewable remediation snapshot from already-published latest summaries, so operators, dashboards, and agents can see what needs follow-up without rerunning upstream checks or rebuilding historical state.

## When to use

- nightly or scheduled checks already publish stable machine-readable latest summaries
- several stable published summaries feed more than one downstream triage consumer
- operators need a compact remediation backlog instead of reading many separate summaries
- one published backlog should serve operators, reports, and agent handoff from the same read-only source
- the project wants deterministic follow-up buckets with explicit caps
- the project needs a read-only helper that can support humans, UIs, and agents from the same published artifacts

## When not to use

- source checks do not publish stable latest summaries yet
- the source set is still small enough that every consumer can read each summary directly without duplicated triage logic
- the workflow must actively execute remediation instead of producing a review surface
- historical replay is required to answer the question, rather than the latest published state
- the bucket policy is still unstable enough that snapshot output would drift from run to run

## Inputs

- a fixed set of latest published summary aliases
- one deterministic bucket policy
- one explicit candidate cap policy
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
5. Apply the explicit candidate cap or truncation policy so the remediation surface stays reviewable.
6. Preserve source references for every emitted candidate item.
7. Report missing or stale sources explicitly in the snapshot instead of silently skipping them.
8. Publish the remediation snapshot as a read-only downstream view over existing summaries.

## Contracts

- the helper reads latest published summaries only
- the helper does not replay history or recompute trend state
- the bucket set is fixed and deterministic for a given snapshot version
- the candidate cap or truncation policy is explicit rather than incidental
- candidate ordering and truncation policy are explicit rather than incidental
- missing or stale source summaries are surfaced explicitly
- emitted items retain traceable references to their source summary paths
- source summaries and upstream runtime behavior are not mutated by snapshot generation
- this technique consumes published summary patterns such as `AOA-T-0006` and can support promoted gate outputs such as `AOA-T-0007`, but it is neither a dual-write layout pattern nor a gate-promotion pattern itself

## Risks

### Failure modes

- missing or stale sources are hidden, making the backlog look healthier than reality
- history replay slips back in and turns the snapshot into a second evaluator
- source references disappear and make remediation items harder to audit or verify

### Negative effects

- the bucket policy can grow ad hoc until the snapshot stops being reviewable as one bounded surface
- remediation output becomes harder to compare over time when grouping and truncation stop being stable

### Misuse patterns

- widening the bucket set or candidate policy casually instead of versioning a fixed bounded policy
- treating the snapshot as a place to recompute history, trend state, or upstream judgments

### Detection signals

- new buckets keep appearing without a clearly documented policy change
- remediation items no longer point back to their source summaries or stale-source reporting goes missing

### Mitigations

- keep the bucket set and candidate cap fixed for each snapshot version and document policy changes explicitly
- preserve latest-only input rules, explicit stale-source reporting, and source references for every emitted item

## Validation

Verify the technique by confirming that:
- only latest published summary aliases are read
- no history replay or trend recomputation is required
- the bucket set is fixed and documented
- the candidate cap policy is documented
- missing or stale sources are reported explicitly
- emitted candidates retain source references
- snapshot generation is read-only with respect to source artifacts

See `checks/remediation-snapshot-checklist.md`.
For source-backed origin proof, see `notes/origin-evidence.md`.
For bounded second-context adaptation guidance, see `notes/second-context-adaptation.md`.
For canonical-prep readiness, see `notes/canonical-readiness.md`.

## Adaptation notes

What can vary across projects:
- summary filenames and alias paths
- whether latest aliases are local files or object-store keys
- bucket names and ordering rules
- freshness windows for stale inputs
- whether the candidate cap applies per snapshot, per bucket, or by priority band
- candidate ranking fields inside each bucket
- output format details such as plain JSON, artifact bundles, or UI adapters

Project-shaped details that should not be treated as invariant:
- the exact G2 bucket names used by `atm10-agent`
- the specific nightly workflow or operator panel that consumes the snapshot
- the exact latest alias path layout used by the origin project
- the exact follow-up reason codes published for one operational loop

What should stay invariant:
- the helper reads latest published summaries rather than historical runs
- the bucket set is deterministic
- the candidate cap policy is explicit
- source references stay attached to emitted candidates
- the snapshot remains a read-only downstream view

Within the G2 published-summary package, this technique is the bounded remediation rollup over the published latest-alias contract from `AOA-T-0006`. `AOA-T-0010` checks whether those published summaries and remediation inputs are trustworthy, and `AOA-T-0011` defines how optional remediation surfaces should render.
Within its natural scope, this becomes the default downstream rollup when several published summaries feed several bounded consumers and direct per-source reading stops being reviewable across each consumer separately.

## Public sanitization notes

ATM10-specific gateway names, workflow names, thresholds, run roots, and remediation scripts were removed. The public version keeps only the reusable pattern: bounded read-only aggregation from latest published summaries into a deterministic remediation snapshot.

## Example

See `examples/minimal-remediation-snapshot.md` and `examples/object-store-remediation-snapshot.md`.

## Checks

See `checks/remediation-snapshot-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through a nightly remediation helper that consumed already-published summaries and emitted a bounded review surface
- promoted to `aoa-techniques` on 2026-03-14
- approved as `canonical` in `aoa-techniques` on 2026-03-16 after fresh public-safety review and default-use confirmation

## Future evolution

- add guidance for versioning bucket policy without breaking snapshot consumers
- add a variant for hierarchical buckets that still preserves fixed candidate caps
