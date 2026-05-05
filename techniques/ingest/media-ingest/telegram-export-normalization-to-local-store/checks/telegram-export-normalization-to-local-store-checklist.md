# telegram-export-normalization-to-local-store checklist

- [ ] normalized message objects preserve ids, timestamps, sender data, reply edges, and media references
- [ ] source provenance stays explicit for export chunks, API batches, or source files
- [ ] resume behavior is bounded and reviewable
- [ ] auth, session conversion, and secret storage stay out of scope
- [ ] the local store is not treated as memory or canon by default
- [ ] downstream routing or curation policy remains outside the normalization contract
