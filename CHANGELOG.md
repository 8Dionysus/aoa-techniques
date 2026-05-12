# Changelog

All notable changes to `aoa-techniques` will be documented in this file.

The format is intentionally simple and human-first.

## [Unreleased]

### Added

- promoted `AOA-T-0101 local-pattern-adoption-gate` from the Method-growth
  pattern-adoption part as one atomic guardrail before durable local adoption
- promoted `AOA-T-0102 skill-proposal-handoff-packet` from the Method-growth
  technique-to-skill handoff part as one atomic proposal packet that does not
  imply skill acceptance or activation
- promoted `AOA-T-0103 adopted-practice-retention-review` from the Method-growth
  retention-checks part as one atomic post-adoption review before keeping a
  practice active
- promoted `AOA-T-0104 superseded-practice-obsolescence-route` from the
  Method-growth obsolescence part as one atomic owner-aware route packet before
  supersession, merge, reanchor, defer, drop, or deprecation review

### Changed

- promoted `AOA-T-0066 transcript-replay-artifact` to `canonical` after
  `dataprofessor/cortex-replay` and Snowflake's public Cortex Code replay
  guide showed exact-fit public reinforcement for transforming already-saved
  AI coding session transcripts into one self-contained replay artifact with
  explicit session selection, direct transcript input, turn/time filtering,
  playback/bookmark/visibility controls, and secret redaction, while excluding
  first-save capture, transcript packaging, local indexing, witness tracing,
  hosted sharing, dashboards, replay editors, memory doctrine, and
  replay-as-proof claims, updating Audit queue posture from `53` promoted
  techniques to `52`
- promoted `AOA-T-0065 mcp-gateway-proxy` to `canonical` after
  `smart-mcp-proxy/mcpproxy-go` showed exact-fit public reinforcement for one
  MCP client endpoint over multiple configured upstream MCP servers, connected
  tool metadata indexing, server-scoped tool names, mediated `call_tool_*`
  variants with explicit intent fields, and sensitive-data inspection over
  tool-call arguments and responses at the proxy boundary, while excluding
  routing-mode policy, BM25 ranking, quarantine governance, Docker isolation,
  lifecycle management, UI/dashboard behavior, OAuth, registry publication,
  marketplace curation, and enterprise MCP platform doctrine, updating Audit
  queue posture from `54` promoted techniques to `53`
- promoted `AOA-T-0064 capability-discovery` to `canonical` after Nacos's
  A2A Registry guide showed exact-fit public reinforcement for bounded lookup
  over already-published AgentCards: SDK lookup by name, HTTP detail lookup
  with `namespaceId` and `agentName`, list search with `pageNo`, `pageSize`,
  `agentName`, `namespaceId`, and `search=blur`, plus skill/tag/description
  filtering kept as a future search dimension rather than silently imported,
  while excluding publication, endpoint subscription, A2A invocation, ranking,
  trust policy, registry console/product behavior, marketplace curation, graph
  semantics, and registry governance, updating Audit queue posture from `55`
  promoted techniques to `54`
- promoted `AOA-T-0063 versioned-agent-registry-contract` to `canonical`
  after Nacos's A2A Registry guide showed exact-fit public reinforcement for
  named versioned AgentCard registry entries with namespace/name identity,
  unique versions, a current default published version, SDK and HTTP
  publication paths, and explicit AgentCard fields including name,
  description, URL, version, and protocol version, while excluding discovery
  ranking, fuzzy search, endpoint subscription, A2A invocation, registry
  console/product behavior, trust policy, marketplace curation, graph
  semantics, and registry governance, updating Audit queue posture from `56`
  promoted techniques to `55`
- promoted `AOA-T-0062 episode-bounded-agent-loop` to `canonical` after
  Cloudflare's long-running Agents guide showed exact-fit public reinforcement
  for durable plan steps, checkpoint recovery, one-step-at-a-time execution,
  next-step scheduling after completion, failed-step state, re-planning, and
  human oversight boundaries, while excluding Durable Objects, Workers,
  schedules, fibers, Workflows, sub-agent RPC, runtime context compression,
  proof settlement, supervision, budgeting, and full autonomous-agent
  lifecycle governance, updating Audit queue posture from `57` promoted
  techniques to `56`
- promoted `AOA-T-0061 cross-repo-resource-map-bootstrap` to `canonical`
  after `calltelemetry/openclaw-linear-plugin` showed exact-fit public
  reinforcement for a multi-repo dispatch map: configured repo keys and paths,
  issue or label selected repo sets, named per-repo worktree paths, injected
  project context, and first-read `CLAUDE.md` / `AGENTS.md` guidance before
  coding or auditing, while excluding issue-routing, model selection, worktree
  lifecycle, audit loops, semantic context maps, infrastructure inventories,
  and full workspace-platform governance, updating Audit queue posture from
  `58` promoted techniques to `57`
- promoted `AOA-T-0060 session-opening-ritual-before-work` to `canonical`
  after `anthropics/cwc-long-running-agents` showed exact-fit public
  reinforcement for reading `PROGRESS.md` before any work, then checking recent
  git history and a smoke/build/test baseline before mutation, while excluding
  handoff authoring, detailed git-claim verification, task routing, universal
  startup test doctrine, evaluator loops, and full long-running-harness
  governance, updating Audit queue posture from `59` promoted techniques to
  `58`
- recorded the 2026-05-12 Pack 16 evidence pass for `AOA-T-0059
  git-verified-handoff-claims`; `confab-framework`, LifeOS handoff-pack,
  `session-handoff`, Mimir handoff-context, SLOPE compaction handoffs, and
  `cwc-long-running-agents` were logged as adjacent or partial rather than
  canonical proof, so the bundle remains `promoted` and Audit queue counts stay
  unchanged
- recorded the 2026-05-12 Pack 15 evidence pass for `AOA-T-0058
  receipt-confirmed-handoff-packet`; `cmux` request ACKs, Gas Town handoff
  mail/session cycling/escalation ACKs, and exact phrase GitHub code-search
  lanes were logged as adjacent rather than canonical proof, so the bundle
  remains `promoted` and Audit queue counts stay unchanged
