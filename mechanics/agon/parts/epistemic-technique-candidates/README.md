# Agon Epistemic Technique Candidates

Requested-only practice candidates behind epistemic move extensions. They are not promoted techniques until owner review.

## Candidate surfaces

```text
config/agon_epistemic_technique_candidates.seed.json
generated/agon_epistemic_technique_candidates.min.json
```

Each candidate remains `requested_only_candidate` until a bundle lands through
normal `aoa-techniques` review.

## Validation

```bash
python mechanics/agon/parts/epistemic-technique-candidates/scripts/build_agon_epistemic_technique_candidates.py --check
python mechanics/agon/parts/epistemic-technique-candidates/scripts/validate_agon_epistemic_technique_candidates.py
python -m pytest -q mechanics/agon/parts/epistemic-technique-candidates/tests/test_agon_epistemic_technique_candidates.py
```

## Provenance

The Wave XV landing receipt is preserved at
[`../../legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md`](../../legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md).
