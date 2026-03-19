---
id: AOA-T-0011
name: required-vs-optional-source-rendering
domain: evaluation
status: canonical
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real operator-facing summary surface where canonical smoke sources remained strict, while optional progress, remediation, integrity, and operating-cycle summaries rendered as not-available or warnings instead of crashing the panel or smoke contract.
owners:
  - 8Dionysus
tags:
  - evaluation
  - ui-surfaces
  - summaries
  - resilience
summary: Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures.
maturity_score: 5
rigor_level: strict
reversibility: moderate
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations:
  - type: complements
    target: AOA-T-0008
  - type: complements
    target: AOA-T-0010
evidence:
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
---

# required-vs-optional-source-rendering

## Intent

Keep summary-driven surfaces resilient by enforcing strict behavior for required sources while letting optional enrichments render as `not available yet` or warnings instead of taking down the whole surface.

## When to use

- a UI, dashboard, CLI report, or smoke check reads multiple published summary artifacts
- some sources are mandatory for the base contract, while others are supporting enrichments
- the surface should stay useful even when supporting summaries are unpublished or temporarily invalid
- smoke or regression checks need to distinguish hard failure from observability noise

## When not to use

- every source is equally required for the surface to be meaningful
- the surface is only for manual debugging and does not need a formal contract
- optional-source tolerance would hide genuinely unsafe behavior
- there is no summary contract or source classification to anchor the rendering policy

## Inputs

- a fixed set of required summary sources
- a fixed set of optional summary sources
- source loading rules that can detect missing files, parse failures, and schema mismatch
- one summary surface, report consumer, or smoke check

## Outputs

- explicit `required_missing_sources`
- explicit `optional_missing_sources`
- stable rendering behavior for missing or invalid optional sources
- strict failure only when required-source or other hard-contract conditions are violated

## Core procedure

1. Define which sources are required for the minimum useful surface.
2. Define which sources are optional enrichments.
3. Load required sources first and fail the strict contract if they are missing or unusable.
4. Load optional sources separately and track their status without promoting them to hard failure.
5. Render missing optional sources as `not available yet`.
6. Render invalid optional sources as warnings while keeping the main surface available.
7. Keep optional-source paths visible through fields such as `optional_missing_sources` so the absence is observable.
8. Treat soft-info artifacts such as companion markdown briefs separately from required JSON summaries so their absence does not escalate into warning or error by default.

## Contracts

- required and optional source sets are explicit
- required-source failure can trigger smoke or strict contract failure
- optional-source absence is observable but does not by itself fail the surface
- invalid optional sources produce warnings rather than silent omission
- backward-compatible fields such as `missing_sources` may alias required missing sources only
- soft-info artifacts such as `brief_md` are optional unless explicitly promoted to required
- the surface reads published summaries only and does not trigger new operational work as part of rendering
- this technique applies to summary-driven operator surfaces, CLI reports, and smoke policies; it is not a general UI style guideline

## Risks

### Failure modes

- an actually critical source is misclassified as optional
- optional-source absence is hidden completely instead of being surfaced explicitly

### Negative effects

- optional-source warnings can accumulate until the surface becomes noisy
- the rendering surface can drift away from its bounded summary role and become harder to trust

### Misuse patterns

- treating `optional` as meaning "never operationally important" rather than "visible but non-fatal for this contract"
- expanding the rendering surface so it performs actions rather than staying read-only

### Detection signals

- operators stop noticing missing-source signals because the warning stream is constant and unsorted
- the renderer starts adding retry, repair, or other mutating behavior to compensate for absent summaries

### Mitigations

- review required-versus-optional classification explicitly and promote sources when the contract changes
- keep warnings bounded, visible, and read-only so missing optional data stays observable without turning the surface into an action layer

## Validation

Verify the technique by confirming that:
- required missing sources and optional missing sources are reported separately
- missing required sources fail the strict smoke or contract path
- missing optional sources render as `not available yet`
- invalid optional sources surface warnings without taking down the whole surface
- optional soft-info artifacts remain non-blocking
- the surface still exposes source references so operators can navigate to the published artifact when available

See `checks/required-vs-optional-rendering-checklist.md`.
For source-backed origin proof, see `notes/origin-evidence.md`.
For bounded second-context adaptation guidance, see `notes/second-context-adaptation.md`.
For canonical-prep readiness, see `notes/canonical-readiness.md`.

## Adaptation notes

What can vary across projects:
- the exact required and optional source lists
- the wording of empty or warning states
- whether warnings are in logs, JSON summary fields, CLI sections, UI badges, or all four
- which soft-info artifacts are attached to a primary summary

Project-shaped details that should not be treated as invariant:
- the specific `Latest Metrics` panel structure used by `atm10-agent`
- the exact optional published sources such as remediation, integrity, or operating-cycle summaries
- the exact alias field names kept for backward compatibility
- the exact non-blocking soft-info artifact name such as `brief_md`

What should stay invariant:
- required and optional sources remain separate policy classes
- optional-source absence is visible but non-fatal
- invalid optional data yields warnings
- promotion from optional to required stays explicit and staged rather than silent
- read-only rendering does not expand into action execution

Within the G2 published-summary package, this technique is the rendering and contract policy for required versus optional published sources across operator panels, CLI reports, and smoke summaries. `AOA-T-0008` supplies one optional remediation surface, and `AOA-T-0010` supplies one optional diagnostic trust surface.

## Public sanitization notes

ATM10-specific Streamlit tab names, gateway summary names, local paths, and UI wording were generalized. The public version keeps the reusable rendering contract: required sources fail strictly, optional sources degrade gracefully, and soft-info artifacts stay non-blocking.

## Example

See `examples/minimal-required-vs-optional-rendering.md` and `examples/non-ui-required-vs-optional-rendering.md`.

## Checks

See `checks/required-vs-optional-rendering-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through operator-panel loading rules and smoke tests that separated `required_missing_sources` from `optional_missing_sources` and preserved non-blocking handling for optional summaries and `brief_md`
- promoted to `aoa-techniques` on 2026-03-14
- approved as `canonical` in `aoa-techniques` on 2026-03-15 after fresh public-safety review and default-use confirmation

## Future evolution

- add a companion technique for operator-facing artifact link panels
- add policy examples for multi-consumer staged promotion from optional to required