- promoted `AOA-T-0057 structured-handoff-before-compaction` to `canonical`
  after `anthropics/cwc-long-running-agents` showed exact-fit public
  reinforcement for a structured `PROGRESS.md` read before restart and kept
  current across long-running sessions, with `openclaw-memory-kit` supporting
  the compaction-specific `memory/handoff.md` flush-before-compression and
  bootstrap-read path, while excluding transcript packaging, mailbox receipt,
  git verification, memory search, hook policy, cron memory, and full
  long-running-harness doctrine, updating Audit queue posture from `60`
  promoted techniques to `59`
- promoted `AOA-T-0056 channelized-agent-mailbox` to `canonical` after
  `mycel` showed exact-fit public reinforcement for an AI-agent mailbox with
  thread identity, replayable thread logs, sync cursor, local outbox retry,
  read/delivery state, and explicit local ACK rows, while keeping ACK semantics
  distinct from remote delivery proof and excluding handoff authorization,
  transcript history, trust policy, encryption, adapters, and full
  messaging-platform doctrine, updating Audit queue posture from `61` promoted
  techniques to `60`
- promoted `AOA-T-0055 requirements-design-tasks-ladder` to `canonical`
  after SpecForge-Agent showed exact-fit public reinforcement for a
  requirements -> design -> tasks planning ladder before implementation, with
  GitHub Spec Kit used as a supporting boundary check while excluding full SDD,
  command, approval, agent-platform, memory, and execution doctrine, updating
  Audit queue posture from `62` promoted techniques to `61`
- promoted `AOA-T-0054 compaction-resilient-skill-loading` to `canonical`
  after Claude Code's official skills lifecycle showed exact-fit public
  post-compaction skill reattachment and re-invocation from canonical skill
  sources, updating Audit queue posture from `63` promoted techniques to `62`
- promoted `AOA-T-0051 commit-triggered-background-review` and `AOA-T-0052
  review-findings-compaction` to `canonical` after Qodo / PR-Agent showed
  exact-fit public push-triggered review updates, persistent review comments,
  visible findings, incremental update behavior, and per-commit findings
  added/resolved audit trail, updating Audit queue posture from `65` promoted
  techniques to `63`
- promoted `AOA-T-0049 dependency-aware-task-graph` and `AOA-T-0050
  ready-work-from-blocker-graph` to `canonical` after Taskwarrior showed
  exact-fit public dependency, blocked / blocking, unblocked, cycle-prevention,
  and prerequisite-completion behavior, updating Audit queue posture from `67`
  promoted techniques to `65`
- promoted `AOA-T-0033 decision-rationale-recording` to `canonical` after
  Markdown Architectural Decision Records showed an exact-fit public
  one-decision record pattern with context/problem, considered options, chosen
  outcome with justification, and accepted consequences, updating Audit queue
  posture from `68` promoted techniques to `67`
- promoted `AOA-T-0045 witness-trace-as-reviewable-artifact` to
  `canonical` after Maida / AgentDbg showed an exact-fit public trace-artifact
  contract with local `run.json`, ordered `events.jsonl`, LLM/tool/error/state
  events, redaction/truncation, and a human-readable timeline / summary panel,
  updating Audit queue posture from `69` promoted techniques to `68`
- advanced the Stage 2 Pack 6 KAG/source-lift evidence pass without status
  flips: `AOA-T-0046 repo-doc-surface-lift` gained first second-context
  support from `nuxt-content/nuxt-llms`, `AOA-T-0047
  github-review-template-lift` gained first second-context support from
  GitHub issue and pull-request template surfaces, while `AOA-T-0020
  evidence-note-provenance-lift` and `AOA-T-0048
  semantic-review-surface-lift` recorded adjacent searched lanes and remain
  promoted
- promoted `AOA-T-0024 upstream-mirroring-with-provenance`, `AOA-T-0025
  capability-spec-versioning`, `AOA-T-0040 skill-vs-command-boundary`,
  `AOA-T-0041 skill-marketplace-curation`, and `AOA-T-0043
  multi-source-primary-input-provenance` to `canonical` after
  managedcode/dotnet-skills, A2A Agent Card, Claude Code skills, VoltAgent
  awesome-agent-skills, and StableNexus showed exact-fit public reinforcement
  for mirror provenance, versioned capability contracts, skill-command
  invocation boundaries, editorial skill curation, and primary/supporting
  source ordering respectively, updating Audit queue posture from `74`
  promoted techniques to `69` while keeping `AOA-T-0042` promoted with
  adjacent skill-health lanes recorded
- promoted `AOA-T-0027 cross-agent-skill-propagation`, `AOA-T-0029
  nested-rule-loading`, and `AOA-T-0030 fragmented-agent-context` to
  `canonical` after ai-rulez, Claude Code memory/rules, and Cline Rules
  showed exact-fit public instruction-surface reinforcement for managed
  skill/rule fan-out, layered rule precedence, and fragment-first authored
  context respectively, updating Audit queue posture from `77` promoted
  techniques to `74`
- promoted `AOA-T-0038 one-command-service-lifecycle` to `canonical` after
  Metaflow Devstack showed a public one-entrypoint local lifecycle contract
  with service selection, dependency startup, readiness follow-through,
  operator shell handoff, and teardown, and promoted `AOA-T-0039
  baseline-first-additive-profile-benchmarks` to `canonical` after LOCOMO /
  OpenClaw showed baseline-first additive backends on the same artifact family,
  updating Audit queue posture from `79` promoted techniques to `77`
- promoted `AOA-T-0037 contextual-host-doctor` to `canonical` after the Get
  Physics Done selected-runtime `gpd doctor` pass found a real public second
  context where runtime-readiness checks stay selector-aware, severity-labeled,
  and separate from render truth, lifecycle, permission, plan, build, smoke, or
  monitoring authority, updating Audit queue posture from `80` promoted
  techniques to `79`
- promoted `AOA-T-0036 render-truth-before-startup` to `canonical` after the
  Dockform plan/render-before-apply pass found a real public second context
  where resolved runtime truth is rendered, reviewed, and confirmed before
  startup without widening into lifecycle, readiness, deployment-preview, or
  secret-publication authority, updating Audit queue posture from `81`
  promoted techniques to `80`
- promoted `AOA-T-0026 session-capture-as-repo-artifact` to `canonical`
  after the Aider `.aider.chat.history.md` artifact-family pass found a real
  public second context in committed repository-visible session-history
  artifacts, adding an adverse-effects review and updating Audit queue posture
  from `82` promoted techniques to `81`
