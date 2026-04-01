# Technique Feat Model

## Purpose

This note defines the second-wave feat / perk reflection contract for `aoa-techniques`.

It exists so that long-horizon quest work can read reusable techniques as mastery-shaped feat cards without mutating source-owned technique meaning.

## Core rule

A technique feat card is a derived reader surface.

It attaches to an existing technique and summarizes why that technique behaves like a transferable feat, perk, stance, or reusable edge.

The owner surfaces remain:

- `techniques/*/TECHNIQUE.md`
- `TECHNIQUE_INDEX.md`
- `generated/technique_capsules*.json`
- `generated/technique_sections.full.json`
- `docs/CANONICAL_RUBRIC.md`
- `docs/DONOR_REFINERY_RUBRIC.md`
- `docs/EXTERNAL_EVIDENCE_*`
- `WALKTHROUGH.md`

Feat cards may help humans and agents read those sources faster. They must not replace them.

## Feat eligibility

A second-wave feat candidate should usually be:

- reusable beyond one local diff
- source-first and public-safe
- backed by explicit validation, adaptation, or evidence posture
- portable enough to state a transfer scope honestly
- legible enough that mastery can be described without score theater

Not every technique deserves a feat card immediately. Pending, thin, or unstable technique work can stay ordinary technique work until the canon is ready.

## Suggested fields

A feat card may summarize:

- technique ID and source path
- feat kind
- source status
- mastery posture tied to first-wave axes
- transfer scope
- nomination sources from readiness, donor-refinery, or evidence work
- synergy tags
- evidence refs

## Boundary rules

### Technique canon stays source-first

The source of meaning remains the technique markdown and its repo-owned readiness/evidence surfaces.

### Skills still package execution

A feat card should not turn `aoa-techniques` into a second executable skill catalog.

### Playbooks still own route method

If several techniques need choreography or scenario ordering, that is still playbook method rather than a feat catalog problem.

## Anti-patterns

- treating every technique as an automatic passive perk
- writing feat doctrine into `TECHNIQUE.md` as primary meaning
- using a feat card to bypass canonical review
- confusing transfer scope with universal applicability
- replacing donor-refinery or evidence surfaces with decorative RPG labels
