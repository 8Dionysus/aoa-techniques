# minimal fail-closed-evidence-gate

Candidate action:

- `delete temp cache directory`

Verdict:

```json
{
  "status": "blocked",
  "reason": "path policy not satisfied",
  "evidence_ref": "artifacts/gate/delete-cache-verdict.json"
}
```

Execution behavior:

- no deletion runs because the verdict is not `allow`

Why this example stays bounded:

- the gate sits before the side effect
- blocked execution still leaves reviewable evidence
- the example does not depend on a full policy platform or durable job system
