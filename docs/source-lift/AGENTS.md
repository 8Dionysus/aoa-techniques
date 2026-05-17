# AGENTS.md

## Applies to

This card applies to `docs/source-lift/` and all source-lift guide surfaces in
this district.

## Role

`docs/source-lift/` holds authored contracts for KAG-friendly source-lift
families and their bounded exports.

It does not own generated Markdown readers, generated JSON, technique bundle
meaning, KAG substrate authority, graph behavior, scoring, or sibling-repo
truth.

## Read before editing

Read root `AGENTS.md`, `docs/AGENTS.md`, `docs/ROOT_SURFACE_LAW.md`,
`docs/guardrails/THEMATIC_DISTRICT_PROTOCOL.md`, and
`docs/source-lift/README.md`.

For generated reader output, also read `docs/readers/AGENTS.md` and the
matching `docs/readers/source-lift/README.md`, `docs/readers/repo/README.md`,
or `docs/readers/review/README.md`.

## Boundaries

- Keep authored source-lift contracts here and generated Markdown readers under
  `docs/readers/`.
- Keep generated JSON under `generated/`.
- Keep technique meaning in `techniques/**/TECHNIQUE.md` and bundle-local
  notes, checks, and examples.
- Do not turn source-lift guides into KAG graph doctrine, selection engines,
  execution policy, or proof verdicts.
- When moving a source-lift guide, update the builder/test links that generate
  the reader companion.

## Validation

Choose the matching narrow builder for the changed family first:

```bash
python scripts/build_section_manifest.py
python scripts/build_checklist_manifest.py
python scripts/build_example_manifest.py
python scripts/build_evidence_note_manifest.py
python scripts/build_repo_doc_surface_manifest.py
python scripts/build_kag_export.py
```

Then run:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```

For broad source-lift topology changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report which source-lift family changed, which generated readers were rebuilt,
which JSON manifests stayed fresh, and whether any flat `docs/*.md` pressure
remains.
