# Agon Roadmap

## Current contour

The first Agon mechanics passes establish the AoA-style split:

- active route in `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/`
- preserved wave receipts in `legacy/raw/`
- lineage bridge in `PROVENANCE.md`
- landing accounting in `LANDING_LOG.md`
- part-local technical artifacts for Wave IV binding candidates, Wave XV
  epistemic candidates, and recurrence observation manifests

## Artifact topology

The Agon artifact-topology pass moved mechanic-owned technical artifacts out of
root districts and into nearest owning parts:

- `parts/move-technique-bridge/config/agon_technique_binding_candidates.seed.json`
- `parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json`
- `parts/epistemic-technique-candidates/config/agon_epistemic_technique_candidates.seed.json`
- `parts/epistemic-technique-candidates/generated/agon_epistemic_technique_candidates.min.json`
- matching part-local schemas, examples, builders, validators, and tests
- `parts/recurrence-adapter/manifests/recurrence/`

See `docs/decisions/2026-05-01-agon-part-local-artifacts.md` for the structural
decision.

## Next Agon pass

Only open a promotion pass after one requested candidate has passed through the
[Distillation Agon Candidate Handoff](../distillation/parts/agon-candidate-handoff/README.md)
lane and can name the atomic move, topology, portability, owner stop-lines, and
nearest overlaps. Keep that pass to one candidate family at a time.

## Not now

Do not promote all Agon candidates at once. Promotion still belongs to
bundle-local technique review under `techniques/`.
