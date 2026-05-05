# Canonical Readiness

## Technique
- id: AOA-T-0001
- name: plan-diff-apply-verify-report

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: born in `abyss-stack` and already published with reusable contracts, checklist, example, and sanitization notes
- second context: `aoa-techniques` uses the same contribution doctrine in `AGENTS.md`, making the workflow operative outside the origin repository
- validation strength: the technique now has one reusable example, one checklist, one public second-context adaptation note, and repo-level canonical criteria in contribution docs

## Default-use rationale
- this is a safe default for non-trivial agent or human+agent changes because it requires scope, validation, and recovery thinking without forcing project-specific tooling
- it scales from documentation changes to code or operations changes while staying reviewable

## Fresh public-safety check
- review date: 2026-03-14
- result: pass
- sanitization still holds: the published technique remains free of secrets, private infrastructure details, internal-only URLs, and project-bound operational assumptions
- public reuse check: examples, checks, and adaptation notes remain repository-agnostic and understandable without origin-project access

## Remaining gaps
- risk tiers are still described narratively rather than through a shared rubric or machine-readable schema
- a future third context would strengthen breadth further, but it is not required for a first canonical promotion review

## Recommendation
- approve `AOA-T-0001` for `promoted -> canonical` in this wave; the repo-level rubric is met, the second-context evidence remains representative, and the public-safety pass is clean
