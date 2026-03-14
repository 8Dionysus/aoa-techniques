# Walkthrough: AOA-T-0001

This walkthrough shows how one real practice moved from an origin project into a public reusable technique and then proved portable in a second context.

## 1. Origin practice

`AOA-T-0001 plan-diff-apply-verify-report` started in `abyss-stack`, where a visible change protocol was used to keep non-trivial agent work reviewable and bounded.

See:
- `techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md`

## 2. Published technique

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

See:
- `techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md`
- `techniques/agent-workflows/plan-diff-apply-verify-report/examples/minimal-change-flow.md`
- `techniques/agent-workflows/plan-diff-apply-verify-report/checks/review-checklist.md`

## 3. Reuse evidence

The technique is not published on abstraction alone.
Its evidence stack includes:
- origin use in `abyss-stack`
- a public second-context adaptation in `aoa-techniques`
- a checklist and example that keep the technique reviewable
- a canonical-readiness review with explicit default-use rationale and fresh public-safety confirmation

See:
- `techniques/agent-workflows/plan-diff-apply-verify-report/notes/second-context-adaptation.md`
- `techniques/agent-workflows/plan-diff-apply-verify-report/notes/canonical-readiness.md`

## 4. Second-context adaptation

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

See:
- `techniques/agent-workflows/plan-diff-apply-verify-report/notes/second-context-adaptation.md`
- `AGENTS.md`
- `CONTRIBUTING.md`

## 5. Why this matters here

This repository prefers techniques that were first tested in real projects, then sanitized, documented, and validated in a reusable public form.

`AOA-T-0001` is a compact example of that path:

`origin practice -> published technique -> public reuse evidence -> canonical recommendation`
