---
id: AOA-T-0102
name: skill-proposal-handoff-packet
domain: agent-workflows
kind: handoff
status: canonical
origin:
  project: aoa-techniques
  path: mechanics/method-growth/parts/technique-to-skill-handoff/README.md + mechanics/method-growth/PROVENANCE.md
  note: Extracted from the Method-growth handoff surface where technique-side adoption pressure may request a skill proposal while technique canon and skill execution remain separate owner truths.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - method-growth
  - skill-proposal
  - handoff
  - owner-boundary
summary: Emit one bounded skill-proposal handoff packet from a technique-side adoption review so reusable practice does not become skill acceptance or activation by implication.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-05-13
export_ready: true
relations:
  - type: complements
    target: AOA-T-0040
  - type: complements
    target: AOA-T-0087
  - type: complements
    target: AOA-T-0101
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

# skill-proposal-handoff-packet

## Intent

Turn one technique-side adoption pressure into a bounded skill-proposal handoff
packet, so the receiving skill owner gets enough trigger, workflow, dependency,
risk, and verification context without treating the packet as skill acceptance
or activation.

## When to use

- a reusable technique or technique candidate is repeatedly needed as part of
  agent-facing execution
- an adoption review shows that the practice may need skill packaging, but the
  skill owner has not accepted or authored a skill yet
- reviewers need to preserve technique dependencies, trigger boundaries, risk
  posture, and verification hints for the receiving owner
- the next honest artifact is a proposal packet rather than a live skill,
  playbook, eval, route, memory object, or runtime change
- the handoff must stay portable for a skill-owning layer outside the origin
  project

## When not to use

- the source material is still several unrelated practices or workflow needs
- the real task is choosing whether the object is a technique, skill, playbook,
  eval, route, memory object, or role contract
- the receiving skill owner has already accepted the skill and only needs
  implementation work
- the request is to activate a skill, install a runtime command, or grant
  durable agent behavior
- the reusable practice still lacks enough evidence to justify a skill-shaped
  proposal

## Inputs

- one technique, technique candidate, or adopted practice under review
- the execution pressure that suggests skill packaging may help
- technique dependency references or equivalent practice anchors
- a proposed trigger boundary for when the skill would be selected
- a sketch of inputs, outputs, and workflow shape
- known risks, approval seams, rollback needs, and verification hints
- the intended receiving owner or skill-owning surface

## Outputs

- one skill-proposal handoff packet
- explicit technique dependency references
- one proposed skill trigger boundary
- one compact workflow-shape sketch with inputs and outputs
- risk, approval, rollback, and verification notes for owner review
- a non-acceptance stop-line stating that the packet does not create, approve,
  or activate a skill

## Core procedure

1. Start from one named reusable practice. Split or defer if several practices
   are still fused together.
2. State the execution pressure that makes a skill proposal plausible: repeated
   agent-facing use, workflow packaging, tool choreography, approval posture, or
   verification needs.
3. Name the receiving skill owner and the nearest wrong owner target that should
   not receive this packet.
4. Draft the packet fields: technique dependencies, proposed trigger boundary,
   inputs, outputs, workflow shape, risk notes, approval seams, rollback path,
   and verification hints.
5. Keep the procedure sketch smaller than the eventual skill. Do not author
   skill wording, command syntax, install behavior, runtime policy, or proof
   claims inside the packet.
6. Add the non-acceptance stop-line: the packet is a proposal for owner review,
   not skill acceptance, skill creation, or activation.
7. If the packet cannot name a trigger, workflow shape, owner, and verification
   hint, return `defer` instead of emitting a vague proposal.

## Contracts

- one packet carries one skill proposal for one receiving owner
- technique canon remains the source of reusable practice meaning
- the receiving skill owner owns any accepted skill workflow, trigger
  contract, packaging, and activation path
- a packet may reference technique dependencies without copying or redefining
  their meaning
- a proposal packet is not skill acceptance, skill creation, skill activation,
  runtime authority, proof verdict, or owner consent
- `defer` is the correct result when workflow shape, trigger boundary, or
  verification hints are too weak

