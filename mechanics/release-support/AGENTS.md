# AGENTS.md

Route card for `mechanics/release-support/`.

## Purpose

This package owns the `aoa-techniques` side of Release-support: installation
practice and release ritual practice that may feed future technique canon.

It does not own AoA release-support law, public claim authority, release
approval, operator consent, sibling acceptance, proof verdicts, runtime
deployment, rollback execution, profile projection, route ABI, SDK
compatibility, stats summaries, or technique status changes.

## Start here

1. Root `AGENTS.md`.
2. `mechanics/AGENTS.md`.
3. `mechanics/release-support/README.md`.
4. `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, and the touched part README.
5. `mechanics/REQUEST_RECEIPTS.md` only when naming AoA center-side pressure.

## Local law

- Keep release-support here technique-layered: reusable practice notes, not
  release authority.
- Do not import `Agents-of-Abyss` release-support law as local implementation
  authority.
- Do not treat installation or release ritual notes as public claim proof,
  owner acceptance, release approval, runtime truth, or rollback execution.
- Keep ToS write boundaries and sibling owner truth outside this package.
- If a stable reusable practice emerges, route it into `techniques/` through
  the normal technique review path.

## Verify

Use the root validation path after changes:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```
