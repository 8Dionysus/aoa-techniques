# Second Context Adaptation

## Technique
- id: AOA-T-0013
- name: single-source-rule-distribution

## Target project
- name: aoa-skills
- environment: public skill repository with authored `SKILL.md` bundles, `techniques.yaml` source refs, generated readers, and validator-backed bridge tooling
- runtime: markdown-first skill corpus where one authoritative source can feed multiple committed instruction surfaces without making each target canonical

## What changed
- paths: the donor contract is now grounded in live `aoa-skills` bridge surfaces, with one upstream technique source pinned in `techniques.yaml` and multiple committed target consumer surfaces in skill bundles
- services: distribution uses bounded refresh and drift helpers, not hand-edited copy fan-out or a product-width orchestration layer
- dependencies: the adaptation depends on pinned source refs, explicit target consumers, and validator-backed skill contracts, not on hidden runtime propagation
- operating assumptions: one authoritative source can stay canonical while multiple downstream instruction surfaces remain derived, reviewable, and refreshable from it

## What stayed invariant
- contract: one canonical rule source fans out to multiple agent-facing instruction surfaces
- validation logic: repeated application should not duplicate shared instructions across targets
- safety rules: managed targets should not become hand-maintained source-of-truth files

## Risks introduced by adaptation
- bridge docs can overstate the pattern if only one upstream technique is ever refreshed in practice
- skill-local wording can blur source-of-truth layout with instruction distribution if the target consumer surfaces are not named explicitly
- future expansions could drift into broader orchestration if the refresh tooling stops being bounded and reviewable

## Evidence
- merged `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` now extends `docs/BRIDGE_SPEC.md` with a current fan-out proof: one upstream source technique, multiple committed target consumer surfaces, and explicit drift-control commands
- the same merged donor change updates `skills/aoa-source-of-truth-check/SKILL.md` so one authoritative source staying aligned across multiple downstream consumer surfaces is now part of an authored runtime skill surface
- the consumer surfaces remain committed and reviewable instead of being generated only at runtime, which keeps the one-source -> many-target contract inspectable
- this closes the first live donor gap for `AOA-T-0013`, but it is still only one repository and one bridge style rather than a second independent instruction-distribution context

## Result
- works as a first live second-context adaptation for one-source -> many-target distribution, while still needing one more independent reinforcement before any future canonical review
