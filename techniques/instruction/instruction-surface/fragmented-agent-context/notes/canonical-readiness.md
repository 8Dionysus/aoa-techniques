# Canonical Readiness

## Technique
- id: AOA-T-0030
- name: fragmented-agent-context

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around deterministic composition, CI reporting, and runtime injection breadth
- exact-fit second context: Cline Rules proves the fragment-first authoring contract outside the donor through workspace `.clinerules/` markdown and text files, topic-specific files such as coding, testing, and architecture guidance, all-file combination into one rule context, and a best-practice rule of one concern per file
- external review: the first import review passed, and the Cline pass confirms fragment-first source authoring survives without importing deterministic composition, CI reporting, runtime injection, or rule-toggle policy
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, exact-fit public second-context evidence, and an adverse-effects review

## Default-use rationale

- this is the right canonical default when the problem is fragment-first context authoring before any generated aggregate or CI report becomes the center of gravity
- it remains distinct from `AOA-T-0012`, which stays centered on deterministic composition into one generated artifact
- it remains narrower than `AOA-T-0032`, which stays centered on CI-facing reporting over composition outcomes rather than on authoring the fragment layer itself
- Cline confirms that the move can survive outside the donor even when the consumer combines fragments at runtime, because the reusable object remains the authored fragment layer and bounded source partitioning

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable fragment-first authoring contract and excludes generator, report, and runtime-loading breadth
- public reuse check: the public examples, checklist, adaptation notes, and Cline evidence remain understandable without hidden donor-repo context
- public-safety boundary: Cline rule paths and activation details are cited only as evidence of bounded authored fragments, not as universal editor doctrine, runtime injection policy, or a requirement to use Cline

## Remaining gaps

- no blocking promotion gap remains as long as the bundle stays centered on bounded fragment-first source authoring
- future review should reject surfaces that are only deterministic assemblers, context compilers, generated reports, runtime injection systems, toggle UIs, or path-trigger mechanisms without the same editable fragment-source layer

## Recommendation

- promote `AOA-T-0030` to `canonical`
- use `AOA-T-0030` as the default instruction-surface technique when agent context or rule guidance should first be split into bounded editable fragments while sibling techniques own deterministic assembly, CI reporting, nested precedence, and runtime loading behavior
