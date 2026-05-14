# AGENTS.md

## Guidance for `live-observation-producers/scripts/`

This directory holds one-owner Recurrence helper scripts for live observation
producer inputs.

`publish_live_receipts.py` appends bounded technique-layer receipts to the
owner-local live JSONL log. The log remains observation evidence only; it does
not create candidates, close quests, change technique status, issue proof
verdicts, or claim runtime recurrence authority.

Keep the helper public-safe and repo-relative. Do not add hidden network calls,
ambient credentials, or private session dumps.

Verify with:

```bash
python -m unittest discover -s mechanics/recurrence/tests -p 'test_publish_live_receipts.py'
python -m unittest discover -s mechanics/recurrence/tests
python scripts/validate_repo.py
```
