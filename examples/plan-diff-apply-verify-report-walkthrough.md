# Walkthrough: AOA-T-0001

This walkthrough shows how one real practice moved from an origin project into a public reusable technique and then proved portable in a second context.

## Source Surfaces

- [Technique](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md)
- [Minimal change flow example](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/examples/minimal-change-flow.md)
- [Review checklist](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/checks/review-checklist.md)
- [Second-context adaptation](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/notes/second-context-adaptation.md)
- [Canonical readiness](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/notes/canonical-readiness.md)
- [Root AGENTS](../AGENTS.md)
- [CONTRIBUTING](../CONTRIBUTING.md)

## Demonstrates

### Origin Practice

`AOA-T-0001 plan-diff-apply-verify-report` started in `abyss-stack`, where a visible change protocol was used to keep non-trivial agent work reviewable and bounded.

### Published Technique

The public technique keeps the invariant workflow:

- `PLAN`
- `DIFF`
- `APPLY`
- `VERIFY`
- `REPORT`

What was generalized for publication:

- project-specific infrastructure details were removed
- private paths and environment-specific assumptions were stripped
- the workflow was rewritten as a repository-agnostic change protocol

### Reuse Evidence

The technique is not published on abstraction alone.
Its evidence stack includes:

- origin use in `abyss-stack`
- a public second-context adaptation in `aoa-techniques`
- a checklist and example that keep the technique reviewable
- a canonical-readiness review with explicit default-use rationale and fresh public-safety confirmation

### Second-Context Adaptation

In `aoa-techniques`, the same workflow applies to repository policy files, technique docs, examples, and checks rather than to deployment or runtime changes.

What stayed invariant:

- every non-trivial change starts with an explicit plan
- the diff stays scoped
- verification is named explicitly
- the result ends with concise reporting

What changed:

- verification is usually document consistency review or checklist confirmation
- the workflow depends on public contribution rules in `AGENTS.md` and `CONTRIBUTING.md`
- no production runtime or deployment layer is involved

This is what makes the technique portable: the core contract survives while project-shaped details change.

## Boundary

This repository prefers techniques that were first tested in real projects, then sanitized, documented, and validated in a reusable public form.

`AOA-T-0001` is a compact example of that path:

`origin practice -> published technique -> public reuse evidence -> canonical recommendation`

This file illustrates that path. It does not replace the technique, adaptation
note, readiness note, root route card, contribution rules, generated catalogs,
or validators.

## Checks

Use [examples/AGENTS.md#validation](AGENTS.md#validation) for the local
validation route. When this walkthrough changes source claims, also validate the
owning technique bundle and generated example manifest.

## Closeout

A clean closeout for this lane names:

- changed example files
- source surfaces consulted
- whether generated example or repo-doc surfaces changed
- checks run and checks skipped
- any owner route discovered during the example update
