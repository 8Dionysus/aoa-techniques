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
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | GitHub Copilot agent-mode terminal-command confirmation plus GitHub Copilot CLI tool approvals | Public coding-agent surfaces keep mutation behind one explicit operator approval seam instead of hiding it inside generic autonomy. |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | OpenAI Codex CLI `codex exec` | A real stdin/stdout/file-first one-shot operator path exists beyond donor documentation and local adaptation. |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | `claude-code-log` | Already-saved session transcripts can survive as portable Markdown review artifacts beyond the donor product family. |
| [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md) | `coding-agent-search (cass)` | A local searchable index over already-saved session artifacts can remain derivative, provenance-aware, and local-first beyond the donor product family. |

## Active Lead Ledger

These are the current live external-evidence lanes worth searching next.

| technique | last checked lane | adjacent or insufficient fits already ruled out | exact proof still needed | next honest search shape |
|---|---|---|---|---|
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | repo-local drift and evaluation-report lane plus public agent-markdown CI check/report lane and public prompt-eval CI lane | local drift reports and composition audits; public instruction-check and workflow-report surfaces such as Continue `/check` and GitHub Agentic Workflows daily repo reports that emit PR checks or activity summaries; Promptfoo CI/CD and `promptfoo-action` surfaces that emit eval JSON or HTML, PR comments, and before/after prompt reports instead of the same CI-facing composition coverage or token-drift artifact | one second public CI-facing report over context composition coverage or token-drift that stays separate from composition mechanics, remediation policy, prompt-quality scoring, and generic PR policy checks | search public CI or docs-validation repos where assembled prompt or multi-fragment context coverage and token budgets are emitted as a read-only artifact, not just as eval matrices, pass or fail gates, or activity digests |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | repo-local witness, checkpoint, and history-adjacent lane plus public local session-store and session-browser/search lane | witness traces, transcript packaging, memory or recall systems, cloud-history wrappers, proposal-only surfaces such as OpenAI Codex issue `#2765`, GitHub Copilot CLI session-state storage under `~/.copilot/session-state/` plus a local SQLite session store that powers resume, `/chronicle`, and history Q&A, and local-first browser/search tools such as Agent Sessions, `cxresume`, `aichat`, and `coding_agent_session_search` that browse home-directory session logs, workspace pointer files, or unified local indexes rather than project-scoped repo artifacts | one second public repo-local session capture surface where history is kept as a reviewable project artifact rather than a memory product, search UI, or home-directory session store | search public repos and tools that write AI session history into versionable workspace directories or repo-visible artifact trees without adding search, recall, or instruction authority as the primary value proposition |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | repo-local runtime and lifecycle lane plus public compose prestart-render lane and public render-before-apply/template lane | lifecycle wrappers, readiness-only checks, config rendering without a real pre-start review seam, `OpenDAX`-style config-before-startup surfaces, CoreMedia's public `docker compose config --services` prestart step backed by Docker Compose config docs, Docker Compose `config` and experimental `alpha dry-run`, and Helm `template`; these lanes prove useful rendering or simulation before apply or startup, but not yet a distinct render-review contract over effective local runtime truth | one second public runtime surface where effective composed truth is rendered and explicitly reviewed before startup as its own safety seam | search operator repos where render output is a named pre-start review step over actual resolved runtime state, not just a template render, deployment preview, or dry-run helper before `up` or install |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | public transcript-log export and rich session-view lane | transcript and log review surfaces such as `claude-conversation-extractor` detailed exports and `claude-code-log` preserve tool use, terminal outputs, session summaries, and Markdown or HTML review views, but they still package transcript or log inspection rather than a bounded witness trace with explicit state-delta review notes and a pre-writeback summary posture | one second downstream consumer where a bounded run emits a structured witness trace plus human-readable summary before any writeback, compost, or canon-lift step | search public agent-run review surfaces where step order, tool visibility, state deltas, and a review-first summary survive together as one trace artifact before later memory or promotion layers |

## Deferred Pack Watch

These bundles still need external evidence, but no new bounded lane note is worth recording here yet beyond the current queue docs.

| technique | current blocker | next honest trigger |
|---|---|---|
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | still needs one second markdown-first corpus beyond the current donor family | one committed non-eval corpus that reuses typed note-kind and note-path provenance |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | remains a long-gap donor lane, not an active sprint target | one non-origin rollout record proving the same checklist on a real new-intent extension path |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | remains a long-gap donor lane, not an active sprint target | one second committed corpus using the exact five-part `Risks` split |

## Notes

- Use [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md) for the full queue and lane counts.
- Use [External Evidence Sprint Runbook](EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md) for execution order and operator rules.
- When a bundle exits the queue, keep the closure precedent here short and move the real verdict back into the bundle-local notes plus shared queue docs.
