# Execution Profile Orchestration Boundary Review

Source packet: [Technique Reform Ingress](../README.md)

Status: direct-read review packet for Phase 3 orchestration calibration. No
local model harness was run. No frontmatter, schema, generated scout rule,
capsule builder, registry, or technique leaf was changed.

## Verdict

Phase 3 confirms the current `orchestration-required` profile as a useful
boundary signal across all 53 current rows.

The profile does not mean "too large to be a technique." Most rows are still
atomic. It means the technique crosses a surface where a safe agentic system
needs an outer wrapper: approval, mutation, runtime/host truth, tool mediation,
public-share, security-sensitive source handling, generated publish parity,
owner-route authority, degraded-mode recovery, or review-pressure control.

Important calibration:

- `orchestration-required` is not a quality demotion.
- Some rows are short and even read-only, but still require orchestration
  because authority, privacy, generated truth, host truth, or tool provenance
  lives outside the atomic move.
- The wrapper belongs outside the technique. The technique should name the
  move and stop line; a skill, eval, owner repo, host workflow, or human gate
  supplies the sequencing.
- `AOA-T-0095` remains a medium-row edge from Phase 2, but direct reading
  suggests it should be sampled in any future relabel or scout-rule review
  because its authored output includes GitHub issue/PR/CI/merge and post-merge
  coordination sync.

Reviewed rows:

| profile | rows reviewed | verdict |
|---|---:|---|
| `orchestration-required` | 53 | boundary confirmed |
| sampled medium edge | 1 | carry to Phase 5 as possible profile mismatch |
| relabels made | 0 | no source/profile mutation in this packet |

## Reviewed Surfaces

Reviewed before this packet:

- `AGENTS.md`
- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `docs/TECHNIQUE_TREE_CONTRACT.md`
- `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md`
- `docs/TECHNIQUE_CAPSULES.md`
- `techniques/continuity/AGENTS.md`
- `techniques/execution/AGENTS.md`
- `techniques/governance/AGENTS.md`
- `techniques/history/AGENTS.md`
- `techniques/ingest/AGENTS.md`
- `techniques/instruction/AGENTS.md`
- `techniques/knowledge-lift/AGENTS.md`
- `techniques/proof/AGENTS.md`
- `techniques/recovery/AGENTS.md`
- `techniques/tool-use/AGENTS.md`
- current scout rows, technique paths, capsule text, frontmatter summaries,
  section maps, and targeted checklist, example, and note surfaces for the 53
  current `orchestration-required` rows

## Boundary Rows

