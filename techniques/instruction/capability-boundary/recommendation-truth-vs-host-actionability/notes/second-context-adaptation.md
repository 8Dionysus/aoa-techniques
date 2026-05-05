# Second Context Adaptation

## Technique
- id: AOA-T-0093
- name: recommendation-truth-vs-host-actionability

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable technique bundles

## What changed
- the `aoa-sdk`-specific runtime seam was reduced to one bounded control-plane law for recommendation truth and host executability
- exact install-root paths, JSON fields, and CLI details were moved into adaptation notes instead of the invariant core
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- semantic recommendation is computed separately from host actionability
- host actionability remains visible as an explicit annotation rather than a hidden filter
- non-executable auto-actions are demoted instead of being left in runnable surfaces
- router-only items remain visible when they still matter for confirmation or manual fallback

## Risks introduced by adaptation
- the public wording can drift into generic discovery or marketplace language if recommendation truth stops being the center
- the bundle can drift into upstream-health or registry doctrine if host inventory precedence becomes too broad
- a tiny example can understate how important actionability gaps are for honest risk gating

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is a control-plane actionability law, not a docs taxonomy
- the public wording keeps workspace posture, upstream source readiness, and discovery semantics adjacent but separate
- the origin evidence remains strong enough to justify a promoted bundle without importing `aoa-sdk`-specific CLI or path doctrine as invariants

## Result
- verdict: works
- note: the adapted bundle stays readable as one bounded recommendation-versus-executability split for skill-oriented control planes
