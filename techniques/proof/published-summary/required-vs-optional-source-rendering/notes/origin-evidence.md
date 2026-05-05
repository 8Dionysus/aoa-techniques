# Origin Evidence

## Technique
- id: AOA-T-0011
- name: required-vs-optional-source-rendering

## Source project
- name: atm10-agent
- source files:
  - `docs/DECISIONS.md`
  - `docs/RUNBOOK.md`
  - `docs/SESSION_2026-03-12.md`
  - `docs/SESSION_2026-03-13.md`

## Evidence
- `docs/DECISIONS.md` records the addition of `required_missing_sources` and `optional_missing_sources`, with strict smoke failure reserved for required canonical sources.
- The same source also records the tolerant rendering rule for optional published summaries: missing optional artifacts render as `not available yet`, while parse or contract drift yields warnings without crashing the surface.
- `docs/RUNBOOK.md` defines the concrete smoke-summary fields `missing_sources`, `required_missing_sources`, and `optional_missing_sources`, and states that optional G2 sources remain observability signals rather than hard failures.
- `docs/RUNBOOK.md` also records soft-info behavior: artifacts such as optional briefs do not escalate into warning or error when the primary JSON summary is present.
- `docs/SESSION_2026-03-12.md` shows the concrete operator surface as `Latest Metrics`, where remediation and integrity summaries are loaded as optional sources with tolerant missing and warning behavior.
- `docs/SESSION_2026-03-13.md` extends the same pattern to `operating_cycle_summary.json`, confirms that `optional_missing_sources` stays observable in smoke output, and keeps the panel useful when optional sources are absent.

## Interpretation
- The origin proves this technique as a concrete rendering and smoke-policy contract over published summaries, anchored in a real operator surface rather than in generic UI guidance.
