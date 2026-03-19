# Concrete Infra Context Map

This example shows a more concrete infra-repository scoping exercise handled through `bounded-context-map`.

## Scenario

An infrastructure repository keeps mixing up "cluster bootstrap" with "service rollout configuration," causing reviews and implementation plans to spill across both areas.

## Flow

1. Name the two neighboring contexts explicitly: cluster bootstrap and service rollout configuration.
2. State the main responsibility of each context in one bounded sentence so the overlap becomes visible.
3. Mark the handoff surface: bootstrap exposes shared platform primitives, while rollout configuration consumes those primitives by reference.
4. Call out overloaded terms such as "environment config" that previously blurred the two areas.
5. Use the map to keep the next change scoped to rollout configuration unless the handoff itself is what needs revision.

## Why this stays bounded

- The example reduces one concrete ambiguity instead of introducing a full architecture taxonomy.
- The handoff between the contexts is named explicitly enough for review and future scoping.
- Broader platform modeling or domain-architecture work is deferred until there is a separate reason to do it.