- ran the `AOA-T-0032 context-report-for-ci` exemplar promotion-evidence
  sprint, keeping the bundle `promoted`, recording adjacent public
  context-report/token-budget/repo-packing/LLM-ready-docs lanes as searched
  but insufficient, and narrowing the next honest search shape without
  changing status, frontmatter, generated surfaces, or technique meaning
- closed the template modernization long pass across all `107` current bundles,
  preserving the `proof/skill-support` pilot as the only source-shape repair
  cohort, recording `104` held-no-repair rows, accepting no new
  `TECHNIQUE.md` rewrites, no route-to-other-lane tails, no schema,
  frontmatter, path, relation, support-file, validator, generated-surface, or
  empirical small-agent proof changes, and keeping `Atomic move`,
  `Topology fit`, and `Small-agent execution shape` as optional fixed-slot
  sections rather than required corpus law
- started the template modernization lane with a bounded
  `proof/skill-support` pilot, adding explicit `Atomic move`, `Topology fit`,
  and `Small-agent execution shape` sections to `AOA-T-0015`, `AOA-T-0016`,
  and `AOA-T-0017` without frontmatter, status, path, relation, support-file,
  template-contract, sibling-skill, generated-hand-edit, or empirical
  small-agent proof changes; the validator now allows those template sections
  as optional fixed-slot headings without forcing a full-corpus rewrite
- landed the second owner-boundary bridge pilot over
  `governance/practice-adoption-lifecycle`, confirming `AOA-T-0101`,
  `AOA-T-0103`, and `AOA-T-0104` keep local adoption, retention, and
  obsolescence authority bounded without source repairs, schema/frontmatter
  changes, generated-surface changes, sibling-owner acceptance, or empirical
  small-agent proof
- landed the first owner-boundary bridge pilot over
  `governance/promotion-boundary`, confirming `AOA-T-0089`, `AOA-T-0090`,
  and `AOA-T-0102` keep destination authority outside the technique atom
  without source repairs, schema/frontmatter changes, generated-surface
  changes, sibling-owner acceptance, or empirical small-agent proof
- closed the portability bridge long pass across all `43` `portability-watch`
  rows with Waves A through C, a residual cross-wave scan, and a closeout
  ledger, confirming standalone portability without source repairs,
  route-away moves, schema/frontmatter changes, generated-surface changes, OS
  Abyss adapter authority, or empirical model proof
- started the portability bridge reform lane with a
  `continuity/handoff-continuation` mini-pilot, confirming all seven handoff
  leaves are standalone-portable with ordinary external adapter surfaces and
  recording the repeatable rhythm for the future portability long pass without
  source rewrites, schema migration, OS Abyss adapter authority, or empirical
  model proof
- removed the retired selector/relation temporary long-pass plan after the
  Phase 15 closeout ledger became the durable resume surface
- closed Phase 15 of the selector/relation long pass with a durable ledger
  covering all `28` shelves and `107` current bundles, `103` selector prompts
  or selector scenarios, `7` accepted direct relation repairs, explicit hold
  classes, generated rebuild posture, validation rhythm, and Phase 16
  temporary-plan disposition
- continued the selector/relation long pass with the residual singleton,
  `proof/review-evidence` addendum, and cross-wave scan, keeping
  `AOA-T-0065 complements AOA-T-0038` plus the current review-evidence
  complement edges and recording a no-repair close before the final
  selector/relation ledger
- continued the selector/relation long pass with Wave F over instruction
  capability, media-ingest, and history-artifact shelves, strengthening
  `AOA-T-0064 capability-discovery` from `complements AOA-T-0063` to
  `requires AOA-T-0063` and adding
  `AOA-T-0071 requires AOA-T-0070` while holding optional OCR, skill curation,
  and history artifact sequence pressure as bounded adjacency
- continued the selector/relation long pass with Wave E over continuity and
  recovery shelves, strengthening `AOA-T-0082 repair-shape-from-diagnosis`
  from `complements AOA-T-0081` to `requires AOA-T-0081` while holding donor
  harvest, review-compaction, checkpoint, and antifragility sequence pressure
  as bounded adjacency
- continued the selector/relation long pass with Wave D over governance split
  shelves, preserving the rejected broad automation-governance split and adding
  `AOA-T-0103 used_together_for AOA-T-0104` so retention reviews can point to
  the bounded obsolescence route packet without creating lifecycle law
- continued the selector/relation long pass with Wave C over execution,
  owner-truth, and approval-evidence shelves, recording an explicit no-repair
  hold for operating-order relation pressure without changing frontmatter or
  generated selection surfaces
- continued the selector/relation long pass with Wave B over instruction,
  KAG/source-lift, docs-boundary, and skill-support shelves, recording an
  explicit no-repair hold for current relation pressure without changing
  frontmatter or generated selection surfaces
- started the selector/relation long pass with Wave A over proof and execution
  shelves, strengthening `AOA-T-0050 ready-work-from-blocker-graph` from
  `complements AOA-T-0049` to `requires AOA-T-0049` and recording the direct
  repair under Distillation technique-reform ingress
- strengthened `AOA-T-0058 receipt-confirmed-handoff-packet` and
  `AOA-T-0059 git-verified-handoff-claims` relations from
  `complements AOA-T-0057` to `requires AOA-T-0057`, with generated selection
  surfaces rebuilt and direct-relation repair evidence recorded under
  Distillation technique-reform ingress
- added an explicit agent-facing GitHub landing workflow, `.github/AGENTS.md`,
  expanded PR intake checks, and broader CODEOWNERS coverage for
  governance-critical route and canon surfaces
- corrected the mechanics direction split after comparing `aoa-techniques`
  against the AoA center mechanics contour, keeping repo-level direction in
  root `ROADMAP.md` and package-local pressure in `mechanics/<slug>/ROADMAP.md`
- added a root charter and root surface law to separate public entry,
  repository authority, root placement, direction, obligations, and generated
  repo-doc routing
- slimmed root `ROADMAP.md` back to live repo direction while preserving the
  previous closure-audit baseline under Audit legacy
- linked Method-growth `pattern-adoption` provenance and roadmap surfaces back
  to the extracted atom while keeping the broader lifecycle in mechanics
- linked Method-growth `technique-to-skill-handoff` provenance and roadmap
  surfaces back to the extracted proposal-packet atom while keeping skill
  acceptance outside `aoa-techniques`
