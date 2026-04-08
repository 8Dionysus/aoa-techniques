# AGENTS.md

Guidance for coding agents and humans contributing to `aoa-techniques`.

## Purpose

`aoa-techniques` is the public practice canon of AoA.
It stores reusable, sanitized, reviewable engineering techniques that can later
be lifted into skills, evals, routing surfaces, KAG exports, and other derived
artifacts without turning practice into lore.

A technique is a portable unit of method.
It is not a skill bundle, not a proof surface, not a questline, and not an
agent identity layer.

## Owns

This repository is the source of truth for:

- technique bundle meaning
- technique IDs
- technique intent and bounded contracts
- public-safe technique wording
- adaptation notes at the technique layer
- generated technique catalogs, capsules, feat-card reader surfaces, and source-lift surfaces
- technique-layer promotion and publication posture

## Does not own

Do not treat this repository as the source of truth for:

- bounded execution workflows in `aoa-skills`
- proof doctrine or verdict logic in `aoa-evals`
- routing and dispatch logic in `aoa-routing`
- role contracts, progression posture, or self-agent checkpoint doctrine in `aoa-agents`
- scenario composition or questline / campaign posture in `aoa-playbooks`
- memory objects or recall surfaces in `aoa-memo`
- derived substrate semantics in `aoa-kag`
- derived observability or movement summaries in `aoa-stats`
- private project operations, secrets, or infrastructure detail

## Core rules

Only contribute techniques that are:

- reusable
- sanitized
- documented
- bounded
- verifiable

If adjacent meaning already has a canonical home, route to it.

If a reusable contract can be extracted cleanly, the extracted technique belongs
here.

When a technique has multiple plausible `kind` values, keep `domain` first,
pick one primary `kind`, and use the registry tie-break rules instead of
widening the axis.

## Growth posture

This repository captures reusable method, not agent destiny.

Higher layers may later package these techniques into bounded workflows,
portable proofs, routing hints, continuity support, or longer-horizon
progression surfaces.
Do not smuggle those higher-layer claims back into the technique canon.

## Read this first

Before making changes, read in this order:

1. `README.md`
2. `docs/START_HERE.md`
3. `WALKTHROUGH.md`
4. `docs/TECHNIQUE_SELECTION.md`
5. `docs/TECHNIQUE_KIND_GUIDE.md`
6. the target `techniques/**/TECHNIQUE.md`
7. any generated catalogs, capsules, feat-card surfaces, or source-lift outputs affected by the change

Then branch by task:

- kind selection, routing fit, or registry tie-breaks:
  `docs/TECHNIQUE_KIND_GUIDE.md`,
  `docs/TECHNIQUE_KIND_HANDOFF_PACK.md`, and
  `generated/technique_kind_manifest.min.json`
- feat-reader or capsule surfaces:
  `docs/TECHNIQUE_FEAT_MODEL.md`,
  `docs/TECHNIQUE_CAPSULES.md`, and
  `docs/TECHNIQUE_CAPSULE_GUIDE.md`
- promotion, review, or release posture:
  `docs/CANONICAL_RUBRIC.md`,
  `docs/CANONICAL_REVIEW_GUIDE.md`,
  `docs/PROMOTION_READINESS_MATRIX.md`, and
  `docs/RELEASING.md`
- donor intake or external refinement:
  `docs/DONOR_REFINERY_RUBRIC.md`,
  `docs/EXTERNAL_IMPORT_RUNBOOK.md`, and
  `docs/CROSS_LAYER_TECHNIQUE_CANDIDATES.md`
- source-lift, KAG export, or section families:
  `docs/KAG_EXPORT.md`,
  `docs/KAG_SOURCE_LIFT_GUIDE.md`,
  `docs/TECHNIQUE_SECTIONS.md`, and the matching section-lift guides

If a deeper directory defines its own `AGENTS.md`, follow the nearest one.

## Primary objects

The most important objects in this repository are:

- canonical technique bundles under `techniques/**/TECHNIQUE.md`
- technique templates under `templates/`
- generated catalogs, capsules, feat-card surfaces, and source-lift manifests under `generated/`
- selection, intake, review, promotion, and release docs under `docs/`
- validation and generation helpers under `scripts/` and `tests/`
- the canonical kind doctrine in `docs/TECHNIQUE_KIND_GUIDE.md`

## Hard NO

Do not contribute:

- secrets, tokens, or internal-only URLs
- private infrastructure details
- raw logs with sensitive data
- environment-specific hacks without adaptation notes
- techniques with unclear boundaries
- techniques that actually belong as skills, evals, routing logic, role contracts, or playbooks
- feat-card or capsule wording that quietly becomes canonical technique meaning
- vague philosophy where an operational method should exist

Keep the repository operational, reviewable, and portable.

## Contribution doctrine

Use this flow: `PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN

State:

- which technique or technique-surface family is changing
- whether intent, contract, adaptation notes, or `kind` selection are changing
- whether any IDs, publication states, or promotion-readiness surfaces are changing
- whether source-lift, feat-card, or capsule surfaces will change
- what downstream impact is possible

### DIFF

Keep the change focused.
Preserve public hygiene, boundedness, and portability.
Do not mix unrelated cleanup into technique meaning unless it is necessary for
repository integrity.

### VERIFY

Minimum validation for meaning, schema, script, or generated-surface changes:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Use the broader release-prep path when the change touches publication posture,
wide generated outputs, or release-facing docs:

```bash
python scripts/release_check.py
git status -sb
```

Confirm that:

- the technique remains reusable and bounded
- caveats and adaptation notes still protect portability
- `kind`, `domain`, ID, and publication posture stay coherent
- generated catalogs, capsules, feat cards, and source-lift surfaces stay aligned when changed
- no neighboring layer meaning was silently pulled into this repo

### REPORT

Summarize:

- what changed
- whether meaning changed or only docs, metadata, or generated surfaces changed
- whether IDs, states, adaptation notes, or kind selection changed
- what validation you actually ran
- any remaining follow-up work

## Validation

Do not claim checks you did not run.
