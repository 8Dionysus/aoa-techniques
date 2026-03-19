---
id: AOA-T-0010
name: telemetry-integrity-snapshot
domain: evaluation
status: canonical
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real nightly helper that consumed published G2 summaries and produced a machine-readable integrity verdict over telemetry counters, dual-write paths, anti-double-count rules, and UTC guardrail consistency without introducing a new hard gate.
owners:
  - 8Dionysus
tags:
  - evaluation
  - integrity
  - telemetry
  - diagnostics
summary: Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface.
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
    target: AOA-T-0008
  - type: complements
    target: AOA-T-0011
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

# telemetry-integrity-snapshot

## Intent

Provide one machine-readable diagnostic verdict over published summary invariants, so operators can quickly tell whether telemetry and artifact layout are trustworthy before acting on downstream rollups or remediation backlogs.

## When to use

- several latest published summaries already exist for one operational decision path
- several published summaries or downstream rollups are interpreted by more than one consumer
- the project needs to validate telemetry counters and artifact-layout invariants across those summaries
- dual-write latest plus history patterns are already in use
- the team wants a diagnostic integrity layer without turning it into a new hard gate by default

## When not to use

- source summaries are not stable enough to serve as inputs yet
- the project needs direct enforcement instead of a diagnostic verdict
- there is no explicit artifact layout or counter policy to verify
- one source alone is sufficient and cross-summary integrity checks add no value
- each consumer can still inspect source trust directly without duplicating integrity logic across surfaces

## Inputs

- a fixed set of latest published summaries
- required and optional source classification
- telemetry counters or mismatch counters emitted by those summaries
- dual-write metadata such as `summary_json`, `history_summary_json`, and `run_dir`
- optional guardrail consistency inputs when a project exposes them

## Outputs

- one integrity snapshot
- one explicit integrity decision such as `clean` or `attention`
- reason codes for broken invariants
- per-invariant observed fields that explain the verdict

## Core procedure

1. Define the small fixed set of latest published summaries that the integrity helper is allowed to read.
2. Classify which of those sources are required and which are optional for extra consistency checks.
3. Validate required source health first: presence, schema compatibility, and usable status.
4. Check telemetry counters that should remain at zero or otherwise stay within invariant expectations.
5. Check dual-write invariants over latest alias plus history copy metadata.
6. Check anti-double-count invariants so nested history remains the canonical accumulation path.
7. If an optional guardrail source is present, validate its internal consistency and surface warnings or attention when it disagrees with itself.
8. Emit one read-only integrity snapshot with a concise decision and supporting reason codes.

## Contracts

- the helper reads latest published summaries only
- the helper is read-only with respect to upstream summaries and runtime behavior
- required source health is validated explicitly before deeper invariant checks
- telemetry counters are checked as invariants rather than silently ignored
- dual-write invariants confirm that latest alias and history copy are both present and coherent
- anti-double-count invariants confirm that history remains the canonical nested accumulation path
- optional guardrail consistency may affect the verdict, but absence of the optional source is surfaced explicitly instead of treated as silent success
- the helper produces a diagnostic verdict such as `clean` or `attention`; it does not itself define a new hard enforcement surface
- this technique consumes summary patterns such as `AOA-T-0006`, can inspect promoted gate outputs such as `AOA-T-0007`, and can validate remediation surfaces such as `AOA-T-0008`, but it is distinct from each of those techniques

## Risks

### Failure modes

- schema drift between latest alias and history copies goes undetected and corrupts integrity conclusions
- teams treat the integrity snapshot as a replacement for fixing broken producers instead of a diagnostic signal

### Negative effects

- checking too many optional invariants turns a focused diagnostic layer into noise
- promoting an integrity helper into a hard gate without an explicit rollout decision can make enforcement brittle

### Misuse patterns

- using the helper as a default enforcement gate even though the technique defines a diagnostic, read-only surface
- expanding optional guardrail or consistency checks until they overshadow required source health and dual-write invariants

### Detection signals

- integrity findings repeat across runs without upstream producer fixes, but the helper keeps being treated as the main response
- optional-source or low-value consistency checks dominate the snapshot more than required health, dual-write, or anti-double-count issues

### Mitigations

- keep the snapshot focused on required source health, telemetry invariants, dual-write coherence, and anti-double-count checks
- make any hard-gate promotion a separate explicit rollout decision rather than an implicit property of the helper

## Validation

Verify the technique by confirming that:
- required source presence and schema health are checked explicitly
- telemetry counters or mismatch counters are surfaced in the snapshot
- dual-write invariants verify both latest alias and nested history copy
- anti-double-count invariants verify that the history path differs from the latest alias and remains canonical for collectors
- optional guardrail consistency is reported as `ok`, `attention`, or `not_available` rather than guessed
- the final decision remains diagnostic and read-only

See `checks/telemetry-integrity-checklist.md`.
For source-backed origin proof, see `notes/origin-evidence.md`.
For bounded second-context adaptation guidance, see `notes/second-context-adaptation.md`.
For canonical-prep readiness, see `notes/canonical-readiness.md`.

## Adaptation notes

What can vary across projects:
- source names and schema versions
- whether published summaries are local files or object-store keys
- the exact telemetry or mismatch counters
- the optional guardrail or cadence source
- decision labels such as `clean`, `attention`, `warn`, or `needs_repair`
- whether the snapshot is consumed by CI, nightly summaries, dashboards, or local operator tools

Project-shaped details that should not be treated as invariant:
- the exact G2 source set used by `atm10-agent`
- the specific telemetry counter names emitted by one producer family
- the exact optional cadence or guardrail source checked by the origin project
- the exact verdict labels or summary section names used in one workflow

What should stay invariant:
- latest published summaries are the only inputs
- required source health is explicit
- dual-write and anti-double-count checks stay first-class
- optional consistency checks remain explicit rather than implicit
- the helper stays diagnostic unless a separate rollout chooses otherwise

Within the G2 published-summary package, this technique is the diagnostic trust layer over the published-summary contract from `AOA-T-0006` and the downstream remediation output from `AOA-T-0008`. `AOA-T-0011` governs how optional integrity and remediation surfaces render to operators, smoke checks, or other summary consumers.
Within its natural scope, this becomes the default trust layer when several published summaries or downstream rollups are consumed in more than one place and each consumer should not re-implement the same integrity checks independently.

## Public sanitization notes

ATM10-specific gateway names, nightly workflow names, thresholds, UTC policy details, and repo-specific run roots were removed. The public version keeps the reusable pattern: a read-only integrity snapshot over published summaries and artifact-layout invariants.

## Example

See `examples/minimal-telemetry-integrity-snapshot.md` and `examples/object-store-telemetry-integrity-snapshot.md`.

## Checks

See `checks/telemetry-integrity-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through nightly integrity summaries and tests covering telemetry counter violations, dual-write mismatches, anti-double-count breakage, and optional guardrail inconsistency
- promoted to `aoa-techniques` on 2026-03-14
- approved as `canonical` in `aoa-techniques` on 2026-03-16 after fresh public-safety review and default-use confirmation

## Future evolution

- add guidance for rolling out an integrity verdict into stricter enforcement
- add a companion technique for operator-facing triage when integrity is not clean
