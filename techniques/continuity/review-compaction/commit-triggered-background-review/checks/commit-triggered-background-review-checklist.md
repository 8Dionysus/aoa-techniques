# commit-triggered-background-review checklist

Use this checklist when reviewing whether a post-commit review loop still behaves like a bounded artifact-producing review surface instead of drifting into remediation or CI governance.

- [ ] the triggering commit or diff is explicit
- [ ] review output remains a read-only artifact
- [ ] findings can be tied back to the reviewed commit or scope
- [ ] no auto-merge or auto-rewrite behavior is implied
- [ ] review and remediation are separate surfaces
- [ ] stale findings can be detected and rerun later
- [ ] background execution stays smaller than full CI governance
- [ ] at least one example shows the artifact fields needed for inspection
