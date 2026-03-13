# Second Context Adaptation

## Technique
- id: AOA-T-0001
- name: plan-diff-apply-verify-report

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human+agent contribution workflow over reviewable repository changes

## What changed
- paths: the origin focused on a source-project `AGENTS.md`; this adaptation applies the same flow across repository policy files, technique docs, examples, and checks
- services: no deployment or production runtime is involved; verification is usually document consistency review, checklist confirmation, or repository hygiene review
- dependencies: the adaptation depends on clear contribution rules in `AGENTS.md` and `CONTRIBUTING.md` rather than environment-specific tooling
- operating assumptions: contributions are public-safe by default, scoped to reviewable diffs, and reported back with explicit validation notes

## What stayed invariant
- contract: every non-trivial change starts with an explicit plan, stays scoped during the diff, names verification, and ends with a concise report
- validation logic: verification is still explicit and cannot be replaced by implied confidence
- safety rules: rollback thinking and reviewability remain required before wider application

## Risks introduced by adaptation
- documentation-heavy work can make `VERIFY` too symbolic if contributors stop naming concrete review steps
- low-risk changes can tempt contributors to skip rollback thinking even when a simple recovery path should still be stated

## Evidence
- `AGENTS.md` codifies `PLAN -> DIFF -> VERIFY -> REPORT` as the repository contribution doctrine
- `CONTRIBUTING.md` and the technique's own example/checklist keep the workflow reviewable at repository scope rather than only in the origin project

## Result
- works
