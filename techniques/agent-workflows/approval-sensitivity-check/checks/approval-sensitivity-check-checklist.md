# approval-sensitivity-check checklist

- [ ] one automation candidate is named explicitly
- [ ] mutation, authority, rollback, and health-check posture are visible
- [ ] `checkpoint_required` is explicit when the candidate is approval-heavy or self-changing
- [ ] low-risk read-only candidates remain distinguishable from mutating ones
- [ ] the result stays smaller than a full repair or governance framework
- [ ] the example does not imply permission to execute
- [ ] the public wording stays reusable and sanitized
