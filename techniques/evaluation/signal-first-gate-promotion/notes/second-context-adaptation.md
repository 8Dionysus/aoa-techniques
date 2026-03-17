# Second Context Adaptation

## Technique
- id: AOA-T-0007
- name: signal-first-gate-promotion

## Target project
- name: generic repository with one published validation signal and one narrow strict release surface
- environment: public-safe validation systems where one summary-producing check starts observational and later graduates into one explicitly chosen strict path
- runtime: CI, scheduled workflows, release-train jobs, or other bounded execution surfaces that can preserve diagnostic summaries while enforcement remains narrow

## What changed
- paths: the origin used ATM10 nightly and telemetry-layer paths; this adaptation uses one generic strict surface such as nightly, release-train, or scheduled validation
- services: the promoted signal may come from service health, docs parity, repo validation, or another summary-producing check; the technique does not depend on one product family
- dependencies: the adaptation assumes only one stable summary-producing producer layer and one place to retain short run history, not ATM10-specific workflow names
- operating assumptions: explicit readiness, governance, progress, and transition telemetry can be lighter-weight than the origin, but staged promotion remains visible and reviewable

## What stayed invariant
- contract: one summary-producing signal starts observational and promotes to one explicitly chosen strict surface only after evidence accumulates
- validation logic: readiness uses history, governance makes `go` or `hold` explicit, and progress/transition keep the rollout interpretable
- safety rules: diagnostics continue to publish even after strict activation, and non-promoted surfaces do not silently inherit strict failure behavior
- default-use trigger: once an already-summary-producing signal should become enforceable without widening the fail surface prematurely, staged promotion is the default pattern before jumping straight to global hard gating

## Risks introduced by adaptation
- teams can collapse the telemetry layers into implicit policy and lose the staged-review nature of the rollout
- strict behavior can spread beyond the chosen narrow surface if the boundary is not written down explicitly
- smaller repositories can under-invest in history and accidentally promote from too little evidence

## Evidence
- the origin already proves observational mode, explicit readiness/governance/progress/transition telemetry, one narrow strict surface, and preserved diagnostics after strict activation
- the semantic review for `AOA-T-0003` versus `AOA-T-0007` already confirms that this technique stays a rollout layer over an existing summary contract rather than a producer or storage contract
- the adaptation changes only the shape of the strict surface, not the invariant staged path from observation to narrow enforcement

## Result
- works as a bounded second context for any repository that already has one stable summary-producing signal and needs an explicit staged path to one narrow strict surface without losing diagnostic publication
