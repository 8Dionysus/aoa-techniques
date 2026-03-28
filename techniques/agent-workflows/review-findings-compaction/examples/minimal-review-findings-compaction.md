# Minimal review-findings-compaction example

Input findings:

- `unused import in app.ts`
- `app.ts has dead import`
- `stale line reference in old diff`

Compacted output:

- one current finding for the dead import
- one stale marker for the old diff reference

Why this works:

- the first two findings point to the same underlying issue and can be represented once
- the third finding no longer matches live code and should not survive as current truth

The point of the example is that compaction preserves the real issue while dropping invalidated duplicates.
