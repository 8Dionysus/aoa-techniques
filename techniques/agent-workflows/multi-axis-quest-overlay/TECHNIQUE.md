---
id: AOA-T-0085
name: multi-axis-quest-overlay
domain: agent-workflows
kind: artifact
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-progression-lift/SKILL.md + skills/aoa-session-donor-harvest/references/rpg-reflection-posture.md
  note: Extracted from the session-harvest family where quest-, RPG-, and chronicle-shaped reflection is allowed as adjunct reading over reviewed progression evidence without replacing owner truth.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - progression
  - quest
  - overlay
  - reflection
summary: Add quest-, RPG-, or chronicle-shaped reflection to a bounded multi-axis progression result so route legibility improves without letting flavor overwrite owner truth, proof, or routing authority.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0084
  - type: complements
    target: AOA-T-0078
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# multi-axis-quest-overlay

## Intent

Add quest-, RPG-, or chronicle-shaped reflection to a bounded progression or
route-reading surface so the path becomes easier to read without letting flavor
overwrite owner truth, proof posture, or routing authority.

## When to use

- a reviewed session already produced a bounded progression delta or route reflection
- quest-, RPG-, or chronicle-shaped language would improve legibility
- the reflective layer should remain descriptive and adjunct rather than sovereign
- reviewers need to preserve narrative usefulness without minting authority

## When not to use

- no reviewed evidence exists underneath the overlay
- quest or RPG flavor is being used to grant rights, rank, or routing policy
- the route needs owner truth, proof, or memory decisions rather than reflective framing
- the overlay would turn every session into a campaign whether or not the evidence supports it

## Inputs

- one reviewed progression delta or other bounded reflective base
- optional quest hooks, chronicle cues, or unlock hints
- one explicit reminder of the underlying owner or proof truth

## Outputs

- one adjunct quest- or RPG-shaped reflection
- one or more narrative cues such as quest residue, campaign hint, chronicle stub, or ability-like unlock hint
- one explicit boundary note that owner truth remains elsewhere
- one rejection path for overlay ideas that would turn into authority claims

## Core procedure

1. Start from a bounded evidence-backed base such as a progression delta.
2. Layer quest or RPG language only after the underlying verdict is explicit.
3. Keep the overlay readable as adjunct reflection rather than rule or status law.
4. Allow narrative cues such as quest residue, chronicle stub, campaign hint, or safe unlock flavor only when they stay small.
5. Reject overlay language that grants rank, rights, or routing authority.
6. Preserve the underlying owner, proof, and memory seams as the real truth surfaces.

## Contracts

- the overlay always rests on reviewed evidence
- the overlay remains adjunct, not sovereign
- quest or RPG language does not replace owner-layer truth
- flavor does not grant authority rights
- the overlay remains smaller than the underlying progression or route-reading object

Relationship to adjacent techniques: unlike [AOA-T-0084](../progression-evidence-lift/TECHNIQUE.md), this technique does not decide the progression verdict or multi-axis movement; it only adds adjunct reflective framing. Unlike [AOA-T-0078](../decision-fork-cards/TECHNIQUE.md), it does not define the explicit route cards themselves; it can only make an already bounded route-reading surface more legible.

## Risks

### Failure modes

- narrative flavor starts replacing the underlying evidence-backed result
- unlock hints become disguised authority grants
- every session is forced into a campaign frame whether it fits or not

### Negative effects

- reflective language can distract from real owner or proof work
- teams may over-read flavor as status law
- too much quest framing can make a bounded reflective note feel theatrical

### Misuse patterns

- using RPG language to avoid explicit owner verdicts
- turning progression overlays into universal power rankings
- treating chronicle stubs as memory authority
- making flavor the only surviving output when the evidence is weak

### Detection signals

- the overlay has no visible underlying evidence-backed base
- quest or RPG words are doing authority work
- narrative cues are larger than the underlying progression or route note
- reviewers cannot say what remains reflection versus what remains real

### Mitigations

- require a bounded underlying base
- keep narrative cues small
- reject authority-bearing flavor
- preserve owner, proof, and routing seams as the real truth surfaces

## Validation

Verify the technique by confirming that:
- the overlay rests on reviewed evidence
- the underlying progression or route note remains explicit
- flavor remains adjunct rather than sovereign
- no rank, rights, or routing authority is granted through narrative language
- narrative cues stay small and reviewable

See `checks/multi-axis-quest-overlay-checklist.md`.

## Adaptation notes

What can vary across projects:
- the quest or RPG vocabulary
- whether the overlay reads as a quest hook, chronicle stub, or campaign hint
- the names of safe unlock hints
- whether the base object is progression-first or route-first

What should stay invariant:
- the overlay rests on reviewed evidence
- flavor remains adjunct
- owner and proof truth remain elsewhere
- narrative cues stay small

Project-shaped details that should not be treated as invariant:
- one game's rank ladder
- one campaign-board format
- one status hierarchy
- one local chronicle store

AoA adaptation example:
- common adjunct cues include quest residue, quest hook, questline hint, chronicle stub, ability-like unlock hint, or feat-like hint
- the underlying owner layer still decides what artifact is real

## Public sanitization notes

This public bundle keeps only the reusable reflective overlay seam: quest- or RPG-shaped cues layered over reviewed evidence while owner truth remains elsewhere. AoA-specific lore, repo-specific campaign boards, and skill wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-multi-axis-quest-overlay.md`.

## Checks

See `checks/multi-axis-quest-overlay-checklist.md`.

## Promotion history

- born in `aoa-skills` as the reflective-overlay half of `aoa-session-progression-lift` and the family-wide RPG reflection posture
- extracted into `aoa-techniques` on 2026-04-05 as a bounded adjunct quest-overlay technique

## Future evolution

- keep progression evidence separate through `AOA-T-0084`
- keep explicit route-card meaning separate through `AOA-T-0078`
- add a second live context that uses the same adjunct quest-overlay seam outside the current AoA session-harvest lineage
