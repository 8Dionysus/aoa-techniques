# Concrete Non-UI Intent Rollout

This example shows a public-safe rollout for one new non-UI intent type, `refresh_skill_index`, on top of an existing intent-to-plan-to-dry-run chain.

## 1. Add the canonical fixture

Create one stable fixture such as:

```json
{
  "schema_version": "skill_ops_intent_v1",
  "intent_type": "refresh_skill_index",
  "intent_id": "intent-refresh-skill-index-001",
  "trace_id": "trace-refresh-skill-index-001",
  "goal": "rebuild the generated skill index from skill metadata and preview the resulting changes"
}
```

Store it in one canonical path such as:

- `tests/fixtures/intent_refresh_skill_index.json`

## 2. Add one dedicated smoke command

```bash
python scripts/intent_chain_smoke.py \
  --intent-json tests/fixtures/intent_refresh_skill_index.json \
  --runs-dir runs/ci-smoke-intent-chain-refresh-skill-index
```

The smoke path must reuse the shared intent-chain flow instead of introducing a one-off maintenance shortcut.

## 3. Add one strict contract-check

```bash
python scripts/check_intent_chain_contract.py \
  --runs-dir runs/ci-smoke-intent-chain-refresh-skill-index \
  --expected-intent-type refresh_skill_index \
  --require-trace-id \
  --require-intent-id \
  --summary-json runs/ci-smoke-intent-chain-refresh-skill-index/contract_summary.json
```

## 4. Publish the review surface

Expose the new intent through the same operator or CI review surface already used for existing chain paths:

- publish one summary row for `refresh_skill_index`
- upload `contract_summary.json` with the smoke artifacts
- keep the artifact path stable enough that humans and agents can find it without log scraping

## 5. Add one regression proof

Add at least one automated test that proves `refresh_skill_index` uses the same normalization, dry-run, and contract-check flow as the existing intent set.

The regression should fail if:

- the new fixture bypasses the shared chain
- the expected intent type drifts
- the smoke and contract-check steps stop agreeing on artifact paths

## 6. Expected contract summary

```json
{
  "status": "ok",
  "observed": {
    "intent_type": "refresh_skill_index",
    "trace_id": "trace-refresh-skill-index-001",
    "intent_id": "intent-refresh-skill-index-001"
  },
  "violations": []
}
```

## What this proves

- one new non-UI intent can be added without changing the underlying chain contract itself
- the rollout remains dry-run only
- the review surface stays consistent with the existing intent family
- the new intent is protected by fixture, smoke, contract-check, artifact, and regression discipline rather than by one-off workflow edits
