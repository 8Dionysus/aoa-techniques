# minimal quest-unit-promotion-review

```yaml
promotion_review:
  repeated_unit: reviewed closeout route
  promotion_verdict: promote_to_playbook
  owner_repo: aoa-playbooks
  next_surface: PLAYBOOK.md
  defer_allowed: true
```

Why this example stays bounded:

- it names one repeated unit instead of a whole session family
- it emits one promotion verdict without drafting the destination
- it keeps defer posture available instead of pretending promotion is mandatory
