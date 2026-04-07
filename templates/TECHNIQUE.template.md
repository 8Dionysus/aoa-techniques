---
id: AOA-T-XXXX
name: technique-name
domain: agent-workflows
# choose one: agent-workflows, docs, evaluation, system-recovery, validation-patterns, history
status: promoted
origin:
  project: source-project-name
  path: optional/original/path
  note: born in a real project, later sanitized for public reuse
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
summary: One-sentence summary of the technique.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations: []
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# technique-name

## Intent

What problem this technique solves.

## When to use

- case 1
- case 2
- case 3

## When not to use

- case 1
- case 2

## Inputs

- input 1
- input 2

## Outputs

- output 1
- output 2

## Core procedure

Describe the technique step by step.

## Contracts

List invariants, rules, interfaces, or expectations.

## Risks

### Failure modes

- how the contract can break

### Negative effects

- what the technique worsens even when it appears to work

### Misuse patterns

- how the technique gets applied outside its bounded role

### Detection signals

- what early signals show drift or false-success

### Mitigations

- how to narrow, roll back, or contain the damage

## Validation

Describe how to verify the technique:
- test
- smoke
- checklist
- contract check

## Adaptation notes

What usually changes when applying this to another project:
- paths
- services
- runtime
- OS assumptions
- repo layout assumptions

## Public sanitization notes

What was removed, generalized, or sanitized from the original project context.

## Example

Point to `examples/` or include a minimal public-safe example.

## Checks

Point to `checks/` or describe the minimal verification surface.

## Promotion history

- born in <project>
- validated in <project>
- promoted to `aoa-techniques` on <date>

## Future evolution

Possible directions for refinement.
