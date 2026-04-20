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
