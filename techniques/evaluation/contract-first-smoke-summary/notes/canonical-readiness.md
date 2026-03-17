# Canonical Readiness

## Technique
- id: AOA-T-0003
- name: contract-first-smoke-summary

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: `atm10-agent` documents the summary-first producer contract across multiple smoke families with stable `--summary-json` outputs and explicit summary-based acceptance behavior
- origin reinforcement: the same origin surfaces show the summary contract reused by CI verdicts, operator-facing review paths, and agent-readable structured outputs rather than by log scraping alone
- second context: the new bounded adaptation note shows the same producer-layer contract holding for a smaller generic repository where one smoke or repo-health path still emits one stable machine-readable summary for multiple consumers
- validation strength: the technique now has a reusable example, checklist, stronger origin evidence, a bounded second-context note, and a semantic review that keeps it distinct from storage/history and staged rollout techniques

## Default-use rationale
- this now reads as the default producer-layer pattern when a runnable smoke or probe path should publish one stable machine-readable acceptance surface for CI, operators, and agents
- it remains narrower than adjacent techniques: `AOA-T-0006` stabilizes published latest/history storage after the summary exists, and `AOA-T-0007` governs staged enforcement only after a summary-producing signal already exists

## Fresh public-safety check
- review date: 2026-03-16
- result: pass
- sanitization still holds: the published technique keeps only the reusable summary-contract pattern and removes ATM10-specific smoke families, workflow names, run layouts, and threshold detail
- public reuse check: the current bundle remains understandable without origin-project access and does not depend on hidden operational surfaces to explain the contract

## Remaining gaps
- a future third live context would widen the proof surface further, but it is not required before a first canonical review of this bounded producer-layer contract

## Recommendation
- approve `AOA-T-0003` for `promoted -> canonical` in this wave; the current support surfaces now make it read as the natural default producer contract within its bounded scope without widening into storage, rollout, or downstream helper semantics
