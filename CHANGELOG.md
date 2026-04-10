# Changelog

All notable changes to `aoa-techniques` will be documented in this file.

The format is intentionally simple and human-first.

## [Unreleased]

## [0.4.0] - 2026-04-10

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
- new repo-owned maintainer and navigation docs, including `docs/START_HERE.md`, `docs/TECHNIQUE_SELECTION_GUIDE.md`, `docs/SEMANTIC_REVIEW_GUIDE.md`, `docs/EXTERNAL_IMPORT_RUNBOOK.md`, `docs/DONOR_REFINERY_RUBRIC.md`, `docs/LONG_GAP_CANON_DESIGN.md`, `docs/DEEP_AUDIT_ROADMAP.md`, `docs/EXTERNAL_TECHNIQUE_CANDIDATES.md`, and `docs/CROSS_LAYER_TECHNIQUE_CANDIDATES.md`
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
