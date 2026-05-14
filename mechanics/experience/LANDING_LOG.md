# Experience Landing Log

This log records structural landings for the `aoa-techniques` Experience
mechanic.

## 2026-05-14 - Contract Packet Part Homes

Changed:

- moved Experience JSON schema/example packets from root `schemas/` and
  `examples/` into owning part-local `schemas/` and `examples/` directories
- replaced old internal local-host JSON identifiers with public part-local
  schema URLs without changing schema fields
- updated part map and provenance so contract packets are found through the
  owning Experience route, not root inventory

Verification lane:

```bash
python -m unittest tests.test_experience_adoption_contracts tests.test_experience_governance_contracts tests.test_experience_release_contracts
python -m unittest tests.test_experience_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no Experience contract field was changed
- no Experience contract became release approval, runtime authority, or
  Tree-of-Sophia write permission
- no Experience part was promoted into `techniques/`

## 2026-05-01 - Active Parts Split

Changed:

- added route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
  `LANDING_LOG.md`, and `ROADMAP.md`
- moved seven formerly flat Experience surfaces into part-local active homes
- added `parts/` route cards
- preserved Experience seed wording without promoting any part into a technique
  bundle or runtime authority

Verification lane:

```bash
python -m unittest tests.test_experience_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no raw wave receipt was copied into `legacy/raw/`
- no Experience surface was promoted into `techniques/`
- no live office, release, runtime, or Tree-of-Sophia authority was claimed

## 2026-05-03 - Legacy Scaffold Bridge

- Added `legacy/` scaffold files for source-to-active accounting.
- Kept raw inventory empty because the pre-split Experience seed surfaces were
  compact active material already distilled into part-local homes.
- Updated provenance to point to the scaffold instead of treating legacy as an
  absent later add-on.

## 2026-05-03 - Technique Candidate Bridge

Changed:

- added `parts/technique-candidate-bridge/` as the Experience extraction gate
- classified current Experience parts into `extract_watch`, `narrow_more`, and
  `hold_overlap` lanes
- linked the bridge to nearest existing technique bundles so future extraction
  starts from current canon instead of redrafting mechanics
- updated the owner request receipt for `ORQ-EXPERIENCE-TECHNIQUES-001`

Verification lane:

```bash
python -m unittest tests.test_experience_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no Experience part was promoted into `techniques/`
- no raw legacy source was added
- no live office, release, runtime, proof, role, memory, routing, or
  Tree-of-Sophia authority was claimed
