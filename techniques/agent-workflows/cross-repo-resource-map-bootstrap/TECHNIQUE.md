---
id: AOA-T-0061
name: cross-repo-resource-map-bootstrap
domain: agent-workflows
status: promoted
origin:
  project: yan5xu/code-relay
  path: README.md + local/orchestrator/ALWAYS/RESOURCE-MAP.yml + github/orchestrator/ALWAYS/RESOURCE-MAP.yml
  note: Adapted from Code Relay's global RESOURCE-MAP bootstrap surface to keep cross-repo startup context explicit without importing the donor's whole boot sequence, infrastructure inventory, or collaboration-mode stack.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - cross-repo
  - bootstrap
  - resource-map
  - handoff
summary: Bootstrap cross-repo work from one explicit resource map so the next session can see which repos and surfaces matter before deeper continuation begins.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0016
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# cross-repo-resource-map-bootstrap

## Intent

Bootstrap cross-repo work from one explicit resource map so the next session can see which repositories and surfaces matter before deeper continuation begins.

## When to use

- the next step spans more than one repository
- a receiving operator or agent needs one compact cross-repo starting surface
- the main risk is not semantic context confusion inside one repo, but not knowing where to look first across several repos
- the reusable object is one bounded startup map, not a whole architecture inventory or workspace platform

## When not to use

- the work is truly single-repo and a normal local starting surface is enough
- the main need is a semantic context map, ownership model, or general architecture explanation
- the map would become a standing encyclopedia of every repo and infrastructure surface
- the workflow only makes sense when bundled with a full boot sequence, collaboration mode, or orchestrator stack

## Inputs

- one current cross-repo task, handoff, or continuation goal
- one list of repositories that materially affect that goal
- one small set of resource paths or surfaces per repo that the next step depends on

## Outputs

- one explicit cross-repo resource map
- one named role for each listed repo
- one visible first-look path across repo boundaries before deeper work begins

## Core procedure

1. Name the repositories that materially affect the current cross-repo task or handoff.
2. For each repo, list the smallest useful set of resources or surfaces the next step depends on.
3. State why each repo and resource matters to the current goal instead of leaving the relationship implicit.
4. Mark the first repo or surface the next session should inspect so startup order is visible.
5. Keep the map small enough to review quickly before deeper work begins.
6. Hand off the map as a bounded startup object rather than as a long-lived system encyclopedia.
7. Route semantic domain modeling, broad architecture diagrams, full infrastructure inventories, and total workspace boot doctrine to sibling techniques when they become the real center of gravity.

## Contracts

- the map names real repositories and real resource surfaces
- each listed repo has an explicit role tied to the current task or handoff
- the next session can identify where to look first across repo boundaries
- the map stays task-bounded instead of expanding into a general architecture inventory
- the technique stays smaller than semantic context mapping, platform-wide topology docs, and full startup or orchestration stacks

Relationship to adjacent techniques: unlike [AOA-T-0016](../../docs/bounded-context-map/TECHNIQUE.md), this technique does not define conceptual bounded contexts or handoff interfaces across a system; it names only the repositories and concrete resource surfaces needed to start a specific cross-repo task safely. Unlike [AOA-T-0060](../session-opening-ritual-before-work/TECHNIQUE.md), it does not define the generic pre-mutation ritual for every resumed session; it owns the cross-repo map object used when one session-start surface must span multiple repos. Unlike [AOA-T-0057](../structured-handoff-before-compaction/TECHNIQUE.md), it does not write the full continuation packet; it only gives the next session a bounded cross-repo index for where to look first.

## Risks

### Failure modes

- the map includes too much inventory and the real first-look path disappears
- an actually relevant repo or resource surface is omitted
- repo roles are listed without explaining why they matter to the current task

### Negative effects

- the map can become ceremony when the cross-repo relationship is obvious and tiny
- contributors may mistake the map for a durable architecture document and stop pruning it
- infrastructure detail can crowd out the bounded startup purpose if every adjacent system gets listed

### Misuse patterns

- treating the map as a permanent workspace encyclopedia
- widening the bundle into topology diagrams, domain models, or deployment inventories
- hiding task assumptions inside unlabeled repo references or generic repo names

### Detection signals

- the map cannot be reviewed quickly before the next session starts work
- a reader still cannot tell which repo or surface to inspect first
- listed resources feel interchangeable or disconnected from the current task
- the artifact grows faster than the bounded cross-repo work it is supposed to enable

### Mitigations

- keep the repo list tied to one current task or handoff
- require one explicit reason for each listed repo and resource
- mark a first-look surface rather than only enumerating everything
- trim infrastructure or architecture detail that does not help the next bounded step

## Validation

Verify the technique by confirming that:
- every listed repo or resource has a stated role in the current task
- a reader can tell where to look first across repo boundaries
- the map stays small enough to inspect quickly
- the map still makes sense without a full workspace platform or architecture program
- the artifact remains smaller than a semantic context map or infrastructure inventory

See `checks/cross-repo-resource-map-bootstrap-checklist.md`.

## Adaptation notes

What can vary across projects:
- whether the map is written as Markdown, YAML, JSON, or another small reviewable format
- how repos are named or grouped
- how fine-grained the listed resources are
- whether infrastructure surfaces are included when they directly affect the next step
- whether the map is attached to a handoff, task sheet, or standalone startup note

What should stay invariant:
- the map is bounded to one current cross-repo task or continuation goal
- repo roles and resource roles remain explicit
- the next reader can tell where to start
- the artifact stays smaller than a broader system model

Project-shaped details that should not be treated as invariant:
- one `RESOURCE-MAP.yml` path under a global orchestrator directory
- GitHub board metadata, organization URLs, or worktree naming conventions
- one local versus GitHub collaboration mode split
- full infrastructure inventories for databases, caches, and deploy providers
- a whole boot-sequence stack or workspace management platform

## Public sanitization notes

This import narrows the donor to one bounded pattern: before cross-repo work continues, provide one explicit map of the repos and concrete surfaces that matter to the next step. Workspace-platform semantics, full infrastructure indexes, collaboration-mode doctrine, and global boot sequencing were intentionally left out of the public contract.

## Example

See `examples/minimal-cross-repo-resource-map-bootstrap.md`.

## Checks

See `checks/cross-repo-resource-map-bootstrap-checklist.md`.

## Promotion history

- adapted from open-source `yan5xu/code-relay`
- staged through the chat wave 3 handoff-bounded-continuation lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for cross-repo startup maps

## Future evolution

- keep semantic context mapping separate instead of widening this bundle into a general boundary doctrine
- keep startup rituals separate instead of treating the map as a full session-opening workflow
- keep full infrastructure and workspace inventory layers separate instead of importing a whole multi-repo platform model
