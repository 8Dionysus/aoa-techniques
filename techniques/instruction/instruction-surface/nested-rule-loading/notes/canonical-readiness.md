# Canonical Readiness

## Technique
- id: AOA-T-0029
- name: nested-rule-loading

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around MCP propagation, skills propagation, installer breadth, and other product-width detail
- exact-fit second context: Claude Code documentation proves a real layered instruction hierarchy through scoped `CLAUDE.md` locations, directory-walk loading, subdirectory on-demand loading, `.claude/rules/`, and explicit priority ordering for broader versus more specific instruction layers
- external review: the first import review passed, and the Claude Code pass confirms the hierarchy-plus-precedence contract survives without importing donor CLI breadth, multi-target propagation, MCP behavior, skill propagation, or installer policy
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, exact-fit public second-context evidence, and an adverse-effects review

## Default-use rationale
- this is the right canonical default when a repository needs hierarchical rule layers with explicit precedence and one-way ownership
- it remains narrower than `AOA-T-0013`, which keeps the broader one-canonical-rule-source-to-many-managed-targets instruction-surface distribution story in focus
- it stays distinct from `AOA-T-0027`, which is about managed-target propagation of a shared skill or rule core rather than nested loading
- Claude Code confirms that the move can survive outside the donor even when implementation is a live agent-product instruction loader rather than a standalone rule-distribution tool

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps the reusable nested-loading contract and excludes donor-specific orchestration behavior
- public reuse check: the examples, checklist, adaptation notes, and Claude Code evidence remain understandable without hidden donor-repo context
- public-safety boundary: Claude Code details are cited only as evidence of hierarchical loading and priority ordering, not as universal Claude memory doctrine, hidden prompt control, path-specific product endorsement, or a requirement to use Claude Code

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on hierarchical rule loading with explicit, reviewable precedence
- future review should reject surfaces that are only generic file imports, fragment organization, target fan-out, config generation, runtime injection, or product memory systems without the same parent/nested rule hierarchy and precedence seam

## Recommendation
- promote `AOA-T-0029` to `canonical`
- use `AOA-T-0029` as the default instruction-surface technique when parent and nested rule layers must resolve through explicit precedence while sibling techniques own multi-target distribution, managed skill propagation, fragment-first authoring, and upstream mirroring
