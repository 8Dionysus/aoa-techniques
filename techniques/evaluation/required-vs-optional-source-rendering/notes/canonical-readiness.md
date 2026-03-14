# Canonical Readiness

## Technique
- id: AOA-T-0011
- name: required-vs-optional-source-rendering

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: `atm10-agent` documents explicit `required_missing_sources` and `optional_missing_sources`, tolerant optional rendering, and non-blocking soft-info behavior in both smoke output and operator-facing summary surfaces
- origin reinforcement: `D:\atm10-agent\docs\SESSION_2026-03-12.md` and `SESSION_2026-03-13.md` show remediation, integrity, and operating-cycle summaries rendered as optional published sources without hiding strict failures
- second context: `aoa-techniques` now documents the same contract beyond UI panels through CLI and machine-readable report consumers, plus explicit staged optional-to-required promotion guidance
- validation strength: the technique has two examples, a checklist, source-backed origin evidence, a bounded second-context adaptation note, and clearer wording that separates invariant source-class policy from one specific UI surface

## Default-use rationale
- this is a strong default whenever one summary-driven surface combines truly required sources with optional enrichments, because it preserves honest hard failures while keeping supporting signals observable and non-fatal
- it scales across operator panels, CLI reports, and smoke summaries without changing the core required-versus-optional contract
- a non-default alternative is still better when every source is equally required, or when optional tolerance would hide genuinely unsafe behavior

## Fresh public-safety check
- review date: 2026-03-15
- result: pass
- sanitization still holds: the public technique keeps only the reusable rendering and contract policy, with ATM10-specific panel names, local paths, and project-specific source names removed
- public reuse check: the public bundle now reads beyond one operator panel and remains understandable without hidden repository surfaces

## Remaining gaps
- a future third live context would strengthen breadth further, but the current smoke plus non-UI evidence is already sufficient for a first canonical promotion review

## Recommendation
- approve `AOA-T-0011` for `promoted -> canonical` in this wave; the contract already travels across operator panels, smoke outputs, and non-UI consumers, and the fresh public-safety pass remains clean
