# Concrete Skill Doc Composition

This example shows several instruction fragments composing into one generated `AGENTS.md`-style artifact with deterministic ordering and explicit source annotations.

## Source fragments

`fragments/00-repo-policy.agents.md`

```md
<!-- priority: 100 -->
## Repository policy

- Keep diffs focused and reviewable.
- Validate generated surfaces after changing source fragments.
```

`fragments/10-safety.agents.md`

```md
<!-- priority: 80 -->
## Safety checks

- Confirm destructive actions before execution.
- Do not treat generated outputs as hand-edited sources of truth.
```

`fragments/20-skill-routing.agents.md`

```md
<!-- priority: 40 -->
## Skill routing

- Use the skill index to choose the smallest applicable workflow.
- Prefer fragment edits over patching the generated instruction artifact directly.
```

## Composition rules

- Fragments are discovered from `fragments/*.agents.md`.
- Ordering is deterministic: higher numeric `priority` first, then stable path order.
- Every rendered section keeps a source annotation so reviewers can trace output back to the fragment that produced it.
- Contributors review the fragment files, not the generated output, as the canonical source of truth.

## Generated `AGENTS.md`-style artifact

```md
<!-- Generated file. Edit fragments/*.agents.md instead. -->
<!-- source: fragments/00-repo-policy.agents.md priority=100 -->
## Repository policy

- Keep diffs focused and reviewable.
- Validate generated surfaces after changing source fragments.
<!-- /source: fragments/00-repo-policy.agents.md -->

<!-- source: fragments/10-safety.agents.md priority=80 -->
## Safety checks

- Confirm destructive actions before execution.
- Do not treat generated outputs as hand-edited sources of truth.
<!-- /source: fragments/10-safety.agents.md -->

<!-- source: fragments/20-skill-routing.agents.md priority=40 -->
## Skill routing

- Use the skill index to choose the smallest applicable workflow.
- Prefer fragment edits over patching the generated instruction artifact directly.
<!-- /source: fragments/20-skill-routing.agents.md -->
```

## What this proves

- several source fragments can compose into one generated context artifact without manual merge steps
- deterministic ordering stays explainable from a small rule set instead of hidden tribal knowledge
- source annotations preserve traceability from each rendered section back to the fragment that produced it
- the bounded contract stays centered on many fragments narrowing into one output, not on one canonical source fanning out to many targets
