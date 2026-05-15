# Spark Scenario: release-prep

Use `release-prep` for a fast release-readiness pass before publication,
release support, or GitHub landing hardens a claim.

## Scope

One release candidate, one repository, one pull request, or one bounded release
surface.

## Done Signal

Changed surfaces, checks, public-claim risks, generated parity, and owner
routes are named.

## Stop-line

Do not publish, tag, push, or merge without an explicit user command.

## Handoff Route

Write a handoff when release wording needs public-claim judgment, owner
acceptance, multi-repo synthesis, or a slower review.

## Validation

Run `python scripts/release_check.py` when local dependencies are available.
