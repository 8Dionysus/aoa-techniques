# Agon Recurrence Adapter

This repository exposes its Agon-facing surfaces to the recurrence control plane through owner-owned manifests.

The adapter is observation-only.

It can produce recurrence pressure such as:

```text
hint
watch
candidate
review_ready
```

It cannot produce:

```text
arena session
verdict
scar
retention schedule
rank mutation
Tree-of-Sophia promotion
automatic source rewrite
```

The owner repository keeps its meaning. Recurrence only notices when a shape returns.

## Component

```text
component:agon:technique-binding-surfaces
```

## Current manifests

```text
mechanics/agon/parts/recurrence-adapter/manifests/recurrence/component.agon.technique-binding-surfaces.json
mechanics/agon/parts/recurrence-adapter/manifests/recurrence/component.agon.epistemic-technique-candidates.json
mechanics/agon/parts/recurrence-adapter/manifests/recurrence/hooks/component.agon.technique-binding-surfaces.hooks.json
mechanics/agon/parts/recurrence-adapter/manifests/recurrence/hooks/component.agon.epistemic-technique-candidates.hooks.json
```

## Provenance

The adapter observes active Agon technique-side surfaces. It does not route
routine work to raw wave notes; use [`../../PROVENANCE.md`](../../PROVENANCE.md)
only when source lineage matters.
