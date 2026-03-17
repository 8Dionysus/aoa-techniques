# Second Context Adaptation

## Technique
- id: AOA-T-0003
- name: contract-first-smoke-summary

## Target project
- name: generic repository with one published repo-health or smoke-validation summary
- environment: public-safe validation paths where CI, operators, or agents need one stable machine-readable result instead of console parsing
- runtime: scheduled, CI, or local validation entrypoints that emit one summary artifact per bounded smoke path

## What changed
- paths: the origin used several ATM10 smoke families and run-directory conventions; this adaptation uses one generic repo-health or service-smoke summary path
- services: the validation entrypoint may check docs, service health, contract parity, or another bounded probe; the technique does not depend on one product domain
- dependencies: downstream consumers rely on one declared summary file or stable `--summary-json` output, not ATM10 workflow naming
- operating assumptions: the project may have only one or a few smoke paths, but each still publishes one stable machine-readable contract surface

## What stayed invariant
- contract: each smoke or probe path emits one machine-readable summary that becomes the primary acceptance surface
- validation logic: explicit status, stable discovery, and enough observed fields for basic diagnosis remain required
- safety rules: downstream consumers still read the summary first and do not fall back to log scraping as the main contract
- default-use trigger: once a runnable smoke or probe path feeds CI, operators, or agents, one summary-first contract is the default producer layer before storage, rollout, or remediation helpers appear

## Risks introduced by adaptation
- small repositories can treat the summary as an afterthought and drift back toward console-first acceptance
- teams can emit a nominal JSON file that still lacks enough observed detail for diagnosis
- one-project naming habits can leak back into the adaptation and make the technique look more ATM10-shaped than it is

## Evidence
- the origin already proves the same contract across multiple smoke families with summary-first acceptance behavior
- the semantic review for `AOA-T-0003` versus `AOA-T-0007` already confirms that this technique stays the producer layer rather than drifting into rollout semantics
- the adaptation changes only the smoke family width and domain flavor, not the core rule that a bounded runnable validation path should publish one stable summary contract for downstream consumers

## Result
- works as a bounded second context for repositories that need one stable smoke or probe summary before any storage, history, gate-promotion, or remediation layer is added
