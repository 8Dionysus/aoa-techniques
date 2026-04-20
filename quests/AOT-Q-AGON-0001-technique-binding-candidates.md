# AOT-Q-AGON-0001: Agon Technique Binding Candidates

## Intent

Receive Wave IV practice candidate requests from `Agents-of-Abyss`.

## Done when

- config and generated candidate index are present;
- every candidate remains `requested_not_landed`;
- validation passes;
- no candidate is promoted as a canonical technique by this quest.

## Verify

```bash
python scripts/build_agon_technique_binding_candidates.py --check
python scripts/validate_agon_technique_binding_candidates.py
python -m pytest -q tests/test_agon_technique_binding_candidates.py
```