| technique | wrapper type | direct-read verdict | why the outer wrapper remains required |
|---|---|---|---|
| `AOA-T-0001` `plan-diff-apply-verify-report` | mutation workflow | `orchestration-boundary-confirmed` | planning, patching, validation, and reporting cross real repo mutation and review sequencing |
| `AOA-T-0014` `tdd-slice` | mutation workflow | `orchestration-boundary-confirmed` | tests, implementation, and refactor limits require ordered execution and verification |
| `AOA-T-0036` `render-truth-before-startup` | runtime truth | `orchestration-boundary-confirmed` | composed runtime truth must be rendered before startup by host-aware tooling |
| `AOA-T-0038` `one-command-service-lifecycle` | runtime lifecycle | `orchestration-boundary-confirmed` | start/stop behavior mutates local service state and needs prerequisite, status, and shutdown controls |
| `AOA-T-0054` `compaction-resilient-skill-loading` | degraded capability recovery | `orchestration-boundary-confirmed` | reloading canonical skills after compaction depends on available host skill inventory and context recovery posture |
| `AOA-T-0060` `session-opening-ritual-before-work` | session mutation gate | `orchestration-boundary-confirmed` | work must read and verify current state before any mutation in a resumed or handed-off session |
| `AOA-T-0062` `episode-bounded-agent-loop` | episode control | `orchestration-boundary-confirmed` | continue, stop, and escalate decisions require checkpointed episode boundaries outside one atomic step |
| `AOA-T-0065` `mcp-gateway-proxy` | tool gateway | `orchestration-boundary-confirmed` | MCP mediation touches configured upstream tools, metadata, sanitization, and approval/public-share boundaries |
| `AOA-T-0068` `fail-closed-evidence-gate` | approval gate | `orchestration-boundary-confirmed` | the gate matters only if missing allow evidence truly blocks later side effects |
| `AOA-T-0070` `two-stage-document-ocr-pipeline` | media pipeline | `orchestration-boundary-confirmed` | OCR detection, recognition, confidence, handoff state, and tool interchange need pipeline control |
| `AOA-T-0071` `template-backed-field-extraction-after-ocr` | media extraction | `orchestration-boundary-confirmed` | templates, OCR uncertainty, missing fields, and conflict signaling depend on upstream OCR and downstream review |
| `AOA-T-0072` `perceptual-media-dedupe-with-threshold-review` | media threshold review | `orchestration-boundary-confirmed` | near-duplicate grouping must avoid silent deletion and needs thresholded review buckets |
| `AOA-T-0073` `semantic-media-bucketing-with-vision-plus-ocr` | multimodal review | `orchestration-boundary-confirmed` | vision plus OCR bucketing needs confidence gates and approval before downstream action |
| `AOA-T-0074` `telegram-export-normalization-to-local-store` | sensitive ingest | `orchestration-boundary-confirmed` | export normalization touches auth/session-adjacent material, provenance, and local-store security boundaries |
| `AOA-T-0078` `decision-fork-cards` | decision routing | `orchestration-boundary-confirmed` | route cards can steer later owner work and must not become hidden recommendation authority |
| `AOA-T-0079` `risk-passport-lift` | route risk posture | `orchestration-boundary-confirmed` | risk passports influence control mode and delegation posture, so approval and stop-condition wrappers remain needed |
| `AOA-T-0082` `repair-shape-from-diagnosis` | recovery planning | `orchestration-boundary-confirmed` | repair shape comes after diagnosis and can route toward owner mutation or degraded-mode recovery |
| `AOA-T-0083` `checkpoint-bound-self-repair` | self-repair checkpoint | `orchestration-boundary-confirmed` | approval, rollback, health checks, iteration limits, and improvement logs must gate any self-repair |
| `AOA-T-0085` `multi-axis-quest-overlay` | symbolic overlay | `orchestration-boundary-confirmed` | quest flavor is safe only over prior evidence and must not overwrite owner truth, proof, or route authority |
| `AOA-T-0088` `approval-sensitivity-check` | automation approval | `orchestration-boundary-confirmed` | approval, rollback, hidden authority, and self-change posture affect whether automation can proceed |
| `AOA-T-0093` `recommendation-truth-vs-host-actionability` | host capability boundary | `orchestration-boundary-confirmed` | host inventory and actionability are security-sensitive and must not erase router recommendation truth |
| `AOA-T-0096` `pinned-validation-matrix-before-generated-publish` | generated publish | `orchestration-boundary-confirmed` | generated outputs must rebuild against workflow-pinned refs before public-share or merge-readiness claims |
| `AOA-T-0101` `local-pattern-adoption-gate` | adoption approval | `orchestration-boundary-confirmed` | owner consent, compatibility evidence, rollback, and retention watch are adoption controls outside one note |
| `AOA-T-0104` `superseded-practice-obsolescence-route` | lifecycle obsolescence | `orchestration-boundary-confirmed` | supersession, merge, reanchor, drop, or deprecation review can become irreversible without owner receipt |
| `AOA-T-0105` `single-missing-evidence-request` | review pressure | `orchestration-boundary-confirmed` | one missing evidence request can mutate review state and must avoid proof theater or broad research creep |
| `AOA-T-0107` `single-locus-claim-challenge` | review pressure | `orchestration-boundary-confirmed` | one claim challenge changes review posture and must not become adjudication, tone policing, or scoring |
| `AOA-T-0013` `single-source-rule-distribution` | managed instruction distribution | `orchestration-boundary-confirmed` | distributing one canonical rule source to several targets needs managed-output and drift controls |
| `AOA-T-0018` `markdown-technique-section-lift` | generated knowledge lift | `orchestration-boundary-confirmed` | section lifts feed derived reader surfaces and must preserve markdown authority through rebuild/check workflow |
| `AOA-T-0034` `public-safe-artifact-sanitization` | public-share approval | `orchestration-boundary-confirmed` | sanitization touches disclosure safety and cannot approve sharing by itself |
| `AOA-T-0024` `upstream-mirroring-with-provenance` | external provenance | `orchestration-boundary-confirmed` | upstream-owned material, manifests, and resync posture need provenance controls beyond one local copy |
| `AOA-T-0025` `capability-spec-versioning` | capability contract mutation | `orchestration-boundary-confirmed` | versioned capability specs can affect registry consumers and need contract review |
| `AOA-T-0027` `cross-agent-skill-propagation` | managed instruction propagation | `orchestration-boundary-confirmed` | skill/rule propagation to multiple targets needs canonical-source, target, and approval boundaries |
| `AOA-T-0030` `fragmented-agent-context` | instruction partitioning | `orchestration-boundary-confirmed` | context fragments can carry sensitive instruction scope and require source/assembly controls |
| `AOA-T-0040` `skill-vs-command-boundary` | capability public boundary | `orchestration-boundary-confirmed` | separating reusable skill meaning from command invocation can affect public capability and acceptance surfaces |
| `AOA-T-0041` `skill-marketplace-curation` | external discovery curation | `orchestration-boundary-confirmed` | curated discoverability over upstream skill sources needs editorial, provenance, and external-evidence controls |
| `AOA-T-0046` `repo-doc-surface-lift` | generated route lift | `orchestration-boundary-confirmed` | authoritative docs/status files become derived routing knowledge and must not replace source truth |
| `AOA-T-0047` `github-review-template-lift` | generated intake lift | `orchestration-boundary-confirmed` | GitHub templates can shape intake behavior and must not become automation or policy scoring |
| `AOA-T-0048` `semantic-review-surface-lift` | generated review lift | `orchestration-boundary-confirmed` | semantic-review docs can guide boundary review but must not create automatic verdicts |
| `AOA-T-0063` `versioned-agent-registry-contract` | public registry contract | `orchestration-boundary-confirmed` | registry-facing records and metadata can affect public discovery and compatibility posture |
| `AOA-T-0064` `capability-discovery` | registry lookup | `orchestration-boundary-confirmed` | published capability lookup can drift into ranking, marketplace curation, trust policy, or product doctrine |
| `AOA-T-0094` `canonical-owner-with-validated-mirror` | owner mirror parity | `orchestration-boundary-confirmed` | cross-repo canonical owner and local mirror parity need validation beyond one local read |
| `AOA-T-0006` `latest-alias-plus-history-copy` | public summary storage | `orchestration-boundary-confirmed` | dual-write latest/history summary storage mutates public artifacts and can double-count without workflow control |
| `AOA-T-0007` `signal-first-gate-promotion` | irreversible proof gate | `orchestration-boundary-confirmed` | promoting a signal to strict enforcement can become irreversible and needs staged approval |
| `AOA-T-0008` `published-summary-remediation-snapshot` | public remediation summary | `orchestration-boundary-confirmed` | remediation snapshots touch published summaries and must not replay history or overclaim runtime state |
| `AOA-T-0010` `telemetry-integrity-snapshot` | public integrity summary | `orchestration-boundary-confirmed` | integrity verdicts over summaries need proof and public-share controls despite read-only intent language |
| `AOA-T-0011` `required-vs-optional-source-rendering` | degraded public rendering | `orchestration-boundary-confirmed` | hard/soft source rendering can hide real failures unless generated and published through a guarded workflow |
| `AOA-T-0037` `contextual-host-doctor` | host readiness | `orchestration-boundary-confirmed` | selector-aware host checks touch current runtime environment and pre-start decisions |
| `AOA-T-0042` `upstream-skill-health-checking` | external health check | `orchestration-boundary-confirmed` | upstream availability and manifest readiness require external-evidence and security-sensitive checks |
| `AOA-T-0097` `degrade-reground-recover` | degraded recovery | `orchestration-boundary-confirmed` | degraded continuation must reground against stronger sources and avoid hidden repair theater |
| `AOA-T-0099` `isolated-service-stop-on-shared-substrate` | runtime stop | `orchestration-boundary-confirmed` | stopping one service while preserving shared substrate mutates live state and needs verification |
| `AOA-T-0100` `stress-receipt-reground-closeout` | stress closeout | `orchestration-boundary-confirmed` | stress receipts and closeout evidence need owner routing before later proof reading |
| `AOA-T-0098` `receipt-first-failure-analysis` | failure review | `orchestration-boundary-confirmed` | failure analysis starts from receipts but may route recovery changes and must separate facts from hypotheses |
| `AOA-T-0044` `versionable-session-transcripts` | history privacy | `orchestration-boundary-confirmed` | transcript packaging needs privacy, redaction, versioning, and public-safe sharing controls |

