# AGENTS.md

Route card for `aoa-techniques/mechanics/method-growth/`.

## Applies to

This card applies to the Method-growth mechanics package and every nested path
under it until a nearer `AGENTS.md` narrows the lane.

## Read before editing

1. Repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/REQUEST_RECEIPTS.md` when touching `ORQ-METHOD-TECHNIQUES-001`
4. `mechanics/method-growth/README.md`
5. The nearest part README, or `PROVENANCE.md` when touching lineage

## Role

This package owns the technique-side Method-growth route inside
`aoa-techniques`: adoption posture, reusable-practice promotion, retention,
obsolescence, and technique-to-skill handoff boundaries.

It does not own AoA center doctrine, skill execution, eval verdicts, memory
objects, playbook choreography, routing behavior, runtime behavior, or final
owner acceptance outside this repository.

## Source split

- `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/` own current active
  route.
- `PROVENANCE.md` is the active-first bridge back to the pre-split v0.7 adoption
  surfaces.
- `LANDING_LOG.md` records structural landings.
- `ROADMAP.md` names the next honest passes.

## Editing posture

- Keep adoption and handoff mechanics distinct from promoted technique bundles.
- If a part starts carrying a stable reusable practice with full bundle shape,
  route the practice into `techniques/` through the normal review path.
- Do not treat technique adoption as skill activation or sibling owner consent.
- Do not treat retention, obsolescence, or pruning notes as proof verdicts.
- Keep local owner consent, rollback, and evidence posture visible.

## Verify

For Method-growth topology changes:

```bash
python -m unittest tests.test_method_growth_mechanics_topology
```

For repository-level safety after structure changes:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```

## Closeout

Report which active parts changed, whether any legacy source was moved, which
validation ran, what was not moved, and where the next Method-growth pass should
resume.
