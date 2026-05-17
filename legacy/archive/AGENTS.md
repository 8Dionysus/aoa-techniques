# AGENTS.md

## Applies to

This card applies to `legacy/archive/`.

## Role

`legacy/archive/` preserves retired public-safe repo-wide surfaces whose active
route now lives elsewhere.

It is for auditability after a root, docs-root, incoming, or other repo-wide
tail surface stops being current. It is not a second current docs tree.

## Read before editing

Read:

1. `../AGENTS.md`
2. `../README.md`
3. `../INDEX.md`
4. `README.md`
5. the current source surface that replaces the archived material

For the archived root-agent reference, also read `AGENTS_ROOT_REFERENCE.md`
before moving or summarizing it.

## Boundaries

- Do not archive active source files without updating links, route docs, and
  `../INDEX.md`.
- Do not use this directory for mechanic-local lineage; use
  `../../mechanics/<slug>/legacy/` when one mechanic owns the history.
- Do not treat archived generated output as stronger than the generator or
  authored source.
- Do not store unreviewed candidate intake here; use `../../incoming/`.
- Do not add archive material without naming the active replacement route or
  explicit hold status.

## Validation

Run:

```bash
python -m unittest tests.test_root_legacy_topology
python scripts/validate_repo.py
```

Use `python scripts/release_check.py` when archived docs affect public release
posture, root links, generated mirrors, or broad route docs.

## Closeout

Report archive files changed, the current replacement route, links updated,
`../INDEX.md` update, public-safe review, and checks run or skipped.
