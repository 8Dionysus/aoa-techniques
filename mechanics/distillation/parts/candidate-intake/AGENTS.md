# AGENTS.md

## Applies to

This card applies to `mechanics/distillation/parts/candidate-intake/` and all
descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`candidate-intake/` is the active Distillation quarantine part for public-safe
incoming candidate packets before they become a ledger entry, import runbook
path, gate packet, technique bundle, hold, exclusion, or legacy archive.

Nothing here is canonical merely because it exists. A candidate must be
reviewed, normalized, linked to source evidence, and promoted through the
documented technique shape before it can speak as canon.

Closed packet roots do not stay here after closeout. Move them to
`mechanics/distillation/legacy/archive/closed-incoming-packets/` once their
first-pass queues are exhausted and all non-landed tails have final verdicts.

## Read before editing

Read root `AGENTS.md`, `docs/START_HERE.md`, `docs/TECHNIQUE_ATOM_CONTRACT.md`,
`docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, `mechanics/distillation/AGENTS.md`,
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Preserve provenance, uncertainty, and review status.
- Do not erase rough edges by turning partial notes into polished doctrine too
  early.
- Do not put secrets, private transcripts, or unreduced project dumps here.
- If material is not public-safe, keep it out of this repository.
- Promotion should end in a source-authored technique bundle, not a generated
  or staging-only artifact.
- New packet roots should name a bounded donor family, source evidence,
  candidate status, likely atom/topology route, owner boundary, and stop line.
- Do not keep or recreate packet-local `candidate_bundles/` for techniques
  that already have landed canonical bundles.
- Do not leave closed packet roots in this active intake; preserve them under
  `mechanics/distillation/legacy/archive/closed-incoming-packets/`.
- Treat closed non-import verdicts as final for the old packet. Any future
  attempt needs a new Distillation intake with fresh evidence; do not treat a
  closeout memo as bundle approval.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report candidate paths changed, provenance retained, public-safe review,
closed verdict status, validation run, and validation skipped.
