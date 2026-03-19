---
id: AOA-T-0001
name: plan-diff-apply-verify-report
domain: agent-workflows
status: canonical
origin:
  project: abyss-stack
  path: AGENTS.md
  note: Derived from a real operational workflow and sanitized for public reuse.
owners:
  - 8Dionysus
tags:
  - agent-workflow
  - safety
  - reviewable
  - reproducible
summary: Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations:
  - type: complements
    target: AOA-T-0004
  - type: complements
    target: AOA-T-0005
evidence:
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: second_context
    path: notes/second-context-adaptation.md
---

# plan-diff-apply-verify-report

## Intent

Reduce unsafe, opaque, or non-reviewable agent changes by requiring a visible workflow before and after apply.

## When to use

- agent-assisted code changes
- infrastructure or configuration edits
- documentation changes with operational impact
- cross-repo adaptations that need clear review boundaries

## When not to use

- trivial wording fixes with no meaningful operational consequence
- urgent manual intervention where immediate human action matters more than formal workflow ceremony

## Inputs

- target goal
- touched files or operational surfaces
- intended validation method
- rollback idea or recovery path

## Outputs

- explicit plan
- scoped diff
- applied change
- validation result
- short final report

## Core procedure

1. `PLAN`
   - define the goal
   - name the surfaces that will change
   - identify the main risk
   - think through rollback before applying
2. `DIFF`
   - prepare the smallest reviewable change that solves the goal
   - avoid unrelated refactors or opportunistic cleanup
3. `APPLY`
   - apply only after the plan is clear enough to review
   - keep the implementation consistent with the stated scope
4. `VERIFY`
   - run checks, smoke tests, or operational validation
   - record what was actually validated and what was not
5. `REPORT`
   - summarize what changed
   - summarize validation results
   - state rollback or recovery considerations

## Contracts

- changes must stay reviewable by another human or agent
- validation must be named explicitly, not implied
- higher-risk changes require stronger reporting discipline
- rollback should be thinkable before apply, even if not fully automated

## Risks

### Failure modes

- weak or symbolic validation creates a false sense of safety around the applied change
- teams use the workflow on trivial edits and lose the bounded judgment about when lighter handling is enough

### Negative effects

- extra ceremony can slow down simple work that does not need a full plan-and-report loop
- reporting overhead can crowd out the clearer review surface that should still come from the diff itself

### Misuse patterns

- treating the report as a substitute for a readable diff
- naming a validation step without running a meaningful check or explicitly documenting why it was skipped

### Detection signals

- trivial wording or formatting edits are going through the same ceremony as higher-impact changes
- final reports describe success in general terms but do not name concrete validation results

### Mitigations

- use a lighter workflow when the change has no meaningful operational consequence
- keep the diff reviewable on its own and make the validation step concrete, explicit, and scoped

## Validation

Verify the technique by confirming that:
- a concrete plan exists before apply
- the diff stays inside the declared scope
- at least one explicit validation method is run or intentionally skipped with explanation
- the final report includes both outcome and rollback thinking

See `checks/review-checklist.md`.
For second-context evidence and canonical-readiness review, see `notes/second-context-adaptation.md` and `notes/canonical-readiness.md`.

## Adaptation notes

What can vary across projects:
- validation depth and tool choice
- risk classification language
- runtime, deployment, or review-surface assumptions
- repository layout and ownership expectations
- whether verification is a runtime smoke test, a checklist, or a document consistency review

Project-shaped details that should not be treated as invariant:
- CI job names or review tool names
- deployment approval gates or release holds
- owner or team labels
- patch transport or execution tooling

What should stay invariant:
- explicit plan before apply
- scoped diff
- named verification
- concise outcome reporting

See `notes/second-context-adaptation.md` for a public second-context example.

## Public sanitization notes

Original project-specific infrastructure details, private paths, and environment-specific assumptions were removed. The workflow was generalized into a repository-agnostic change protocol.

## Example

See `examples/minimal-change-flow.md`.

## Checks

See `checks/review-checklist.md`.

## Promotion history

- born in `abyss-stack`
- validated as a reusable agent workflow outside the original project context
- promoted to `aoa-techniques` on 2026-03-13
- approved as `canonical` in `aoa-techniques` on 2026-03-14 after fresh public-safety review and default-use confirmation

## Future evolution

- add clearer risk tiers for lightweight versus high-impact changes
- capture a third context with stronger runtime validation
- add optional machine-readable check metadata if the repository later needs it
