# AGENTS.md

Route card for `aoa-techniques/mechanics/experience/`.

## Applies to

This card applies to the Experience mechanics package and every nested path
under it until a nearer `AGENTS.md` narrows the lane.

## Read before editing

1. Repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/REQUEST_RECEIPTS.md` when touching `ORQ-EXPERIENCE-TECHNIQUES-001`
4. `mechanics/experience/README.md`
5. The nearest part README, or `PROVENANCE.md` when touching lineage

## Role

This package owns the technique-side Experience route inside `aoa-techniques`:
governance, authority, scope, handoff, appeal, sealed decision, and service
clarity practice surfaces.

It does not own live office runtime, release approval, assistant self-authority,
Tree-of-Sophia meaning, proof verdicts, skill execution, or owner acceptance
outside this repository.

## Source split

- `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/` own current active
  route.
- `PROVENANCE.md` is the active-first bridge back to the pre-split Experience
  seed surfaces.
- `LANDING_LOG.md` records structural landings.
- `ROADMAP.md` names the next honest passes.

## Editing posture

- Keep reusable practice separate from live office, release, runtime, and ToS
  authority.
- If a part becomes a stable technique bundle, move it through the normal
  `techniques/` review path.
- Keep upstream AoA and ToS references as authority boundaries, not hidden
  dependencies for portable practice.
- Do not turn service clarity or handoff compression into workflow execution.

## Verify

For Experience topology changes:

```bash
python -m unittest tests.test_experience_mechanics_topology
```

For repository-level safety after structure changes:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```

## Closeout

Report which active parts changed, whether any legacy source was moved, which
validation ran, what was not moved, and where the next Experience pass should
resume.
