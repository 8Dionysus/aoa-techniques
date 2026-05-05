# Second Context Adaptation

## Technique
- id: AOA-T-0007
- name: signal-first-gate-promotion

## Target project
- name: generic repository with one published repo-validation signal and one narrow strict nightly surface
- environment: public-safe repository validation where pull requests stay observational while nightly validation becomes the first strict surface
- runtime: CI plus one scheduled nightly validation path that can preserve summaries before and after strict activation

## What changed
- paths: the origin used ATM10 nightly and telemetry-layer paths; this adaptation uses `runs/repo-validation/` plus explicit readiness, governance, progress, and transition summary directories
- services: the promoted signal is a repo-validation or docs-parity style check rather than an ATM10 gateway signal
- dependencies: pull requests publish one observational summary such as `pr_summary.json`, while nightly uses one strict `nightly_summary.json`; the rollout still depends on short retained history and explicit decision summaries
- operating assumptions: strict activation happens only on nightly, while pull requests and local debugging remain observational during the rollout

## What stayed invariant
- contract: one summary-producing signal starts observational and promotes to one explicitly chosen strict surface only after evidence accumulates
- validation logic: readiness uses history, governance makes `go` or `hold` explicit, and progress/transition summaries stay published with explicit artifact paths
- safety rules: diagnostics continue to publish even after strict activation, and non-promoted surfaces do not silently inherit strict failure behavior
- default-use trigger: once an already-summary-producing repo-validation signal should become enforceable without turning every pull request red immediately, staged promotion is the default pattern before jumping straight to broad hard gating

## Risks introduced by adaptation
- teams can collapse readiness, governance, progress, and transition summaries into one implicit policy and lose the staged-review nature of the rollout
- strict behavior can spread from nightly into pull requests if the strict-surface boundary is not written down explicitly
- small repositories can under-invest in retained history and promote from too little evidence

## Evidence
- the origin already proves observational mode, explicit readiness/governance/progress/transition telemetry, one narrow strict surface, and preserved diagnostics after strict activation
- the semantic review for `AOA-T-0003` versus `AOA-T-0007` already confirms that this technique stays a rollout layer over an existing summary contract rather than a producer or storage contract
- the concrete repo-validation scenario keeps the same staged path while making the beyond-origin rollout surfaces explicit: pull-request observation, nightly-only strict enforcement, and named readiness/governance/progress/transition summaries
- the paired example `examples/concrete-repo-validation-rollout.md` shows the same contract without relying on ATM10-specific policy labels, product domains, or hidden donor context

## Result
- works as a bounded concrete second context for repositories that want to move one repo-validation signal from pull-request observation to one strict nightly surface without losing explicit rollout telemetry or diagnostic publication
