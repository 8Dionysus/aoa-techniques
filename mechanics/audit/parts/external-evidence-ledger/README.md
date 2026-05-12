# External Evidence Ledger

This ledger records the current search memory for external-evidence work over the remaining `promoted` queue.

Use it when the question is not "what is the whole promotion queue?", but "which external lanes have already been checked, what was adjacent-only, and where should the next honest search start?"

This ledger complements [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md), [Promotion Evidence Runbook](../promotion-evidence-runbook/README.md), and [External Evidence Sprint Runbook](../external-evidence-sprint-runbook/README.md).
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
| [AOA-T-0018](../../../../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md) | `aoa-routing` after existing `aoa-skills` and `aoa-evals` downstream use | Markdown-first section surfaces are real `expand` targets in more than one downstream repo. |
| [AOA-T-0013](../../../../techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md) | `dyoshikawa/rulesync` plus `EmberAGI/arbitrum-vibekit` | One-source instruction distribution can survive beyond the donor lineage as a real multi-target pattern. |
| [AOA-T-0034](../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md) | `Truth-Zeeker-AI-Public` | Public-safe sanitization is a real second-consumer surface, not just a prerequisite inside origin repos. |
| [AOA-T-0023](../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md) | GitHub Copilot CLI's programmatic one-prompt fast path | A real shell-side single-shot operator path exists beyond donor documentation and local adaptation. |
| [AOA-T-0028](../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) | GitHub Copilot agent-mode terminal-command confirmation plus GitHub Copilot CLI tool approvals | Public coding-agent surfaces keep mutation behind one explicit operator approval seam instead of hiding it inside generic autonomy. |
| [AOA-T-0031](../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md) | OpenAI Codex CLI `codex exec` | A real stdin/stdout/file-first one-shot operator path exists beyond donor documentation and local adaptation. |
| [AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) | Aider plus committed public `.aider.chat.history.md` artifacts | Local AI coding session capture can survive as a project-visible Markdown artifact beyond the donor product family. |
| [AOA-T-0036](../../../../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md) | Dockform plan/render-before-apply plus masked full Compose render | Effective local runtime truth can be rendered, reviewed, and confirmed before startup without becoming lifecycle, readiness, deployment-preview, or secret-publication authority. |
| [AOA-T-0044](../../../../techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md) | `claude-code-log` | Already-saved session transcripts can survive as portable Markdown review artifacts beyond the donor product family. |
| [AOA-T-0053](../../../../techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md) | `coding-agent-search (cass)` | A local searchable index over already-saved session artifacts can remain derivative, provenance-aware, and local-first beyond the donor product family. |

## Active Lead Ledger

These are the current live external-evidence lanes worth searching next.

