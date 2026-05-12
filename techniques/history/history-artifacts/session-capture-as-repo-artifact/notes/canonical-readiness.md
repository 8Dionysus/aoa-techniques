# Canonical Readiness

## Technique
- id: AOA-T-0026
- name: session-capture-as-repo-artifact

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around cloud sync, search UX, history-derived skills, and memory-style behavior
- second context: Aider plus the public `.aider.chat.history.md` artifact family now provides an independent public context where AI coding session history is saved as local Markdown and appears as committed project-visible artifacts in multiple public repositories
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the promoted scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, one real public second context beyond the donor product family, and an adverse-effects review, so first-save capture as a project artifact is no longer proven only by imported documentation

## Default-use rationale
- this is the right canonical default when the main problem is making AI coding sessions persist as local project history artifacts rather than disappear into transient chat state
- it remains narrower than [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md) because it owns first-save capture and persistence, not post-capture transcript shaping
- it remains narrower than [AOA-T-0053](../local-first-session-index/TECHNIQUE.md) because it owns the saved artifact layer, not derivative search or indexing over saved artifacts
- the current evidence now shows that the capture-as-artifact contract survives outside the donor lineage in public Aider-based repository artifacts while keeping memory, search, and instruction authority out of scope

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable local-first session-artifact contract and excludes donor-specific cloud, search, wrapper, account, and history-to-instructions behavior
- public reuse check: the examples, checklist, adaptation notes, and second-context evidence remain understandable without hidden donor-repo context

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on deliberately retained project-visible session artifacts and does not widen into ignored tool-local state, transcript packaging, search/indexing, memory recall, or instruction authority
- future review should keep watching the Aider-shaped edge where `.aider*` can be ignored by default; ignored local logs are adjacent until a project intentionally keeps the artifact reviewable and project-visible

## Recommendation
- promote `AOA-T-0026` to `canonical`
- use `AOA-T-0026` as the default history technique when an AI-assisted project needs first-save local session capture as a reviewable history-artifact layer before transcript packaging, indexing, summaries, memory, or instruction distillation
