# Minimal TDD Slice

This example shows a small bounded behavior change handled through `tdd-slice`.

## Scenario

A formatter should preserve leading `+` for international phone numbers instead of stripping it during normalization.

## Flow

1. State the bounded behavior change: "`+15551234567` should remain prefixed with `+` after normalization."
2. Add or update one failing test around that observable behavior.
3. Make the smallest implementation change needed to satisfy the test.
4. Refactor only the normalization helper touched by that slice.
5. Re-run the relevant tests and report the result.

## Why this stays bounded

- The change is framed as one concrete behavior rule.
- The tests constrain observable output rather than internal helper structure.
- Any larger cleanup of phone-number parsing is explicitly left for a separate change.
