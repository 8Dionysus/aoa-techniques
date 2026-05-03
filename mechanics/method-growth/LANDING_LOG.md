# Method-Growth Landing Log

This log records structural landings for the `aoa-techniques` Method-growth
mechanic.

## 2026-05-01 - Active Parts Split

Changed:

- added route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
  `LANDING_LOG.md`, and `ROADMAP.md`
- moved five formerly flat Method-growth surfaces into part-local active homes
- added `parts/` route cards
- preserved v0.7 downstream adoption-wave wording without promoting any part
  into a technique bundle

Verification lane:

```bash
python -m unittest tests.test_method_growth_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no raw wave receipt was copied into `legacy/raw/`
- no adoption surface was promoted into `techniques/`
- no technique-to-skill handoff was treated as skill acceptance

## 2026-05-03 - Legacy Scaffold Bridge

- Added `legacy/` scaffold files for source-to-active accounting.
- Kept raw inventory empty because the pre-split adoption surfaces were compact
  active material already distilled into part-local homes.
- Updated provenance to point to the scaffold instead of treating legacy as an
  absent later add-on.

## 2026-05-03 - Pattern Adoption Gate Extraction

- Extracted the atomic local adoption gate into
  `AOA-T-0101 local-pattern-adoption-gate`.
- Kept request, readiness, shadow, decision, activation, and retention lifecycle
  pressure in Method-growth instead of widening the technique bundle.
- Updated the pattern-adoption part and provenance bridge to point to the
  promoted atom without treating it as skill activation or sibling owner
  acceptance.

## 2026-05-03 - Skill Proposal Handoff Packet Extraction

- Extracted the atomic proposal packet handoff into
  `AOA-T-0102 skill-proposal-handoff-packet`.
- Kept skill acceptance, skill workflow meaning, and activation outside
  `aoa-techniques`.
- Updated the technique-to-skill-handoff part and provenance bridge to point to
  the promoted atom without treating the packet as a skill.

## 2026-05-03 - Adopted Practice Retention Review Extraction

- Extracted the atomic retention review into
  `AOA-T-0103 adopted-practice-retention-review`.
- Kept obsolescence, deletion, proof, memory writeback, skill activation, route
  behavior, and runtime mutation outside the technique bundle.
- Updated the retention-checks part and provenance bridge to point to the
  promoted atom without treating past adoption as permanent approval.

## 2026-05-03 - Superseded Practice Obsolescence Route Extraction

- Extracted the atomic obsolescence route packet into
  `AOA-T-0104 superseded-practice-obsolescence-route`.
- Kept deletion, deprecation execution, proof, memory writeback, skill
  activation, route behavior, runtime mutation, and owner-local retirement
  outside the technique bundle.
- Updated the obsolescence part and provenance bridge to point to the promoted
  atom without treating pruning or cleanup as erasure.
