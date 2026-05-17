# AGENTS.md

## Applies to

This card applies to `docs/review/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`docs/review/` owns active review, maturity, semantic-review, and caution
contracts for the technique canon.

It explains how review fields, promotion decisions, semantic review packets,
and shadow/caution language should be read. It does not own technique bundle
meaning, generated manifest truth, mechanic-local review packets, or proof
doctrine from neighboring AoA repositories.

## Read before editing

Read root `AGENTS.md`, `DESIGN.md`, `docs/AGENTS.md`,
`docs/ROOT_SURFACE_LAW.md`, and this district [README](README.md).

For promotion or maturity wording, also read:

- [Canonical Rubric](CANONICAL_RUBRIC.md)
- [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
- [Promotion Readiness Matrix](../../mechanics/audit/parts/promotion-readiness-matrix/README.md)
- [Promotion Evidence Runbook](../../mechanics/audit/parts/promotion-evidence-runbook/README.md)

For semantic or shadow review wording, also read:

- [Semantic Review Guide](SEMANTIC_REVIEW_GUIDE.md)
- [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
- [Review Readers](../readers/review/README.md)
- [Distillation Reviews](../../mechanics/distillation/parts/technique-reform-ingress/reviews/README.md)

## Boundaries

- Keep review guides as contracts for interpreting review evidence, not as
  substitute `TECHNIQUE.md` meaning.
- Do not let generated manifests promote, demote, rank, or score techniques.
- Keep mechanic-owned review packets under their mechanic owner.
- Keep proof or verdict doctrine in `aoa-evals`; this district may only route
  to it when a future technique-review handoff needs that owner.
- Keep caution language markdown-first unless a later decision promotes a
  bounded schema or validator contract.

## Validation

For review-guide changes, run the narrow affected test first when possible:

```bash
python scripts/build_catalog.py
python scripts/build_semantic_review_manifest.py
python scripts/build_shadow_review_manifest.py
python -m unittest tests.test_validate_repo
python -m unittest tests.test_docs_surface_guardrails
python scripts/validate_repo.py
```

If generated review, selection, catalog, or evidence-note outputs move, rebuild
the matching surfaces before validation.

## Closeout

Report which review contract moved, whether generated review or selection
companions were rebuilt, which validators ran, and which review/mechanic owner
still carries any remaining packet-level evidence.
