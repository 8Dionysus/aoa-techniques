# Root Legacy Receipts

`legacy/receipts/` holds short dated accounting notes for repo-wide preservation
moves, path migrations, and compactions.

Current receipt inventory: one review-compaction tree pilot receipt.

For technique tree migration, receipts may record old paths, new paths, reviewed
packet references, regenerated surfaces, and validation commands. They do not
make a proposed tree path current by themselves.

Do not move active technique bundles through this directory. Preserve the
accounting here, then move active bundles directly between authored homes.

When adding a receipt:

1. keep it public-safe and compact
2. link the reviewed source packet or active route
3. update `../INDEX.md`
4. run the validation lane in `../AGENTS.md`
