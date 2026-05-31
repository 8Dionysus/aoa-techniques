# Canonical Decision IDs And Indexes

Status: accepted
Date: 2026-05-31

## Index Metadata

- Decision ID: AOA-TECH-D-0065
- Original date: 2026-05-31
- Surface classes: decision record, docs route, validation guard
- Technique axes: decision index
- Mechanic parents: none
- Guard families: decision index/read-model, docs route
- Posture: accepted

## Context

`docs/decisions/` already held useful rationale for technique-canon structure,
mechanic package homes, root/docs placement, agent surfaces, and generated
read-model choices. Its live files were still addressed by date-prefixed names,
and the directory README carried a manually maintained record table.

That shape made the district harder to use as the corpus grows: chronological
paths are not stable handles, manual indexes invite drift, and agents need a
fast way to find rationale by technique axis, mechanic parent, surface class, or
validation guard without treating generated readouts as authority.

## Options considered

1. Keep date-prefixed filenames and keep updating the README table by hand.
2. Add a generated compatibility lookup while leaving source filenames
   date-prefixed.
3. Give each record a canonical `AOA-TECH-D-####` ID, rename source files to
   full canonical-ID filenames, and generate lookup indexes from explicit
   per-record metadata.

## Decision

Use full canonical-ID decision filenames as the active source files for
`aoa-techniques` decisions:

- `docs/decisions/AOA-TECH-D-0001-*.md`
- `docs/decisions/AOA-TECH-D-0002-*.md`
- `docs/decisions/AOA-TECH-D-####-*.md`

Each decision record now owns an `## Index Metadata` block with original date,
surface classes, technique axes, mechanic parents, guard families, and posture.
Generated lookup indexes under `docs/decisions/indexes/` are derived from that
metadata and checked by `python scripts/generate_decision_indexes.py --check`.

Previous date-prefixed paths live in git and PR history only. They are not kept
as a live repository lookup layer.

## Rationale

The stable ID gives agents and reviewers a durable handle that does not change
when the original landing date is no longer the best lookup key.

The metadata-backed indexes preserve the useful parts of chronological reading
while adding technique-canon-specific lookup routes: surface class, technique
axis, mechanic parent, and validation or guard family. This matches the local
organ better than copying a skill-lane index from `aoa-skills`.

Keeping the generated indexes weaker than decision notes protects the authority
boundary: indexes make lookup cheaper, but the decision record still owns the
rationale, and current source surfaces still define what the repository now
does.

## Consequences

- Decision references should use canonical `AOA-TECH-D-####` paths.
- New decisions must include index metadata before generated lookup indexes can
  remain fresh.
- The release check now catches stale decision indexes or drifted
  `index_contract.yaml`.
- Historical date-prefixed links are not kept as live compatibility files, so
  external references to old paths should route through git/PR history.
- The district gains one more generated surface family, with the usual rule
  that generated output is a read model, not authored meaning.

## Source surfaces

- `AGENTS.md`
- `docs/AGENTS.md`
- `docs/decisions/AGENTS.md`
- `docs/decisions/README.md`
- `docs/decisions/TEMPLATE.md`
- `docs/ROOT_SURFACE_LAW.md`
- `scripts/generate_decision_indexes.py`
- `scripts/decision_indexes.py`
- `scripts/release_check.py`
- `tests/test_decision_indexes.py`

## Follow-up route

When a future decision changes technique axes, mechanic parent families, guard
families, or the index contract itself, update `scripts/decision_indexes.py`,
`docs/decisions/indexes/index_contract.yaml`, the generated indexes, and tests
together.

Do not add date-path aliases unless a separate compatibility decision proves
that live compatibility files are worth the extra route surface.

## Verification

Use:

```bash
python scripts/generate_decision_indexes.py --check
python scripts/run_tests.py
python scripts/validate_repo.py
python scripts/release_check.py
```
