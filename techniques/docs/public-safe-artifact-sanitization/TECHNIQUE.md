---
id: AOA-T-0034
name: public-safe-artifact-sanitization
domain: docs
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-sanitized-share/SKILL.md
  note: Extracted from the bounded public-safe share-prep workflow surface and sanitized into a reusable docs technique.
owners:
  - 8Dionysus
tags:
  - docs
  - sanitization
  - sharing
  - public-safe
  - bounded
summary: Turn sensitive technical material into a shareable artifact by removing, redacting, or generalizing details while preserving the lesson and staying distinct from approval gating or execution planning.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-22
export_ready: true
relations: []
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# public-safe-artifact-sanitization

## Intent

Convert potentially sensitive technical material into a shareable artifact that keeps the lesson while removing or generalizing what should not leave the local context.

## When to use

- logs, configs, diagnostics, reports, or examples contain sensitive details
- a result needs to be shared with a broader audience
- the goal is to preserve the technical lesson without preserving unsafe detail
- the artifact should remain useful after paths, identifiers, or topology are generalized

## When not to use

- the material is already clearly public-safe and minimal
- the real question is whether sharing is allowed at all; use `aoa-approval-gate-check` first
- the real question is whether to preview or execute the change; use `aoa-dry-run-first` or `aoa-safe-infra-change` first
- the task is incident handling or operational response rather than preparing a shareable artifact

## Inputs

- the material to share
- the intended audience
- known sensitive surfaces
- the minimum useful detail needed for the audience

## Outputs

- a sanitized shareable artifact
- a short note on what was removed or generalized
- any remaining sensitivity warning that still matters
- a result that stays understandable without exposing unsafe context

## Core procedure

1. Inspect the material for secrets, tokens, private paths, topology, or unsafe operational detail.
2. Remove, redact, or generalize the sensitive parts.
3. Preserve the technical lesson or signal.
4. Note what kind of sanitization was applied when that matters for interpretation.
5. Verify that the final artifact still teaches the intended point.

## Contracts

- the shared artifact does not leak secrets or private infrastructure detail
- sanitization preserves meaning where possible
- generalization does not silently change the core lesson beyond recognition
- uncertainty about sensitivity leans toward caution
- the technique does not own approval classification, dry-run planning, or incident response

## Risks

### Failure modes

- over-sanitizing until the artifact stops being useful
- under-sanitizing because a value looked harmless in isolation
- the artifact looks "safe enough" after obvious redaction even though topology, approval assumptions, or sensitive deltas still leak through
- confusing share-prep work with approval or execution work

### Negative effects

- the shared artifact becomes hard to reuse or verify
- sensitive topology or naming still leaks through
- a cleaned-up artifact can create false confidence that the underlying action or system is approved or safe, even though only the shareable surface was reviewed
- the technique can become a proxy for decision-making if its boundary is not respected

### Misuse patterns

- sharing raw excerpts when a bounded summary would be safer
- treating a sanitized artifact as proof that the underlying action is allowed
- using the technique to preview or carry out the operational change itself

### Detection signals

- the sanitized output still points too directly to private topology or naming
- reviewers say the artifact "looks safe" but still cannot tell what was generalized, what was omitted, or what remains uncertain
- a reviewer cannot tell what was generalized or removed
- the artifact no longer communicates the lesson it was meant to preserve

### Mitigations

- generalize paths, hostnames, and private identifiers when needed
- name the sanitization level and remaining uncertainty
- separate "safe to share" from "safe to approve or execute" in the final note
- verify the shared result remains useful without preserving the sensitive surface
- route approval or execution questions to the narrower workflow techniques first

## Validation

Verify the technique by confirming that:
- obvious sensitive surfaces were checked deliberately
- the resulting artifact is still understandable
- the sanitization level matches the intended audience
- raw sensitive detail was not preserved by accident
- the shared result does not pretend to authorize the underlying action or prove the underlying system is safe
- the technique stays distinct from approval gating, dry-run planning, and infra-change execution

See `checks/public-safe-artifact-sanitization-checklist.md`.

## Adaptation notes

What can vary across projects:
- the shareable artifact format
- the redaction style
- the amount of detail that can stay visible
- the review ritual for public or broad internal circulation

What should stay invariant:
- sensitive surfaces are checked before sharing
- the lesson remains useful after sanitization
- the result stays bounded and reviewable
- approval and execution decisions stay outside this technique

Project-shaped details that should not be treated as invariant:
- exact hostnames or paths
- internal ticket references
- runtime tooling names
- incident-response or deployment workflows

## Public sanitization notes

This public version keeps the reusable share-prep contract and removes source-repo-specific incident detail, private topology, and operational context that should not be circulated as-is.

## Example

See `examples/minimal-public-safe-artifact-sanitization.md`.

## Checks

See `checks/public-safe-artifact-sanitization-checklist.md`.

## Promotion history

- extracted from the `aoa-sanitized-share` skill surface in `aoa-skills`
- promoted into `aoa-techniques` on 2026-03-22 as a bounded public-safe sharing technique

## Future evolution

- add a sibling for redaction policy review if the review step becomes reusable on its own
- add a sibling for incident-summary preparation if incident share-prep proves distinct from general sanitization
- add a sibling for sanitized example generation if example transformation becomes a recurring reusable object
