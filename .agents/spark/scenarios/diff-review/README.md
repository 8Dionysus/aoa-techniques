# Spark Scenario: diff-review

Use `diff-review` to review a concrete diff or pull request for technique-canon
bugs, drift, missed validators, generated parity gaps, and scope creep.

## Scope

Review only the provided diff or pull request context.

## Done Signal

Findings are ordered by severity and tied to exact files or lines where
available.

## Stop-line

Do not rewrite the diff while acting as reviewer.

## Handoff Route

Write a handoff when the review exposes a broader design problem, ambiguous
source authority, or owner judgment outside the diff.

## Validation

Run read-only checks when useful, such as the diff hygiene check or the changed
surface validator.
