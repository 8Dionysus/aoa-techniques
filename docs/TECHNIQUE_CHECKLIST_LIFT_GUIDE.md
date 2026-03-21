# Technique Checklist Lift Guide

This guide defines the bounded contract for the checklist source-lift family.

Use it when the repository already has authored checklist files under technique bundles, but the next question is how to expose them as derived validation knowledge without turning them into executable policy, hard gates, or scoring.

See also:
- [Start Here](START_HERE.md)
- [Technique Checklists](TECHNIQUE_CHECKLISTS.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [Documentation Map](README.md)

This family uses one stable shape:

- authoritative source: authored checklist markdown under `checks/`
- reader companion: `TECHNIQUE_CHECKLISTS.md`
- derived manifests: `generated/technique_checklist_manifest.json` and `generated/technique_checklist_manifest.min.json`
- what it must not become: executable policy, hard gates, scoring, or replacement checklist authorship

## Source Contract

The current checklist lift stays bundle-local and markdown-first:

- checklist files live under `checks/`
- each checklist keeps one authored title
- intro text may be present or absent
- checklist items remain authored markdown bullets
- techniques may publish more than one checklist

## Reader Companion And Derived Manifests

The generated outputs for this source class are:

- `generated/technique_checklist_manifest.json`
- `generated/technique_checklist_manifest.min.json`
- `docs/TECHNIQUE_CHECKLISTS.md`

Those outputs stay derived from authored checklist markdown and source bundles.

## Reader Surface Contract

`TECHNIQUE_CHECKLISTS.md` stays domain-first and technique-first.

For each checklist it shows only:

- checklist title
- whether intro text is present
- item count
- check path
- source routing back to the technique bundle

That is derived validation knowledge only.

## Boundaries

Checklist lift does not become:

- executable policy
- hard-gate semantics
- scoring
- replacement checklist authorship

If a reviewer needs the actual checklist wording, the answer still lives in the authored `checks/*.md` file.

## Validation

Regenerate and verify this source class with:

- `python scripts/build_checklist_manifest.py`
- `python scripts/release_check.py`
- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
