# Origin Evidence

## Technique
- id: AOA-T-0097
- name: degrade-reground-recover

## Source project
- name: ATM10-Agent
- source files:
  - `scripts/hybrid_query_demo.py`
  - `scripts/gateway_v1_local.py`
  - `docs/ANTIFRAGILITY_FIRST_WAVE.md`

## Evidence
- first-wave antifragility landing in `ATM10-Agent` already had a real bounded degraded path around hybrid-query fallback
- the owner-local surface already persisted `run.json` and `hybrid_query_results.json`, so one stressor receipt could be emitted without inventing a second runtime authority
- the reusable core was the posture sequence rather than the repo-local topology: detect one named stressor, degrade into a weaker truthful mode, reground on stronger authority, emit one source-owned receipt, and recover later through reviewed adaptation

## Interpretation
- the technique came from live owner-repo behavior rather than abstract resilience language
- the portable part is the degrade -> reground -> recover posture, not the specific `ATM10-Agent` runtime stack
- other repos can adopt the sequence without inheriting the origin repo's directories, transport, or operator UI
