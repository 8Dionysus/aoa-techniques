# AGENTS.md

## Guidance for `mechanics/tests/`

`mechanics/tests/` owns mechanics-wide regression tests that span more than one
mechanic package.

Use this home for package-card standards, shared request-receipt posture, shared
legacy scaffold expectations, and cross-mechanic contract checks. Tests that
only serve one mechanic belong in `mechanics/<slug>/tests/`; tests that only
serve one part belong in `mechanics/<slug>/parts/<part>/tests/`.

These tests guard mechanics route contracts. They do not authorize technique
promotion, owner acceptance, runtime behavior, or sibling-repo status changes.

Verify with:

```bash
python -m unittest discover -s mechanics/tests
python scripts/run_tests.py
```