- linked Method-growth `retention-checks` provenance and roadmap surfaces back
  to the extracted retention-review atom while keeping obsolescence and owner
  authority outside the technique
- linked Method-growth `obsolescence` provenance and roadmap surfaces back to
  the extracted route-packet atom while keeping deletion, deprecation
  execution, proof, memory, skill, routing, runtime, and owner-local retirement
  authority outside the technique
- added root `legacy/` as a public-safe provenance district with `raw/`,
  `archive/`, and `receipts/`
- moved `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054` into the first technique
  tree pilot shelf at `techniques/continuity/review-compaction/` while keeping
  `domain`, `kind`, IDs, status, evidence, and `tree_path` frontmatter
  unchanged
- accepted the landed `review-compaction` pilot review and selected
  `handoff-continuation` for the next direct-read migration review without
  moving a second shelf yet
- accepted the `handoff-continuation` direct-read migration review over
  `AOA-T-0056` through `AOA-T-0062` as the second tree pilot while keeping the
  review itself non-mutating
- moved `AOA-T-0056` through `AOA-T-0062` into
  `techniques/continuity/handoff-continuation/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `handoff-continuation` pilot review and selected
  `media-ingest` for the next direct-read migration review while repairing
  staging links in `incoming/` to current authored paths
- accepted the `media-ingest` direct-read migration review over `AOA-T-0070`
  through `AOA-T-0074` as the third tree pilot while keeping the review itself
  non-mutating
- moved `AOA-T-0070` through `AOA-T-0074` into
  `techniques/ingest/media-ingest/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `media-ingest` pilot review and selected
  `diagnosis-repair` for the next direct-read migration review without moving
  a fourth shelf yet
- accepted the `diagnosis-repair` direct-read migration review over
  `AOA-T-0080` through `AOA-T-0083` as the fourth tree pilot while keeping the
  review itself non-mutating
- moved `AOA-T-0080` through `AOA-T-0083` into
  `techniques/recovery/diagnosis-repair/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `diagnosis-repair` pilot review and selected
  `instruction-surface` for the next direct-read migration review without
  moving a fifth shelf yet
- accepted the `instruction-surface` direct-read migration review over
  `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`, `AOA-T-0029`,
  `AOA-T-0030`, and `AOA-T-0035` as the fifth tree pilot while keeping the
  review itself non-mutating
- moved `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`,
  `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035` into
  `techniques/instruction/instruction-surface/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `instruction-surface` pilot review and selected
  `kag-source-lift` for the next direct-read migration review without moving a
  sixth shelf yet
- accepted the `kag-source-lift` direct-read migration review over
  `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`, `AOA-T-0022`,
  `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048` as the sixth tree pilot while
  keeping the review itself non-mutating
- moved `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`,
  `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048` into
  `techniques/knowledge-lift/kag-source-lift/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `kag-source-lift` pilot review and selected
  `docs-boundary` for the next direct-read migration review without moving a
  seventh shelf yet
- accepted the `docs-boundary` direct-read migration review over `AOA-T-0002`,
  `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033` as the seventh tree pilot while
  keeping the review itself non-mutating
- moved `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033` into
  `techniques/instruction/docs-boundary/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `docs-boundary` pilot review and selected
  `capability-registry` for the next direct-read migration review without
  moving an eighth shelf yet
- accepted the `capability-registry` direct-read migration review over
  `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064` as the eighth tree pilot while
  keeping the review itself non-mutating
- moved `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064` into
  `techniques/instruction/capability-registry/` while keeping `domain`,
  `kind`, IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `capability-registry` pilot review and selected
  `capability-boundary` for the next direct-read migration review without
  moving a ninth shelf yet
- accepted the `capability-boundary` direct-read migration review over
  `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093` as the ninth tree pilot while
  keeping the review itself non-mutating
- moved `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093` into
  `techniques/instruction/capability-boundary/` while keeping `domain`,
  `kind`, IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `capability-boundary` pilot review and selected
  `skill-discovery` for the next direct-read migration review without moving a
  tenth shelf yet
- accepted the `skill-discovery` direct-read migration review over
  `AOA-T-0041` and `AOA-T-0042` as the tenth tree pilot while keeping the
  review itself non-mutating
- moved `AOA-T-0041` and `AOA-T-0042` into
  `techniques/instruction/skill-discovery/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `skill-discovery` pilot review and selected
  `skill-support` for the next direct-read migration review without moving an
  eleventh shelf yet
- accepted the `skill-support` direct-read migration review over `AOA-T-0016`,
  `AOA-T-0015`, and `AOA-T-0017` as the eleventh tree pilot while keeping the
  review itself non-mutating
- moved `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017` into
  `techniques/proof/skill-support/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `skill-support` pilot review and selected
  `evaluation-chain` for the next direct-read migration review without moving
  a twelfth shelf yet
- accepted the `evaluation-chain` direct-read migration review over
  `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032` as the twelfth tree pilot while
  keeping the review itself non-mutating
- moved `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032` into
  `techniques/proof/evaluation-chain/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `evaluation-chain` pilot review and selected
  `published-summary` for the next direct-read migration review without moving
  a thirteenth shelf yet
- accepted the `published-summary` direct-read migration review over
  `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011` as the
  thirteenth tree pilot while keeping the review itself non-mutating
- moved `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011` into
  `techniques/proof/published-summary/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `published-summary` pilot review and selected
  `history-artifacts` for the next direct-read migration review without
  moving a fourteenth shelf yet
- accepted the `history-artifacts` direct-read migration review over
  `AOA-T-0044`, `AOA-T-0053`, `AOA-T-0026`, `AOA-T-0045`, `AOA-T-0066`, and
  `AOA-T-0067` as the fourteenth tree pilot while keeping the review itself
  non-mutating
- moved `AOA-T-0044`, `AOA-T-0053`, `AOA-T-0026`, `AOA-T-0045`,
  `AOA-T-0066`, and `AOA-T-0067` into
  `techniques/history/history-artifacts/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `history-artifacts` pilot review and selected
  `recovery/antifragility-recovery` for the next direct-read migration review
  without moving a fifteenth shelf yet
- accepted the `antifragility-recovery` direct-read migration review over
  `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and `AOA-T-0098` as the fifteenth
  tree pilot while keeping the review itself non-mutating
