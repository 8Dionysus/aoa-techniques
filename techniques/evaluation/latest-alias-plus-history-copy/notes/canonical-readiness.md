# Canonical Readiness

## Technique
- id: AOA-T-0006
- name: latest-alias-plus-history-copy

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: `atm10-agent` documents the dual-write contract across `readiness`, `governance`, `progress`, and `transition`, with explicit latest alias paths, nested history copies, and anti-double-count reader rules
- origin reinforcement: `D:\atm10-agent\docs\SESSION_2026-03-12.md` and `SESSION_2026-03-13.md` show live integrity checks over `history_summary_json` plus higher-level helpers that reuse latest aliases as a real consumer surface
- second context: `aoa-techniques` now documents the same contract in a bounded object-store-backed adaptation without changing the invariant latest-plus-history pattern
- validation strength: the technique has two examples, a checklist, source-backed origin evidence, a second-context adaptation note, and explicit package adjacency to downstream published-summary consumers

## Default-use rationale
- this is a strong default when a repository publishes machine-readable summaries that need both easy latest discovery and trustworthy historical accumulation
- it preserves backwards-friendly latest consumption without sacrificing immutable run history or allowing silent double-count drift
- a non-default alternative is still better when summaries are purely ephemeral or when consumers already address immutable per-run objects directly and do not need a stable latest alias

## Fresh public-safety check
- review date: 2026-03-15
- result: pass
- sanitization still holds: the published technique keeps only the reusable dual-write storage and reader contract, without ATM10-specific workflow names, thresholds, run roots, or private operational details
- public reuse check: the public examples, checklist, and adaptation note remain understandable without origin-project access and do not depend on hidden tooling assumptions

## Remaining gaps
- a future third live context would widen the proof surface further, but it is not required for a first canonical promotion review

## Recommendation
- approve `AOA-T-0006` for `promoted -> canonical` in this wave; the default-use case is strong, the validation surfaces are already broader than the initial promotion baseline, and the fresh public-safety pass is clean
