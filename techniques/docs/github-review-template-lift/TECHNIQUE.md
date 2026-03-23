---
id: AOA-T-0047
name: github-review-template-lift
domain: docs
status: promoted
origin:
  project: aoa-techniques
  path: generated/github_review_template_manifest.json
  note: Extracted from the current GitHub review-template manifest and the authored `.github` templates to keep review intake bounded while the templates remain human-first.
owners:
  - 8Dionysus
tags:
  - docs
  - kag
  - intake
  - templates
  - manifests
summary: Lift authored GitHub issue and pull-request review templates into derived intake knowledge without turning templates into workflow automation or policy scoring.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0019
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# github-review-template-lift

## Intent

Lift authored GitHub issue and pull-request review templates into a bounded derived intake surface so reviewers and tooling can find the right prompt shape without turning templates into workflow automation, approval policy, triage logic, or review-state storage. Within the current KAG/source-lift family, use this when the next question is "which review template should anchor the intake?" rather than "how should the review be decided?"

## When to use

- repositories that keep review prompts in authored GitHub issue or pull-request templates
- intake paths where proposal, import, promotion, or PR review prompts need one bounded lookup surface
- generated readers that should expose template shape without replacing the template body
- KAG-oriented work that needs template-level intake handles before any workflow registry or policy engine exists
- cases where the review prompt itself is the source of meaning, but the current question is routing to the right prompt

## When not to use

- cases that need workflow automation, approval policy, triage, or state transitions instead of bounded prompt lookup
- repos where templates are unstable, ad hoc, or mostly incidental to the intake path
- situations where a manifest would become the editable source of truth instead of a derived surface
- workflows that would use the template layer to infer review decisions, not just review shape
- requests for a review-state registry or a decision engine

## Inputs

- authored `.github/ISSUE_TEMPLATE/*.md` and `.github/PULL_REQUEST_TEMPLATE.md` files
- a current template manifest or generator that can project template scope from those authored files
- review-intake questions such as promotion, external import, proposal, or pull-request review
- explicit agreement that template meaning still lives in the authored markdown files

## Outputs

- bounded template inventory for intake lookup
- derived section scopes for review prompts
- preserved template authority over review wording and fields
- reusable intake surface for later bounded consumers
- no implied workflow automation, approval logic, or review-state registry

## Core procedure

1. Keep the authored GitHub templates as the primary review prompt source.
2. Project the template shapes into a derived manifest or reader surface.
3. Use the derived surface to locate the right review prompt without editing the prompt through the manifest.
4. Keep the template types and section scopes explicit so intake stays bounded and reviewable.
5. Route questions about actual review decisions, policy, or state back to the owning workflow or technique.
6. Rebuild the derived surface whenever the authored templates change.

## Contracts

- authored GitHub templates remain the source of review prompt meaning
- the derived manifest stays bounded to prompt shape, section scope, and template inventory
- template lookup supports intake and review routing, not approval policy or triage behavior
- the technique does not require a workflow engine, a state registry, or a new `kag` domain
- prompt meaning still routes back to the authored `.github` files

## Risks

### Failure modes

- template scopes drift from the authored `.github` files and the manifest stops matching the real intake shape
- the derived surface becomes the thing people edit instead of the templates themselves
- review intake starts asking for decisions or state transitions that the template layer was never meant to answer

### Negative effects

- a tidy template inventory can create false confidence that review routing is fully governed when the actual decision logic still lives elsewhere
- a derived manifest can make intake feel more formal than it is
- template lookup can hide the fact that different review flows still need different human judgment

### Misuse patterns

- treating the template manifest as a workflow policy engine
- adding approval rules or triage state because the intake template surface is already useful
- using review templates as a substitute for a real bounded review contract

### Detection signals

- contributors ask the manifest to decide outcomes instead of just locating the right review prompt
- template section scopes need constant hand edits that are not reflected in the authored markdown
- review routing questions start requiring generated state rather than the template body

### Mitigations

- keep the manifest inventory-only and regenerate from authored templates
- route decision policy and triage behavior back to the workflow or review technique that owns them
- add or change template fields only when the intake prompt itself needs to change
- stop widening the surface when the next request is really for state tracking or policy logic

## Validation

Verify the technique by confirming that:
- the derived surface matches the authored GitHub templates
- the template scopes stay bounded to prompt shape and section inventory
- reviewers can find the right intake prompt without editing the manifest
- template meaning still lives in `.github` markdown files
- no workflow automation or review-state registry was needed to make the surface useful

See `checks/github-review-template-lift-checklist.md` and `examples/minimal-github-review-template-lift.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- the exact set of review templates
- whether templates are issue-only, pull-request-only, or both
- the derived manifest format or reader surface
- how many intake paths share the same template inventory

What should stay invariant:
- templates remain human-first
- the manifest stays derived
- prompt meaning remains in authored markdown
- intake lookup stays bounded to template shape
- the technique does not become workflow automation or state policy

This technique sits beside the metadata spine, but it should not absorb that spine's job or become a registry for review outcomes. If the next question is policy, triage, or approval state, that is a different surface.

## Public sanitization notes

This public version keeps the reusable intake-lift contract and strips repo-specific implementation trivia, local file paths beyond the canonical `.github` template area, and any implication that review decisions are already automated.

## Example

See `examples/minimal-github-review-template-lift.md` for a small GitHub review template excerpt and the corresponding derived intake manifest excerpt.

## Checks

See `checks/github-review-template-lift-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while the GitHub review template manifest and authored templates became the repo's intake surface
- extracted into first public reusable form on 2026-03-23 as part of the initial KAG/source-lift family wave

## Future evolution

- strengthen second-context evidence once another markdown-first corpus uses the same bounded template-intake pattern
- clarify when a template question should move to a workflow contract instead of widening the template manifest
- keep workflow automation, approval policy, triage logic, and review-state storage deferred