## Wrapper Types

The reviewed rows point to these reusable wrapper classes:

| wrapper class | examples | note |
|---|---|---|
| mutation and verification | `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0038`, `AOA-T-0099` | real state changes need planning, approval, rollback, and validation outside the atom |
| runtime and host truth | `AOA-T-0036`, `AOA-T-0037`, `AOA-T-0093` | host capability and rendered runtime truth are not portable technique authority |
| generated/public publish | `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, `AOA-T-0011`, `AOA-T-0096` | generated or public surfaces require rebuild, parity, and disclosure controls |
| tool and external source mediation | `AOA-T-0065`, `AOA-T-0041`, `AOA-T-0042`, `AOA-T-0074` | connectors, upstreams, and exports need provenance and security wrappers |
| review and owner pressure | `AOA-T-0078`, `AOA-T-0079`, `AOA-T-0105`, `AOA-T-0107` | tiny review moves still need social/review-state bounds |
| recovery and degraded mode | `AOA-T-0082`, `AOA-T-0083`, `AOA-T-0097`, `AOA-T-0098`, `AOA-T-0100` | degraded continuation must remain evidence-linked and owner-routed |
| instruction and capability distribution | `AOA-T-0013`, `AOA-T-0025`, `AOA-T-0027`, `AOA-T-0063`, `AOA-T-0064` | managed instruction or registry surfaces can affect downstream agents |
| media and history safety | `AOA-T-0070` through `AOA-T-0074`, `AOA-T-0044` | media/transcript pipelines need confidence, privacy, and retention controls |

## Medium Edge Revisited

`AOA-T-0095` `github-only-owner-endcap-with-reality-sync` is still a
`medium-agent` row in the current scout. Phase 2 flagged it because direct
reading shows a GitHub-native issue/PR/CI/merge lane plus post-merge
coordination sync.

Phase 3 does not relabel it, but it should be carried to Phase 5 as a concrete
profile-pressure example:

- if the technique is used only to compare owner anchors and coordination
  truth after merge, `medium-agent` is plausible;
- if the technique includes opening, driving, validating, and merging the
  GitHub owner-side landing, `orchestration-required` is the more honest
  execution envelope.

That distinction may need registry wording, scout-rule nuance, or a future leaf
split. It is not repaired in this packet.

## Calibration Notes

- The strongest current rule: orchestration is about authority and side-effect
  boundaries, not only task length.
- Read-only rows can still be orchestration-required when they touch host
  actionability, external source trust, generated truth, owner mirrors,
  public-share claims, or review pressure.
- The current scout values are broadly coherent; no mass relabel is justified.
- The likely Phase 5 question is wording: make it easier to explain "medium
  for comparison; orchestration for execution side effects."
- Actual harness execution for orchestration rows belongs outside
  `aoa-techniques`; this repo should carry technique shape and future fixture
  contrast, not tool choreography proof.

## Useful Threads

Carry these forward:

- Phase 4 should include negative fixtures that test small-agent refusal when a
  row secretly needs an outer wrapper.
- Phase 5 should inspect `AOA-T-0095` and the public-summary rows for profile
  wording pressure.
- Phase 6 repair queue is likely small, not broad: direct reading found one
  likely profile-edge, not widespread bundle ambiguity.
- Phase 7 empirical harness should route orchestration proof to `aoa-evals` or
  owner workflows rather than trying to run side-effecting orchestration inside
  `aoa-techniques`.

## Stop Lines

- Do not relabel rows from this packet alone.
- Do not treat `orchestration-required` as a defect.
- Do not mutate technique leaves, generated scout rules, registry wording, or
  frontmatter in this wave.
- Do not move runtime, host, tool, connector, GitHub merge, public-share
  approval, proof verdict, recovery repair, memory, transcript privacy, or KAG
  graph authority into `aoa-techniques`.

## Validation

This packet is a review-only source artifact. Required validation after landing
this wave:

1. `python -m unittest tests.test_distillation_mechanics_topology`
2. `python scripts/validate_repo.py`
3. `python scripts/release_check.py` before GitHub merge
