# Second Context Adaptation

## Technique
- id: AOA-T-0011
- name: required-vs-optional-source-rendering

## Target project
- name: generic evaluation repository with CLI and machine-readable summary consumers
- environment: public-safe summary pipelines where dashboards are optional and many consumers are JSON reports, smoke summaries, or command-line status views
- runtime: read-only summary loaders that classify required and optional sources before rendering one report

## What changed
- surface: the origin centered on an operator-facing panel; this adaptation applies the same policy to CLI and machine-readable report consumers
- services: no UI framework is required, only explicit source loading and rendering rules
- dependencies: the adaptation depends on source classification and stable summary discovery rather than tab layout or panel components
- operating assumptions: promotion of an optional source to required must be explicit, staged, and auditable rather than silent contract drift

## What stayed invariant
- contract: required sources fail strictly, while optional sources remain observable but non-fatal
- validation logic: missing required sources, missing optional sources, and invalid optional sources stay separate outcomes
- safety rules: the consumer remains read-only and does not hide critical failures by overusing the optional class

## Risks introduced by adaptation
- CLI or JSON consumers can hide warning detail if they collapse optional-source problems into one generic status
- teams can silently promote optional sources to required behavior without updating the documented contract
- optional-source noise can accumulate if warning surfaces are not kept concise and reviewable

## Evidence
- the origin already proves that required and optional sources can be separated in smoke outputs as well as in a human-facing panel
- `AOA-T-0008` and `AOA-T-0010` already define optional published-summary surfaces that a non-UI consumer may want to render tolerantly
- the adaptation changes only the consumer surface, not the required-versus-optional contract

## Result
- works as a bounded non-UI second context for promoted summary consumers, with staged optional-to-required rollout kept explicit instead of silent