- moved `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and `AOA-T-0098` into
  `techniques/recovery/antifragility-recovery/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `antifragility-recovery` pilot review and selected
  `execution/ready-work-graphs` for the next direct-read migration review
  without moving a sixteenth shelf yet
- accepted the `ready-work-graphs` direct-read migration review over
  `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055` as the sixteenth tree pilot
  while keeping the review itself non-mutating
- moved `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055` into
  `techniques/execution/ready-work-graphs/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `ready-work-graphs` pilot review and selected
  `execution/intent-chain` for the next direct-read migration review without
  moving a seventeenth shelf yet
- accepted the `intent-chain` direct-read migration review over `AOA-T-0004`
  and `AOA-T-0005` as the seventeenth tree pilot while keeping the review
  itself non-mutating
- moved `AOA-T-0004` and `AOA-T-0005` into
  `techniques/execution/intent-chain/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `intent-chain` pilot review and selected
  `execution/agent-workflows-core` for the next direct-read migration review
  without moving an eighteenth shelf yet
- accepted the `agent-workflows-core` direct-read migration review over
  `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`, and `AOA-T-0031`
  as the eighteenth tree pilot while keeping the review itself non-mutating
- moved `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`, and
  `AOA-T-0031` into `techniques/execution/agent-workflows-core/` while
  keeping `domain`, `kind`, IDs, status, evidence, and `tree_path`
  frontmatter unchanged
- accepted the landed `agent-workflows-core` pilot review and selected
  `continuity/donor-harvest` for the next direct-read migration review without
  moving a nineteenth shelf yet
- accepted the `donor-harvest` direct-read migration review over `AOA-T-0075`,
  `AOA-T-0077`, `AOA-T-0084`, and `AOA-T-0085` as the nineteenth tree pilot
  while keeping the review itself non-mutating
- moved `AOA-T-0075`, `AOA-T-0077`, `AOA-T-0084`, and `AOA-T-0085` into
  `techniques/continuity/donor-harvest/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `donor-harvest` pilot review and selected
  `governance/decision-routing` for the next direct-read migration review
  without moving a twentieth shelf yet
- accepted the `decision-routing` direct-read migration review over
  `AOA-T-0076`, `AOA-T-0078`, and `AOA-T-0079` as the twentieth tree pilot
  while keeping the review itself non-mutating
- moved `AOA-T-0076`, `AOA-T-0078`, and `AOA-T-0079` into
  `techniques/governance/decision-routing/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `decision-routing` pilot review and selected
  `governance/approval-evidence` for the next direct-read migration review
  without moving a twenty-first shelf yet
- accepted the `approval-evidence` direct-read migration review over
  `AOA-T-0068` and `AOA-T-0069` as the twenty-first tree pilot while keeping
  the review itself non-mutating
- moved `AOA-T-0068` and `AOA-T-0069` into
  `techniques/governance/approval-evidence/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `approval-evidence` pilot review and selected
  `proof/review-evidence` for the next direct-read migration review without
  moving a twenty-second shelf yet
- accepted the `review-evidence` direct-read migration review over
  `AOA-T-0107`, `AOA-T-0105`, and `AOA-T-0106` as the twenty-second tree pilot
  while keeping the review itself non-mutating
- moved `AOA-T-0107`, `AOA-T-0105`, and `AOA-T-0106` into
  `techniques/proof/review-evidence/` while keeping `domain`, `kind`, IDs,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `review-evidence` pilot review and selected
  `execution/runtime-truth-lifecycle` for the next direct-read migration review
  without moving a twenty-third shelf yet
- accepted the `runtime-truth-lifecycle` direct-read migration review over
  `AOA-T-0036`, `AOA-T-0038`, `AOA-T-0037`, and `AOA-T-0039` as the
  twenty-third tree pilot while keeping the review itself non-mutating
- moved `AOA-T-0036`, `AOA-T-0038`, `AOA-T-0037`, and `AOA-T-0039` into
  `techniques/execution/runtime-truth-lifecycle/` while keeping `domain`,
  `kind`, IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `runtime-truth-lifecycle` pilot review and selected
  `proof/owner-truth-closeout` for the next direct-read migration review
  without moving a twenty-fourth shelf yet
- accepted the `owner-truth-closeout` direct-read migration review over
  `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, `AOA-T-0096`, and `AOA-T-0094` as
  the twenty-fourth tree pilot while keeping the review itself non-mutating
