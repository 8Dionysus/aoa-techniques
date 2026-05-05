# Canonical Readiness

## Technique

- id: AOA-T-0034
- name: public-safe-artifact-sanitization

## Verdict

- approve for canonical promotion

## Evidence summary

- origin evidence: the source skill already defines a bounded sanitization contract with a review checklist, explicit approval/execution exclusions, and a public-safe example
- second context: `Truth-Zeeker-AI-Public` publishes a sanitized public snapshot with pseudonymized captures and outputs, documentation-reserved replacements, change-summary notes, and verification language that keeps the artifact useful for research readers
- local and external boundary sweep: `aoa-playbooks`, `aoa-evals`, `aoa-agents`, `aoa-routing`, and `aoa-skills` overlay branches stayed adjacent or same-lineage rather than becoming a second consumer, while broader public-release/export surfaces such as `br-acc` and `Tiny-Lab` stayed useful adjacent evidence but not exact-fit share-prep closure
- validation strength: the bundle now has a bounded contract, an explicit example, a reviewer-facing checklist, a real external second consumer, and a clearer map of nearby false-positive surfaces

## Default-use rationale

- this is a good default when material is useful but not safe to share raw
- it stays narrower than approval gating, dry-run planning, and safe infra change
- it stays narrower than public-release governance or privacy-engineering programs because the center of gravity is still one bounded artifact made shareable without losing the lesson
- it helps future reviewers without turning the repository into a sharing-policy engine or pretending that share-prep authorizes the underlying action

## Fresh public-safety check

- review date: 2026-03-23
- result: pass
- sanitization still holds: the public bundle keeps only the reusable share-prep contract and excludes source-specific incident detail, release choreography, and broader policy logic
- public reuse check: the example and checklist remain understandable without source-repo access

## Remaining gaps

- no blocking gap remains for canonical use as long as the technique stays bounded to sanitize-for-sharing work over one artifact or artifact set
- future review should keep watching for over-sanitizing already-safe material, false authorization drift, and widening into public-release governance or generic privacy tooling

## Recommendation

- promote `AOA-T-0034` to `canonical`
- use `AOA-T-0034` as the default bounded share-prep technique when sensitive technical material must be made shareable without turning the workflow into approval policy or execution planning
