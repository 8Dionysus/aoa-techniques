---
id: AOA-T-XXXX
name: cross-repo-resource-map-bootstrap
domain: agent-workflows
status: draft-seed
origin: chat-wave-3-handoff-bounded-continuation
note: seed bundle staged for operator-guided chat wave 3 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - handoff-bounded-continuation
summary: Bootstrap cross-repo work from an explicit resource map so shared context stays reviewable across repo boundaries.
maturity_score: 1
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: donor_soil
export_ready: false
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.seed.md
---
# cross-repo-resource-map-bootstrap

## Intent

Start cross-repo work from one explicit resource map so the operator can see which repos, files, and owned surfaces matter before continuation.

## When to use

- work spans more than one repository
- a receiving operator needs a compact context map
- repo boundaries matter to the next step

## When not to use

- the work is single-repo only
- the map would become a full architecture inventory
- the map cannot stay smaller than a broad context model

## Inputs

- repo list
- key resource paths or surfaces per repo
- current task or handoff goal

## Outputs

- explicit cross-repo resource map
- named repo roles
- starting context for the next bounded step

## Core procedure

1. list the repos involved
2. name the relevant resources in each repo
3. state why each resource matters to the current handoff or task
4. keep the map small enough to review quickly
5. hand off the map before deeper cross-repo work begins

## Contracts

- the map names real repos and resources
- repo roles stay explicit
- the technique stays smaller than full architecture mapping
- the next operator can identify where to look first

## Risks

### Failure modes

- the map includes too much irrelevant inventory
- critical repo resources are omitted

### Negative effects

- the map turns into an architecture encyclopedia
- repo boundaries blur instead of becoming clearer

### Misuse patterns

- treating the map as a long-lived system model
- hiding task assumptions inside unlabeled repo references

### Detection signals

- the map cannot be reviewed quickly
- the next operator still cannot tell where to start

### Mitigations

- keep the resource set task-bounded
- name repo roles explicitly
- review for omissions before handoff

## Validation

- confirm every listed resource has a stated role
- confirm the map stays small enough to inspect quickly
- verify the seed stays smaller than a general architecture map

## Adaptation notes

- repo naming
- path granularity
- map format
- task-to-resource linkage

## Public sanitization notes

Remove donor-specific platform coordination language. Keep only the bounded cross-repo resource map contract.

## Example

See `examples/resource_map.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 3 cross-repo cluster

## Future evolution

- resource ownership markers
- bounded freshness checks
- handoff receipts that reference map versions
