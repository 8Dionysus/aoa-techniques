# Concrete Application Handler Slice

This example shows a more concrete bounded behavior change handled through `tdd-slice`.

## Scenario

An application handler returns a status summary for background imports. It currently collapses `partial_success` into `success`, which hides item-level failures from callers that only inspect the final handler result.

## Flow

1. State the bounded behavior slice explicitly: when some items succeed and some fail, the handler should return `partial_success` instead of `success`.
2. Add one failing test at the handler boundary around the observable returned status and summary payload.
3. Make the smallest implementation change needed in the nearby result-mapping logic.
4. Refactor only the local status-mapping helper touched by that slice.
5. Re-run the relevant tests and report that the handler now distinguishes partial success without widening the change into a broader import redesign.

## Why this stays bounded

- The example centers one observable behavior rule rather than a larger boundary or schema rewrite.
- The test surface stays focused on handler output, not a wider API or downstream contract package.
- Broader questions about retry policy, import orchestration, or payload redesign are explicitly deferred.
