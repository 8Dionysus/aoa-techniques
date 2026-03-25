# AGENTS.md

Guidance for coding agents and humans working under `techniques/agent-workflows/`.

## Purpose

This domain stores reusable workflow techniques for bounded execution chains.

Representative bundles here include `plan-diff-apply-verify-report`, `render-truth-before-startup`, `shell-composable-agent-invocation`, `stateless-single-shot-agent`, and `tdd-slice`.

## Domain rules

Keep the sequence explicit. These techniques should tell a reader what happens first, what gets checked, and how closure is reported.
Preserve explicit dry-run, diff, verify, and report stages when they are part of the contract.
Prefer a small reversible slice over a sweeping one-shot flow.

## Boundary

A technique belongs here when the workflow stays reusable across projects and remains lighter than a live skill or runtime playbook.
If the object starts to encode project-specific operators, shell wrappers, or deployment posture, route that meaning to `aoa-skills` or the owning runtime repository instead of widening this technique.

## Hard NO

Do not:

- hide required state behind unstated shell assumptions
- hard-code one repo's private paths or hostnames
- blur workflow technique meaning with product policy or role doctrine
- remove the verification step just to make the flow shorter

## Validation

After changing an agent-workflow technique, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or docs changed too.
