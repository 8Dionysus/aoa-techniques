# AGENTS.md

## Guidance for `tests/`

`tests/` protects technique contracts, validators, builders, generated parity, and downstream-consumer assumptions.

Tests should keep reusable practice reproducible. Prefer cases that expose invariants, boundary conditions, drift, and transfer behavior rather than incidental formatting.

Do not update snapshots or expected generated surfaces without rebuilding and checking the source-authored technique or manifest that owns meaning.

Keep fixtures public-safe. No secrets, private transcripts, hidden benchmark data, or machine-local paths.

Verify with:

```bash
python -m unittest discover -s tests
python scripts/validate_semantic_agents.py
```
