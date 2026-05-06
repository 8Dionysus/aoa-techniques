# minimal approval-bound-durable-jobs

Durable job:

```json
{
  "job_id": "review-pack-42",
  "status": "waiting_for_approval",
  "checkpoint_ref": "jobs/review-pack-42/checkpoint.json"
}
```

Approval seam:

- the job finished collection work and now waits for explicit approval before resume

Resume behavior:

- after approval is recorded, the job resumes from `checkpoint_ref` instead of reconstructing state from memory

Why this example stays bounded:

- one durable job identity survives the pause
- continuation waits on explicit approval
- the example does not require a scheduler platform or orchestration dashboard
