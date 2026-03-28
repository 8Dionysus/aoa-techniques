# minimal session-opening ritual before work

Before the first edit:

- read the current handoff note or recent session summary
- check `git status --short`
- open the file or files named as the next work surface

Visible opening note:

```markdown
# Opening Check
- handoff_read: yes
- baseline_checked: `git status --short` plus `src/parser.ts`
- mismatch: handoff said the parser cleanup was complete, but `src/parser.ts` still has the unresolved normalization TODO
- decision: restage the first task before editing
```

Why this example stays bounded:

- it uses one read step and one visible baseline check before mutation
- it does not become a full git-verification report for every claim
- it does not pick tasks, run a full startup test suite, or import an orchestrator protocol
