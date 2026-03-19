# Intent-Chain Semantic Review

This review-only pilot checks whether the promoted intent-chain pair still reads as two distinct techniques rather than one blurred "intent automation chain" package.

Why this pair was chosen now:

- both techniques are still `promoted`, so semantic clarity matters before any future status review
- both techniques are directly related and already sit in the same operating path
- the main remaining question is semantic separation, not missing repo structure
- this is the highest-value review pass before any second-context evidence strengthening for the pair

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Pair Map

| technique | current role |
|---|---|
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | artifact-first intent normalization and dry-run contract chain |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | bounded rollout checklist for one new intent type on an existing chain |

## Seam Review

### `AOA-T-0004` vs `AOA-T-0005`

Question: where does the underlying artifact-first intent chain stop and the bounded rollout checklist for one new intent on top of that chain begin?

- Invariant boundary: [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) owns intent normalization, plan artifact creation, dry-run execution, chain artifacts, and contract-check before any real execution path exists. [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) begins only when an existing chain already exists and one new intent type must be added without fixture, routing, artifact, or regression drift.
- Default-use trigger: use `0004` when the system still needs the reusable chain contract itself. Use `0005` when the chain already exists and the main problem is safe extension of one new intent path.
- Relation check: current `0005 -> requires -> 0004` and `0004 -> used_together_for -> 0005` remain helpful and bounded. The pair reads as underlying contract plus bounded extension path rather than as duplicate workflow descriptions.
- Evidence check: `0004` support surfaces stay chain-contract centric, focusing on normalized artifacts, dry-run safety, and contract validation. `0005` support surfaces stay rollout-checklist centric, focusing on one canonical fixture, one routed smoke path, aligned artifacts, and at least one regression surface for the new intent. Outcome: `clear`.

## Findings

- `AOA-T-0004` is semantically distinct as the underlying artifact-first intent-chain contract.
- `AOA-T-0005` is semantically distinct as the safe extension checklist for adding one new intent type to an existing chain.
- Current relation language is helpful and does not justify cleanup.
- Current examples and checks are sufficient for a review-only semantic pass, even though broader support strengthening may still come later.
- No status change, relation cleanup, or narrow remediation wave is justified from this pilot alone.

Overall outcome: `clear`

## Next Step

No immediate semantic-remediation wave is justified for this pair from this pilot alone.

The next step should move to second-context evidence strengthening for `AOA-T-0004` and `AOA-T-0005`, rather than directly to canonical review or broader restructuring.
