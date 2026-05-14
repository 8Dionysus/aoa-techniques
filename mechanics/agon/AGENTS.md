# AGENTS.md

Route card for `aoa-techniques/mechanics/agon/`.

## Applies to

This card applies to the Agon mechanics package and every nested path under it
until a nearer `AGENTS.md` narrows the lane.

## Read before editing

1. Repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/agon/README.md`
4. The nearest part README, or `PROVENANCE.md` when touching legacy lineage

## Role

This package owns the technique-side Agon route inside `aoa-techniques`.
It stages and constrains requested practice candidates, but it does not own Agon
doctrine, arena behavior, skill execution, proof verdicts, memory, routing, or
ToS canon.

## Source split

- `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/` own current active route.
- `PROVENANCE.md` is the active-first bridge to preserved wave sources.
- `legacy/` preserves raw Wave IV and Wave XV landing receipts.
- Part-local `config/`, `generated/`, `schemas/`, `examples/`, `scripts/`,
  `tests/`, and recurrence manifests own current Agon technical artifacts.

## Editing posture

- Do not edit raw wave receipts to change current behavior.
- If a raw source changes current behavior, update the relevant active part
  first, then update `PROVENANCE.md`, `legacy/INDEX.md`, and `LANDING_LOG.md`.
- Keep requested candidates distinct from promoted technique bundles.
- Keep cross-repo boundaries explicit in every new route.

## Verify

For Agon technique binding candidates:

```bash
python mechanics/agon/parts/move-technique-bridge/scripts/build_agon_technique_binding_candidates.py --check
python mechanics/agon/parts/move-technique-bridge/scripts/validate_agon_technique_binding_candidates.py
python -m pytest -q mechanics/agon/parts/move-technique-bridge/tests/test_agon_technique_binding_candidates.py
```

For Agon epistemic candidates:

```bash
python mechanics/agon/parts/epistemic-technique-candidates/scripts/build_agon_epistemic_technique_candidates.py --check
python mechanics/agon/parts/epistemic-technique-candidates/scripts/validate_agon_epistemic_technique_candidates.py
python -m pytest -q mechanics/agon/parts/epistemic-technique-candidates/tests/test_agon_epistemic_technique_candidates.py
```

For repository-level safety after structure changes:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```

## Closeout

Report which active parts changed, whether any legacy source was moved or
distilled, which validation ran, what was not moved, and where the next Agon
pass should resume.
