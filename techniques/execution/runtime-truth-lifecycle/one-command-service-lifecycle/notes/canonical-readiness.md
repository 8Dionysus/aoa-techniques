# Canonical Readiness

## Technique

- id: AOA-T-0038
- name: one-command-service-lifecycle

## Verdict

- bounded defer for now

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around memory semantics, logging and OAuth side programs, global install behavior, and broader launcher doctrine
- second context: `aoa-techniques` now records the same lifecycle contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repo

## Default-use rationale

- this is the right promoted default when the main reusable object is one explicit lifecycle entrypoint for a bounded local multi-service stack
- it remains distinct from `AOA-T-0036`, which stays centered on pre-start rendered runtime truth rather than on startup and shutdown ownership
- it remains distinct from `AOA-T-0037`, which stays centered on selector-aware readiness verdicts rather than on launch control

## Fresh public-safety check

- review date: 2026-03-23
- result: pass
- sanitization still holds: the bundle keeps only the reusable local-lifecycle contract and excludes donor-specific ports, paths, integration surfaces, and memory breadth
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public workflow surface where one-entrypoint local lifecycle ownership is used as a real operator contract rather than only as imported documentation

## Recommendation

- keep `AOA-T-0038` `promoted`
- defer canonical promotion until another live adopter confirms that the same bounded local lifecycle contract survives outside the donor repository
