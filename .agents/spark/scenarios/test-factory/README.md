# Spark Scenario: test-factory

Use `test-factory` to add a bounded set of tests for a contract that already
has a source surface.

## Scope

One source contract, one test family, and one validation path.

## Done Signal

Tests prove a named existing contract and pass locally.

## Stop-line

Do not invent new semantics to make tests interesting.

## Handoff Route

Write a handoff when the invariant is unclear or needs deeper source-of-truth
work before tests can be honest.

## Validation

Run the targeted test command for the changed test family and the validator
named by the owning source surface. Use the repository test runner only when
the user, owner route, or release-prep explicitly asks for broader proof.
