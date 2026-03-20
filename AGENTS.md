# AGENTS.md

Guidance for coding agents and humans contributing to `aoa-techniques`.

## Purpose

`aoa-techniques` is the public practice canon of AoA.

It stores reusable, sanitized, reviewable engineering techniques that can later be lifted into skills, evals, routing surfaces, or other derived artifacts.

Use this repository for technique meaning, not for project-specific operations.

## Owns

This repository is the source of truth for:

- technique bundle meaning
- technique IDs
- technique intent and bounded contract
- public-safe technique wording
- adaptation notes at the technique layer
- technique metadata and generated technique catalogs/capsules

## Does not own

Do not treat this repository as the source of truth for:

- bounded agent execution workflows in `aoa-skills`
- proof doctrine or verdict logic in `aoa-evals`
- routing and dispatch logic in `aoa-routing`
- role contracts in `aoa-agents`
- recurring scenario composition in `aoa-playbooks`
- memory objects or recall surfaces in `aoa-memo`
- derived knowledge substrate semantics in `aoa-kag`
- private project operations, secrets, or infra detail

## Core rule

Only contribute techniques that are:

- reusable
- sanitized
- documented
- bounded
- verifiable

If adjacent meaning already has a canonical home, do not recreate it here. Route to it.

## Read this first

Before making changes, read in this order:

1. `README.md`
2. `WALKTHROUGH.md`
3. `docs/TECHNIQUE_SELECTION.md`
4. the target `TECHNIQUE.md` bundle you plan to edit
5. any generated catalogs or capsules affected by the change

If the task touches promotion, selection, or metadata shape, read the neighboring docs that govern those surfaces before editing.

## Primary objects

The most important objects in this repository are:

- `techniques/**/TECHNIQUE.md`
- `generated/technique_catalog.min.json`
- `generated/technique_capsules.json`
- docs that define selection, publication, and lift posture
- validation or generation helpers referenced by the README

## Allowed changes

Safe, normal contributions include:

- improving wording, clarity, and boundedness of an existing technique
- tightening “when to use” and “when not to use”
- improving adaptation notes
- adding examples that strengthen the contract
- repairing metadata drift between source markdown and generated outputs
- adding a new technique when it clearly belongs to the public reusable canon

## Changes requiring extra care

Use extra caution when:

- changing a technique ID
- changing promotion status
- changing generated catalog or capsule shape
- changing a technique in ways that may break downstream references
- changing wording that downstream skills or evals may rely on
- removing caveats that currently protect boundedness or public hygiene

## Hard NO

Do not contribute:

- secrets
- tokens
- internal-only URLs
- private infrastructure details
- project-only dumps
- raw logs with sensitive data
- environment-specific hacks without adaptation notes
- techniques with unclear boundaries
- techniques that belong as skills, evals, routing logic, or role contracts

Do not turn a technique into a vague philosophy piece. Keep it operational and reviewable.

## Public hygiene

Assume everything here is public and reusable by strangers.

Write for portability:

- generalize paths
- generalize hostnames
- generalize private IDs
- strip secrets
- explain assumptions
- prefer small explicit contracts

If an example is useful but too project-shaped, sanitize it rather than copying it raw.

## Contribution doctrine

Use this flow:

`PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN

State:

- what is being added or changed
- why it belongs in `aoa-techniques`
- whether downstream repos may be affected

### DIFF

Keep the change focused and reviewable.

Do not mix unrelated cleanup into a technique change unless the cleanup is necessary to preserve repository integrity.

### VERIFY

Confirm that the technique is still:

- public-safe
- coherent
- reusable
- bounded
- verifiable

If metadata or generated outputs are affected, regenerate and validate them.

### REPORT

Summarize:

- what changed
- whether technique meaning changed or only metadata changed
- whether generated outputs changed
- any remaining limits
- any likely downstream follow-up in `aoa-skills`, `aoa-evals`, or `aoa-routing`

## Validation

Run the repository validation commands documented in `README.md`.

If your change affects generated surfaces, regenerate them and validate them before finishing.

If tests or checks exist for the touched surface, run them. Do not claim validation you did not execute.

## Cross-repo neighbors

Use these neighboring repositories when the task crosses boundaries:

- `aoa-skills` for bounded execution workflows built from techniques
- `aoa-evals` for proof surfaces and bounded claim checks
- `aoa-routing` for smallest-next-object navigation
- `aoa-agents` for role and handoff posture
- `aoa-playbooks` for recurring higher-level compositions
- `Agents-of-Abyss` for ecosystem-level map and boundary doctrine

## Output expectations

When reporting back after a change, include:

- which technique objects changed
- whether meaning changed or only metadata changed
- whether generated outputs changed
- what validation was run
- any downstream repos that may need follow-up

## Default editing posture

Prefer the smallest reviewable change.
Preserve canonical wording unless the task explicitly requires semantic change.
If semantic change is made, report it explicitly.