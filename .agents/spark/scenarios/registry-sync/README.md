# Spark Scenario: registry-sync

Use `registry-sync` when a file moved or appeared and its README, AGENTS,
registry, validator, release gate, or generated companion needs alignment.

## Scope

One district, registry family, generated companion, or validator lane.

## Done Signal

Source, registry, docs, validator, and generated mirror agree.

## Stop-line

Do not create a new source of truth while syncing derived routes.

## Handoff Route

Write a handoff when the registry change implies a new authority boundary,
source contract, or cross-repository owner decision.

## Validation

Run the local registry validator, generated-freshness check, and targeted tests
for that district.
