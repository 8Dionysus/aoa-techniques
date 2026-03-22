# Second Context Adaptation

## Technique

- id: AOA-T-0034
- name: public-safe-artifact-sanitization

## Target project

- name: aoa-techniques
- environment: public technique repository with authored bundles, selection surfaces, and generated catalogs
- runtime: documentation-first corpus that records a reusable share-prep contract instead of shipping the source skill manifest

## What changed

- paths: the source lived in `aoa-skills/skills/aoa-sanitized-share`; this adaptation packages the same bounded contract as a standalone docs technique
- artifacts: the technique now owns its own example, checklist, and compact public notes
- dependencies: the reusable contract stands on redaction, generalization, and useful sharing, not on authority or execution tooling
- operating assumptions: the resulting artifact should stay understandable after sanitization and safe for the intended audience

## What stayed invariant

- the shared artifact must not leak sensitive technical detail
- the lesson must survive redaction or generalization
- the contract stays bounded and reviewable
- the technique stays out of approval classification and operational execution

## Risks introduced by adaptation

- the technique can be overused on already-safe material
- the result can become too abstract to be useful
- a reviewer can mistake the technique for a permissioning workflow

## Evidence

- the source skill already has a public-safe runtime example and a review checklist
- the source skill already calls out approval-gate and execution-path boundaries
- the source skill remains focused on share-prep, not on allowing the underlying action

## Result

The same sanitization contract survives a public docs-technique adaptation without carrying over source-specific incident detail or execution semantics.
