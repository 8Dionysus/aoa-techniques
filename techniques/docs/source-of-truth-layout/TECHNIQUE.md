---
id: AOA-T-0002
name: source-of-truth-layout
domain: docs
status: promoted
origin:
  project: atm10-agent
  path: docs/SOURCE_OF_TRUTH.md
  note: Derived from a real solo+AI repository with explicit document-role policy and reduced doc drift.
owners:
  - 8Dionysus
tags:
  - docs
  - repo-hygiene
  - anti-drift
  - reusable
summary: Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes.
---

# source-of-truth-layout

## Intent

Reduce documentation drift by giving each recurring kind of project information one canonical document home and one clear update route.

## When to use

- multi-document repositories that mix planning, execution, history, and operations
- solo+AI or human+agent projects where many edits happen quickly
- long-running repositories where status, commands, and decisions tend to spread across multiple files
- repositories that want lightweight entrypoint docs without losing detailed history

## When not to use

- very small repositories where one short `README` is enough
- projects that already use an external system as the single authoritative home for plans, runbooks, and decisions
- repositories that are unwilling to maintain an explicit document-role map

## Inputs

- current repository document set
- recurring information classes such as status, plans, run history, decisions, and commands
- update events that should route to one primary document

## Outputs

- explicit document role map
- update-routing rules
- lightweight entrypoint docs
- lower risk of duplicated or contradictory status

## Core procedure

1. Inventory the recurring information classes in the repository.
2. Assign one primary document to each class of information.
3. Keep entrypoint documents short and link outward instead of duplicating detail.
4. Define update-routing rules so each meaningful change lands in one primary document first.
5. Review the document map regularly and remove accidental duplication.

Recommended role map:

| Document | Primary role |
|---|---|
| `README` | Short human-facing entrypoint |
| `MANIFEST` | Short machine/human snapshot |
| `TODO` | Active execution plan |
| `PLANS` | Goals, milestones, DoD, and risks |
| `SESSION_*` | Long history, runs, experiments, and artifacts |
| `DECISIONS` | Architecture and policy changes |
| `RUNBOOK` | Runnable commands and operating procedures |
| `ARCHIVED_TRACKS` | Recoverable or paused directions |

Recommended update-routing rules:

- architecture or policy change -> `DECISIONS`
- command, setup, or operator procedure change -> `RUNBOOK`
- active work item or current focus change -> `TODO`
- goals, milestones, or DoD change -> `PLANS`
- completed run, experiment, or detailed chronology -> `SESSION_*`
- lightweight status summary -> `README` or `MANIFEST`

## Contracts

- each recurring information class has one canonical home
- each meaningful change routes to exactly one primary document first
- `README` and `MANIFEST` stay lightweight and mostly link outward
- long run history does not live in `README` or `TODO`
- decisions do not hide inside session logs or runbooks

## Risks

- over-structuring a repository that is too small to need this layout
- letting the role map go stale after repo evolution
- creating duplicate summaries anyway because contributors ignore routing rules

## Validation

Verify the technique by confirming that:
- each major document has an explicit role
- a sample change can be routed to one primary document without ambiguity
- active status is not duplicated across multiple documents
- long history and artifact detail stay out of lightweight entrypoint docs

See `checks/doc-role-checklist.md`.
For second-context evidence and canonical-readiness review, see `notes/second-context-adaptation.md` and `notes/canonical-readiness.md`.

## Adaptation notes

What can vary across projects:
- `MANIFEST` can be omitted in smaller repositories
- `SESSION_*` can be daily, weekly, or milestone-based
- `ARCHIVED_TRACKS` is optional if the project has no recoverable sidelines
- active work and goal tracking can live in repository files or an external system
- filenames can vary as long as the role map stays explicit

Project-shaped details that should not be treated as invariant:
- exact filenames used by the origin repository
- whether `MANIFEST` or `SESSION_*` exists at all
- whether `TODO`, `PLANS`, and `RUNBOOK` live in the repository or are delegated elsewhere
- the size of the role map in a compact public repository versus an operational one

What should stay invariant:
- one canonical home per recurring information class
- explicit update-routing rules
- lightweight entrypoint docs
- deliberate separation between active work, long history, decisions, and runnable operations

See `notes/second-context-adaptation.md` for a compact public-repository variant.

## Public sanitization notes

Project-specific milestone names, metrics, run IDs, nightly workflow details, local paths, and environment-specific operational details were removed. The published version keeps only the reusable document-role pattern and update-routing logic.

## Example

See `examples/minimal-doc-routing.md`.

## Checks

See `checks/doc-role-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through active use across `README`, `MANIFEST`, `TODO`, `PLANS`, `DECISIONS`, `RUNBOOK`, and `SESSION_*` documents
- promoted to `aoa-techniques` on 2026-03-13

## Future evolution

- add guidance for repositories that keep active work outside the repo
- capture a third context with issue-tracker-backed planning or external runbooks
- add an optional machine-readable role-map format if the repository later needs automated checks
