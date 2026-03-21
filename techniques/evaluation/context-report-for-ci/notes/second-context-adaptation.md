# Second Context Adaptation

## Technique
- id: AOA-T-0032
- name: context-report-for-ci

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit provenance-note discipline
- runtime: documentation-first repository that records the reporting pattern rather than shipping the donor report engine itself

## What changed

- paths: the donor uses composable markdown fragments and CI-facing report surfaces; this adaptation presents a generic report pattern that can fit other public repositories
- services: no provider/runtime telemetry layer is required in this repository
- dependencies: the adaptation depends on declared source coverage, token comparison, and read-only reporting, not on the donor report scripts
- operating assumptions: contributors should treat the report as a bounded CI artifact and keep repair decisions in a separate follow-up surface

## What stayed invariant

- contract: the report stays read-only and CI-facing
- validation logic: the report compares source coverage and token drift instead of executing the composition itself
- safety rules: the report stays subordinate to the composition technique and does not become a remediation engine

## Risks introduced by adaptation

- the pattern can become vague if a project copies the report but loses the explicit link to source coverage
- some repositories may keep the report while silently letting it drift into generic telemetry or remediation guidance

## Evidence

- the donor `README.md` describes composable markdown fragments plus CI reporting around context composition
- the donor pattern also shows the report as a companion to fragment assembly rather than the assembly engine itself
- this imported technique narrows those behaviors into one reusable docs pattern for CI-facing composition reporting

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific telemetry or remediation breadth
