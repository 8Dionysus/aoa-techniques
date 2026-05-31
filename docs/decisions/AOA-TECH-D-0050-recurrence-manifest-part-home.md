# Recurrence Manifest Part Home

Status: accepted
Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0050
- Original date: 2026-05-14
- Surface classes: mechanic package, mechanic part, generated/readout
- Technique axes: mechanic bridge
- Mechanic parents: recurrence
- Guard families: mechanic topology, part-local artifact, generated/read-model
- Posture: accepted

## Context

The repository root still had `manifests/recurrence/` with the
`component:techniques:canon-and-intake-beacons` manifest and its session-stop
hook binding set.

Those files are recurrence observation evidence. They describe technique canon,
candidate-intake, promotion-readiness, and live-receipt beacons that feed local
review pressure. They are not root public entry surfaces, technique bundle
meaning, generated catalog truth, or repo-wide manifest authority.

`mechanics/recurrence/parts/live-observation-producers/` already owns the local
producer inputs that may feed technique review while keeping generated evidence
advisory.

## Options

- Keep `manifests/recurrence/` at root as a special technical district.
- Move the files to generic `generated/`.
- Move the files under the owning Recurrence live-observation producer part.

## Decision

Move the recurrence manifest package to:

```text
mechanics/recurrence/parts/live-observation-producers/manifests/recurrence/
```

Keep manifest and hook-binding language advisory. The manifest may expose
observation inputs, beacon rules, and refresh routes, but it cannot create
technique candidates, release holds, promote status, or claim recurrence law.

## Consequences

- The repository root no longer carries a generic `manifests/` district for a
  mechanic-local recurrence package.
- Recurrence manifests now live beside the part that interprets them.
- Tests assert both the new part-local paths and the absence of the old root
  paths.
- Any future root manifest district must justify a repo-wide owner route rather
  than inheriting this old placement.

## Verification

Expected checks:

```bash
python -m unittest tests.test_recurrence_manifest_topology
python -m unittest tests.test_recurrence_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
git diff --check
```