- moved `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, `AOA-T-0096`, and
  `AOA-T-0094` into `techniques/proof/owner-truth-closeout/` while keeping
  `domain`, `kind`, IDs, status, evidence, and `tree_path` frontmatter
  unchanged
- accepted the landed `owner-truth-closeout` pilot review and selected
  `governance/automation-governance` for direct-read split review without
  moving a twenty-fifth shelf yet
- rejected one bulk `governance/automation-governance` shelf after direct
  reading and named `governance/automation-readiness`,
  `governance/promotion-boundary`, and
  `governance/practice-adoption-lifecycle` as split candidates before any
  automation-governance path movement
- landed the automation-governance split expansion closeout, activated
  `governance/automation-readiness` as Candidate A, and kept
  `governance/promotion-boundary` plus
  `governance/practice-adoption-lifecycle` queued without moving files
- accepted the `automation-readiness` direct-read migration review over
  `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` as the twenty-fifth tree pilot
  while keeping the review itself non-mutating
- moved `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` into
  `techniques/governance/automation-readiness/` while keeping `domain`,
  `kind`, IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `automation-readiness` pilot review and selected
  `governance/promotion-boundary` for direct-read review without moving a
  twenty-sixth shelf yet
- accepted the `promotion-boundary` direct-read migration review over
  `AOA-T-0089`, `AOA-T-0090`, and `AOA-T-0102` as the twenty-sixth tree pilot
  while keeping the review itself non-mutating
- moved `AOA-T-0089`, `AOA-T-0090`, and `AOA-T-0102` into
  `techniques/governance/promotion-boundary/` while keeping `domain`, `kind`,
  IDs, status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `promotion-boundary` pilot review and selected
  `governance/practice-adoption-lifecycle` for direct-read review without
  moving a twenty-seventh shelf yet
- accepted the `practice-adoption-lifecycle` direct-read migration review over
  `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104` as the twenty-seventh tree
  pilot while keeping the review itself non-mutating
- moved `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104` into
  `techniques/governance/practice-adoption-lifecycle/` while keeping
  `domain`, `kind`, IDs, status, evidence, and `tree_path` frontmatter
  unchanged
- accepted the landed `practice-adoption-lifecycle` pilot review, closed the
  rejected bulk `automation-governance` split tail with all nine IDs
  accounted, and selected `tool-use/tool-gateway` for direct-read singleton
  review without moving a twenty-eighth shelf yet
- accepted the `tool-gateway` direct-read singleton review over `AOA-T-0065`
  as the twenty-eighth tree pilot while keeping the review itself non-mutating
- moved `AOA-T-0065` into
  `techniques/tool-use/tool-gateway/` while keeping `domain`, `kind`, ID,
  status, evidence, and `tree_path` frontmatter unchanged
- accepted the landed `tool-gateway` pilot review, resolved the singleton
  shelf after migration, and selected whole-tree closeout review as the next
  reform step
- accepted the whole-tree closeout review, validating the current tree as
  `107` bundles across `10` trunks and `28` shelves with `107/107` path
  parity, `28/28` root receipts, and no remaining split, singleton, or
  unassigned holds
- consolidated tree route cards so every current trunk and retained
  frontmatter lane is validator-backed, current-tree aware, and still weaker
  than authored bundle meaning
- added the final tree migration ledger, confirming generated parity,
  `28/28` shelf receipt coverage, temporary-plan distillation, and the next
  direction toward technique-bundle reform

### Validation

- `python scripts/validate_repo.py`
- `python -m unittest discover -s tests`
- `python scripts/release_check.py`

## [0.4.2] - 2026-04-23

### Summary

- this patch adds Agon technique binding candidates, recurrence technique
  manifests, Wave XV epistemic practice candidates, technique-to-skill
  handoff posture, and owner-observation boundaries
- Experience wave3, wave4, and wave5 technique contracts are aligned with
  adoption, governance, installation, service clarity, handoff compression,
  scope boundaries, appeal reasoning, authority resolution, and
  sovereign-release posture
- `aoa-techniques` remains the reusable practice canon rather than a runtime,
  skill, or package-publication authority

### Added

- Agon Wave IV technique candidate bridge docs, seed/config, generated index,
  and explicit builder / validator / test surfaces
- Agon recurrence technique manifests, Wave XV epistemic technique candidates,
  recurrence live-observation and review-decision closure notes, and
  recurrence owner-observation boundaries
- Experience wave3-wave5 practice surfaces for adoption boundaries,
  governance precedent, installation notes, service clarity, handoff
  compression, scope boundaries, sealed decisions, appeal reasoning,
  authority resolution, retention checks, obsolescence, and
  technique-to-skill handoff

### Changed

- root and docs entry routes now expose the Agon practice-candidate bridge as a
  requested-not-landed companion surface instead of leaving it implicit
- Agon review follow-ups, generated doc-surface manifests, technique adoption
  contract tests, Experience governance contracts, and Wave5 RFC3339 datetime
  checking were tightened

### Validation

- `python scripts/release_check.py`
- `python mechanics/agon/parts/move-technique-bridge/scripts/build_agon_technique_binding_candidates.py --check`
- `python mechanics/agon/parts/move-technique-bridge/scripts/validate_agon_technique_binding_candidates.py`
- `python -m pytest -q mechanics/agon/parts/move-technique-bridge/tests/test_agon_technique_binding_candidates.py`

### Notes

- this patch expands practice surfaces and contract validation without turning
  technique candidates into executable skill truth or runtime authority

## [0.4.1] - 2026-04-19

### Summary

- this patch adds chaos-wave stress closeout guidance, recurrence beacons, and
  stronger promotion-readiness alignment across the public technique corpus
- pull request template coverage, Node24 workflow refs, and required-check
  posture are aligned with the current release contract
- `aoa-techniques` remains the curated public technique layer rather than a
  runtime or package authority

### Added

- a chaos wave 1 stress closeout technique, recurrence beacons with hook
  bindings, and filesystem-aware PR template test coverage

### Changed

- promotion-readiness matrix, roadmap/root-entry docs, canonical PR template
  path handling, and CI/protection surfaces are refreshed for the current
  technique wave

### Validation

- `python scripts/release_check.py`

### Notes

- this patch extends technique guidance and validation posture without turning
  the repository into a package registry or runtime authority

## [0.4.0] - 2026-04-10

### Summary

- this release adds workspace ingress and mutation-gate techniques, audit-to-closeout proof loops, promotion-readiness surfaces, live technique receipt publishing, and antifragility/via-negativa guidance
- pinned validation evidence, repo/root scouting, and current-practice posture are strengthened while new shared-substrate and owner-sync techniques are promoted into the public set
- `aoa-techniques` remains a curated public corpus and documentation surface rather than a package or registry authority

### Validation

- `python scripts/release_check.py`

### Notes

- detailed corpus, generated-surface, report, and validation-asset coverage for this release remains enumerated below under `Added`, `Changed`, and `Included in this release`

### Added

- workspace ingress and mutation-gate techniques plus audit-to-closeout
  proof-loop, recommendation-truth-vs-host-actionability, canonical-owner
  mirror, and pinned-validation techniques
- technique promotion-readiness surfaces and live technique receipt publishing
- antifragility recovery domains, via negativa techniques checklist, and quest
  feed validation surfaces

### Changed

- strengthened pinned validation evidence, repo/root technique-kind scouting,
  and next-wave practice posture across the published corpus
- promoted new isolated shared-substrate and GitHub-only owner-sync techniques
  into the public set

### Included in this release

- technique corpus growth across `techniques/`, `docs/`, `generated/`,
  `reports/`, `config/`, `data/`, and `templates/`, including the
  session-donor and session-harvest family, workspace ingress and
  mutation-gate techniques, audit-to-closeout proof loops, canonical-owner
  mirror, pinned validation, and live receipt publishing
- repo-local validation and release surfaces under `.agents/`, `AGENTS.md`,
  `README.md`, `CONTRIBUTING.md`, `TECHNIQUE_INDEX.md`, `schemas/`, `scripts/`,
  `tests/`, and `quests/`, including promotion-readiness manifests, via
  negativa guidance, quest-feed validation, and public corpus status refreshes

## [0.3.0] - 2026-04-01

Third public corpus release.

This changelog entry uses the release-prep merge date.

### Summary

- `26` new public technique bundles since `v0.2.0`, growing the published corpus from `48` techniques to `74`
- public corpus status is now `25` `canonical` techniques and `49` `promoted` techniques
- this release extends the corpus across handoff and continuation patterns, capability discovery and registry contracts, transcript lineage, fail-closed and approval-bound job control, OCR and media-ingest workflows, and Telegram normalization

### Added

- `AOA-T-0049` `dependency-aware-task-graph`, a promoted `agent-workflows` technique adapted from `steveyegge/beads` for explicit blocker graphs and derived ready work
- `AOA-T-0050` `ready-work-from-blocker-graph`, a promoted `agent-workflows` technique adapted from `steveyegge/beads` for blocker-aware ready-frontier derivation
- `AOA-T-0051` `commit-triggered-background-review`, a promoted `agent-workflows` technique adapted from `roborev-dev/roborev` for post-commit asynchronous review artifacts
- `AOA-T-0052` `review-findings-compaction`, a promoted `agent-workflows` technique adapted from `roborev-dev/roborev` for findings verification and consolidation against current code
- `AOA-T-0053` `local-first-session-index`, a promoted `history` technique adapted from `wesm/agentsview` for local searchable lookup over already-saved session artifacts
- `AOA-T-0054` `compaction-resilient-skill-loading`, a promoted `agent-workflows` technique adapted from `joshuadavidthomas/opencode-agent-skills` for bounded post-compaction skill-availability recovery
- `AOA-T-0055` `requirements-design-tasks-ladder`, a promoted `agent-workflows` technique adapted from `gotalab/cc-sdd` for a bounded requirement -> design -> task planning ladder
- `AOA-T-0056` `channelized-agent-mailbox`, a promoted `agent-workflows` technique adapted from `agentralabs/agentic-comm` for durable named-channel communication with replay and explicit acknowledgment
- `AOA-T-0057` `structured-handoff-before-compaction`, a promoted `agent-workflows` technique adapted from `thebasedcapital/nightcrawler` with supporting checkpoint framing from `yan5xu/code-relay` for explicit continuation packets before context compaction or rollover
- `AOA-T-0058` `receipt-confirmed-handoff-packet`, a promoted `agent-workflows` technique adapted from `jeremiah-k/agor` with supporting explicit-acceptance surfaces from `ax-platform/ax-platform-mcp` for visible handoff receipt before continuation
- `AOA-T-0059` `git-verified-handoff-claims`, a promoted `agent-workflows` technique adapted from `thebasedcapital/nightcrawler` with supporting snapshot-verification posture from `jeremiah-k/agor` for repo-backed verification of handoff claims before continuation
- `AOA-T-0060` `session-opening-ritual-before-work`, a promoted `agent-workflows` technique adapted from `thebasedcapital/nightcrawler` for explicit pre-mutation session-start reading and baseline verification before resumed work begins
- `AOA-T-0061` `cross-repo-resource-map-bootstrap`, a promoted `agent-workflows` technique adapted from `yan5xu/code-relay` for task-bounded cross-repo startup maps that name which repos and surfaces matter before continuation
- `AOA-T-0062` `episode-bounded-agent-loop`, a promoted `agent-workflows` technique adapted from `thebasedcapital/nightcrawler` for checkpointed multi-episode continuation with explicit continue, stop, or escalate decisions
- `AOA-T-0063` `versioned-agent-registry-contract`, a promoted `docs` technique adapted from `agntcy/dir` for named versioned registry-entry contracts with explicit references and bounded metadata
- `AOA-T-0064` `capability-discovery`, a promoted `docs` technique adapted from `agntcy/dir` for bounded discovery-query contracts over already-published capability records
- `AOA-T-0065` `mcp-gateway-proxy`, a promoted `agent-workflows` technique adapted from `lasso-security/mcp-gateway` for one reviewable proxy seam in front of configured MCP servers
- `AOA-T-0066` `transcript-replay-artifact`, a promoted `history` technique adapted from `es617/claude-replay` with supporting context from `wesm/agentsview` for post-capture replay artifacts over saved sessions
- `AOA-T-0067` `transcript-linked-code-lineage`, a promoted `history` technique adapted from `git-ai-project/git-ai` for bounded code-to-session provenance links
- `AOA-T-0068` `fail-closed-evidence-gate`, a promoted `agent-workflows` technique adapted from `Clyra-AI/gait` for fail-closed execution gating with reviewable evidence output
- `AOA-T-0069` `approval-bound-durable-jobs`, a promoted `agent-workflows` technique adapted from `Clyra-AI/gait` for durable jobs that pause and resume across an explicit approval seam
- `AOA-T-0070` `two-stage-document-ocr-pipeline`, a promoted `agent-workflows` technique adapted from `PaddleOCR` and `docTR` for staged OCR handoff before later extraction or review
- `AOA-T-0071` `template-backed-field-extraction-after-ocr`, a promoted `agent-workflows` technique adapted from `invoice2data`, `receiptparser`, and `receipt-parser-legacy` for bounded post-OCR field extraction through explicit templates, heuristics, and review fallback
- `AOA-T-0072` `perceptual-media-dedupe-with-threshold-review`, a promoted `agent-workflows` technique adapted from `imagededup` and `imgdupes` for reviewable near-duplicate media grouping before later cleanup actions
- `AOA-T-0073` `semantic-media-bucketing-with-vision-plus-ocr`, a promoted `agent-workflows` technique adapted from `CLIP` and `PaddleOCR` for confidence-aware mixed-media bucketing through bounded taxonomy and OCR side text
- `AOA-T-0074` `telegram-export-normalization-to-local-store`, a promoted `agent-workflows` technique adapted from `Telethon`, `TDLib`, `opentele`, `Chatistics`, `tg-archive`, and `telegram-mcp` for resumable Telegram-source normalization into a provenance-preserving local store
- live questbook projection surfaces under `generated/quest_catalog.min.json`, `generated/quest_dispatch.min.json`, and matching example outputs
- downstream technique feed contracts and feat adjunct surfaces for current consumer layers

### Changed

- promoted `AOA-T-0028` `confirmation-gated-mutating-action` to `canonical` after GitHub Copilot's public coding-agent approval surfaces confirmed the same explicit confirmation-before-mutation seam beyond the donor lineage
- promoted `AOA-T-0031` `shell-composable-agent-invocation` to `canonical` after OpenAI Codex CLI's public `codex exec` surface confirmed the same stdin/stdout/file-first one-shot shell contract beyond the donor lineage
- promoted `AOA-T-0044` `versionable-session-transcripts` to `canonical` after `claude-code-log` confirmed a second public post-capture Markdown transcript-export surface beyond the donor product family
- promoted `AOA-T-0053` `local-first-session-index` to `canonical` after `coding-agent-search (cass)` confirmed a second public local-first derivative session-index surface beyond the donor product family
- current corpus status is now `25` `canonical` techniques and `49` `promoted` techniques

### Included in this release

- the current `74`-bundle technique corpus under `techniques/` plus the updated `TECHNIQUE_INDEX.md`
- questbook projection surfaces, downstream feed contracts, capsules, sections, checklists, examples, evidence notes, semantic reviews, and shadow reviews under `generated/` and `docs/`

### Validation

- `python scripts/release_check.py`

### Notes

- this release remains a curated public corpus and validated documentation surface rather than a package or registry artifact

## [0.2.0] - 2026-03-23

Second public corpus release.

This changelog entry uses the release-prep merge date.

### Added

- `35` new public technique bundles since `v0.1.0`, growing the published corpus from `13` techniques to `48`
- corpus coverage now spans `9` `agent-workflows` techniques, `24` `docs` techniques, `12` `evaluation` techniques, and the first `3` `history` techniques
- the first public KAG/source-lift family inside the `docs` domain, including `AOA-T-0018` through `AOA-T-0022`
- the first bounded `history` domain for session and history artifacts that stay local-first and reviewable without widening into memory ownership, including `AOA-T-0026`, `AOA-T-0044`, and `AOA-T-0045`
- new repo-owned maintainer and navigation docs, including `docs/START_HERE.md`, `docs/TECHNIQUE_SELECTION_GUIDE.md`, `docs/SEMANTIC_REVIEW_GUIDE.md`, `docs/EXTERNAL_IMPORT_RUNBOOK.md`, `docs/DONOR_REFINERY_RUBRIC.md`, `docs/LONG_GAP_CANON_DESIGN.md`, the roadmap now kept at `ROADMAP.md`, `docs/EXTERNAL_TECHNIQUE_CANDIDATES.md`, and `docs/CROSS_LAYER_TECHNIQUE_CANDIDATES.md`
- new derived surface families for technique capsules, repo-doc routing, technique sections, checklists, examples, evidence notes, GitHub review templates, semantic reviews, and shadow reviews

### Changed

- public corpus status is now `21` `canonical` techniques and `27` `promoted` techniques, up from `9` `canonical` and `4` `promoted` in `v0.1.0`
- the canonical default set expanded across agent workflows, docs, evaluation, and KAG/source-lift surfaces, including `AOA-T-0004`, `AOA-T-0013` through `AOA-T-0019`, `AOA-T-0021`, `AOA-T-0023`, and `AOA-T-0034`
- evidence and review posture is stronger across the corpus through broader `second-context-adaptation`, `canonical-readiness`, `external-origin`, `external-import-review`, and canonical-only `adverse-effects-review` coverage
- repo routing now centers on `docs/START_HERE.md` and the bounded `pick -> inspect -> expand -> object use` operating path
- release and validation posture now centers on `python scripts/release_check.py`, with tighter generator-drift checks, repo-doc and review-surface validation, broader public-hygiene URL scanning, and cleaner worktree behavior

### Included in this release

- technique bundles under `techniques/` plus the expanded [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md)
- capsule surfaces: `docs/TECHNIQUE_CAPSULES.md`, `docs/TECHNIQUE_CAPSULE_GUIDE.md`, `generated/technique_capsules.json`, and `generated/technique_capsules.min.json`
- repo-doc routing surfaces: `docs/REPO_DOC_SURFACES.md`, `generated/repo_doc_surface_manifest.json`, and `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md`
- source-lift reader and guide surfaces: `docs/TECHNIQUE_SECTIONS.md`, `docs/TECHNIQUE_SECTION_LIFT_GUIDE.md`, `docs/TECHNIQUE_CHECKLISTS.md`, `docs/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, `docs/TECHNIQUE_EXAMPLES.md`, `docs/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`, `docs/EVIDENCE_NOTE_SURFACES.md`, and `docs/EVIDENCE_NOTE_PROVENANCE_GUIDE.md`
- review routing surfaces: `docs/SHADOW_PATTERNS.md`, `docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md`, `docs/EVALUATION_CHAIN_SHADOW_REVIEW.md`, `generated/shadow_review_manifest.json`, `generated/semantic_review_manifest.json`, and `generated/github_review_template_manifest.json`
- governance and intake surfaces under `.github/` plus the release and validation helpers under `scripts/`

