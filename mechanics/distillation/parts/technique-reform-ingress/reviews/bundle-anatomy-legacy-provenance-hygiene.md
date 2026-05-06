# Bundle Anatomy Legacy And Provenance Hygiene

Source packets:

- [Bundle Anatomy Corpus Synthesis](bundle-anatomy-corpus-synthesis.md)
- [Bundle Anatomy Capsule Gap Repair Cohort](bundle-anatomy-capsule-gap-repair-cohort.md)
- [Bundle Anatomy Post-Repair Follow-Through](bundle-anatomy-post-repair-follow-through.md)
- [Final Tree Migration Ledger](final-tree-migration-ledger.md)

Status: provenance hygiene review, no legacy move, no root receipt, no active
bundle source change.

## Verdict

Close the legacy and provenance hygiene gate without adding new legacy
material.

The bundle anatomy pass did not move active technique bundles, did not migrate
paths, did not archive source packets, and did not disturb the root tree-pilot
receipt inventory. The only source repair was the capsule builder follow-up,
which changed generated-reader extraction and its validation, not historical
provenance.

## Reviewed Surfaces

Reviewed:

- `legacy/AGENTS.md`
- `legacy/README.md`
- `legacy/INDEX.md`
- `mechanics/distillation/legacy/AGENTS.md`
- `mechanics/distillation/legacy/INDEX.md`
- bundle anatomy review packets
- root technique-tree receipt inventory

Current accounting remains stable:

- root legacy has `28` tree-pilot receipts.
- root legacy receipt coverage still maps to active `techniques/<trunk>/<shelf>/`
  routes plus `docs/TECHNIQUE_TREE_CONTRACT.md`.
- Distillation mechanic-local legacy still owns pre-split Distillation lineage.
- bundle reform review packets live under the active
  `mechanics/distillation/parts/technique-reform-ingress/reviews/` route.

## Provenance Decision

No root `legacy/INDEX.md` update is needed.

Reason: there is no new preserved raw packet, archive item, receipt, or
root-wide preservation move. Adding a receipt for this phase would be a
placeholder receipt, which root legacy explicitly rejects.

No `mechanics/distillation/legacy/INDEX.md` update is needed.

Reason: the reform pass did not move pre-split Distillation material or turn a
legacy source into current behavior. It produced active review packets in the
technique reform ingress part instead.

## Active Route

Durable bundle reform evidence stays here:

- baseline inventory
- rubric hardening
- wave A, B, and C audit packets
- corpus synthesis
- capsule gap repair cohort
- template and contract feedback
- post-repair follow-through
- this hygiene review

Those are active review artifacts, not legacy receipts.

## Stop Lines

- Do not add root legacy receipts for audits that do not move paths or preserve
  historical material.
- Do not put active reform review packets under `legacy/`.
- Do not treat generated reader repairs as provenance migration.
- Do not change legacy receipts to alter current technique behavior.
