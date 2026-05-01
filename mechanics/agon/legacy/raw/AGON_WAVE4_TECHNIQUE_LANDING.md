# Agon Wave IV Technique Landing

## Scope

This landing receives candidate requests from `Agents-of-Abyss` Wave IV owner binding.

It does not create canonical techniques.

## Validation

```bash
python scripts/build_agon_technique_binding_candidates.py --check
python scripts/validate_agon_technique_binding_candidates.py
python -m pytest -q tests/test_agon_technique_binding_candidates.py
```

## Exit criteria

- candidate requests are deterministic;
- all candidates remain `requested_not_landed`;
- no candidate defines legal move vocabulary;
- no candidate creates skill workflow;
- no candidate writes proof verdicts or scars;
- no candidate starts arena runtime.

## Later growth

A later technique wave may choose a small subset of candidates and turn them into real technique bundles.

Do not promote all candidates at once. Agon grows by tested organs, not by stuffing the beast with paper.
