# Canonical Readiness

## Technique
- id: AOA-T-0009
- name: lightweight-status-snapshot

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: `atm10-agent/docs/SOURCE_OF_TRUTH.md`, `README.md`, `MANIFEST.md`, and `docs/DECISIONS.md` already show lightweight snapshot discipline as an active doc-hygiene policy rather than a one-off cleanup
- second context: `aoa-techniques` applies the same pattern to a smaller public repository where `README.md` stays short and links outward to `TECHNIQUE_INDEX.md`, `AGENTS.md`, `CONTRIBUTING.md`, and `SECURITY.md`
- semantic reinforcement: `docs/DOCS_BOUNDARY_SEMANTIC_REVIEW.md` found the `AOA-T-0002` / `AOA-T-0009` seam `clear`, confirming that the snapshot discipline stays distinct from the broader source-of-truth layout
- validation strength: the technique already has source-backed origin evidence, second-context adaptation, a reusable example, and a bounded checklist

## Default-use rationale
- this is a good default when a repository already has canonical homes for detail but its entrypoint docs are starting to accumulate long status prose, counters, or history that should be linked rather than recopied
- `AOA-T-0009` remains narrower than `AOA-T-0002`: it is the default snapshot-discipline layer for top-level docs, not a replacement for the broader document-role layout

## Fresh public-safety check
- review date: 2026-03-16
- result: pass
- sanitization still holds: the published technique keeps only reusable snapshot-discipline guidance, with origin-specific capabilities, workflow names, local paths, and session-specific counters removed
- public reuse check: the public second context remains understandable on its own and does not rely on hidden operator-only surfaces to explain the core contract

## Remaining gaps
- the public second context uses only one lightweight top-level snapshot doc rather than both `README` and `MANIFEST`, so the smaller variant does not exercise every possible snapshot split

## Recommendation
- approve `AOA-T-0009` for `promoted -> canonical` in this wave; it now reads as the default narrow snapshot discipline for repositories that already have canonical homes for detailed operational truth
