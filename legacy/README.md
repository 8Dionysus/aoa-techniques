# Root Legacy

Root legacy is the repo-wide provenance district for `aoa-techniques`.

It preserves public-safe source packets, pre-prune snapshots, migration
receipts, and retired tail surfaces that are too historical or too heavy for
the active route.

Legacy is not a trash archive. It is also not a second `incoming/`.

## Current route first

Use the active route when it answers the task:

- current technique meaning: `techniques/**/TECHNIQUE.md`
- technique path architecture: `docs/TECHNIQUE_TREE_CONTRACT.md`
- current candidate quarantine and staging: `incoming/`
- mechanic-local lineage: `mechanics/<slug>/legacy/`
- generated companions: `generated/` and `reports/`
- repo-wide root placement law: `docs/ROOT_SURFACE_LAW.md`

Open root legacy only when you need preserved repo-wide history, a
pre-migration receipt, or an archived tail surface that no longer belongs in
the active route.

## Layout

- `raw/`: preserved public-safe source packets or pre-prune snapshots.
- `archive/`: retired historical surfaces whose current route now lives
  elsewhere.
- `receipts/`: short dated accounting for path migrations, compactions, and
  root-wide preservation moves.
- `INDEX.md`: inventory and route map for every preserved item.
- `AGENTS.md`: local agent guidance and validation lane.

## Entry rule

Material belongs here only when all of this is true:

- it is public-safe
- it is repo-wide, or it does not have a cleaner mechanic-local legacy home
- it is historical, evidential, or accounting material rather than active canon
- it names an active route, owner route, or explicit hold status
- it is indexed in `INDEX.md`

## Stop-lines

- Do not use root legacy as the first route for routine technique edits.
- Do not move active technique bundles into root legacy during tree migration.
- Do not put secrets, private transcripts, raw logs, or unreduced project dumps
  here.
- Do not let archived generated output outrank the generator or authored source.
- Do not add placeholder receipts just to make the directory look full.

## Validation

Use the validation lane in [legacy/AGENTS.md](AGENTS.md#validation).
