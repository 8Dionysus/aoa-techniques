# Release Support Landing Log

This log records checked structural landings for the `aoa-techniques`
release-support package. It is not a live release-status surface and not a
substitute for technique review, public-claim proof, or owner acceptance.

## 2026-05-14 - Contract Packet Part Homes

- Moved release-support JSON schema/example packets from root `schemas/` and
  `examples/` into owning part-local `schemas/` and `examples/` directories.
- Replaced old internal local-host JSON identifiers with public part-local
  schema URLs without changing schema fields.
- Updated part map and provenance so contract packets are found through the
  owning release-support route, not root inventory.
- Did not change release-support contract fields, claim release authority,
  claim public support proof, or promote release-support pressure into direct
  owner acceptance.

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

## 2026-05-02

- Split the two pre-split flat release-support files into active part-local
  homes: `parts/installation-techniques/README.md` and
  `parts/sovereign-release-techniques/README.md`.
- Added active package route files: `AGENTS.md`, `DIRECTION.md`, `PARTS.md`,
  `PROVENANCE.md`, `LANDING_LOG.md`, `ROADMAP.md`, `parts/AGENTS.md`, and
  `parts/README.md`.
- Recorded release-support as non-ORQ candidate-only pressure in
  `mechanics/REQUEST_RECEIPTS.md`; no direct
  `ORQ-RELEASE-TECHNIQUES-*` request exists in the current AoA queue.
- Added topology coverage for the active release-support split.

## 2026-05-03 - Legacy Scaffold Bridge

- Added `legacy/` scaffold files for source-to-active accounting.
- Kept raw inventory empty because the pre-split release-support surfaces were
  compact active material already distilled into part-local homes.
- Updated provenance to point to the scaffold instead of treating legacy as an
  absent later add-on.
