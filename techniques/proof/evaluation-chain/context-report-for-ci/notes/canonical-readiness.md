# Canonical Readiness

## Technique
- id: AOA-T-0032
- name: context-report-for-ci

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around composition mechanics, remediation snapshot doctrine, provider/runtime telemetry, and other product-width detail
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with examples and a checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repository

## Default-use rationale
- this is the right promoted default when a CI job needs to report on context composition health without opening the composition engine itself
- it remains narrower than `AOA-T-0012`, which owns deterministic context composition, and narrower than `AOA-T-0008`, which owns the published-summary remediation snapshot doctrine
- the report is intentionally read-only: it observes coverage and drift, then hands off any fix decision to another surface

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps only the reusable CI-facing report contract and excludes donor-specific telemetry, remediation, and composition machinery
- public reuse check: the examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses the same CI-facing context report as a real report artifact rather than only as imported documentation
- latest evidence pass, 2026-05-12: defer still holds after searching public context-report, token-budget, repo-packing, LLM-ready-docs, and CI reporting surfaces
- adjacent or insufficient surfaces from that pass: GitHub Agentic Workflows token and audit reports, Repomix repo-packing and token-count surfaces, Repo Tokens badge-style token counts, `pytest-llm-report` test/LLM annotation reports, Calcis prompt cost estimates, and `llms-txt-action` documentation conversion workflows
- why those surfaces do not close the gap: each is useful but either owns context assembly, token/cost monitoring, documentation conversion, prompt/test reporting, or generic workflow audit rather than a read-only CI-facing report over composed-context source coverage plus token drift
- Stage 1 long-pass, 2026-05-12: defer still holds after inspecting newer public context-compiler, context-drift, fragment-assembly, dependency-graph, and repo-quality report surfaces
- adjacent or insufficient surfaces from that pass: LogicStamp Context, Claude Code Guide context-engineering CI drift detection, ctxloom, Depwire, and FastPace repo-quality/context-score reports
- why those surfaces do not close the gap: they are useful context compilation, configuration drift, fragment assembly, graph context, governance, or repo-quality surfaces, but none clearly emits the same separate read-only CI artifact over already-composed context source coverage plus token drift
- next honest search shape: look for artifact-first public workflows where CI compares an expected source or fragment inventory against a generated prompt/context artifact and records token deltas, while keeping assembly, scoring, and remediation outside the report

## Recommendation
- keep `AOA-T-0032` `promoted`
- defer canonical promotion until another live adopter confirms that the CI-facing context-report contract survives outside the donor repository
