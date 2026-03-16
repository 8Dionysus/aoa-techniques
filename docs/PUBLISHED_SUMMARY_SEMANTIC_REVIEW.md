# Published-Summary Semantic Review

This review-only pilot checks whether the published-summary cluster still reads as four distinct techniques rather than one blurred evaluation package.

Why this cluster was chosen first:

- all four techniques are already `canonical`
- all four are tightly connected by current `relations`
- the cluster already has strong examples, checks, and second-context notes
- the main remaining question is semantic clarity, not missing structure

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Cluster Map

| technique | current role |
|---|---|
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | storage contract for stable latest alias plus immutable history copy |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | bounded remediation rollup over latest published summaries |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | diagnostic trust layer over published summaries and downstream rollups |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | rendering and contract policy for required versus optional summary sources |

## Seam Review

### `AOA-T-0006` vs `AOA-T-0008` / `AOA-T-0010`

Question: where does the storage contract end and the downstream consumer layer begin?

- Invariant boundary: [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) owns alias/history layout, dual-write invariants, and anti-double-count reader behavior. [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) and [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) begin only after stable latest published summaries already exist.
- Default-use trigger: use `0006` when a producer must publish discoverable current state and trustworthy history. Use `0008` when several published summaries need one bounded remediation backlog. Use `0010` when several published summaries or rollups need one reusable trust verdict.
- Relation check: current `shares_contract_with` from `0006` to `0008` and `0010` helps. It correctly reads as shared dependency on the latest-summary contract rather than semantic duplication.
- Evidence check: `0006` examples and checklist stay focused on alias/history layout, not downstream rollups. The object-store example reinforces storage invariants without bleeding into remediation or integrity semantics. Outcome: `clear`.

### `AOA-T-0008` vs `AOA-T-0010`

Question: are remediation rollup and integrity verdict still distinct, or are they drifting toward one combined downstream helper?

- Invariant boundary: [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) answers "what needs follow-up?" through bounded buckets and source references. [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) answers "are these published summaries trustworthy enough to interpret?" through diagnostic invariants and reason codes.
- Default-use trigger: choose `0008` when operators or agents need one reviewable backlog instead of reading each latest summary directly. Choose `0010` when multiple consumers should not duplicate source-health, dual-write, and anti-double-count checks independently.
- Relation check: mutual `complements` is appropriate and still minimal. Anything stronger than `complements` would risk implying one technique subsumes the other.
- Evidence check: `0008` checklist and object-store example stay bucket-and-source-reference centric; `0010` checklist and object-store example stay trust-and-integrity centric. The support surfaces currently reinforce separation rather than blur it. Outcome: `clear`.

### `AOA-T-0008` / `AOA-T-0010` vs `AOA-T-0011`

Question: where do downstream summary surfaces stop and rendering policy begin?

- Invariant boundary: [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) and [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) define optional downstream summary artifacts. [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) defines how a consumer treats those artifacts once they exist or are missing.
- Default-use trigger: use `0008` or `0010` when the project needs the remediation or integrity artifact at all. Use `0011` when a UI, CLI report, or smoke summary must stay useful while optional supporting artifacts remain observable but non-fatal.
- Relation check: `0008 -> complements -> 0011` and `0010 -> complements -> 0011` are helpful because they point from optional published artifacts to the rendering policy that consumes them. The current relation set is enough; adding `requires` here would overstate dependency.
- Evidence check: `0008` and `0010` examples focus on emitting optional downstream artifacts; `0011` example and checklist focus on required/optional handling in a consumer, including non-UI output. That keeps producer semantics separate from rendering semantics. Outcome: `watch`.

Why `watch` instead of `clear`:

- `AOA-T-0011` uses remediation and integrity as its clearest optional-source examples, so future wording drift could accidentally make `0011` read like a bundle-specific rendering appendix instead of a general summary-consumer policy.
- The current support surfaces are still strong enough, but this seam is the most likely place for future overlap if later examples become too package-shaped.

## Findings

- `AOA-T-0006` is semantically distinct as the storage contract. No drift signal found.
- `AOA-T-0008` and `AOA-T-0010` are distinct downstream consumers: one prioritizes follow-up backlog, the other trustworthiness of interpretation.
- `AOA-T-0011` remains distinct as rendering policy, but its strongest examples are currently anchored in the same package. This is acceptable now and worth watching later.
- Current `relations` for this cluster are helpful and still bounded. No relation cleanup is justified in this pilot.
- Current `examples/` and `checks/` support the claimed contracts well enough for a review-only first semantic surface.

Overall outcome: `clear with one watch seam`

## Next Step

No immediate published-summary remediation wave is justified from this pilot alone.

The next semantic-review wave should move upstream to `AOA-T-0003` and `AOA-T-0007`, where the likely boundary question is producer contract versus staged gate-promotion semantics.
