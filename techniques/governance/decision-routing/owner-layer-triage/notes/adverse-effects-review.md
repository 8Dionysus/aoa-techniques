# Adverse Effects Review

## Technique
- id: AOA-T-0076
- name: owner-layer-triage
- current role: bounded canonical default

## Review focus

Review the effects of making one owner-layer verdict the default move for one
already-isolated reusable unit.

## Failure modes

- mixed units are forced into one owner before they are actually split
- the chosen owner becomes the convenient repository rather than the honest
  primary shape
- nearest-wrong rejection is omitted, leaving boundary drift invisible
- downstream routing, KAG, eval, SDK, or playbook consumers are mistaken for
  first-authoring authority

## Negative effects

- premature owner certainty can hide weak evidence
- local repo taxonomy can overfit the verdict and reduce portability
- obvious cases can become slower if every placement becomes ceremonial

## Misuse patterns

- treating usefulness as its own owner layer
- routing every executable-looking unit to a skill surface
- using derivative routing or graph surfaces as the first authored home
- substituting owner triage for donor extraction, context mapping, or final
  promotion review

## Detection signals

- reviewers cannot name one adjacent owner that was rejected
- the proposed next artifact is larger than the verdict requires
- several owner layers still look equally primary after the verdict
- a derivative surface becomes the place where source-owned meaning is first
  authored

## Mitigations

- split mixed units before placement
- require one chosen owner, one next artifact, and one nearest-wrong target
- keep derivative consumers downstream of source-owned authoring
- preserve `hold` when evidence is still weak or mixed

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should sharpen the one-unit owner verdict without widening it into
ecosystem route law, playbook authorship, eval proof, memory writeback, KAG
truth, or SDK execution policy.
