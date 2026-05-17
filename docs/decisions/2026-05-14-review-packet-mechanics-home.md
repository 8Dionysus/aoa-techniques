# Review Packet Mechanics Home

Status: accepted
Date: 2026-05-14

## Context

The repository root docs had already been slimmed toward public route,
authority, canon, generated-reader guides, and status surfaces. After that
cleanup, the flat `docs/` directory still carried authored
`*_SEMANTIC_REVIEW.md` and `*_SHADOW_REVIEW.md` files.

Those files are useful, but they are review packets: they capture bounded
working-set judgment, migration pressure, and caution seams. They are not
public entry docs, root doctrine, generated readers, or technique bundle
meaning.

`mechanics/distillation/parts/technique-reform-ingress/reviews/` already owns
the classification-reform review packet lane.

## Options

- Keep all semantic and shadow review packets flat in `docs/`.
- Move them to root `legacy/` as old evidence.
- Move them under the Distillation technique-reform ingress review lane, while
  keeping public guides and generated reader surfaces in `docs/`.

## Decision

Move authored semantic and shadow review packets to:

- `mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/`
- `mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/`

Keep `docs/review/SEMANTIC_REVIEW_GUIDE.md`, `docs/review/TECHNIQUE_SHADOW_GUIDE.md`,
`docs/readers/selection/SELECTION_PATTERNS.md`, and
`docs/readers/review/SHADOW_PATTERNS.md` as public reader
routes into those packets.

Update validators and generated manifests so the packet paths are source paths,
not post-hoc link aliases.

## Consequences

- `docs/` stays closer to its public route and guide role.
- Review packets remain active, not legacy, because validators and generated
  manifests still consume them.
- Distillation owns the movement/review lane; technique bundles still own
  technique meaning.
- Generated semantic and shadow manifests remain derived lookup aids, not
  review authority.
- Historical raw legacy receipts are not rewritten just because packet paths
  moved.

## Verification

Expected checks:

```bash
python -m unittest tests.test_validate_repo
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```
