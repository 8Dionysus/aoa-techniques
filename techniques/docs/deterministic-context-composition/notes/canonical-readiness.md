# Canonical Readiness

## Technique
- id: AOA-T-0012
- name: deterministic-context-composition

## Verdict
- approved for canonical promotion

## Evidence summary
- external origin: `notes/external-origin.md` already records the donor source, retained bounded contract, and explicit exclusions around toolchain-specific donor behavior
- external import review: `notes/external-import-review.md` already found the first external-import path readable, bounded, and public-safe without widening the bundle
- second context: `notes/second-context-adaptation.md` shows the same contract surviving in `aoa-techniques` as a documentation-first adaptation rather than a donor-specific toolchain clone
- semantic reinforcement: `docs/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md` kept the `AOA-T-0012` vs `AOA-T-0013` seam clear, confirming that one-output deterministic composition remains distinct from one-source multi-target rule distribution
- stronger validation: the bundle now carries two public-safe examples plus the existing checklist, which is stronger than the initial promoted import floor

## Default-use rationale
- this is the default when the main problem is many source fragments composing into one generated context artifact with deterministic ordering and explicit source traceability
- `AOA-T-0013` remains the better non-default adjacent alternative when one canonical rule source must fan out to multiple managed targets instead of many fragments collapsing into one output

## Fresh public-safety check
- review date: 2026-03-18
- result: pass
- sanitization still holds: the public bundle keeps only the reusable fragment-first composition contract, with donor-specific CLI packaging, runtime assumptions, migration helpers, and other product-width behavior still excluded
- public reuse check: the public examples, checklist, semantic-review reinforcement, and adaptation notes remain understandable without hidden internal context or donor-repo access

## Remaining gaps
- another external adaptation context would widen the proof surface further, but it is not required for a first canonical promotion review

## Recommendation
- approve `AOA-T-0012` for `promoted -> canonical`; it now reads as the default one-output composition pattern within its bounded scope
