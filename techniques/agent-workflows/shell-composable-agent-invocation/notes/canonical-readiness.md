# Canonical Readiness

## Technique
- id: AOA-T-0031
- name: shell-composable-agent-invocation

## Verdict
- bounded defer for now

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around generic shell advice, confirmation as the core invariant, and broader autonomous loop behavior
- second context: `aoa-techniques` now records the same shell-composable invocation contract as a documentation-first adaptation with examples and a checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repo

## Default-use rationale

- this is the right promoted default when the main reusable object is shell composability through stdin, stdout, files, and pipes
- it remains distinct from `AOA-T-0023`, which stays centered on the broader stateless single-shot fast path rather than on shell composability itself
- it remains distinct from `AOA-T-0028`, which stays centered on the explicit confirmation seam before mutation rather than on shell-visible invocation boundaries

## Fresh public-safety check

- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps only the reusable shell-composability contract and excludes generic shell advice, provider breadth, and autonomous-loop behavior
- public reuse check: the public examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public workflow surface where shell-composable one-shot invocation is used as a real execution pattern rather than only as imported documentation

## Recommendation

- keep `AOA-T-0031` `promoted`
- defer canonical promotion until another live adopter confirms that shell-composable invocation survives outside the donor repository
