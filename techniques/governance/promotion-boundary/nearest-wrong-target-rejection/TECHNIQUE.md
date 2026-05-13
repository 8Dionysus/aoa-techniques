---
id: AOA-T-0090
name: nearest-wrong-target-rejection
domain: agent-workflows
kind: guardrail
status: canonical
origin:
  project: aoa-skills
  path: skills/aoa-quest-harvest/SKILL.md + skills/aoa-quest-harvest/references/promotion-outcomes.md + skills/aoa-quest-harvest/checks/review.md
  note: Extracted from the aoa-quest-harvest skill where the chosen owner target is paired with an explicit rejected nearest-wrong target to keep adjacent layers distinct under promotion pressure.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - boundaries
  - promotion
  - rejection
  - review
summary: Reject the nearest wrong promotion target explicitly so repeated reviewed work does not collapse into the most convenient adjacent owner layer.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-05-12
export_ready: true
relations:
  - type: complements
    target: AOA-T-0089
  - type: complements
    target: AOA-T-0076
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
---

# nearest-wrong-target-rejection

## Intent

Make the nearest wrong target explicit when writing a bounded owner or
promotion verdict so adjacent layers stay visibly distinct under reuse
pressure.

## When to use

- one chosen owner or promotion target already looks plausible, but at least
  one adjacent target also feels tempting
- reviewers need to explain not only why the chosen target fits, but why the
  closest wrong target does not
- the workflow risks collapsing `skill`, `playbook`, `agent`, `eval`, `memo`,
  or `quest` into one convenience surface

## When not to use

- there is no meaningful adjacent target to reject
- the real need is still donor extraction, diagnosis, or first owner placement
- the work is so under-specified that any chosen target would be fake certainty

## Inputs

- one chosen owner or promotion target
- one bounded unit that target claims to fit
- at least one adjacent plausible target that feels tempting
- one short boundary reason that can distinguish the chosen target from the rejected one

## Outputs

- one explicitly rejected nearest-wrong target
- one short reason why that target is wrong
- one clearer boundary around the chosen target

## Core procedure

1. Start from one chosen owner or promotion verdict.
2. Ask which adjacent target would be easiest to confuse with the chosen one.
3. Name that target explicitly instead of leaving it implicit.
4. Write one short reason why it is wrong for this bounded unit.
5. Keep the rejection small, concrete, and boundary-focused rather than rhetorical.
6. If no honest chosen target exists yet, fall back to `hold`, `quest`, or `defer` rather than inventing a fake rejection pair.

## Contracts

- the rejection stays paired to one chosen target
- the rejected target must be adjacent and plausible, not theatrical
- the reason for rejection stays boundary-focused
- the technique strengthens one verdict; it does not replace the verdict workflow

Relationship to adjacent techniques: unlike [AOA-T-0076](../../decision-routing/owner-layer-triage/TECHNIQUE.md), this technique does not decide the full placement verdict; it only strengthens that verdict by naming the nearest wrong target. Unlike [AOA-T-0089](../quest-unit-promotion-review/TECHNIQUE.md), it does not choose the final quest-promotion outcome; it makes the rejected adjacent outcome explicit once a chosen target already exists.

## Risks

### Failure modes

- the rejected target is not actually the nearest wrong one
- the rejection reason is vague and does not clarify the boundary
- the technique is used to defend a weak verdict instead of improving it

### Negative effects

- forced rejection can create false certainty when the right answer is still `defer`
- reviewers may pick a dramatic wrong target instead of the closest one
- repeated rhetoric can replace concrete boundary reasoning

### Misuse patterns

- naming a strawman target no one would actually confuse with the chosen one
- using rejection language to hide that the chosen target is also weak
- widening the rejection into a long anti-pattern essay inside a small verdict

### Detection signals

- the rejected target is too distant from the chosen one to teach anything
- the rejection reason cannot point to a boundary difference
- reviewers still argue about the same adjacent target after reading the verdict

### Mitigations

- require the rejected target to be adjacent and plausible
- keep the rejection reason short and boundary-shaped
- fall back to `hold`, `quest`, or `defer` when no honest chosen target exists
- use the rejection to clarify the chosen boundary, not to decorate the verdict

## Validation

Verify the technique by confirming that:
- the rejected target is adjacent and plausible
- the rejection reason clarifies one concrete boundary
- the chosen target becomes clearer after the rejection is added
- `hold`, `quest`, or `defer` remain available when the whole verdict is weak

See `checks/nearest-wrong-target-rejection-checklist.md`.

## Adaptation notes

What can vary across projects:
- the set of adjacent targets in scope
- how rejection reasons are written
- whether the rejection appears inline or in a sidecar field

What should stay invariant:
- the rejected target is plausible and adjacent
- the rejection reason clarifies a boundary
- the technique stays smaller than the chosen verdict workflow

Project-shaped details that should not be treated as invariant:
- one owner-layer taxonomy
- one repo naming scheme
- one review template
- one packet format

AoA adaptation example:
- `promote_to_playbook` may reject `promote_to_skill` when the repeated unit is route-shaped
- `promote_to_skill` may reject `promote_to_playbook` when the repeated unit is leaf-workflow-shaped
- `keep_quest` may reject `promote_to_skill` when repetition is still weak or mixed

## Public sanitization notes

This public bundle keeps only the reusable rejection seam: name the nearest
wrong adjacent target and give one small boundary reason. AoA repo names,
verdict wrappers, and local review templates were reduced to adaptation
examples or kept out of the invariant core.

## Example

See `examples/minimal-nearest-wrong-target-rejection.md`.

## Checks

See `checks/nearest-wrong-target-rejection-checklist.md`.

## Promotion history

- born in `aoa-skills` as the rejection half of `aoa-quest-harvest`
- extracted into `aoa-techniques` on 2026-04-06 as a bounded nearest-wrong-target clarification technique
- promoted to `canonical` on 2026-05-12 after `aoa-playbooks`, `aoa-techniques` quest carry, and supporting `aoa-evals` owner-fit surfaces used explicit nearest-wrong rejection to prevent convenience promotion into skill, memo, KAG, routing, proof, or playbook authority

## Future evolution

- keep final promotion review separate through `AOA-T-0089`
- keep long-form anti-pattern doctrine outside this bundle
- keep nearest-wrong rejection paired to one chosen verdict when downstream consumers use it for owner follow-through, quest carry, or proof review
