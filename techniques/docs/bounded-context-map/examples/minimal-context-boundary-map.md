# Minimal Context Boundary Map

This example shows a small mapping exercise handled through `bounded-context-map`.

## Scenario

A repository keeps mixing up “retrieval orchestration” with “evidence storage,” causing changes and reviews to spill across both areas.

## Flow

1. Name the two neighboring contexts explicitly: retrieval orchestration and evidence storage.
2. State the core responsibility of each context in one bounded sentence.
3. Mark the handoff surface: retrieval writes bounded evidence artifacts, storage preserves and indexes them.
4. Call out the overloaded terms that previously blurred the two contexts.
5. Use the map to keep the next change scoped to one context unless the handoff itself is being changed.

## Why this stays bounded

- The map clarifies one concrete confusion instead of introducing a full architecture taxonomy.
- The interface between the contexts is named explicitly.
- Larger restructuring questions are deferred until there is a real need for them.
