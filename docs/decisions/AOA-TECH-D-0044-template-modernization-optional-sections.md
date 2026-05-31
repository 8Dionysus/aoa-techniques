# Template Modernization Optional Sections

Date: 2026-05-06

## Index Metadata

- Decision ID: AOA-TECH-D-0044
- Original date: 2026-05-06
- Surface classes: technique template
- Technique axes: template
- Mechanic parents: none
- Guard families: template validation
- Posture: accepted

## Status

Accepted.

## Context

`templates/TECHNIQUE.template.md` already names three current technique-shape
sections:

- `Atomic move`
- `Topology fit`
- `Small-agent execution shape`

The first template-modernization pilot over `proof/skill-support` made those
sections explicit in three canonical bundles. The rebuild then exposed a
contract mismatch: `scripts/validate_repo.py` still rejected those headings as
unexpected top-level sections even though the template presented them as the
desired source shape.

The corpus still contains many healthy older bundles that predate those
headings. Requiring the new sections immediately would turn a small pilot into
a full-corpus rewrite.

## Decision

Allow `Atomic move`, `Topology fit`, and `Small-agent execution shape` as
optional top-level sections in `TECHNIQUE.md` bundles.

The validator keeps them bounded:

- each optional section may appear at most once;
- optional sections must appear only in their fixed template positions;
- optional sections must not be empty when present;
- legacy bundles without those sections remain valid;
- `domain` and `kind` remain the current authoritative frontmatter axes.

This aligns the validator with the current template while preserving
template-modernization as a direct-read, cohort-by-cohort reform lane rather
than a required global migration.

## Alternatives

- Require the new sections in all `107` current bundles now.
  Rejected because old-template pressure is not itself a defect and the first
  pilot does not justify a mass rewrite.
- Remove the sections from the template and from the pilot sources.
  Rejected because the atom, topology-fit, and small-agent execution shape are
  already the right authoring direction for new or modernized techniques.
- Accept the sections in arbitrary positions.
  Rejected because ordering is part of the technique bundle contract and loose
  placement would make generated readers and small-agent extraction less
  predictable.

## Consequences

- Modernized bundles can expose their atom, topology fit, and small-agent
  execution shape without breaking validation.
- Older bundles can remain untouched until direct review shows that the new
  headings materially improve execution.
- The corpus is temporarily mixed by source shape, so future modernization
  waves must stay evidence-linked and avoid claiming that every old-template
  bundle is broken.
- Generated surfaces remain source-derived; generated hand edits are still not
  allowed.
- Any later decision to make these sections required across the corpus needs a
  separate migration plan, tests, generated rebuild, and closeout evidence.

## Verification

Expected checks:

```bash
python -m unittest tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```
