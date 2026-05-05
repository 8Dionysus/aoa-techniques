# Minimal Invariant Check

This example shows a small rule expressed through `property-invariants`.

## Scenario

A normalization helper should always return lowercase ASCII slugs containing only letters, digits, and hyphens for accepted input titles.

## Flow

1. Name the invariant explicitly: accepted titles should normalize into a slug-safe shape every time.
2. Keep the input strategy bounded to meaningful title-like strings instead of arbitrary byte noise.
3. Run an invariant-oriented check that the result stays lowercase and matches the allowed slug character set.
4. Pair the invariant with a few concrete examples only if they make the rule easier to understand.
5. Report what the invariant constrains and what input cases still remain outside the current property surface.

## Why this stays bounded

- The invariant is tied to one stable output rule.
- The input space is broad enough to add signal but narrow enough to review.
- Bigger questions about slug semantics or unsupported languages are deferred to separate work.