Relationship to adjacent techniques: unlike
[AOA-T-0040](../../../instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md), this
technique does not separate an already-shaped skill from a command wrapper; it
packages a technique-side proposal before a skill exists. Unlike
[AOA-T-0087](../../automation-readiness/human-loop-to-first-landing/TECHNIQUE.md), it does not choose the
first honest automation landing from a recurring human loop; it assumes a
skill proposal is plausible and emits the packet for owner review. Unlike
[AOA-T-0101](../../practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md), it does not gate
local adoption itself; it can follow that gate when adoption pressure exposes a
skill-shaped need.

## Risks

### Failure modes

- the packet quietly becomes a skill draft instead of a handoff
- technique meaning is copied into the packet and drifts from the source bundle
- a vague desire for automation is treated as enough evidence for a skill
  proposal

### Negative effects

- extra handoff paperwork can slow a simple technique-only reuse path
- receiving owners may overread the packet as approval pressure
- too many proposal packets can create queue noise if `defer` is underused

### Misuse patterns

- calling the packet an accepted skill because it has trigger and workflow
  fields
- adding command syntax, installer steps, or runtime activation to the packet
- hiding missing verification behind broad "owner will decide later" language
- routing scenario composition or proof claims to a skill owner because the
  packet format is convenient

### Detection signals

- reviewers cannot tell which owner must accept or reject the proposal
- the packet lacks a trigger boundary, workflow shape, or verification hint
- the proposal contains live activation wording
- the packet repeats technique text instead of referencing technique IDs or
  source anchors
- no nearest wrong target or defer condition is visible

### Mitigations

- keep the packet to one proposed skill and one receiving owner
- reference technique dependencies instead of copying their bodies
- include an explicit non-acceptance stop-line in every packet
- use `defer` when evidence, trigger boundary, or workflow shape is missing
- route proof, scenario, memory, runtime, and command concerns to their owners

## Validation

Verify the technique by confirming that:
- one reusable practice or technique candidate is named
- one receiving skill owner is named
- trigger boundary, inputs, outputs, workflow shape, risks, and verification
  hints are visible
- technique dependencies are referenced instead of redefined
- the packet states that it does not create, accept, or activate a skill
- nearest wrong targets or defer conditions are explicit

See `checks/skill-proposal-handoff-packet-checklist.md`.

## Adaptation notes

What can vary across projects:
- the name and format of the receiving skill owner
- the fields used for trigger, inputs, outputs, risks, and verification
- whether proposal packets live as Markdown, YAML, issue templates, or review
  notes
- whether a local owner calls the result `proposal`, `candidate`, `request`, or
  another bounded pre-acceptance state

What should stay invariant:
- technique meaning remains separate from skill workflow meaning
- the handoff packet does not accept or activate the skill
- one packet covers one proposed skill for one receiving owner
- trigger boundary, workflow shape, risks, and verification hints remain
  visible
- weak proposals defer instead of becoming vague skill queue items

Project-shaped details that should not be treated as invariant:
- one repository map
- one skill bundle template
- one command system
- one runtime activation path
- one proof or evaluation pipeline

AoA adaptation example:
- `aoa-techniques` may emit a proposal packet when Method-growth pressure shows
  that a technique should be considered by `aoa-skills`
- `aoa-skills` owns any accepted skill bundle, trigger boundary, procedure,
  verification, and activation discipline
- proof claims still route to `aoa-evals`, scenario composition to
  `aoa-playbooks`, and reusable practice meaning stays in `aoa-techniques`

## Public sanitization notes

This public bundle keeps only the portable handoff move: one technique-side
proposal packet with trigger, workflow, dependency, risk, verification, and
non-activation fields. AoA center wording, session-specific decisions, local
command wrappers, and sibling-owner acceptance mechanics were reduced to
provenance and adaptation context.

## Example

See `examples/minimal-skill-proposal-handoff-packet.md`.

## Checks

See `checks/skill-proposal-handoff-packet-checklist.md`.

## Promotion history

- born in `aoa-techniques` Method-growth mechanics as part of the v0.7
  downstream adoption wave
- extracted into `aoa-techniques` on 2026-05-03 as one bounded proposal packet
  rather than skill acceptance, skill authorship, or activation

## Future evolution

- keep skill acceptance and skill workflow wording in the receiving skill owner
  rather than widening this handoff bundle
- add a second live context where another skill-owning layer consumes the same
  packet shape without adopting AoA repository vocabulary
- consider a sibling proposal-to-eval or proposal-to-playbook packet only after
  separate mechanics pressure proves one atomic move for those owner routes
