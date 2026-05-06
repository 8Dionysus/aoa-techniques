# minimal example seed

Input findings:
- `unused import in app.ts`
- `app.ts has dead import`
- `stale line reference in old diff`

Compacted output:
- one current finding for the dead import
- one stale marker for the old diff reference

The point of the example is that compaction preserves the real issue while dropping invalidated duplicates.
