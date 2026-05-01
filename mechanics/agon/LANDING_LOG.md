# Agon Landing Log

This ledger records checked landings for the `aoa-techniques` side of Agon
mechanics.

## 2026-05-01 - Active/legacy split

Scope:

- moved Wave IV and Wave XV landing receipts into `legacy/raw/`
- moved current Agon behavior into active `parts/`
- added `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, and legacy accounting
- kept requested candidate posture unchanged

Stop-lines preserved:

- requested candidates are not promoted techniques
- `aoa-techniques` does not define Agon lawful move vocabulary
- no skill workflow, proof verdict, scar, retention, rank, arena, KAG, memory, or
  ToS authority is created here

Validation lane:

- `python mechanics/agon/parts/move-technique-bridge/scripts/build_agon_technique_binding_candidates.py --check`
- `python mechanics/agon/parts/move-technique-bridge/scripts/validate_agon_technique_binding_candidates.py`
- `python -m pytest -q mechanics/agon/parts/move-technique-bridge/tests/test_agon_technique_binding_candidates.py`
- `python mechanics/agon/parts/epistemic-technique-candidates/scripts/build_agon_epistemic_technique_candidates.py --check`
- `python mechanics/agon/parts/epistemic-technique-candidates/scripts/validate_agon_epistemic_technique_candidates.py`
- `python -m pytest -q mechanics/agon/parts/epistemic-technique-candidates/tests/test_agon_epistemic_technique_candidates.py`
- `python scripts/validate_repo.py`
- `python -m unittest discover -s tests`
