# Evaluation-Chain Semantic Review

This review-only pilot checks whether the upstream evaluation-chain pair still reads as two distinct techniques rather than one merged "smoke plus gate" pattern.

Why this pair was chosen now:

- it is the next nearest-neighbor evaluation pair after the published-summary pilot
- both techniques are still `promoted`, so semantic clarity matters before any future status review
- both techniques already share current relation language in the catalog
- the main question is whether summary-contract production stays distinct from staged enforcement rollout

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Pair Map

| technique | current role |
|---|---|
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | summary-contract producer for runnable smoke or probe paths |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | staged rollout pattern that promotes one observed signal from non-blocking publication to one narrow strict enforcement surface |

## Seam Review

### `AOA-T-0003` vs `AOA-T-0007`

Question: where does summary-contract production stop and staged promotion semantics begin?

- Invariant boundary: [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) owns the existence and shape of one stable machine-readable summary per smoke path, including exit-code alignment and basic diagnosability. [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) begins only after that contract already exists and governs how one observed signal moves from `signal_only` publication to a narrow strict surface through readiness, governance, progress, and transition layers.
- Default-use trigger: use `0003` when a runnable smoke or probe path still needs a real summary contract that CI, dashboards, or agents can consume without log scraping. Use `0007` when an already-summary-producing check must be promoted gradually into enforcement without losing diagnostics or widening strict failure too early.
- Relation check: `AOA-T-0007 -> requires -> AOA-T-0003` helps and reads correctly as "rollout depends on a stable summary producer." `AOA-T-0003 -> used_together_for -> AOA-T-0007` also helps because the producer can exist independently, while the rollout pattern is only one downstream use of that contract. The current relation pair is bounded and does not yet look noisy.
- Evidence check: `0003` example and checklist remain contract-centric: summary emission, machine-readable status, stable discovery, and no log scraping. `0007` example and checklist remain rollout-centric: signal-only mode, readiness over history, explicit `go|hold`, progress telemetry, narrow strict enforcement, and preserved diagnostics. The support surfaces reinforce separation rather than collapse the pair into one technique. Outcome: `clear`.

## Adjacent Technique Note: `AOA-T-0006`

[AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) matters here as an adjacent dependency, but not as a third full review target in this pilot.

- `AOA-T-0007` currently `requires` `AOA-T-0006` because staged promotion becomes stronger once history and latest-alias layout are trustworthy across repeated runs.
- That adjacency does not make `AOA-T-0007` a storage-layout technique. The semantic core of `0007` is still staged enforcement policy over an existing signal, not dual-write layout or anti-double-count behavior.
- This dependency is worth watching later only if rollout wording starts absorbing too much latest/history implementation detail. At the moment, the boundary still reads cleanly. Outcome: `watch`.

## Findings

- `AOA-T-0003` is semantically distinct as the summary-contract producer. No drift signal found.
- `AOA-T-0007` is semantically distinct as the staged promotion pattern over an existing summary-producing signal.
- Current relation language for this pair is helpful and still bounded. No cleanup is justified in this pilot.
- The main watch point is adjacency to `AOA-T-0006`: future wording should keep storage-layout assumptions subordinate to rollout semantics.
- Current `examples/` and `checks/` support the claimed contracts well enough for a review-only second semantic surface.

Overall outcome: `clear with one watch dependency note`

## Next Step

No narrow remediation wave is justified for this pair from this pilot alone.

The downstream docs-boundary review wave has already landed, so the next step here is only to keep the `AOA-T-0006` dependency watch note bounded and open a new pilot only if storage-layout detail starts crowding out rollout semantics.
