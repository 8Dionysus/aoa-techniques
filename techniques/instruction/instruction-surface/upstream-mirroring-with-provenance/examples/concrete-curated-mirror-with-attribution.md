# Concrete Curated Mirror With Attribution

Scenario: a public collection wants to mirror one externally maintained skill into a local curated directory.

1. Add one source-manifest entry naming the upstream repository, upstream path, and local destination.
2. Sync the upstream skill into the local collection.
3. Write one adjacent provenance file that preserves origin attribution.
4. Keep any local curation note in a separate file instead of editing the mirrored payload inline.
5. On refresh, re-run the sync path first and only then review whether local wrapper notes still make sense.

This stays inside the technique because the local collection mirrors upstream-owned content with explicit provenance rather than turning the mirror into a new canonical source.
