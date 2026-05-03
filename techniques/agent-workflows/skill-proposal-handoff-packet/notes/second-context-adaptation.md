# Second Context Adaptation

## Technique
- id: AOA-T-0102
- name: skill-proposal-handoff-packet

## Target project
- name: aoa-skills
- environment: bounded skill corpus that may consume technique dependencies
- runtime: human and agent review workflow over skill bundle proposals

## What changed
- the Method-growth handoff was narrowed to one proposal packet before skill acceptance
- trigger boundary, workflow shape, risk, approval, rollback, and verification fields were retained as proposal context
- accepted skill wording, command syntax, install behavior, and activation discipline were excluded from the technique
- AoA repo names moved into adaptation examples rather than the invariant core

## What stayed invariant
- technique canon remains separate from skill workflow meaning
- the receiving owner decides whether any skill exists
- technique dependencies are referenced rather than copied or redefined
- the packet must state that it does not create, accept, install, or activate a skill

## Risks introduced by adaptation
- the packet can look like a skill draft if workflow fields become too detailed
- receiving owners can overread a proposal as pressure to accept
- proof, scenario, memory, runtime, or command concerns can be misrouted to the skill owner because the packet format is convenient

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is one handoff move
- the adjacent-technique notes keep skill-command boundary, first automation landing, and local adoption gate separate
- the example uses generic owner names and does not require OS Abyss deployment

## Result
- verdict: works
- note: the adapted bundle stays readable as a proposal packet rather than skill acceptance or activation