### Validation

- `python scripts/release_check.py`
- the bounded release check reruns repo-doc, catalog, capsule, section, checklist, example, evidence-note, GitHub review-template, semantic-review, and shadow-review builders before `unittest` and `validate_repo`

### Notes

- this release remains a curated public corpus and validated documentation surface rather than a package or registry artifact
- package publishing to PyPI, npm, or other registries remains out of scope for `v0.2.0`
- release identity for this repository remains the changelog entry, Git tag, and GitHub release body

## [0.1.0] - 2026-03-17

First public baseline release.

This changelog entry uses the release-prep merge date.
The GitHub release for `v0.1.0` was published on `2026-03-18`.

### Added

- initial public release of `aoa-techniques` as a public library of reusable techniques for coding agents and humans
- repository entry documents: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `WALKTHROUGH.md`
- repository-wide technique map in `TECHNIQUE_INDEX.md`
- curated public technique catalog containing:
  - 9 `canonical` techniques
  - 4 `promoted` techniques
- public templates, schemas, and validation helpers for technique authoring and promotion

### Included in this release

- technique bundles under `techniques/`
- generated selection and semantic-review navigation surfaces referenced from `README.md`
- bounded KAG-oriented manifest pilot series for:
  - section manifests
  - checklist manifests
  - example manifests
  - evidence-note manifests
  - GitHub review template manifests
  - semantic review manifests

### Validation

Documented local validation path for this release:

- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`

### Notes

- this is the first public baseline release for the repository
- package publishing to PyPI, npm, or other registries is out of scope for `v0.1.0`
- release emphasis is the curated public technique corpus and its repo-level validation/documentation surface