| technique | last checked lane | adjacent or insufficient fits already ruled out | exact proof still needed | next honest search shape |
|---|---|---|---|---|
| [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) | repo-local drift and evaluation-report lane plus public agent-markdown CI check/report lane, public prompt-eval CI lane, the 2026-05-12 exemplar sweep over public context-report, token-budget, repo-packing, LLM-ready-docs, and CI reporting surfaces, and the Stage 1 long-pass sweep over public context-compiler, context-drift, fragment-assembly, dependency-graph, and repo-quality report surfaces | local drift reports and composition audits; public instruction-check and workflow-report surfaces such as Continue `/check` and GitHub Agentic Workflows daily repo reports that emit PR checks or activity summaries; Promptfoo CI/CD and `promptfoo-action` surfaces that emit eval JSON or HTML, PR comments, and before/after prompt reports; GitHub Agentic Workflows token/audit reports, Repomix repo-packing and token-count surfaces, Repo Tokens badge-style token counts, `pytest-llm-report`, Calcis prompt cost estimates, `llms-txt-action`, LogicStamp Context, Claude Code Guide context-engineering CI drift detection, ctxloom, Depwire, and FastPace, all of which are adjacent because they own workflow audit, context assembly or compilation, configuration drift, fragment/profile injection, graph context, token/cost monitoring, test or prompt reports, repo-quality/governance reports, or documentation conversion instead of the same CI-facing composition coverage or token-drift artifact | one second public CI-facing report over context composition coverage or token-drift that stays separate from composition mechanics, remediation policy, prompt-quality scoring, generic PR policy checks, context compilers, fragment assemblers, and repo-quality dashboards | search artifact-first public CI or docs-validation repos where an expected source or fragment inventory is compared against an assembled prompt/context artifact and token deltas are emitted as a read-only report, not just as eval matrices, pass or fail gates, token badges, repo-packing outputs, LLM-ready-doc generation, product dashboards, graph compilers, or activity digests |
| [AOA-T-0045](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | public transcript-log export and rich session-view lane | transcript and log review surfaces such as `claude-conversation-extractor` detailed exports and `claude-code-log` preserve tool use, terminal outputs, session summaries, and Markdown or HTML review views, but they still package transcript or log inspection rather than a bounded witness trace with explicit state-delta review notes and a pre-writeback summary posture | one second downstream consumer where a bounded run emits a structured witness trace plus human-readable summary before any writeback, compost, or canon-lift step | search public agent-run review surfaces where step order, tool visibility, state deltas, and a review-first summary survive together as one trace artifact before later memory or promotion layers |

## AOA-T-0032 Exemplar Sprint Notes

2026-05-12 result: no exact-fit second consumer found in the exemplar sweep.
The pass is still useful because it narrows a tempting false-positive band
before the long promotion-evidence pass.

Searched and rejected as adjacent:

- GitHub Agentic Workflows token-budget and audit reports: useful workflow
  audit and token telemetry, but not a context-composition coverage report.
- Repomix: useful repo packing, file summaries, and token-count tree support,
  but the object is context assembly or packing rather than a separate
  read-only CI report over an already-composed context.
- Repo Tokens: useful badge-style repository token count and context-window
  percentage, but no source-coverage or composed-context drift report.
- `pytest-llm-report`: useful test coverage plus LLM annotation/token reports,
  but the object is test reporting and annotation telemetry rather than
  context-composition coverage.
- Calcis: useful prompt-file cost and token estimation, but no source coverage
  and no composed-context report artifact.
- `llms-txt-action`: useful documentation conversion for LLM consumption, but
  it generates LLM-ready docs rather than reporting on composition health.
- OpenAI Codex issue `#2765`: useful public context-window pressure signal,
  but an issue discussion is not a CI-facing report artifact over composed
  context coverage or token drift.

GitHub code search was also attempted for exact phrases around context
composition, source coverage, token drift, and CI report artifacts. It found no
exact-match candidates before rate limiting stopped broader code-search
expansion. Do not treat that rate limit as proof that no public candidate
exists; treat it only as searched-lane memory for this pass.

2026-05-12 Stage 1 long-pass result: no exact-fit second consumer found.
The pass sharpened the false-positive boundary before the matrix-wide
promotion-evidence pass moves beyond the old lead queue.

Searched and rejected as adjacent:

- [LogicStamp Context](https://github.com/LogicStamp/logicstamp-context):
  strong public context compiler and CI-friendly stats / compare surface with
  token estimates, generated `context.json` bundles, and context drift
  validation, but the object is context compilation and validation rather than
  a separate read-only report over an already-composed context's expected
  source coverage plus token drift.
- [Claude Code Guide context-engineering CI drift detection](https://cc.bruniaux.com/guide/context-engineering/):
  useful profile and configuration drift discipline, but the object is
  regenerated instruction configuration freshness rather than a
  context-composition coverage artifact.
- [ctxloom](https://ctxloom.dev/): useful fragment/profile assembly, remote
  sync, and token optimization surface, but it owns assembly and injection
  rather than an independent CI report observing a composed artifact.
- [Depwire](https://depwire.dev/): useful graph context, impact analysis,
  generated docs, and CI-ready JSON for code health signals, but not a
  composed-context source-coverage and token-drift report.
- [FastPace](https://fastpace.net/): useful read-only
  repo-quality/context-score and governance reporting, but the object is
  repository quality, audit, and guardrail posture rather than CI-facing
  composition coverage.

Next honest search shape: look for artifact-first public docs-validation or
prompt-build workflows that commit or publish a CI report comparing expected
source or fragment inventories against generated prompt/context artifacts plus
token deltas.

Previous next-shape wording: look for public docs-validation or prompt-build
workflows that emit an artifact comparing expected prompt/context fragments
against the assembled artifact plus token drift, while leaving assembly,
scoring, and remediation to other surfaces.

## AOA-T-0026 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0026` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- Aider's public options reference documents a default `.aider.chat.history.md`
  chat-history file.
- Aider's public configuration docs make git-root configuration a normal
  project-scoped shape.
- Aider's public FAQ treats `.aider.chat.history.md` as Markdown chat logs that
  can be copied into a gist or otherwise published as raw Markdown.
- GitHub code search found committed `.aider.chat.history.md` artifacts in
  public non-fork repositories, including `launchapp-dev/animus-cli`,
  `terraphim/terraphim-ai`, and
  `CEDARScript/cedarscript-llm-prompt-engineering`.

Rejected as still adjacent:

- Aider's release history also documents `.aider*` gitignore behavior, so
  ignored local tool state is not enough by itself.
- Session browsers, resume databases, local search products, transcript
  packaging tools, and cloud-history wrappers remain sibling or adjacent lanes
  unless the saved session itself is a project-visible artifact.

Future watch shape: keep distinguishing deliberate project-visible session
artifacts from accidental raw-log commits and ignored local tool history.

## AOA-T-0036 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0036` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- Dockform documents `plan` before `apply`, so the operator sees the planned
  service/config change before Docker Compose startup is invoked.
- Dockform documents `compose render` as a fully resolved Docker Compose config
  render, with secrets masked by default unless explicitly shown.
- Dockform source builds and prints the plan before confirmation, then applies
  the already-built plan; its Docker Compose wrapper renders services, config
  hashes, full config JSON, and raw resolved YAML before `docker compose up -d`.

Rejected as still adjacent:

- Plain `docker compose config`, `docker compose config --services`, and Docker
  Compose `alpha dry-run` expose useful render or simulation primitives, but do
  not by themselves establish the operator review seam.
- Helm `template`, Kustomize build, Skaffold render, deployment previews, and
  generic dry-run surfaces render manifests or deployment plans, but drift into
  deployment-preview authority unless they center local runtime truth review.
- `OpenDAX`-style config-before-startup lanes, Devcontainer
  `read-configuration`, runtime utility pages, and Docker validation checklists
  expose resolved configuration or service lists, but the object is readiness,
  validation, or utility support rather than a distinct pre-start review
  contract.

Future watch shape: keep `AOA-T-0036` centered on the rendered-truth review seam
and route lifecycle control, host readiness, deployment preview, and benchmark
comparison back to their sibling techniques.

## Deferred Pack Watch

These bundles still need external evidence, but no new bounded lane note is worth recording here yet beyond the current queue docs.

| technique | current blocker | next honest trigger |
|---|---|---|
| [AOA-T-0020](../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md) | still needs one second markdown-first corpus beyond the current donor family | one committed non-eval corpus that reuses typed note-kind and note-path provenance |
| [AOA-T-0005](../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md) | remains a long-gap donor lane, not an active sprint target | one non-origin rollout record proving the same checklist on a real new-intent extension path |
| [AOA-T-0022](../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md) | remains a long-gap donor lane, not an active sprint target | one second committed corpus using the exact five-part `Risks` split |

## Notes

- Use [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md) for the full queue and lane counts.
- Use [External Evidence Sprint Runbook](../external-evidence-sprint-runbook/README.md) for execution order and operator rules.
- When a bundle exits the queue, keep the closure precedent here short and move the real verdict back into the bundle-local notes plus shared queue docs.
