# Minimal Contract Boundary

This example shows a small boundary change handled through `contract-test-design`.

## Scenario

A worker emits a JSON summary consumed by another service, and the team needs to refactor internals without breaking the consumer-facing shape.

## Flow

1. Name the boundary explicitly: the emitted summary file and the consumer that reads it.
2. Describe the expected contract in bounded terms: required keys, value shapes, and error behavior.
3. Add a contract-oriented test or smoke check around that emitted summary.
4. Refactor the internal worker logic without widening the contract.
5. Run the contract check and report both what is guaranteed and what remains outside the contract.

## Why this stays bounded

- The contract is framed around the consumer-visible artifact.
- Internal refactor freedom is preserved as long as the boundary behavior remains stable.
- Any broader redesign of the summary format is deferred to a separate change.
