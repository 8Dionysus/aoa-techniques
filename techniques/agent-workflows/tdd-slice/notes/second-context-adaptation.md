# Second Context Adaptation

## Technique
- id: AOA-T-0014
- name: tdd-slice

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human+agent contribution workflow over reviewable repository changes

## What changed
- adaptation path: the technique was rehomed from a broader draft wave into one focused promoted bundle rather than landing as part of an umbrella branch
- support surfaces: the public form now includes a bounded checklist, a minimal example, an origin note, and derived repository manifests
- workflow surface: the adaptation turns planning-layer testing pressure into a portable repository technique that can guide bounded behavior changes across public-safe engineering work
- operating assumptions: contributors work through explicit diffs, named validation steps, and reviewable out-of-scope boundaries

## What stayed invariant
- contract: one bounded behavior slice is named before implementation widens
- sequence: tests-first where appropriate, smallest passing change next, bounded refactor only after the slice is green
- reporting: the final result still names what behavior is now covered and what remains outside the slice

## Risks introduced by adaptation
- documentation packaging can make the technique sound like generic TDD ritual if future examples stop centering one concrete bounded slice
- narrow example surfaces can create false confidence if contributors copy the checklist without keeping the behavior boundary explicit
- repository promotion can hide the execution discipline if future notes focus on artifacts rather than the bounded change path itself

## Evidence
- The focused landing into `aoa-techniques` kept the technique distinct from boundary-contract and property-oriented validation patterns rather than leaving it inside one mixed skill-support branch.
- The public checklist and minimal example still center behavior-shaped tests, smallest passing change, and bounded refactor instead of generic testing advice.
- The later `Skill-Support Semantic Review` kept `AOA-T-0014` distinct as an execution discipline for one bounded behavior slice rather than as a generic evaluation technique.

## Result
- verdict: works
- note: the technique remained readable, bounded, and semantically distinct after public extraction into `aoa-techniques`
