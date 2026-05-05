# minimal-intent-rollout

This example shows a generic checklist-shaped rollout for a new dry-run intent path.

## 1. Add the canonical fixture

Create one public fixture placeholder such as:

```json
{
  "schema_version": "intent_v1",
  "intent_type": "<new_intent_type>",
  "intent_id": "intent-demo-001",
  "trace_id": "trace-demo-001",
  "goal": "Describe the operator-facing goal here"
}
```

Store it in a stable location such as `tests/fixtures/intent_<new_intent_type>.json`.

## 2. Add one dedicated chain smoke command

```bash
python scripts/intent_chain_smoke.py \
  --intent-json tests/fixtures/intent_<new_intent_type>.json \
  --runs-dir runs/ci-smoke-intent-chain-<new_intent_type>
```

## 3. Add one strict contract-check command

```bash
python scripts/check_intent_chain_contract.py \
  --runs-dir runs/ci-smoke-intent-chain-<new_intent_type> \
  --expected-intent-type <new_intent_type> \
  --require-trace-id \
  --require-intent-id \
  --summary-json runs/ci-smoke-intent-chain-<new_intent_type>/contract_summary.json
```

## 4. Publish the artifacts and review row

Make the smoke run and contract summary part of the same review surface:

- include one summary row for `<new_intent_type>` in CI output
- upload `contract_summary.json` with the rest of the smoke artifacts
- keep the artifact path stable so humans and agents can find it without log scraping

## 5. Add one regression expectation

Add at least one automated test that proves the new intent flows through normalization, dry-run, and contract-check without real side effects.

## 6. Expected contract summary shape

The published contract summary should make rollout drift obvious:

```json
{
  "status": "ok",
  "observed": {
    "intent_type": "<new_intent_type>",
    "trace_id": "trace-demo-001",
    "intent_id": "intent-demo-001"
  },
  "violations": []
}
```

## 7. Common rollout failures to catch

- The fixture exists but is not wired into the shared smoke path.
- The smoke path works, but the contract-check is still asserting the old `intent_type`.
- `contract_summary.json` is produced locally but not published in the main review surface.
- The rollout looks green in CI, but no targeted regression test proves the new intent uses the existing chain.
