# Root Legacy Raw

`legacy/raw/` preserves public-safe repo-wide source packets and pre-prune
snapshots after their current route has been distilled or explicitly held.

Current raw inventory: none preserved.

Use this directory for exact historical material only when the active route
should not carry the full source packet.

Do not add secrets, private transcripts, unreduced project dumps, raw logs, or
material that belongs in `incoming/` quarantine or a mechanic-local
`legacy/raw/` directory.

When adding a raw packet:

1. update `../INDEX.md`
2. name the active route or owner route it pressures
3. update the relevant provenance bridge when one exists
4. run the validation lane in `../AGENTS.md`
