---
id: AOA-T-0098
name: receipt-first-failure-analysis
domain: validation-patterns
status: promoted
origin:
  project: ATM10-Agent
  path: docs/ANTIFRAGILITY_FIRST_WAVE.md
  note: Generalized from first-wave stressor review work where the safest starting point was the owner-local receipt rather than retrospective summary or dashboard narrative.
owners:
  - 8Dionysus
tags:
  - antifragility
  - validation
  - receipts
  - failure-analysis
summary: Start failure review from source-owned receipts, separate facts from hypotheses, and tie any recovery change to explicit evidence rather than folklore or dashboard mythology.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-07
export_ready: true
relations:
  - type: complements
    target: AOA-T-0097
  - type: complements
    target: AOA-T-0015
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
---

# receipt-first-failure-analysis

## Intent

Turn failure review into bounded evidence-led iteration by starting from source-owned receipts, separating facts from guesses, and defining improvement checks before any remediation story becomes credible.

## When to use

- a degraded run completed and needs explicit follow-up learning
- the same stressor family repeats across a bounded window
- a team needs to decide whether one change deserves promotion
- a later eval or derived stats view needs owner-local grounding

## When not to use

- the repo does not yet emit any trustworthy source-owned receipt surface
- the main need is immediate runtime containment rather than post-event analysis
- the review is trying to prove broad quality rather than explain one bounded failure family
- a dashboard aggregate is being mistaken for primary evidence

## Inputs

- source-owned stressor receipts
- owner-local run artifacts
- optional adaptation deltas
- optional bounded eval reports

## Outputs

- one named stressor family
- one bounded hypothesis for improvement
- one explicit change candidate
- one verification plan tied to receipts or eval outputs

## Core procedure

1. collect owner-local receipts before opening summaries or narrative dashboards
2. group events by named family, surface, degraded mode, or blocked-mutation posture
3. separate facts backed by receipts or artifacts from guesses that remain hypotheses
4. identify the narrowest plausible change rather than a sprawling theory patch
5. define how improvement will be checked the next time the stressor appears
6. publish an adaptation delta only when a reviewed change actually lands

## Contracts

- source-owned receipts remain the first trustworthy object after the stress event
- facts and hypotheses stay explicitly separated
- proposed changes stay narrower than the observed failure family
- improvement checks name the future receipt or eval path that should show the difference
- adaptation deltas do not exist without originating receipts

## Risks

### Failure modes

- dashboards, memory, or retrospective summaries replace source-owned evidence
- causality claims are made from raw log volume or anecdotal recollection alone
- adaptation deltas get written without a clear receipt lineage

### Negative effects

- evidence-led review can feel slower than jumping straight to a fix
- repeated receipt review can bias teams toward only what is already instrumented
- narrow hypotheses can look under-ambitious when broader architecture frustration is high

### Misuse patterns

- treating a summary aggregate as if it were the owner-local source
- collapsing several stressor families into one prestige narrative
- calling a remediation idea verified before the next receipt or eval surface shows improvement

### Detection signals

- reviewers cannot point to the originating receipts for a proposed change
- change candidates widen across several unrelated surfaces at once
- the writeup states strong causal conclusions but cites only dashboards or memory

### Mitigations

- start every bounded review from the receipt set itself
- keep change candidates as small as the evidence honestly supports
- require an explicit future verification path before calling a remediation plan credible

## Validation

Verify the technique by confirming that:
- the originating receipts are named explicitly
- facts and hypotheses remain separate in the review
- the proposed change is narrower than the stressor family under discussion
- the improvement check names a future receipt or eval surface
- any adaptation delta cites the original receipt lineage

## Adaptation notes

What can vary across projects:
- receipt schema details
- how stressor families are grouped
- whether follow-up checks land in receipts, evals, or both
- which surfaces are eligible remediation targets

What should stay invariant:
- receipt-first reading
- explicit separation of facts from guesses
- narrow change hypotheses
- explicit future verification path

## Public sanitization notes

The public bundle removes project-local dashboards, logs, and runtime detail while preserving the reusable evidence-led review pattern.

## Example

See `examples/minimal-receipt-review.md`.

## Checks

See `checks/receipt-first-failure-analysis-checklist.md`.

## Promotion history

- born from first-wave antifragility review needs around `ATM10-Agent`
- promoted into `aoa-techniques` as a reusable validation pattern on 2026-04-07

## Future evolution

- add a second context with repeated-window evidence rather than one family only
- connect more explicitly to adaptation-delta review patterns
- clarify where this pattern stops and `aoa-evals` begins
