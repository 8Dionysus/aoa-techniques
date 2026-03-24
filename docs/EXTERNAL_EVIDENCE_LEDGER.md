# External Evidence Ledger

This ledger records the current search memory for external-evidence work over the remaining `promoted` queue.

Use it when the question is not "what is the whole promotion queue?", but "which external lanes have already been checked, what was adjacent-only, and where should the next honest search start?"

This ledger complements [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md), [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md), and [External Evidence Sprint Runbook](EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md).
It does not replace bundle-local `notes/`.

## Recording Rules

- log only real searched lanes, not hopeful ideas
- record adjacent fits when they would otherwise tempt a later false-positive rerun
- keep exact-fit closure notes short and point back to the bundle-local evidence when that becomes the real source
- expand this ledger when a new lane search happens or a bundle exits the queue

## Recent Closure Precedents

These are the most useful recent examples of what honest queue closure looked like.

| technique | closure surface | what it proved |
|---|---|---|
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | `aoa-routing` after existing `aoa-skills` and `aoa-evals` downstream use | Markdown-first section surfaces are real `expand` targets in more than one downstream repo. |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `dyoshikawa/rulesync` plus `EmberAGI/arbitrum-vibekit` | One-source instruction distribution can survive beyond the donor lineage as a real multi-target pattern. |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) | `Truth-Zeeker-AI-Public` | Public-safe sanitization is a real second-consumer surface, not just a prerequisite inside origin repos. |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | GitHub Copilot CLI's programmatic one-prompt fast path | A real shell-side single-shot operator path exists beyond donor documentation and local adaptation. |

## Active Lead Ledger

These are the current live external-evidence lanes worth searching next.

| technique | last checked lane | adjacent or insufficient fits already ruled out | exact proof still needed | next honest search shape |
|---|---|---|---|---|
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | repo-local drift and evaluation-report lane plus public near-fit report surfaces | local drift reports and composition audits; public context-audit or snapshot surfaces such as `AgentBible` and `AgentRules Architect` that inspect context but do not emit the same CI-facing read-only artifact | one second public CI-facing report over context composition coverage or token-drift that stays separate from composition mechanics and remediation policy | search public CI or docs-validation repos where context composition health is emitted as a reviewable artifact, not as the engine itself |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | repo-local witness, checkpoint, and history-adjacent lane plus public proposal-class session-history surfaces | witness traces, transcript packaging, memory or recall systems, cloud-history wrappers, and proposal-only surfaces such as OpenAI Codex issue `#2765` | one second public repo-local session capture surface where history is kept as a reviewable project artifact rather than a memory product | search public repos that persist AI session history into versionable artifacts without adding search, recall, or instruction authority |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | repo-local runtime and lifecycle lane plus public config-publication near fits | lifecycle wrappers, readiness-only checks, config rendering without a real pre-start review seam, and `OpenDAX`-style config-before-startup surfaces that do not expose the same bounded render-review contract | one second public runtime surface where effective composed truth is rendered and reviewed before startup | search operator repos where declared config and effective runtime state can diverge enough that pre-start render review is a real safety seam |

## Deferred Pack Watch

These bundles still need external evidence, but no new bounded lane note is worth recording here yet beyond the current queue docs.

| technique | current blocker | next honest trigger |
|---|---|---|
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | still needs one public confirmation-gated mutation seam beyond donor plus adaptation | one public workflow surface where explicit confirmation really gates mutation in practice |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | still needs one public shell-composable one-shot operator path beyond donor plus adaptation | one public workflow surface where stdin, stdout, files, or pipes stay first-class operator seams |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | still needs one second markdown-first corpus beyond the current donor family | one committed non-eval corpus that reuses typed note-kind and note-path provenance |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | remains a long-gap donor lane, not an active sprint target | one non-origin rollout record proving the same checklist on a real new-intent extension path |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | remains a long-gap donor lane, not an active sprint target | one second committed corpus using the exact five-part `Risks` split |

## Notes

- Use [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md) for the full queue and lane counts.
- Use [External Evidence Sprint Runbook](EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md) for execution order and operator rules.
- When a bundle exits the queue, keep the closure precedent here short and move the real verdict back into the bundle-local notes plus shared queue docs.
