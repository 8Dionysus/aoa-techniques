# Minimal audit-to-closeout-proof-loop example

Input findings:

- `repo A accepts an optional path as required and aborts the closeout path`
- `repo B appends JSONL receipts without restoring a missing trailing newline`

Proof-backed closeout:

1. Re-confirm both findings in live code rather than trusting the audit wording alone.
2. Patch the smallest owner-surface causes in each repository.
3. Add one targeted regression seam for the optional-path behavior and one for the JSONL boundary behavior.
4. Rerun the targeted checks immediately after each fix.
5. Rerun the broader repo validation or full test suite before the findings are marked closed.
6. Record any remaining warnings or follow-on seams instead of pretending the route is perfectly clean.

Why this works:

- the findings are closed on named proof, not only on patch presence
- the targeted checks prove the failure mode directly
- the broader closeout rerun checks that the repositories still hold together after the local fixes
