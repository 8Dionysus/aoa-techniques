# Recurrence Landing Log

This log records checked structural landings for the `aoa-techniques`
recurrence package. It is not a live status surface and not a substitute for
technique review.

## 2026-05-14 - Live Receipt Publisher Part Home

- Moved `publish_live_receipts.py` from root `scripts/` into
  `parts/live-observation-producers/scripts/`.
- Kept `.aoa/live_receipts/technique-receipts.jsonl` as owner-local
  observation evidence only, not technique status, candidate, proof, runtime,
  quest closure, or recurrence-law authority.
- Updated README, part map, provenance, root surface law, changelog, tests, and
  roadmap parity references to use the part-local script home.
- Recorded the placement rationale in
  [mechanic-script-homes](../../docs/decisions/AOA-TECH-D-0048-mechanic-script-homes.md).

Verification lane:

```bash
python -m unittest tests.test_publish_live_receipts
python -m unittest tests.test_recurrence_mechanics_topology
python scripts/validate_repo.py
python scripts/release_check.py
git diff --check
```

## 2026-05-14 - Manifest Part Home

- Moved recurrence beacon manifests from root `manifests/recurrence/` into
  `parts/live-observation-producers/manifests/recurrence/`.
- Kept the component and hook binding set as advisory observation evidence,
  not technique status, candidate, proof, runtime, or recurrence-law authority.
- Updated `PARTS.md`, `PROVENANCE.md`, the producer part README, root surface
  law, changelog, decision record, and topology tests to use the part-local
  manifest home.

Verification lane:

```bash
python -m unittest tests.test_recurrence_manifest_topology
python -m unittest tests.test_recurrence_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

## 2026-05-02

- Split the two pre-split flat recurrence files into active part-local homes:
  `parts/live-observation-producers/README.md` and
  `parts/review-decision-closure/README.md`.
- Added active package route files: `AGENTS.md`, `DIRECTION.md`, `PARTS.md`,
  `PROVENANCE.md`, `LANDING_LOG.md`, `ROADMAP.md`, `parts/AGENTS.md`, and
  `parts/README.md`.
- Recorded recurrence as non-ORQ candidate-only pressure in
  `mechanics/REQUEST_RECEIPTS.md`; no direct
  `ORQ-RECURRENCE-TECHNIQUES-*` request exists in the current AoA queue.
- Added topology coverage for the active recurrence split and updated manifest
  topology coverage to the new part-local producer path.

## 2026-05-03 - Legacy Scaffold Bridge

- Added `legacy/` scaffold files for source-to-active accounting.
- Kept raw inventory empty because the pre-split recurrence surfaces were
  compact active material already distilled into part-local homes.
- Updated provenance to point to the scaffold instead of treating legacy as an
  absent later add-on.
