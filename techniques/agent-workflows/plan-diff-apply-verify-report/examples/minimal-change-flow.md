# Minimal Change Flow

This example shows the technique as a reusable outline for a small, reviewable change.

## Scenario

Update a public README section to clarify repository intent without changing repository structure or policy.

## PLAN

- Goal: make the README clearer for first-time readers
- Touched surface: `README.md`
- Main risk: accidentally changing meaning instead of clarifying wording
- Rollback idea: revert the single documentation patch if the wording introduces ambiguity

## DIFF

- Prepare one focused patch that changes only the target section
- Avoid unrelated formatting cleanup or additional document edits

## APPLY

- Apply the scoped README patch
- Keep the change aligned with the stated goal

## VERIFY

- Re-read the updated section for clarity and consistency
- Confirm that no other repository documents now contradict the new wording

## REPORT

- Changed: clarified the README intent statement
- Verified: wording matches repository purpose and does not conflict with contribution rules
- Rollback: restore the previous README wording if reviewers find the new text less precise
