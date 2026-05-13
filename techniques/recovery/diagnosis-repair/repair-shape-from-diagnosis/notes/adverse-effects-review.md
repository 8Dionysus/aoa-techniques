# Adverse Effects Review

## Technique
- id: AOA-T-0082
- name: repair-shape-from-diagnosis
- current role: bounded canonical default

## Review focus

Review the effects of making one smallest honest repair shape the default move
after a reviewed diagnosis already exists.

## Failure modes

- a vague improvement wish is treated as a bounded repair
- the chosen repair shape is larger than the diagnosis justifies
- validation, owner target, or escalation remains implicit
- checkpoint posture or playbook rollout replaces the repair-shape seam

## Negative effects

- too-small repair shapes can hide a wider scenario problem
- too much repair ceremony can slow obvious small fixes
- downstream routes may treat a prepared packet as executed or verified

## Misuse patterns

- starting repair-shaping before diagnosis exists
- choosing a scenario rollout as if it were one repair packet
- using repair shape as roadmap planning
- skipping escalation when the repair no longer fits one owner-facing unit

## Detection signals

- reviewers cannot name the diagnosis that justified the repair
- the proposed artifact is larger than the diagnosis packet
- validation is generic or missing
- the same repair packet reopens because the real problem was wider

## Mitigations

- require reviewed diagnosis first
- name one primary owner target and one target artifact class
- keep validation and stop conditions visible
- hand checkpoint posture and scenario rollout to adjacent surfaces

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should keep repair shaping smaller than checkpoint execution, playbook
coordination, proof, memory writeback, runtime repair, or general
self-improvement doctrine.
