# Minimal single-locus claim challenge

```yaml
single_locus_claim_challenge:
  target_claim: generated docs readers are complete because release check passed
  vulnerable_locus: generated docs readers are complete
  pressure_reason: release check proves validation passed, but it does not by itself show which reader exposes the new entry
  next_support_question: name one generated reader or manifest entry that exposes the new technique, or narrow the claim to release validation passed
  stop_condition: this challenge is not a proof verdict; do not treat the claim as false unless a separate validation check proves it
```

This example challenges one claim at one locus and asks one next support
question. It does not decide correctness, assign a route, or open a broad
debate.
