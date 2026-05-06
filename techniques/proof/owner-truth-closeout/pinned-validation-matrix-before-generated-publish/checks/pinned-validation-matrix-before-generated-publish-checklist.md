# pinned-validation-matrix-before-generated-publish checklist

- [ ] the generated outputs about to publish are named explicitly
- [ ] the workflow-pinned sibling refs or mirrored inputs are named explicitly
- [ ] the local rebuild or `--check` pass uses that same pinned matrix
- [ ] publish does not rely only on workspace `main` state
- [ ] repo-native validators also stay green after the pinned-matrix pass
- [ ] the technique stays smaller than release automation or split-wave playbook doctrine
- [ ] the public wording stays reusable and sanitized
