# Experience Active Parts Split

Status: accepted

Date: 2026-05-01

## Context

`mechanics/experience/` kept seven active seed surfaces as flat package-root
files. The files mixed governance, authority, appeal, sealed decision,
office/service scope, handoff compression, and service clarity notes.

The current project direction asks mechanics packages to follow the AoA-style
active/parts/provenance split when they carry more than a simple README. The
Experience files were active owner-local practice notes, not large raw receipts.

## Decision

Move the seven flat Experience surfaces into `parts/*/README.md` and add the
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

## Consequences

- Experience now has the same active route shape as the other grown mechanics
  packages.
- `ORQ-EXPERIENCE-TECHNIQUES-001` can point at concrete local response surfaces
  without treating them as technique canon.
- Governance, office/service, handoff, and sealed decision practice stay
  portable only as practice notes; they do not become live office, release,
  runtime, proof, or ToS authority.
- Future work can decide one part at a time whether a real technique bundle is
  warranted.

## Verification

Verify with:

```bash
python -m unittest tests.test_experience_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```
