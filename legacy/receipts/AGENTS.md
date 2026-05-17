# AGENTS.md

## Applies to

This card applies to `legacy/receipts/`.

## Role

`legacy/receipts/` holds short dated accounting notes for repo-wide preservation
moves, path migrations, and compactions.

Receipts preserve why a move happened and which surfaces were checked. They do
not make a proposed path current by themselves.

## Read before editing

Read:

1. `../AGENTS.md`
2. `../README.md`
3. `../INDEX.md`
4. `README.md`
5. the reviewed source packet, active route, or migration contract being
   accounted for

For technique-tree migration receipts, also read
`../../docs/TECHNIQUE_TREE_CONTRACT.md`.

## Boundaries

- Do not move active technique bundles through this directory. Preserve the
  accounting here, then move active bundles directly between authored homes.
- Do not add placeholder receipts just to make an inventory look complete.
- Do not add secrets, private transcripts, raw logs, or unreduced project
  dumps.
- Do not let a receipt replace the source packet, decision record, active
  route, or validation evidence it references.
- Do not add or remove a receipt without updating `../INDEX.md`.

## Validation

Run:

```bash
python -m unittest tests.test_root_legacy_topology
python scripts/validate_repo.py
```

## Closeout

Report receipts changed, the reviewed source or active route linked, the
`../INDEX.md` update, public-safe review, and checks run or skipped.
