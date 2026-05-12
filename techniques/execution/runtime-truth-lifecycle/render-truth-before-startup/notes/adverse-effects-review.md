# Adverse Effects Review

## Technique
- id: AOA-T-0036
- name: render-truth-before-startup

## Review focus
- current role: canonical default for read-only pre-start review of resolved runtime truth
- current watch seam: keep the bundle centered on render/plan review before apply or startup rather than lifecycle ownership, readiness proof, deployment previews, or config publication

## Failure modes
- teams run a render command but never actually review the service set or resolved config before startup
- rendered config is treated as a harmless artifact and leaks secrets, host paths, or local environment values
- preview, dry-run, plan, or template output is mistaken for proof that the host is ready or the runtime will be healthy after launch
- the technique widens into Docker Compose management, deployment orchestration, dashboard operation, image management, or prune policy

## Negative effects
- a required render/review step can add friction when the runtime selection is already trivial
- full rendered config can overwhelm reviewers when the service-list or plan view would answer the question
- local rendered files can linger and become sensitive residue
- canonical status can tempt later authors to treat every deployment preview as equivalent, even when it lacks resolved runtime truth or a human review seam

## Misuse patterns
- committing full rendered config or treating it as the new source of truth
- replacing readiness checks, smoke tests, or lifecycle stop paths with a render-only step
- using generic Helm, Kustomize, Skaffold, Terraform, or Docker dry-run output as proof of this technique without checking the exact pre-start runtime-truth seam
- folding secret handling, volume lifecycle, image upgrade, dashboard, or remote deployment behavior into the render technique

## Detection signals
- guidance says "start" or "apply" before it answers what will actually start
- reviewers cannot distinguish declared config, resolved runtime truth, readiness state, and post-start health
- rendered output appears in public commits, issue comments, or generated docs without redaction
- a tool's value proposition is deployment preview or lifecycle control, while the rendered service/config truth is incidental

## Mitigations
- make the review question explicit: what service/config truth will this runtime actually apply or start now
- use service-list, plan, or config-hash views first; reserve full rendered config for deeper local review
- mask, redact, keep local, or delete full rendered config after inspection
- route readiness, smoke, lifecycle, deployment, monitoring, and proof verdicts to sibling techniques or owning repos
- record adjacent preview tools as searched lanes unless they also provide a distinct operator review seam over resolved runtime truth

## Recommendation
- keep current `canonical` status and use this note as the watch surface for false readiness, secret leakage, deployment-preview drift, and expansion into lifecycle or runtime owner authority
