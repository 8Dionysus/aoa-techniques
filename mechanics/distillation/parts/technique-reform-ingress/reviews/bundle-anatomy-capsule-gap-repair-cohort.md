# Bundle Anatomy Capsule Gap Repair Cohort

Source packet: [Bundle Anatomy Corpus Synthesis](bundle-anatomy-corpus-synthesis.md)

Status: first-repair-cohort, generated-reader repair, no technique path
movement, no frontmatter migration, no status promotion.

## Verdict

Repair the first concrete post-synthesis cohort by fixing capsule extraction
for wrapped Markdown list items.

The corpus synthesis selected `AOA-T-0095` and `AOA-T-0096` because their
generated capsule shorts lost readability around wrapped bullets:

- `AOA-T-0095`: `before the;`
- `AOA-T-0096`: `older or.`

Direct inspection showed the authored source was coherent and the defect lived
in generator extraction: `capsule_markdown_items` collected only lines with a
list marker and ignored indented continuation lines that belong to the same
bullet.

## Repair Shape

Chosen repair: builder-level extraction fix.

Touched source surfaces:

- `scripts/validate_repo.py`
- `tests/test_validate_repo.py`
- `docs/selection/TECHNIQUE_CAPSULE_GUIDE.md`

Regenerated derived surfaces:

- `generated/technique_capsules.json`
- `generated/technique_capsules.min.json`
- `docs/readers/runtime/TECHNIQUE_CAPSULES.md`

No technique bundle source was edited. The generated capsule changes are
derived from the existing authored bundles plus the corrected wrapped-bullet
extraction rule.

## Blast Radius

The builder repair changes capsule text for `11` entries, all in places where
the previous extraction dropped wrapped sentence tails:

- `AOA-T-0089`
- `AOA-T-0090`
- `AOA-T-0095`
- `AOA-T-0096`
- `AOA-T-0101`
- `AOA-T-0102`
- `AOA-T-0103`
- `AOA-T-0104`
- `AOA-T-0105`
- `AOA-T-0106`
- `AOA-T-0107`

The repair remains bounded because it does not change capsule fields, ordering,
schema, source-of-truth posture, or bundle meaning. It only preserves wrapped
list item text that was already authored.

## Validation

Passed locally:

1. the targeted tests
2. the capsule builder
3. the repository test suite
4. the release lane
5. repository validation

## Stop Lines

- Do not hand-edit generated capsule files.
- Do not rewrite technique source just to make generated text easier.
- Do not widen capsule extraction into selection, scoring, KAG, or policy
  routing.
- Do not treat this repair as template modernization.
