# Rollout Failure Triage

This note generalizes the rollout-debugging path behind `AOA-T-0005` so a new intent can be repaired without widening scope or bypassing the shared chain.

## Triage order

Check failures in this order:

1. canonical fixture
2. smoke path
3. contract-check
4. artifact publishing
5. regression coverage

That order keeps the diagnosis close to the source of truth and avoids debugging summary surfaces before the underlying rollout path is valid.

## 1. Fixture problems

Look here first when:

- the new intent never appears in the smoke run
- the contract summary shows the wrong `intent_type`
- required `trace_id` or `intent_id` fields are missing from the observed data

Typical fix:

- repair the canonical fixture before touching CI or summary wiring

## 2. Smoke path problems

Look here when:

- the fixture exists but the run directory or expected artifacts are missing
- the rollout path uses a one-off helper instead of the shared intent-chain flow
- the smoke step fails before any contract summary is produced

Typical fix:

- reproduce the dry-run smoke locally against the canonical fixture and confirm it writes the same artifact family expected by existing intent paths

## 3. Contract-check problems

Look here when:

- `expected_intent_type` does not match the new route
- summary `violations` show missing artifact, routing mismatch, or missing traceability fields
- the smoke run succeeds but the contract verdict is failing

Typical fix:

- adjust the strict routing or traceability assertions so they match the intended contract of the new rollout, not the previous intent path

## 4. Artifact publishing problems

Look here when:

- `contract_summary.json` exists locally but is absent from the main review surface
- the new intent path runs, but there is no summary row or stable artifact path for reviewers
- humans can only discover the result by opening raw logs

Typical fix:

- wire the new summary and artifact path into the same surface already used for existing intents

## 5. Regression coverage problems

Look here when:

- the rollout appears green in smoke and contract checks, but there is no targeted regression proof
- future refactors can silently remove the new intent path without an obvious failure signal

Typical fix:

- add at least one automated test that exercises the new intent through normalization, dry-run, and contract-check

## Source backing

This triage shape is generalized from the ATM10 material around `M6.8` troubleshooting guidance, `M6.19` rollout policy, the 2026-02-24 traceability hardening, and the 2026-03-03 `open_world_map` rollout.
