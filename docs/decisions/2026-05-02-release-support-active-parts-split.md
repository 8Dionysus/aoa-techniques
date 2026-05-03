# Release Support Active Parts Split

Status: accepted

Date: 2026-05-02

## Context

`mechanics/release-support/` kept two active technique-layer surfaces as flat
package-root files: installation techniques and sovereign release techniques.

`Agents-of-Abyss` owns the center Release-support mechanic with
state-transition law, public support posture, federation release protocol,
owner split, and owner request packets. The current AoA queue has no direct
`ORQ-RELEASE-TECHNIQUES-*` request, so `aoa-techniques` should not present this
split as owner-request acceptance.

The local job is narrower: keep release-shaped reusable practice pressure
legible without letting installation or release ritual notes become release
approval, public claim proof, operator consent, runtime rollback, sibling
acceptance, or technique promotion.

## Decision

Move the two flat Release-support surfaces into `parts/*/README.md` and add the
active package route files:

- `AGENTS.md`
- `DIRECTION.md`
- `PARTS.md`
- `PROVENANCE.md`
- `LANDING_LOG.md`
- `ROADMAP.md`
- `parts/AGENTS.md`
- `parts/README.md`

Do not create `legacy/raw/` in this pass because no large wave receipt or raw
source packet is being preserved. The previous flat files become active
part-local homes.

Add Release-support to `mechanics/REQUEST_RECEIPTS.md` only under Non-ORQ
Center Pressure, with `candidate-only` posture.

## Consequences

- Release-support now matches the active route shape used by the grown
  mechanics packages.
- Installation practice remains bounded by owner-local validation, operator
  review, and fail-closed behavior.
- Sovereign release practice remains bounded by no authority sealing, no
  operator substitution, no policy precedent, and no runtime rollback
  execution.
- AoA release-support law, public claim proof, public projection, routing ABI,
  SDK compatibility, stats summaries, runtime deployment, rollback execution,
  sibling acceptance, and ToS write authority stay with their owning
  repositories.

## Verification

Verify with:

```bash
python -m unittest tests.test_release_support_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
