# Minimal single-missing-evidence request

```yaml
single_missing_evidence_request:
  claim_or_decision: generated compact index was rebuilt after the seed registry changed
  current_review_state: diff shows seed and generated files changed, but no builder receipt is visible
  requested_object: one command receipt or CI line for `python path/to/build_registry.py --check` on the current branch
  why_it_matters: the receipt distinguishes generated parity from hand-edited generated output
  if_object_appears: mark generation parity observed and continue normal review
  if_object_absent: keep generated index under review and do not treat it as validated
  stop_line: do not issue proof or verdict; ask for this one object and stop
```

This example asks for one object, not a full investigation. If the receipt is
provided, review can continue with observed generation parity. If it is absent,
the generated output remains under review, but the absence does not prove the
output is wrong.
