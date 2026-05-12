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
| [AOA-T-0038](../../../../techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md) | Metaflow Devstack | One local operator entrypoint can select services, resolve dependencies, start the local stack, wait through follow-through, expose the operator shell path, and tear the stack down without becoming generic launcher doctrine. |
| [AOA-T-0039](../../../../techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | LOCOMO / OpenClaw benchmark harness | Baseline and additive profile backends can reuse the same corpus, runner, artifact family, parallel path, and summary surface without turning comparison into product scoring or benchmark governance. |
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

## AOA-T-0005 Stage 2 Long-Pass Notes

2026-05-12 result: no exact-fit second consumer found.
The pass moved `AOA-T-0005` out of "not yet actively searched" posture and
recorded the first durable adjacent-lane boundary for the long-gap donor row.

Searched and rejected as adjacent:

- GitHub code search for `expected_intent_type`, `new intent`, `intent_type`
  plus dry-run / contract / fixture phrases found public intent-classification
  and intent-benchmark surfaces, but no non-origin rollout record with the
  full checklist shape.
- [PRISM Monitor `InstructionRF/data/README.md`](https://github.com/PRISM-System/PRISM-Monitor/blob/f8680e27bb7e4b3494d9c3a17d3f704a41842b17/InstructionRF/data/README.md):
  useful manufacturing intent-classification dataset with expected intent and
  priority labels, but it is an evaluation dataset rather than a one-new-intent
  extension through an existing dry-run chain.
- [ARTE Chatbot `evaluation/intent_eval/run_eval.py`](https://github.com/creep1ng/arte-chatbot/blob/c0f20b994bba4ee8d63acaa86f5c8044d8e220b1/evaluation/intent_eval/run_eval.py):
  useful `intent_type` classification harness with saved results and accuracy
  thresholds, but the object is classifier evaluation against annotated
  queries, not a rollout checklist with fixture, smoke, contract summary,
  published review row, and regression coverage for one new intent path.
- [CS4730 IBN `experiments/run_benchmarks.py`](https://github.com/siddu1324/cs4730-IBN/blob/191704ab4ce680e7b700867ce9e8ac99c6286f75/experiments/run_benchmarks.py):
  useful intent-based networking benchmark that compares translators,
  guardrails, policy rendering, and simulation outcomes against expected
  intent types, but it is a benchmark/evaluation lane rather than a bounded
  rollout record for adding one new intent to a shared chain.
- [Rasa testing docs](https://legacy-docs-oss.rasa.com/docs/rasa/next/testing-your-assistant/):
  useful assistant validation, test-story, NLU evaluation, and CI guidance, but
  it validates conversation and NLU behavior after authoring rather than
  recording a dry-run chain extension checklist.
- [Botpress ADK eval docs](https://botpress.com/docs/adk/testing/evals):
  useful conversation eval, tool assertion, workflow assertion, and regression
  tagging shape, but it is an eval runner surface rather than a new-intent
  rollout artifact.

Next honest search shape: look for a public repository where an existing
intent-to-plan or intent-to-action chain records the addition of exactly one
new intent with a canonical fixture, dedicated smoke run, strict expected
intent routing check, machine-readable summary, visible review artifact, and
regression proof. Do not reopen generic chatbot NLU, intent-classification, or
IBN benchmark lanes without a new rollout-specific signal.

## AOA-T-0022 Stage 2 Long-Pass Notes

2026-05-12 result: no exact-fit second corpus found.
The pass moved `AOA-T-0022` beyond the seeded `aoa-skills` donor and recorded
which tempting public risk lanes are adjacent rather than closure evidence.

Searched and rejected as adjacent:

- GitHub code search for the exact heading family `Failure modes`, `Negative
  effects`, `Misuse patterns`, `Detection signals`, and `Mitigations` found no
  public non-AoA repository candidates.
- Workspace search across sibling owner repositories found only the already
  recorded `aoa-skills/skills/risk/aoa-sanitized-share/SKILL.md` exact donor;
  `aoa-evals` uses `Failure modes` plus `Blind spots`, and `aoa-agents` service
  certification uses a narrower `Failure modes` section, so both remain
  adjacent contrast rather than the same five-part caution split.
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/):
  useful open security-risk taxonomy with mitigations around LLM application
  vulnerabilities, but it is a vulnerability/governance framework rather than
  a markdown-first caution section attached to reusable method bundles.
- [Microsoft taxonomy of failure modes in AI agents](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/):
  useful failure-mode taxonomy with harm categories, effects, mitigations, and
  detection/response opportunities, but it is a broad threat-modeling and
  defensive strategy surface rather than the exact five authored caution
  headings.
- [Microsoft autonomous agentic AI risk guidance](https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk):
  useful agentic-risk design, security, governance, monitoring, and misuse
  guidance, but it organizes risks by design/security pillars rather than by
  the five markdown caution distinctions.
- [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10):
  useful cross-sector AI risk-management framework, but it is intentionally
  use-case agnostic and governance-oriented rather than a committed reusable
  corpus with the exact five-part `Risks` contract.

Next honest search shape: look for a committed public or sibling corpus where
authored reusable method, skill, playbook, or evaluation bundles use the exact
five headings together as their risk section. Do not count broad AI safety,
security taxonomy, governance framework, or `Failure modes` plus `Blind spots`
surfaces unless they actually adopt the same five-part markdown contract.

## AOA-T-0035 Stage 2 Long-Pass Notes

2026-05-12 result: no exact-fit second consumer found.
The pass moved `AOA-T-0035` out of pending Pack 3 posture and recorded the
first durable adjacent-lane boundary for profile, preset, module, and
composition lookalikes.

Searched and rejected as adjacent:

- GitHub code search for exact combinations around `preset`, `profile`,
  `module`, `resolved`, `dedupe`, `first appearance`, `--list-profiles`, and
  `--list-presets` found no public non-origin candidate carrying the full
  three-layer composition contract.
- [Docker Compose profiles](https://docs.docker.com/compose/how-tos/profiles/):
  useful service-profile activation and environment selection, but the object
  is service gating inside a Compose application rather than a separate
  module -> profile -> preset contract with preset-first profile expansion and
  read-only inspection as the technique center.
- [SoS report plugin profiles and policy presets](https://sos.readthedocs.io/en/main/plugins.html)
  plus [`sos report` preset/profile options](https://manpages.ubuntu.com/manpages/bionic/man1/sosreport.1.html):
  useful adjacent vocabulary where plugins belong to profiles and presets
  store option sets, but the preset layer is an option/default set rather than
  an ordered profile bundle that expands to deduped modules before launch.
- [VS Code Profiles](https://code.visualstudio.com/docs/configure/profiles):
  useful named editor configuration sets that can be switched, exported, and
  imported, but they are complete profile states rather than an explicit
  module -> profile -> preset layering contract.
- [Dev Container Features](https://containers.dev/features) and
  [Templates](https://containers.dev/templates): useful reusable environment
  building blocks and starter packages, but the public object is feature or
  template selection rather than ordered preset expansion over profiles.
- [Kustomize bases and overlays](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/):
  useful declarative composition, resource assembly, and overlay reuse, but it
  is Kubernetes configuration customization rather than profile/preset runtime
  posture composition with the same dedupe and inspection rule.

Next honest search shape: look for a public runtime or tool repository where
small modules are grouped into ordered profiles, named presets are ordered
profile bundles, preset-expanded profiles resolve before direct profiles,
duplicate profiles and modules are kept once at first appearance, and a
read-only command or artifact shows the resolved profiles/modules before
startup. Do not count profile-only systems, editor profiles, option presets,
templates, overlays, or generic config renderers unless they carry the same
layer contract.

## AOA-T-0037 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0037` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- [Get Physics Done README](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/README.md)
  documents `gpd doctor --runtime <runtime> --local` and
  `gpd doctor --runtime <runtime> --global` as runtime-readiness checks for a
  selected runtime target, and keeps paper/manuscript readiness warnings
  distinct from `paper-build` truth.
- [GPD CLI doctor command](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/src/gpd/cli.py)
  routes `doctor --runtime` into runtime-readiness mode with normalized
  runtime, install scope, target directory, and optional live executable
  probes.
- [GPD health implementation](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/src/gpd/core/health.py)
  resolves runtime, scope, and target into one doctor context, checks
  runtime-specific launcher/target/provider/toolchain surfaces, returns
  `mode="runtime-readiness"` for selected runtime checks, and separates
  failures from warnings.
- [GPD installer preflight](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/bin/install.js)
  consumes the structured doctor report, treats `fail` checks as blockers,
  preserves advisories, and points the operator back to the exact selected
  `gpd doctor --runtime ...` command before continuing.

Rejected as still adjacent:

- Generic `doctor` commands such as package-manager, framework, editor, or
  project-health diagnostics remain adjacent unless the selected runtime,
  profile, preset, target, or equivalent selector changes which checks matter.
- Permission gates, unattended-readiness validators, plan preflight, build
  checks, smoke tests, and monitoring dashboards remain sibling surfaces unless
  they preserve the same selected-target pre-start diagnostic seam.

Future watch shape: keep `AOA-T-0037` centered on selected-target doctor
readiness with item-level severity, and route render truth, lifecycle,
permission alignment, plan validation, build truth, smoke, and monitoring back
to their sibling techniques or owner repos.

## AOA-T-0038 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0038` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- [Metaflow Devstack README](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/README.md)
  documents a local Kubernetes development stack with `make up`, `make
  all-up`, `SERVICES_OVERRIDE=... make up`, `make shell`, and `make down`;
  service selection and dependency resolution stay inside the devstack
  lifecycle contract.
- [Metaflow Devstack Makefile](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/Makefile)
  keeps Docker checks, local tool setup, service selection or override,
  Minikube tunnel startup, Tilt startup, operator next steps, shell handoff,
  and teardown under one bounded local lifecycle surface.
- [Metaflow service picker](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/pick_services.sh)
  supports interactive service selection and a default all-services path while
  preserving one lifecycle entrypoint.
- [Metaflow non-TUI devstack start path](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/ci/start-devstack.sh)
  starts the local stack without the Tilt TUI and waits for API, Tiltfile, and
  generated config readiness before handing control onward.

Rejected as still adjacent:

- Generic launchers, install wizards, plain Docker Compose `up`/`down`, and
  Kubernetes or Tilt documentation remain adjacent unless one repo-owned local
  lifecycle contract owns startup, follow-through, and teardown for a bounded
  stack.
- Readiness checks, render previews, smoke tests, and benchmark harnesses
  remain sibling surfaces unless their entrypoint also owns the bounded local
  lifecycle.

Future watch shape: keep `AOA-T-0038` centered on operator-triggered local
stack lifecycle, and route profile composition, rendered truth, readiness
diagnosis, smoke testing, and benchmark comparison back to sibling techniques.

## AOA-T-0039 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0039` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- [LOCOMO / OpenClaw README](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/README.md)
  names `memory-core` as the baseline backend, compares `memory-lancedb` and
  `memory-lancedb-pro` as additive backends, and keeps all three on the same
  LOCOMO benchmark output family.
- [LOCOMO runner](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/src/runner.py)
  writes the same run artifacts and summary shape across backend scripts.
- [LOCOMO parallel runner](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/scripts/run_parallel.py)
  preserves the same output contract while enabling parallel benchmark
  execution.
- [LOCOMO result summarizer](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/scripts/summarize_results.py)
  reads the shared `summary.json` family and renders comparable results across
  baseline and additive runs.

Rejected as still adjacent:

- Benchmark matrices, A/B tests, product leaderboards, rolling baseline gates,
  and regression dashboards remain adjacent unless the baseline-first and
  additive paths share the same measurement surface and artifact shape.
- Baseline fixtures or Criterion-style performance history remain adjacent
  unless additive profiles are explicitly compared against the same baseline
  profile without mutating the default path.

Future watch shape: keep `AOA-T-0039` centered on stable baseline-first
comparison discipline, and route benchmark-suite governance, promotion policy,
rolling regression gates, product scoring, profile composition, and lifecycle
control to their owning techniques or repos.

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
| [AOA-T-0005](../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md) | Stage 2 checked intent-classification, chatbot eval, and IBN benchmark lanes; they remain adjacent because they evaluate intents rather than recording one-new-intent dry-run-chain rollout | one non-origin rollout record proving the same checklist on a real new-intent extension path |
| [AOA-T-0022](../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md) | Stage 2 checked exact-heading public code search, sibling corpus search, and broad AI risk/framework lanes; they remain adjacent unless the exact five-part markdown contract is present | one second committed corpus using the exact five-part `Risks` split |

## Notes

- Use [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md) for the full queue and lane counts.
- Use [External Evidence Sprint Runbook](../external-evidence-sprint-runbook/README.md) for execution order and operator rules.
- When a bundle exits the queue, keep the closure precedent here short and move the real verdict back into the bundle-local notes plus shared queue docs.
