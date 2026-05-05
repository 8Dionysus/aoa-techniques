# Canonical Readiness

## Technique
- id: AOA-T-0028
- name: confirmation-gated-mutating-action

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around stateless-shell invariants, generic caution prose, and broader orchestration breadth
- second context: GitHub Copilot's public coding-agent docs now provide an independent confirmation-gated mutation seam across both CLI tool approvals and agent-mode terminal-command confirmation
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one real public second context beyond the donor lineage, so the confirmation boundary is no longer proven only by imported documentation

## Default-use rationale
- this is the right promoted default when a workflow must cross from read or plan into mutation only after one explicit confirmation seam
- it remains distinct from `AOA-T-0023`, which stays centered on a stateless single-shot shell fast path rather than the confirmation boundary itself
- it remains narrower than `AOA-T-0001`, which stays the default workflow backbone for multi-step repository work that needs planning, verification, and reporting across more than one step
- the current evidence now shows that the explicit confirmation-before-mutation seam survives in an independent public coding-agent family, so the bundle reads as the natural default when mutation must stay visibly gated instead of being implied by a broader fast path or workflow

## Fresh public-safety check
- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable confirmation boundary and excludes donor-specific configuration, workspace-trust policy, session-wide approval breadth, and broader workflow ceremony
- public reuse check: the public examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on one explicit operator confirmation before a bounded mutation
- future review should keep watching for drift into generic approval policy, weak caution prompts, or multi-step governed workflows that belong to sibling techniques instead

## Recommendation
- promote `AOA-T-0028` to `canonical`
- use `AOA-T-0028` as the default mutation-gating technique when read or plan work must pause behind one explicit confirmation seam before a bounded write or command execution step
