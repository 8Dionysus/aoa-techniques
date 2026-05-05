# Canonical Readiness

## Technique
- id: AOA-T-0031
- name: shell-composable-agent-invocation

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around generic shell advice, confirmation as the core invariant, and broader autonomous loop behavior
- second context: OpenAI Codex CLI now provides an independent public one-shot execution surface where `codex exec` reads prompts from stdin, streams to stdout or JSONL, and writes final output to files for downstream shell use
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one real public second context beyond the donor lineage, so shell composability is no longer proven only by imported documentation

## Default-use rationale

- this is the right promoted default when the main reusable object is shell composability through stdin, stdout, files, and pipes
- it remains distinct from `AOA-T-0023`, which stays centered on the broader stateless single-shot fast path rather than on shell composability itself
- it remains distinct from `AOA-T-0028`, which stays centered on the explicit confirmation seam before mutation rather than on shell-visible invocation boundaries
- the current evidence now shows that the stdin or stdout or file-first invocation seam survives in an independent public CLI family, so the bundle reads as the natural default when shell I/O composability is the main bounded contract

## Fresh public-safety check

- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable shell-composability contract and excludes generic shell advice, approval-policy breadth, provider breadth, and autonomous-loop behavior
- public reuse check: the public examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- no blocking promotion gap remains as long as the bundle stays centered on shell-visible one-shot composition through stdin, stdout, files, or pipes
- future review should keep watching for drift into interactive session doctrine, approval governance, or broader automation posture that belongs to sibling techniques instead

## Recommendation

- promote `AOA-T-0031` to `canonical`
- use `AOA-T-0031` as the default shell-composability technique when the main reusable object is a one-shot agent run that behaves like a pipe or file-friendly command instead of a hidden session
