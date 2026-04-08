# AGENTS.md

Guidance for coding agents and humans contributing to `aoa-techniques`.

## Purpose

`aoa-techniques` is the public practice canon of AoA. It stores reusable, sanitized, reviewable engineering techniques that can later be lifted into skills, evals, routing surfaces, and other derived artifacts.

## Owns

This repository is the source of truth for:

- technique bundle meaning
- technique IDs
- technique intent and bounded contracts
- public-safe technique wording
- adaptation notes at the technique layer
- generated technique catalogs, capsules, and source-lift surfaces

## Does not own

Do not treat this repository as the source of truth for:

- bounded execution workflows in `aoa-skills`
- proof doctrine or verdict logic in `aoa-evals`
- routing and dispatch logic in `aoa-routing`
- role contracts in `aoa-agents`
- scenario composition in `aoa-playbooks`
- memory objects or recall surfaces in `aoa-memo`
- derived substrate semantics in `aoa-kag`
- private project operations, secrets, or infra detail

## Core rule

Only contribute techniques that are:

- reusable
- sanitized
- documented
- bounded
- verifiable

If adjacent meaning already has a canonical home, route to it. If a reusable contract can be extracted cleanly, the extracted technique belongs here.
When a technique has multiple plausible `kind` values, keep `domain` first, pick one primary `kind`, and use the registry tie-break rules instead of widening the axis.

## Read this first

Before making changes, read in this order:

1. `README.md`
2. `docs/START_HERE.md`
3. `WALKTHROUGH.md`
4. `docs/TECHNIQUE_SELECTION.md`
5. `docs/TECHNIQUE_KIND_GUIDE.md` and `docs/TECHNIQUE_KINDS_SEED.md` when the task touches kind selection, review, or routing
6. the target `techniques/**/TECHNIQUE.md`
7. any generated catalogs or capsules affected by the change

If the task touches donor intake, promotion, or source-lift surfaces, read the neighboring docs that govern those flows before editing.

If a deeper directory defines its own `AGENTS.md`, follow the nearest one.

## Primary objects

The most important objects in this repository are:

- canonical technique bundles under `techniques/**/TECHNIQUE.md`
- technique templates under `templates/`
- generated catalogs, capsules, and source-lift manifests under `generated/`
- selection, intake, promotion, and release docs under `docs/`
- validation and generation helpers under `scripts/` and `tests/`
- the canonical kind doctrine in `docs/TECHNIQUE_KIND_GUIDE.md`, with `docs/TECHNIQUE_KINDS_SEED.md` kept only as a historical wave1 note

## Hard NO

Do not contribute:

- secrets, tokens, or internal-only URLs
- private infrastructure details
- raw logs with sensitive data
- environment-specific hacks without adaptation notes
- techniques with unclear boundaries
- techniques that actually belong as skills, evals, routing logic, role contracts, or playbooks

Do not turn a technique into vague philosophy. Keep it operational and reviewable.

## Contribution doctrine

Use this flow: `PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN

State:

- which technique or source-lift surface is changing
- whether intent, contract, or adaptation notes are changing
- whether any IDs or publication states are changing
- what downstream impact is possible

### DIFF

Keep the change focused. Preserve public hygiene and boundedness. Do not mix unrelated cleanup into technique meaning unless it is necessary for repository integrity.

### VERIFY

Confirm that:

- the technique remains reusable and bounded
- caveats and adaptation notes still protect portability
- generated catalogs or capsules stay aligned when they changed
- no neighboring layer meaning was silently pulled into this repo

### REPORT

Summarize:

- what changed
- whether meaning changed or only docs, metadata, or generated surfaces changed
- whether IDs, states, or adaptation notes changed
- what validation you actually ran
- any remaining follow-up work

## Validation

Run the documented repo check from `README.md`.

Minimum validation for meaning or generated-surface changes:

```bash
python scripts/release_check.py
```

Add targeted tests when scripts, schemas, or generated outputs change. Do not claim checks you did not run.
