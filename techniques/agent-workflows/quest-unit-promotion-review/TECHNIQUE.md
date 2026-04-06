---
id: AOA-T-0089
name: quest-unit-promotion-review
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-quest-harvest/SKILL.md + skills/aoa-quest-harvest/techniques.yaml + skills/aoa-quest-harvest/references/promotion-outcomes.md
  note: Extracted from the aoa-quest-harvest skill where one repeated reviewed quest unit receives one bounded promotion verdict without collapsing owner layers.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - quest
  - promotion
  - reviewed-work
  - boundaries
summary: Review one repeated reviewed quest unit and emit one bounded promotion verdict so leaf workflow, route, role, proof, and recall surfaces do not collapse into generic reuse pressure.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-06
export_ready: true
relations:
  - type: complements
    target: AOA-T-0090
  - type: complements
    target: AOA-T-0076
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# quest-unit-promotion-review

## Intent

Review one repeated, reviewed quest-shaped unit and decide whether it should
stay a quest or be promoted into the next honest owner surface.

## When to use

- one repeated reviewed quest unit is already isolated from the wider session
  family
- the remaining question is the final promotion target rather than donor
  extraction, automation fit, fork routing, diagnosis, or repair
- the reviewer must distinguish leaf workflow, route, role, proof, and recall
  shapes without collapsing them
- the output needs one bounded verdict instead of more exploratory discussion

## When not to use

- the route is still active, unreviewed, or only happened once
- the source still contains several mixed reusable units
- the real need is already straightforward authoring in the chosen owner layer
- the work is mainly a theme cloud with no bounded repeated unit

## Inputs

- one repeated reviewed quest unit
- one reviewed harvest pack, run summary, or equivalent evidence packet
- repeat count and repeat shape
- current owner-layer candidates
- known ambiguity, risk, or defer signals

## Outputs

- one bounded promotion verdict
- one chosen owner repo and next surface
- one short reason for the chosen target
- one defer or keep-quest posture when promotion is still premature

## Core procedure

1. Start from one repeated reviewed quest unit rather than from raw session history.
2. Re-state what repeated: leaf workflow, route, proof pattern, recall pattern, or boundary law.
3. Reject topic-only repetition and aesthetic similarity when no reusable unit survives.
4. Match the repeated unit to the owner shape that fits best: `skill`, `playbook`, `agent`, `eval`, `memo`, or `quest`.
5. Keep `quest` or `defer` when repeat signal, ownership, or boundary safety remains weak.
6. Emit one verdict with one chosen owner repo and one next surface.

## Contracts

- the technique starts after review and after the repeated unit is already isolated
- one repeated unit receives one promotion verdict
- verdicts stay bounded to owner placement, not authorship completion
- `quest` and `defer` remain valid outputs
- active quest state does not become canon merely because repetition exists

Relationship to adjacent techniques: unlike [AOA-T-0076](../owner-layer-triage/TECHNIQUE.md), this technique starts from an already repeated quest unit and closes the final promotion verdict rather than performing a first owner-placement pass over any reusable unit. Unlike [AOA-T-0090](../nearest-wrong-target-rejection/TECHNIQUE.md), it owns the chosen promotion verdict itself rather than the explicit rejection pattern that keeps adjacent targets honest.

## Risks

### Failure modes

- a mixed or weakly repeated unit is treated as promotion-ready
- the verdict reflects convenience or excitement rather than the honest owner shape
- the unit is promoted before review evidence is stable

### Negative effects

- premature promotion can create canon debt in the wrong repo
- repeated discussion can be mistaken for repeated work
- quest pressure can hide the need to keep or reopen a quest

### Misuse patterns

- treating one strong run as enough evidence
- using the technique before donor extraction or bounded review exists
- promoting a scenario route into a skill because it feels executable
- treating proof or memory posture as workflow meaning

### Detection signals

- the repeated unit is not named explicitly
- reviewers cannot explain why the chosen owner fits better than staying a quest
- the next surface is larger than the verdict requires
- the route still needs wider session-family work before triage

### Mitigations

- require one isolated repeated unit
- preserve `quest` and `defer` as honest results
- keep the verdict smaller than the authored next surface
- pair the verdict with explicit nearest-wrong-target rejection

## Validation

Verify the technique by confirming that:
- one repeated reviewed unit is named explicitly
- the chosen owner target matches the repeat shape
- keep-quest or defer posture remains available
- the verdict stays smaller than the authored next surface
- the source material was reviewed before triage

See `checks/quest-unit-promotion-review-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of owner layers
- how repeat count is represented
- whether the output is markdown, YAML, or JSON
- whether local policy asks for extra approval before authoring

What should stay invariant:
- the technique starts after review
- one repeated unit gets one verdict
- keep-quest and defer remain available
- the verdict stays smaller than the authored destination

Project-shaped details that should not be treated as invariant:
- one repo layout
- one questboard vocabulary
- one local naming scheme for packets or verdict files
- one downstream authoring workflow

AoA adaptation example:
- leaf executable workflow usually maps to `aoa-skills`
- recurring route usually maps to `aoa-playbooks`
- role or actor-boundary law usually maps to `aoa-agents`
- proof posture usually maps to `aoa-evals`
- recall or writeback posture usually maps to `aoa-memo`
- weak or mixed repetition can stay a quest

## Public sanitization notes

This public bundle keeps only the reusable final-promotion seam: one repeated
reviewed quest unit, one bounded verdict, and one honest keep-or-promote
decision. AoA repo names, packet wrappers, and local runtime invocation details
were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-quest-unit-promotion-review.md`.

## Checks

See `checks/quest-unit-promotion-review-checklist.md`.

## Promotion history

- born in `aoa-skills` as the verdict spine of `aoa-quest-harvest`
- extracted into `aoa-techniques` on 2026-04-06 as a bounded final-promotion review over one repeated quest unit

## Future evolution

- keep nearest-wrong-target rejection separate through `AOA-T-0090`
- add a second live context outside the current AoA session-harvest family
- keep authorship, drafting, and downstream repo doctrine outside this bundle
