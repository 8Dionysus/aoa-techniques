# Second Context Adaptation

## Technique
- id: AOA-T-0101
- name: local-pattern-adoption-gate

## Target project
- name: aoa-techniques
- environment: public technique corpus with Method-growth mechanics and authored technique bundles
- runtime: human and agent review workflow over portable technique documentation

## What changed
- the Method-growth adoption cycle was narrowed to one local gate before adoption
- lifecycle hooks such as request, readiness, shadow, decision, activation, and retention stayed in mechanics
- AoA owner names and downstream adoption-wave context moved into origin evidence and adaptation notes instead of the invariant core
- the bundle was reduced to one `TECHNIQUE.md`, one checklist, one example, and three evidence notes

## What stayed invariant
- adoption remains explicit
- local owner consent remains required before durable behavior changes
- evidence, rollback or quarantine, and retention watch remain visible
- upstream approval does not become local adoption by itself

## Risks introduced by adaptation
- the public technique can widen into a full adoption workflow if lifecycle hooks are pulled into the core procedure
- the gate can drift into a generic approval policy if one local behavior surface is not named
- the AoA example can look like required ecosystem structure unless public adaptation notes keep it optional

## Evidence
- the adapted bundle stays in `agent-workflows` because the reusable object is one review-side guardrail over a local behavior change
- the bundle's adjacent-technique notes keep owner-layer triage and nearest-wrong-target rejection separate
- the example uses Method-growth only as an adaptation example and does not require OS Abyss deployment

## Result
- verdict: works
- note: the adapted bundle stays readable as one local adoption gate rather than a full Method-growth mechanic
