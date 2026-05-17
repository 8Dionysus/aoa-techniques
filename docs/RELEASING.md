# Releasing `aoa-techniques`

This repository is released as a public documentation-and-technique corpus.
Releases should stay small, explicit, public-safe, and easy to verify.

See also [START_HERE.md](START_HERE.md), [Documentation Map](README.md),
[Technique Capsule Guide](selection/TECHNIQUE_CAPSULE_GUIDE.md), and
[CHANGELOG](../CHANGELOG.md).

## Release goals

A release should make four things easy to answer: what changed, why it matters,
how it was validated, and what is intentionally not included.

## Recommended release flow

1. Confirm the target release scope.
2. Update [CHANGELOG](../CHANGELOG.md).
3. Run the bounded release-prep gate:

```bash
python -m pip install -r requirements-dev.txt
python scripts/release_check.py
git status -sb
```

`python scripts/release_check.py` runs the repo builders, tests, nested-AGENTS
validation, and `python scripts/validate_repo.py`. If generated files materialize
on the first pass, it reruns once and requires the second pass to leave the
git-backed snapshot unchanged.

For a read-only current-state pass before release prep, run:

```bash
python scripts/run_tests.py
python scripts/validate_repo.py
```

4. Confirm [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) matches the current
   published catalog.
5. Confirm generated docs and manifests are fresh for the changed families.
6. Review public-safety hygiene: no secrets, internal-only URLs, private
   infrastructure detail, raw sensitive logs, or hand-maintained corpus counts.
7. Merge the release-prep PR to `main`.
8. Create a Git tag such as `v0.1.0`.
9. Publish GitHub release notes from the matching changelog section.

## Generated surface checklist

Use the family row that matches the change; the release gate runs these through
the full sequence.

| Family | Builder or source | Surfaces to notice |
|---|---|---|
| Repo docs | `python scripts/build_repo_doc_surface_manifest.py` | `docs/START_HERE.md`, `generated/repo_doc_surface_manifest.json`, `generated/repo_doc_surface_manifest.min.json`, `docs/readers/repo/REPO_DOC_SURFACES.md` |
| Catalog | `python scripts/build_catalog.py` | `TECHNIQUE_INDEX.md`, `generated/technique_catalog.min.json` |
| Kind | `python scripts/build_kind_manifest.py` | `docs/selection/TECHNIQUE_KIND_GUIDE.md`, `docs/selection/TECHNIQUE_KIND_HANDOFF_PACK.md`, `generated/technique_kind_manifest.json`, `generated/technique_kind_manifest.min.json`, `docs/readers/kind/TECHNIQUE_KINDS.md` |
| Capsule | `python scripts/build_capsules.py` | `docs/selection/TECHNIQUE_CAPSULE_GUIDE.md`, `generated/technique_capsules.json`, `generated/technique_capsules.min.json`, `docs/readers/runtime/TECHNIQUE_CAPSULES.md` |
| Sections | `python scripts/build_section_manifest.py` | `docs/source-lift/TECHNIQUE_SECTION_LIFT_GUIDE.md`, `generated/technique_section_manifest.json`, `docs/readers/source-lift/TECHNIQUE_SECTIONS.md` |
| Checklists | `python scripts/build_checklist_manifest.py` | `docs/source-lift/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, `generated/technique_checklist_manifest.json`, `docs/readers/source-lift/TECHNIQUE_CHECKLISTS.md` |
| Examples | `python scripts/build_example_manifest.py` | `docs/source-lift/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`, `generated/technique_example_manifest.json`, `docs/readers/source-lift/TECHNIQUE_EXAMPLES.md` |
| Evidence notes | `python scripts/build_evidence_note_manifest.py` | `docs/source-lift/EVIDENCE_NOTE_PROVENANCE_GUIDE.md`, `generated/technique_evidence_note_manifest.json`, `docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md` |
| KAG export | `python scripts/build_kag_export.py` | `docs/source-lift/KAG_EXPORT.md`, `generated/kag_export.json`, `generated/kag_export.min.json` |
| GitHub review templates | `python scripts/build_github_review_template_manifest.py` | template manifest surfaces under `generated/` |
| Semantic review | `python scripts/build_semantic_review_manifest.py` | semantic review manifest surfaces under `generated/` |
| Shadow review | `python scripts/build_shadow_review_manifest.py` | `generated/shadow_review_manifest.json`, `generated/shadow_review_manifest.min.json`, `docs/readers/review/SHADOW_PATTERNS.md` |
| Promotion readiness | `python scripts/build_promotion_readiness.py` | promotion readiness generated outputs |

## Release note shape

Recommended release note sections are summary, added, included in this release,
validation, and notes or not included. Exact headings can vary, but the
changelog entry and GitHub release should answer the same release-goal
questions.

## Versioning guidance

Use `0.x.y` for early public shaping and structure refinement. Use `1.0.0` only
when repository structure, contribution path, and validation surface are stable
enough to promise a durable public baseline.

## What not to optimize yet

Do not overbuild release machinery before there is a real package artifact,
policy promise, or semantic-version baseline to protect. Avoid packaging theater
and automation claims that exceed current validation.

## Current stance

Right now, `aoa-techniques` is best released as a curated public corpus, a
self-serve repo with one bounded repo-owned entrypoint, a reusable technique
library, a validated repo structure, and a documented contribution and
promotion path.
