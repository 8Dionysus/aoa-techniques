# AGENTS.md

## Applies to

This card applies to `incoming/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`incoming/` is a quarantine and staging area for candidate technique material.

Nothing here is canonical merely because it exists. A candidate must be
reviewed, normalized, linked to source evidence, and promoted through the
documented technique shape before it can speak as canon.

Closed packet roots may remain here only as evidence. In that state, packet
docs and support registries preserve provenance and final non-import verdicts,
but old seed bundles must not duplicate landed `techniques/**/TECHNIQUE.md`
meaning.

## Read before editing

Read root `AGENTS.md`, `docs/START_HERE.md`, `docs/TECHNIQUE_ATOM_CONTRACT.md`,
`docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, and the relevant Distillation or Audit
mechanic route before moving candidate material.

## Boundaries

- Preserve provenance, uncertainty, and review status.
- Do not erase rough edges by turning partial notes into polished doctrine too
  early.
- Do not put secrets, private transcripts, or unreduced project dumps here.
- If material is not public-safe, keep it out of this repository.
- Promotion should end in a source-authored technique bundle, not a generated
  or staging-only artifact.
- Do not keep or recreate packet-local `candidate_bundles/` for techniques that
  already have landed canonical bundles.
- Treat closed non-import verdicts as final for the packet. Any future attempt
  needs a new Distillation intake with fresh evidence; do not treat a closeout
  memo as bundle approval.

## Validation

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```

## Closeout

Report candidate paths changed, provenance retained, public-safe review,
closed verdict status, validation run, and validation skipped.
