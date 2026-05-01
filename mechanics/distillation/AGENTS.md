# AGENTS.md

Route card for `aoa-techniques/mechanics/distillation/`.

## Applies to

This card applies to the Distillation mechanics package and every nested path
under it until a nearer `AGENTS.md` narrows the lane.

## Read before editing

1. Repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/distillation/README.md`
4. The nearest part README, or `PROVENANCE.md` when touching lineage

## Role

This package owns the technique-side Distillation route inside
`aoa-techniques`. It turns donor pressure, cross-layer notes, and long-gap
material into reusable-practice candidates, holds, or import paths.

It does not own AoA center doctrine, skill execution, eval verdicts, routing
policy, role contracts, memory semantics, runtime behavior, ToS canon, or final
technique promotion.

## Source split

- `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/` own current active
  route.
- `PROVENANCE.md` is the active-first bridge back to donor and legacy evidence.
- `legacy/` preserves distillation accounting and is the place for future
  pre-prune receipts.
- `incoming/` wave packets and sibling-repo donor notes are evidence surfaces;
  they do not become active law by appearing here.

## Editing posture

- Keep candidate ledgers distinct from promoted technique bundles.
- If a candidate becomes a stable reusable practice with inputs, outputs, risks,
  and validation, route it into `techniques/` through the normal bundle path.
- If a ledger is compacted, preserve the pre-pruned accounting in `legacy/raw/`
  or point to an explicit preserved source.
- Keep external donor wording sanitized and narrower than the donor's total
  worldview.
- Keep sibling-repo routes as provenance, not owner transfer.

## Verify

For Distillation topology changes:

```bash
python -m unittest tests.test_distillation_mechanics_topology
```

For the external candidate registry:

```bash
python mechanics/distillation/parts/external-candidate-ledger/scripts/build_external_candidate_registry.py --check
python mechanics/distillation/parts/external-candidate-ledger/scripts/validate_external_candidate_registry.py
python -m pytest -q mechanics/distillation/parts/external-candidate-ledger/tests/test_external_candidate_registry.py
```

For the cross-layer candidate registry:

```bash
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/build_cross_layer_candidate_registry.py --check
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/validate_cross_layer_candidate_registry.py
python -m pytest -q mechanics/distillation/parts/cross-layer-candidate-ledger/tests/test_cross_layer_candidate_registry.py
```

For repository-level safety after structure changes:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```

## Closeout

Report which active parts changed, whether any legacy source was moved or
distilled, which validation ran, what was not moved, and where the next
Distillation pass should resume.
