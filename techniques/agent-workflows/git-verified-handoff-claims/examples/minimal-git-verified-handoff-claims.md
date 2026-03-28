# minimal git-verified handoff claims

Handoff claim:

```markdown
# Handoff
- summary: The parser refactor is finished and `src/parser.ts` was updated in commit `abc1234`
- next_step: Continue in `src/serializer.ts`
```

Git evidence checked:
- `git log --oneline -5 -- src/parser.ts`
- `git diff -- src/parser.ts`

Verification result:

```markdown
# Handoff Claim Verification
- claim: `src/parser.ts` was updated in the refactor
- evidence:
  - `git log --oneline -5 -- src/parser.ts`
  - `git diff -- src/parser.ts`
- verdict: verified

- claim: serializer work already landed
- evidence:
  - `git diff -- src/serializer.ts`
- verdict: mismatch
```

Continuation rule:
- continue from the verified repo-backed view, not from the mismatched serializer claim

Why this example stays bounded:
- it checks only the handoff claims that matter for immediate continuation
- it does not become a full review report or witness trace
- trust is anchored to visible git evidence rather than memory
