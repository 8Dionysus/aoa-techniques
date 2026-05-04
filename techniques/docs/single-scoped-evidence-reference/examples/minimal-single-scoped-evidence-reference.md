# Minimal single-scoped evidence reference

```yaml
single_scoped_evidence_reference:
  claim_or_decision: public CLI docs declare a dry-run flag for write actions
  current_review_state: a reviewer needs one source before citing the interface
  evidence_reference: docs/cli.md#write-actions, the line documenting `--dry-run`
  relevance: the reference supports the claim that the public CLI interface declares the flag
  support_scope: documented interface availability
  support_limit: does not prove implementation behavior, test coverage, or runtime enforcement
  reliance_condition: inspect or quote this one reference before relying on it; route runtime behavior to a separate validation check
  stop_line: do not treat this reference as proof or as a bundle of sources
```

This example offers one reference, names what it can and cannot support, and
stops before proof or runtime validation. If the review later needs behavior
evidence, that later question belongs to a separate validation check.
