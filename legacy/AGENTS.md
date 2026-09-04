# AGENTS.md

## Applies to

This card applies to `legacy/` and every root-level raw, archive, or receipt
surface inside it.

## Role

Root legacy preserves public-safe repo-wide provenance for `aoa-techniques`.
It is for historical source packets, pre-prune snapshots, migration receipts,
and retired tail surfaces whose active route now lives elsewhere.

It is not a second `incoming/`, not active technique canon, not a generated
surface, and not mechanic-local lineage.

## Read before editing

Read:

1. `../AGENTS.md`
2. `../docs/ROOT_SURFACE_LAW.md`
3. `INDEX.md`
4. the active route or owner surface that the legacy material maps to

For technique-tree migration receipts, also read
`../docs/TECHNIQUE_TREE_CONTRACT.md` and the current reviewed migration packet.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep this district public-safe. Do not add secrets, private transcripts,
  unreduced project dumps, host details, or raw logs.
- Do not start routine technique edits in root legacy when the current route
  answers the task.
- Do not move active technique bundles through `legacy/`. Move published
  bundles directly from their old authored path to their new authored path, and
  preserve the accounting here as a receipt.
- Do not store current generated outputs here as if they were authority.
- Do not duplicate mechanic-local legacy; use `mechanics/<slug>/legacy/` when
  the lineage belongs to one mechanic.
- Do not add placeholder receipts just to make the directory look full.
- Do not add raw, archive, or receipt material without indexing it in
  `INDEX.md` and naming the active route, owner route, or explicit hold status
  it pressures.

## Validation

Inherit parent validation: source-fast/generated/advisory; see [VALIDATION.md](../VALIDATION.md) and config/validation_lanes.json.

## Closeout

Report files added or moved under root legacy, the active route they map to,
`INDEX.md` updates, public-safety review, and checks run or skipped.
