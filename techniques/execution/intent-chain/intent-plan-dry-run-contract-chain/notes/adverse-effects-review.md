# Adverse Effects Review

## Technique
- id: AOA-T-0004
- name: intent-plan-dry-run-contract-chain

## Review focus
- current role: default underlying contract for intent-driven dry-run chains
- current watch seam: keep traceability and contract-check discipline subordinate to the artifact-first chain, and keep the chain from collapsing back into generic caution guidance

## Failure modes
- the chain emits artifacts that look complete even though the plan step never actually constrained execution
- traceability metadata drifts between intent, plan, and contract-check layers until routing or validation breaks

## Negative effects
- overfitting the chain to one project's artifact names or CI layout makes the pattern harder to reuse
- the workflow can become ceremony-heavy if every small intent is forced through the full chain even when a lighter contract would be enough

## Misuse patterns
- treating dry-run completeness as proof that real execution would be safe
- using the technique as a generic "be careful" wrapper instead of an artifact-first contract with explicit failure behavior

## Detection signals
- reviewers start relying on logs again because the artifacts no longer carry enough routing or traceability detail
- example text and rollout notes talk mostly about file names or table layout instead of the intent-plan-contract invariant

## Mitigations
- keep the contract anchored to plan-first artifacts, dry-run-only execution, and explicit contract verdicts
- re-check the chain in a second context whenever the wording starts to center one project's filenames or execution surface

## Recommendation
- keep the canonical bundle and use this note as the watch surface for artifact-chain drift, traceability drift, or accidental fallback to log-scraping habits
