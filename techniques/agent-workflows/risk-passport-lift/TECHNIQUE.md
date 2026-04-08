---
id: AOA-T-0079
name: risk-passport-lift
domain: agent-workflows
kind: assessment
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-route-forks/SKILL.md + skills/aoa-session-route-forks/checks/review.md
  note: Extracted from the aoa-session-route-forks skill where each branch carries a small route passport with difficulty, risk, control mode, delegate tier, and stop-condition posture.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - risk
  - passport
  - branching
  - control-mode
summary: Attach one small risk passport to each explicit next route so difficulty, risk, control mode, delegate tier, and stop-condition posture stay visible without turning branch analysis into hidden routing policy.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0078
  - type: complements
    target: AOA-T-0083
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# risk-passport-lift

## Intent

Attach one small risk passport to each explicit next route so route choice
keeps bounded control posture, difficulty, and stop-condition visibility
instead of dissolving into vague risk prose or hidden planner metadata.

## When to use

- explicit next routes already exist and need a smaller per-route posture summary
- reviewers need to compare difficulty, risk, control mode, delegate tier, or stop-condition posture across branches
- branch analysis should remain visible without inflating into a full routing system
- the main need is route posture metadata, not the branch-card seam itself

## When not to use

- there is only one route and no meaningful comparison surface
- the real need is donor extraction, diagnosis, repair, or scenario design
- the route passport would become a hidden authority score
- the team needs a full operational runbook rather than a small branch posture summary

## Inputs

- one explicit next route
- route-level gain and cost summary
- known risk signals and blockers
- desired control mode or approval posture
- any already known delegate tier or escalation cue

## Outputs

- one small route passport
- one difficulty cue
- one risk cue
- one control-mode cue
- one delegate-tier cue
- one stop-condition cue

## Core procedure

1. Start from one explicit route rather than from a whole route set.
2. Name only the smallest posture fields that help comparison and review.
3. Keep the passport short enough to sit alongside a branch card instead of replacing it.
4. Record stop conditions whenever risk or cost meaningfully rises.
5. Reject fake precision such as synthetic scores that pretend to be authority.
6. Keep the passport readable as posture metadata rather than hidden routing policy.

## Contracts

- one passport belongs to one route
- the passport stays smaller than the branch card it complements
- risk posture remains descriptive, not sovereign
- stop conditions remain explicit when risk or cost is meaningful
- the passport informs branch choice but does not decide authority by itself

Relationship to adjacent techniques: unlike [AOA-T-0078](../decision-fork-cards/TECHNIQUE.md), this technique does not decide which materially distinct branches exist; it only keeps route posture metadata small and explicit per branch. Unlike [AOA-T-0083](../checkpoint-bound-self-repair/TECHNIQUE.md), it does not govern mutation checkpoints over a repair packet; it only lifts comparison-ready route posture.

## Risks

### Failure modes

- the passport becomes a hidden scorecard instead of a small posture summary
- stop conditions disappear and risk becomes decorative
- too many metadata fields make the passport larger than the route itself

### Negative effects

- fake precision can create false confidence
- passport proliferation can over-formalize obvious routes
- teams may treat control mode or delegate tier as sovereign routing authority

### Misuse patterns

- attaching passports before any route is honestly explicit
- using passport fields as command dispatch policy
- inflating posture fields into a full runbook
- flattening uncertainty into one synthetic risk score

### Detection signals

- passports contain more metadata than route meaning
- reviewers cannot explain what changed when a route passport changes
- stop conditions or uncertainty cues are missing
- difficulty or risk labels are treated as final authority instead of comparison help

### Mitigations

- keep the field set small
- require one stop-condition cue when risk is meaningful
- reject synthetic total scores
- keep passports adjacent to branch cards instead of replacing them

## Validation

Verify the technique by confirming that:
- each passport belongs to one explicit route
- the field set stays small and reviewable
- difficulty, risk, control mode, delegate tier, and stop-condition cues remain visible where needed
- the passport does not become hidden routing authority

See `checks/risk-passport-lift-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of difficulty or risk bands
- the control-mode vocabulary
- whether delegate tier is numeric, named, or absent
- the exact passport rendering format

What should stay invariant:
- one passport belongs to one route
- the passport stays small
- risk posture remains descriptive
- stop-condition cues remain visible for meaningful risk

Project-shaped details that should not be treated as invariant:
- one planner schema
- one orchestration permission model
- one repo-specific approval ladder
- one project's routing engine

AoA adaptation example:
- passports often carry `difficulty`, `risk`, `control_mode`, and `delegate_tier`
- the same posture language may later appear in repair packets, but route choice and repair checkpoints remain separate seams

## Public sanitization notes

This public bundle keeps only the reusable route-passport seam: one explicit route, one small posture summary, and visible stop-condition cues. AoA field names, local approval ladders, and planner wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-risk-passport-lift.md`.

## Checks

See `checks/risk-passport-lift-checklist.md`.

## Promotion history

- born in `aoa-skills` as the route-passport half of `aoa-session-route-forks`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded per-route posture technique

## Future evolution

- keep branch-card meaning separate through `AOA-T-0078`
- keep repair checkpoints separate through `AOA-T-0083`
- add a second live context that uses the same small per-route posture seam outside the current AoA session-harvest lineage
