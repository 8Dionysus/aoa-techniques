# AGENTS.md

## Guidance for `tests/`

`tests/` protects root-owned technique contracts, validators, builders,
generated parity, root legacy, and downstream-consumer assumptions.

Mechanic-owned tests belong beside the owning mechanic under
`mechanics/<slug>/tests/`, shared mechanics-wide tests belong under
`mechanics/tests/`, and part-local tests belong under
`mechanics/<slug>/parts/<part>/tests/`.

Tests should keep reusable practice reproducible. Prefer cases that expose invariants, boundary conditions, drift, and transfer behavior rather than incidental formatting.

Do not update snapshots or expected generated surfaces without rebuilding and checking the source-authored technique or manifest that owns meaning.

Keep fixtures public-safe. No secrets, private transcripts, hidden benchmark data, or machine-local paths.

Verify with:

```bash
python scripts/run_tests.py
python scripts/validate_semantic_agents.py
```
