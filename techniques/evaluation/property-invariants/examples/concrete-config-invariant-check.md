# Concrete Config Invariant Check

This example shows a more concrete config-validation case handled through `property-invariants`.

## Scenario

A configuration merger combines a base worker config with bounded environment overrides. Across realistic profile combinations, every enabled worker should still resolve to exactly one queue name in the final rendered config.

## Flow

1. Name the invariant explicitly: no enabled worker should end up with zero queue names or multiple queue names after config merge.
2. Keep the input strategy bounded to realistic base-and-override combinations rather than arbitrary random structures.
3. Run a repeated invariant-oriented check across those bounded configuration cases.
4. Pair the invariant with a few concrete examples only if they make the rule easier to read, not as a substitute for the invariant.
5. Report what the invariant now constrains and what remains outside scope, such as queue priority policy or autoscaling behavior.

## Why this stays bounded

- The example centers one meaningful invariant about rendered config shape rather than a broad contract suite.
- The input space is wide enough to add coverage but still narrow enough to review.
- Larger questions about deployment policy or API compatibility are explicitly deferred.
