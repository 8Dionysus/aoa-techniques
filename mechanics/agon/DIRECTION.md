# Agon Direction

## Current operating contour

Agon inside `aoa-techniques` is a requested-practice lane. It receives pressure
from center-owned Agon moves and turns only the reusable practice question into
a technique-side candidate.

The current active surface is not the old wave notes. Start here:

- [README](README.md)
- [PARTS](PARTS.md)
- [parts/move-technique-bridge](parts/move-technique-bridge/README.md)
- [parts/epistemic-practice-boundary](parts/epistemic-practice-boundary/README.md)
- [parts/epistemic-technique-candidates](parts/epistemic-technique-candidates/README.md)
- [parts/recurrence-adapter](parts/recurrence-adapter/README.md)

## Source split

Wave IV and Wave XV landing notes are now preserved under `legacy/raw/`. They
remain useful for provenance, but they are no longer the first route for current
Agon technique-side behavior.

Use [PROVENANCE](PROVENANCE.md) when you need to audit how a preserved wave
feeds an active part. Do not copy raw wave inventories into active part docs.

## Boundary

This package can say:

- which practice candidates are requested but not landed
- which generated candidate indexes are still owner-local evidence
- which stop-lines prevent practice candidates from becoming Agon authority
- which recurrence observations may point back to technique review

It cannot say:

- what Agon lawful moves mean
- whether an arena/session move is valid
- whether a proof verdict, scar, retention, rank, trust, KAG, or ToS change
  should happen
- that a candidate is a promoted technique before bundle review lands it

When a requested candidate starts looking technique-shaped, route the narrowing
through
[Distillation Agon Candidate Handoff](../distillation/parts/agon-candidate-handoff/README.md)
before any bundle draft. The handoff lane can name first-narrowing pressure,
source-boundary holds, or owner-route holds; it still cannot accept Agon
candidates or define Agon law.

## Artifact posture

The current Agon technical artifacts live under their owning active parts:

- `parts/move-technique-bridge/config/agon_technique_binding_candidates.source.json`
- `parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json`
- `parts/epistemic-technique-candidates/config/agon_epistemic_technique_candidates.source.json`
- `parts/epistemic-technique-candidates/generated/agon_epistemic_technique_candidates.min.json`
- matching part-local schemas, examples, scripts, tests, and recurrence manifests

Root technical districts keep repo-wide surfaces. Agon-owned generated outputs
stay with the part that owns the candidate meaning.
