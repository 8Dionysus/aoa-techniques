---
id: AOA-T-0078
name: decision-fork-cards
domain: agent-workflows
kind: assessment
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-route-forks/SKILL.md + skills/aoa-session-route-forks/techniques.yaml
  note: Extracted from the aoa-session-route-forks skill where several plausible next routes are rendered as explicit branch cards rather than one hidden recommendation.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - forks
  - branching
  - post-session
  - decision-support
summary: Turn one reviewed session or harvest packet into explicit decision fork cards so materially different next routes stay visible with gains, costs, owner targets, and stop conditions instead of collapsing into one hidden recommendation.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0079
  - type: complements
    target: AOA-T-0077
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# decision-fork-cards

## Intent

Turn one reviewed session or harvest packet into explicit decision fork cards
so materially different next routes stay legible and reviewable instead of
being buried in one favored recommendation.

## When to use

- the session is already reviewed and more than one honest next route remains
- different branches have meaningfully different gains, costs, risks, or owner targets
- reviewers need visible choice architecture rather than one compressed recommendation
- the route needs bounded branch analysis without turning branch cards into runtime policy

## When not to use

- there is only one obvious next bounded move
- donor extraction or packet shaping still has not happened
- the real need is diagnosis, repair, progression reflection, or final quest promotion
- the branch surface would only restate cosmetic variants of the same move

## Inputs

- one reviewed session artifact or bounded harvest packet
- one set of candidate next routes
- known blockers, dependencies, and uncertainty notes
- any already named owner targets or control posture preferences

## Outputs

- one fork card per materially different route
- one likely gain, cost, and risk for each route
- one likely first owner target for each route
- one explicit stop condition for risky or expensive routes
- one hold, defer, or reanchor route when uncertainty is still honest

## Core procedure

1. Start from reviewed evidence rather than free speculation.
2. Split routes until each card describes one materially distinct next move.
3. Reject cosmetic variants that only rename the same route.
4. Name the likely first owner target for each surviving route.
5. Record at least one likely gain, one likely cost, and one likely risk for each route.
6. Keep stop conditions visible for risky, expensive, or uncertain routes.
7. Preserve a hold, defer, or reanchor card when the honest outcome is still uncertainty.
8. Keep the card set legible as branch analysis rather than hidden routing authority.

## Contracts

- fork cards describe choices; they do not decide authority
- each card must represent one materially distinct route
- visible downside is required, not optional polish
- stop conditions remain first-class for risky routes
- a default route may be suggested, but alternatives must remain visible

Relationship to adjacent techniques: unlike [AOA-T-0077](../harvest-packet-contract/TECHNIQUE.md), this technique does not define the nucleus packet shape; it assumes the source packet or reviewed artifact already exists. Unlike [AOA-T-0079](../risk-passport-lift/TECHNIQUE.md), it owns the branch cards themselves rather than the smaller per-route passport fields. It should stay narrower than playbook design because it keeps next-route choices legible without authoring a full recurring scenario.

## Risks

### Failure modes

- the cards describe variants of the same route instead of real forks
- a favorite branch is smuggled in as if alternatives do not exist
- routes omit visible costs or risks and become optimism theater

### Negative effects

- too many thin cards can create fake complexity
- card sets can encourage analysis loops when one route is already obvious
- teams may confuse fork cards with runtime routing policy

### Misuse patterns

- writing branch cards before donor extraction or reviewed evidence exists
- using fork cards to hide an already decided route
- flattening large playbook design into a handful of vague route cards
- treating quest-board language as execution authority

### Detection signals

- several cards differ only cosmetically
- reviewers cannot explain why one branch is distinct from another
- costs, risks, or stop conditions are missing from the route set
- the cards read like policy or command selection rather than choice support

### Mitigations

- require materially different routes
- keep at least one downside visible per route
- preserve hold or defer as a valid card
- keep route-card output bounded to next-step analysis rather than full scenario design

## Validation

Verify the technique by confirming that:
- the source material is reviewed
- each card represents a materially distinct route
- each route names gains, costs, risks, and owner target cues
- stop conditions exist for risky routes
- hold, defer, or reanchor remains available when uncertainty is real

See `checks/decision-fork-cards-checklist.md`.

## Adaptation notes

What can vary across projects:
- the card format
- the names of owner targets
- how costs and risks are scored or labeled
- whether one default route is allowed in addition to visible alternatives

What should stay invariant:
- branch cards start after review
- each card remains materially distinct
- downside remains visible
- cards stay advisory rather than authoritative

Project-shaped details that should not be treated as invariant:
- one quest-board vocabulary
- one delegate-tier system
- one repo naming scheme
- one routing engine or planner

AoA adaptation example:
- fork cards often point toward `aoa-techniques`, `aoa-skills`, `aoa-playbooks`, or `hold`
- route passports may later refine difficulty, risk, control mode, or delegate tier
- quest-board language may help legibility, but it does not replace owner truth

## Public sanitization notes

This public bundle keeps only the reusable branch-card seam: one reviewed source, several materially distinct next routes, visible upside and downside, and clear stop conditions. AoA repo names, quest-board wrappers, and local routing posture were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-decision-fork-cards.md`.

## Checks

See `checks/decision-fork-cards-checklist.md`.

## Promotion history

- born in `aoa-skills` as the branch-card half of `aoa-session-route-forks`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded post-session branch-analysis workflow

## Future evolution

- keep route passports smaller through `AOA-T-0079` instead of widening this bundle into policy metadata
- keep playbook-scale scenario design outside this bundle
- add a second live context that uses the same explicit branch-card seam outside the current AoA session-harvest lineage
