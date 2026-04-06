---
id: AOA-T-0081
name: diagnosis-from-reviewed-evidence
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-self-diagnose/SKILL.md + skills/aoa-session-self-diagnose/techniques.yaml
  note: Extracted from the aoa-session-self-diagnose skill where reviewed friction evidence becomes a diagnosis packet with symptoms, probable causes, owner hints, and explicit unknowns.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - diagnosis
  - reviewed-evidence
  - read-only
  - post-session
summary: Turn reviewed friction evidence into a bounded diagnosis packet that separates symptoms from probable causes, preserves unknowns, and names likely owner hints without mutating anything yet.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0080
  - type: complements
    target: AOA-T-0082
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# diagnosis-from-reviewed-evidence

## Intent

Turn reviewed friction evidence into a bounded diagnosis packet so symptoms,
probable causes, owner hints, and explicit unknowns become legible before any
repair work starts.

## When to use

- the session is reviewed and repeated friction or contradiction survived it
- the next honest move is diagnosis before repair
- probable causes need to be named without pretending certainty the evidence does not support
- the workflow needs likely owner hints without treating them as final verdicts

## When not to use

- the session is still live or unreviewed
- diagnosis already exists and the next honest move is repair
- the work only needs one drift taxonomy pass without a full diagnosis packet
- the real need is a final promotion verdict instead of a read-only diagnosis

## Inputs

- one reviewed session artifact or harvest packet
- explicit symptoms, frictions, contradictions, or failures
- any drift taxonomy already available
- touched owner layers or repos if known
- previous related evidence if available

## Outputs

- one `DIAGNOSIS_PACKET`
- one symptom list
- one probable-cause layer with explicit uncertainty where needed
- one likely owner hint set
- one suggested repair shape
- one unknowns section when evidence remains incomplete

## Core procedure

1. Start from reviewed evidence rather than live debugging.
2. Gather symptoms and evidence refs before stating any cause.
3. Keep symptoms separate from probable causes.
4. Use drift taxonomy as a bounded input when it helps, but do not confuse labels with diagnosis.
5. Map likely owner hints only after the diagnosis shape is visible.
6. Suggest a repair shape without silently performing it.
7. Preserve unknowns and probabilities where evidence is thin.
8. Keep the diagnosis packet read-only and reviewable.

## Contracts

- diagnosis starts from reviewed evidence
- symptom and probable-cause layers stay distinct
- probable causes remain probabilistic when the evidence is thin
- owner hints do not override later owner-layer law
- diagnosis is read-only and must not silently mutate anything
- unknowns remain valid outputs when the evidence is incomplete

Relationship to adjacent techniques: unlike [AOA-T-0080](../session-drift-taxonomy/TECHNIQUE.md), this technique owns the full diagnosis packet rather than just the drift label layer. Unlike [AOA-T-0082](../repair-shape-from-diagnosis/TECHNIQUE.md), it does not choose the smallest repair packet or checkpoint posture; it only prepares the diagnosis that later repair work can consume.

## Risks

### Failure modes

- symptoms and causes collapse into one vague narrative
- owner hints are stated as if they were already final verdicts
- diagnosis starts performing repair work implicitly

### Negative effects

- overconfident diagnosis can make weak evidence look settled
- repeated diagnosis passes can create ritual delay when repair is already justified
- teams may mistake a likely cause for a proven cause

### Misuse patterns

- using diagnosis as a replacement for repair planning
- naming one convenient owner layer before the evidence supports it
- turning one anecdote into structural certainty
- silently fixing the problem while writing the diagnosis

### Detection signals

- the packet has no explicit unknowns even though evidence is mixed
- symptoms and causes are worded as if they were the same thing
- the diagnosis output already contains repair commands or silent edits
- reviewers cannot explain what evidence supports each probable cause

### Mitigations

- require evidence refs for meaningful symptoms
- keep probable-cause language explicitly probabilistic when needed
- preserve owner hints as hints, not verdicts
- hand off to repair instead of smuggling mutation into diagnosis

## Validation

Verify the technique by confirming that:
- the source evidence is reviewed and bounded
- symptoms and probable causes stay distinct
- likely owner hints remain explicit but non-sovereign
- suggested repair shapes remain suggestions rather than hidden mutations
- unknowns remain visible where the evidence is incomplete

See `checks/diagnosis-from-reviewed-evidence-checklist.md`.

## Adaptation notes

What can vary across projects:
- the diagnosis packet format
- whether drift taxonomy is inline or referenced
- how likely owner hints are named
- whether severity or urgency notes are included

What should stay invariant:
- diagnosis starts after review
- symptoms and causes remain separate
- mutation stays out of the diagnosis pass
- unknowns remain available

Project-shaped details that should not be treated as invariant:
- one incident template
- one repo naming scheme for owner hints
- one escalation ladder
- one proof rubric

AoA adaptation example:
- likely owner hints often point toward `aoa-skills`, `aoa-techniques`, `aoa-evals`, or `aoa-agents`
- suggested repair shapes may later feed a bounded repair packet instead of immediate mutation

## Public sanitization notes

This public bundle keeps only the reusable diagnosis seam: reviewed evidence, separated symptoms and causes, explicit unknowns, likely owner hints, and no hidden mutation. AoA repo names, local remediation workflows, and skill invocation wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-diagnosis-from-reviewed-evidence.md`.

## Checks

See `checks/diagnosis-from-reviewed-evidence-checklist.md`.

## Promotion history

- born in `aoa-skills` as the diagnosis-packet half of `aoa-session-self-diagnose`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded read-only diagnosis workflow

## Future evolution

- keep drift taxonomy separate through `AOA-T-0080`
- keep repair packet planning separate through `AOA-T-0082`
- add a second live context that uses the same diagnosis-from-reviewed-evidence seam outside the current AoA session-harvest lineage
