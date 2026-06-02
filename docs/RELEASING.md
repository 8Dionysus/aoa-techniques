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
3. Run the bounded `release` lane. The authoritative lane definition lives in
   [validation_lanes](../config/validation_lanes.json); the active entrypoint
   and lane ids are recorded in
   [Command Authority](validation/COMMAND_AUTHORITY.md). `release_check.py`
   remains the worktree stabilizer, not a second command store.

The `release` lane runs the repo builders, tests, nested-AGENTS validation, and
repo validators through the lane manifest. If generated files materialize on
the first pass, the release entrypoint reruns once and requires the second pass
to leave the git-backed snapshot unchanged.

For a read-only current-state pass before release prep, use the `source-fast`
lane and the nearest `AGENTS.md` owner checks for the surface being changed.

4. Confirm [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) matches the current
   published catalog.
5. Confirm generated docs and manifests are fresh for the changed families.
6. Review public-safety hygiene: no secrets, internal-only URLs, private
   infrastructure detail, raw sensitive logs, or hand-maintained corpus counts.
7. Merge the release-prep PR to `main`.
8. Create a Git tag such as `v0.1.0`.
9. Publish GitHub release notes from the matching changelog section.

## Generated surface checklist

Use the family row that matches the change; the `generated` and `release` lanes
run the actual command sequences from `config/validation_lanes.json`.

| Family | Lane group or owner route | Surfaces to notice |
|---|---|---|
| Repo docs | `generated` lane, `catalog` group | `docs/START_HERE.md`, `generated/repo_doc_surface_manifest.json`, `generated/repo_doc_surface_manifest.min.json`, `docs/readers/repo/REPO_DOC_SURFACES.md` |
| Catalog | `generated` lane, `catalog` group | `TECHNIQUE_INDEX.md`, `generated/technique_catalog.min.json` |
| Kind | `generated` lane, `catalog` group | `docs/selection/TECHNIQUE_KIND_GUIDE.md`, `docs/selection/TECHNIQUE_KIND_HANDOFF_PACK.md`, `generated/technique_kind_manifest.json`, `generated/technique_kind_manifest.min.json`, `docs/readers/kind/TECHNIQUE_KINDS.md` |
| Capsule | `generated` lane, `catalog` group | `docs/selection/TECHNIQUE_CAPSULE_GUIDE.md`, `generated/technique_capsules.json`, `generated/technique_capsules.min.json`, `docs/readers/runtime/TECHNIQUE_CAPSULES.md` |
| Sections | `generated` lane, `catalog` group | `docs/source-lift/TECHNIQUE_SECTION_LIFT_GUIDE.md`, `generated/technique_section_manifest.json`, `docs/readers/source-lift/TECHNIQUE_SECTIONS.md` |
| Checklists | `generated` lane, `catalog` group | `docs/source-lift/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, `generated/technique_checklist_manifest.json`, `docs/readers/source-lift/TECHNIQUE_CHECKLISTS.md` |
| Examples | `generated` lane, `catalog` group | `docs/source-lift/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`, `generated/technique_example_manifest.json`, `docs/readers/source-lift/TECHNIQUE_EXAMPLES.md` |
| Evidence notes | `generated` lane, `catalog` group | `docs/source-lift/EVIDENCE_NOTE_PROVENANCE_GUIDE.md`, `generated/technique_evidence_note_manifest.json`, `docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md` |
| KAG export | `generated` lane, `kag_export` group | `docs/source-lift/KAG_EXPORT.md`, `generated/kag_export.json`, `generated/kag_export.min.json` |
| GitHub review templates | `generated` lane, `catalog` group | template manifest surfaces under `generated/` |
| Semantic review | `generated` lane, `catalog` group | semantic review manifest surfaces under `generated/` |
| Shadow review | `generated` lane, `catalog` group | `generated/shadow_review_manifest.json`, `generated/shadow_review_manifest.min.json`, `docs/readers/review/SHADOW_PATTERNS.md` |
| Promotion readiness | `generated` lane, `catalog` group | promotion readiness generated outputs |

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
