# Distillation Landing Log

This log records structural landings for the `aoa-techniques` Distillation
mechanic.

## 2026-05-18 - Incoming packet evidence-only closeout

Changed:

- moved all closed root `incoming/` packet roots into
  [closed incoming packets](legacy/archive/closed-incoming-packets/README.md)
  after their first-pass landing queues were exhausted
- moved active intake ownership to
  [Candidate Intake](parts/candidate-intake/README.md)
- removed packet-local `candidate_bundles/**` seed drafts for already landed
  techniques so archived packet evidence no longer duplicates canonical bundle
  meaning
- closed all non-landed packet tails as `closed-no-import` in packet docs and
  support registries:
  `markdown-definition-of-done-defaults`, `agent-readiness-telemetry`,
  `signed-trace-artifacts`, `semantic-linkage-records`,
  `preflight-reputation-check`, and
  `telegram-account-auth-and-session-bridge`
- kept `governed-action-surfaces` as a closed explicit exclusion from the
  handoff packet
- recorded the source-of-truth decision in
  [incoming evidence-only closeout](../../docs/decisions/AOA-TECH-D-0063-incoming-evidence-only-closeout.md)
- recorded the archive placement decision in
  [closed incoming packets Distillation legacy](../../docs/decisions/AOA-TECH-D-0062-closed-incoming-packets-distillation-legacy.md)

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no closed non-import candidate became a technique bundle
- no technique ID, frontmatter field, generated reader, schema, or kind/domain
  contract changed
- no donor auth, runtime, graph, analytics, scanner, or governance-platform
  doctrine was imported into canon

## 2026-05-14 - Technique reform scout script homes

Changed:

- moved `build_topology_scout.py` and `build_tree_projection.py` from root
  `scripts/` into
  [technique reform scripts](parts/technique-reform-ingress/scripts/)
- kept shared parsing and validation logic in root `scripts/validate_repo.py`
  because it still validates repo-wide generated parity and frontmatter
  contracts
- updated release-check, validators, docs, tests, and generated report command
  hints to use the part-local command paths
- recorded the placement rationale in
  [mechanic-script-homes](../../docs/decisions/AOA-TECH-D-0048-mechanic-script-homes.md)

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- root `scripts/validate_repo.py` remains the repo-wide validator and shared
  helper surface
- root `scripts/build_kind_manifest.py` remains root because it writes root
  generated kind manifests and reader docs as well as mechanic reports

## 2026-05-14 - Technique reform scout input homes

Changed:

- moved scout-only family and topology input registries from root `config/`
  into [technique reform config](parts/technique-reform-ingress/config/)
- moved kind-overlay YAML/CSV data from root `data/` into
  [technique reform data](parts/technique-reform-ingress/data/)
- kept root `config/technique_kind_registry.yaml` as the repo-wide current
  `kind` contract
- updated builders, validators, generated report source maps, docs, and tests
  so scout inputs route through the Distillation part that interprets them

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- root `config/technique_kind_registry.yaml` remains the current `kind`
  registry
- no technique bundle, frontmatter field, status, relation, or schema changed
- no scout-only input became frontmatter truth or automatic remap authority

## 2026-05-14 - Technique reform reports mechanics home

Changed:

- moved generated scout and projection reports from root `reports/` into
  [technique reform reports](parts/technique-reform-ingress/reports/)
- updated report builders, validators, and tests to use the mechanic-local
  report home
- updated root, docs, legacy, and review links so `reports/` is not treated as
  the current root home for technique-reform evidence
- regenerated kind, family, topology, and tree scout reports with relative links
  from the deeper mechanic-local route
- recorded the placement rationale in
  [technique-reform-report-home](../../docs/decisions/AOA-TECH-D-0055-technique-reform-report-home.md)

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no technique frontmatter, status, or relation changed
- no generated report became source truth
- no proof, eval, or public-share authority was imported into Distillation

## 2026-05-14 - Review packet mechanics home

Changed:

- moved authored semantic-review packets from flat `docs/` into
  [semantic review packets](parts/technique-reform-ingress/reviews/semantic/)
- moved authored shadow-review packets from flat `docs/` into
  [shadow review packets](parts/technique-reform-ingress/reviews/shadow/)
- kept public reader routes in `docs/review/SEMANTIC_REVIEW_GUIDE.md`,
  `docs/readers/selection/SELECTION_PATTERNS.md`,
  `docs/review/TECHNIQUE_SHADOW_GUIDE.md`, and
  `docs/readers/review/SHADOW_PATTERNS.md`
- updated the semantic and shadow manifests so the mechanics packet paths are
  the source paths, not aliases back to `docs/`
- recorded the placement rationale in
  [review-packet-mechanics-home](../../docs/decisions/AOA-TECH-D-0051-review-packet-mechanics-home.md)

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no technique frontmatter, status, or relation changed
- no generated output became source truth
- historical raw legacy receipts were not rewritten

## 2026-05-06 - Roadmap contour cleanup

Changed:

- slimmed `ROADMAP.md` back to future contour after the completed tree migration
  program
- left checked migration history in
  [Technique Reform Ingress reviews](parts/technique-reform-ingress/reviews/),
  especially the
  [final tree migration ledger](parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md)
- kept `LANDING_LOG.md`, `PROVENANCE.md`, and `legacy/` as the source route for
  landed history and lineage instead of making the roadmap a ledger

Not moved:

- no technique bundle moved
- no frontmatter changed
- no generated output became source truth
- no source receipt was deleted

## 2026-05-05 - Final tree migration ledger

Changed:

- added
  [final-tree-migration-ledger](parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md)
  as the permanent closeout ledger for the tree migration program
- confirmed `107/107` current paths still match generated projection paths
- confirmed `28/28` current shelves have root legacy tree-pilot receipts
- confirmed direct two-level technique leaves remain `0`
- confirmed split, singleton, and unassigned projection holds remain `0`
- distilled the temporary plan into permanent route surfaces and routed next
  work toward technique-bundle reform

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no generated output became source truth
- the temporary plan was not committed as an authority surface

## 2026-05-05 - Tree route-card consolidation

Changed:

- updated the root `techniques/AGENTS.md` route card to name the current
  authored bundle shape as
  `techniques/<trunk>/<shelf>/<slug>/TECHNIQUE.md`
- consolidated all current trunk route cards around current shelves, trunk
  rules, and the no-`tree_path` boundary
- kept `agent-workflows`, `docs`, and `evaluation` as retained frontmatter
  review lanes with no active direct leaf bundle
- expanded `scripts/validate_nested_agents.py` so every current trunk and
  retained lane is validator-backed
- moved the next bounded step to the final migration ledger and generated
  parity pass

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added
- no generated output became source truth

## 2026-05-05 - Whole-tree closeout review

Changed:

- added
  [whole-tree-closeout-review](parts/technique-reform-ingress/reviews/whole-tree-closeout-review.md)
  as the closeout packet for the first full technique tree migration pass
- confirmed the current tree covers `107` bundles across `10` trunks and `28`
  shelves
- confirmed `107/107` current paths match projected paths and no old
  two-level direct broad-domain leaves remain under `techniques/`
- confirmed `28/28` shelves have root legacy receipts
- confirmed `split-review-needed`, `singleton-hold`, and `unassigned-hold`
  projection rows are all `0`
- moved the next bounded step to tree route-card consolidation

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added
- no generated projection row became source truth

## 2026-05-05 - Landed tool-gateway pilot review

Changed:

- added
  [landed-tool-gateway-pilot-review](parts/technique-reform-ingress/reviews/landed-tool-gateway-pilot-review.md)
  as the post-migration review for the first `tool-use` trunk shelf
- confirmed `AOA-T-0065` stayed promoted, kept
  `domain: agent-workflows`, and preserved `kind: composition` after landing
- accepted the singleton as resolved by direct reading, not as a generic
  leftover bucket
- confirmed `techniques/agent-workflows/AGENTS.md` is now a retained
  frontmatter review lane with no active direct leaf bundle
- selected whole-tree closeout review as the next bounded reform step

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no runtime, connector, marketplace, scanner, trust, or skill authority moved

## 2026-05-05 - Tool-gateway tree pilot migration

Changed:

- moved `AOA-T-0065` from `techniques/agent-workflows/` into
  `techniques/tool-use/tool-gateway/`
- added the root legacy receipt
  [2026-05-05-tool-gateway-tree-pilot](../../legacy/receipts/2026-05-05-tool-gateway-tree-pilot.md)
- added the compact `tool-use` trunk route card and updated
  `agent-workflows` as a retained frontmatter review lane with no active
  direct leaf bundles
- repaired active adjacent links into runtime lifecycle, skill-discovery, and
  capability-registry leaves
- preserved the bundle as `domain: agent-workflows`, `kind: composition`,
  `status: promoted`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no runtime, connector, marketplace, scanner, trust, or skill authority moved

## 2026-05-05 - Tool-gateway direct-read singleton review

Changed:

- added
  [tool-gateway-direct-read-singleton-review](parts/technique-reform-ingress/reviews/tool-gateway-direct-read-singleton-review.md)
  as the direct-read review over `AOA-T-0065`
- accepted `tool-use/tool-gateway` as the twenty-eighth bounded migration
  pilot without moving files
- treated the former singleton hold as resolved by direct reading: the old hold
  was useful while larger split pressure remained, but `AOA-T-0065` is now the
  last broad `agent-workflows` representative and has one honest tool-use home
- preserved `AOA-T-0065` as `domain: agent-workflows`, `kind: composition`,
  `status: promoted`
- kept MCP platform ownership, API gateway product doctrine, connector
  registry authority, tool marketplace curation, security-scanner doctrine,
  trust scoring, runtime deployment ownership, skill activation, and canonical
  promotion outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no `tool-use/tool-gateway` shelf moved yet

## 2026-05-05 - Landed practice-adoption-lifecycle pilot review

Changed:

- added
  [landed-practice-adoption-lifecycle-pilot-review](parts/technique-reform-ingress/reviews/landed-practice-adoption-lifecycle-pilot-review.md)
  as the post-migration review for the third automation-governance split shelf
- confirmed `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104` stayed promoted,
  kept `domain: agent-workflows`, and preserved their `guardrail`,
  `assessment`, and `handoff` kind split after landing
- closed the rejected bulk `automation-governance` route with all nine split
  IDs accounted across `automation-readiness`, `promotion-boundary`, and
  `practice-adoption-lifecycle`
- selected `tool-use/tool-gateway` for direct-read singleton review before
  any twenty-eighth movement

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no `tool-use/tool-gateway` shelf moved

## 2026-05-05 - Practice-adoption-lifecycle tree pilot migration

Changed:

- moved `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104` from
  `techniques/agent-workflows/` into
  `techniques/governance/practice-adoption-lifecycle/`
- added the root legacy receipt
  [2026-05-05-practice-adoption-lifecycle-tree-pilot](../../legacy/receipts/2026-05-05-practice-adoption-lifecycle-tree-pilot.md)
- updated governance and agent-workflows route-card accounting for the new
  shelf
- repaired active adjacent links into the moved practice-adoption-lifecycle
  leaves and existing decision-routing, promotion-boundary, audit,
  experience, growth-cycle, and Method-growth surfaces
- preserved all three bundles as `domain: agent-workflows`, while keeping
  `kind: guardrail`, `kind: assessment`, and `kind: handoff` respectively

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no `tool-use/tool-gateway` shelf moved

## 2026-05-05 - Practice-adoption-lifecycle direct-read migration review

Changed:

- added
  [practice-adoption-lifecycle-direct-read-migration-review](parts/technique-reform-ingress/reviews/practice-adoption-lifecycle-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104`
- accepted `governance/practice-adoption-lifecycle` as the twenty-seventh
  bounded migration pilot without moving files
- kept the shelf centered on local adoption gate, adopted-practice retention,
  and obsolescence route posture
- preserved `AOA-T-0101` as `domain: agent-workflows`, `kind: guardrail`,
  `status: promoted`
- preserved `AOA-T-0103` as `domain: agent-workflows`, `kind: assessment`,
  `status: promoted`
- preserved `AOA-T-0104` as `domain: agent-workflows`, `kind: handoff`,
  `status: promoted`
- kept Method-growth law, local owner consent, deletion, deprecation
  execution, proof authority, memory truth, skill activation, route mutation,
  runtime change, permanent practice retention, sibling owner acceptance, and
  the tool-use singleton outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no bundle was promoted to canonical
- no `tool-use/tool-gateway` shelf moved

## 2026-05-05 - Landed promotion-boundary pilot review

Changed:

- added
  [landed-promotion-boundary-pilot-review](parts/technique-reform-ingress/reviews/landed-promotion-boundary-pilot-review.md)
  as the post-migration review for the second automation-governance split shelf
- validated `governance/promotion-boundary` as the second landed split shelf
  after migration
- confirmed the moved bundles kept `domain: agent-workflows`, `status:
  promoted`, and their separate `kind: assessment`, `kind: guardrail`, and
  `kind: handoff` values
- selected `governance/practice-adoption-lifecycle` for direct-read review
  before any twenty-seventh movement

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no Candidate C or `tool-use/tool-gateway` shelf was accepted yet

## 2026-05-05 - Promotion-boundary tree pilot migration

Changed:

- moved `AOA-T-0089`, `AOA-T-0090`, and `AOA-T-0102` from
  `techniques/agent-workflows/` into
  `techniques/governance/promotion-boundary/`
- added the root legacy receipt
  [2026-05-05-promotion-boundary-tree-pilot](../../legacy/receipts/2026-05-05-promotion-boundary-tree-pilot.md)
- updated governance and agent-workflows route-card accounting for the new
  shelf
- repaired active adjacent links into the moved promotion-boundary leaves and
  existing decision-routing, automation-readiness, instruction, and
  agent-workflows leaves
- preserved all three bundles as `domain: agent-workflows`, while keeping
  `kind: assessment`, `kind: guardrail`, and `kind: handoff` respectively

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no `governance/practice-adoption-lifecycle` or `tool-use/tool-gateway`
  shelf moved

## 2026-05-05 - Promotion-boundary direct-read migration review

Changed:

- added
  [promotion-boundary-direct-read-migration-review](parts/technique-reform-ingress/reviews/promotion-boundary-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0089`, `AOA-T-0090`, and `AOA-T-0102`
- accepted `governance/promotion-boundary` as the twenty-sixth bounded
  migration pilot without moving files
- kept the shelf centered on promotion verdict, nearest-wrong-target
  rejection, and skill-proposal handoff boundaries
- preserved all three bundles as `domain: agent-workflows` while keeping
  `kind: assessment`, `kind: guardrail`, and `kind: handoff` respectively
- kept skill acceptance, skill activation, quest/playbook promotion doctrine,
  role contract law, proof verdict authority, memory write, routing policy,
  Method-growth law, local owner consent, runtime behavior, KAG promotion,
  ToS canon, broad orchestration governance, Candidate C, and the tool-use
  singleton outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no bundle was promoted to canonical
- no `governance/practice-adoption-lifecycle` or `tool-use/tool-gateway`
  shelf moved

## 2026-05-05 - Landed automation-readiness pilot review

Changed:

- added
  [landed-automation-readiness-pilot-review](parts/technique-reform-ingress/reviews/landed-automation-readiness-pilot-review.md)
  as the post-migration review for the first automation-governance split shelf
- validated `governance/automation-readiness` as the first landed split shelf
  after migration
- confirmed all three moved bundles kept `domain: agent-workflows`,
  `kind: assessment`, and `status: promoted`
- selected `governance/promotion-boundary` for direct-read review before any
  twenty-sixth movement

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no Candidate B or Candidate C shelf was accepted yet

## 2026-05-05 - Automation-readiness tree pilot migration

Changed:

- moved `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` from
  `techniques/agent-workflows/` into
  `techniques/governance/automation-readiness/`
- added the root legacy receipt
  [2026-05-05-automation-readiness-tree-pilot](../../legacy/receipts/2026-05-05-automation-readiness-tree-pilot.md)
- updated governance and agent-workflows route-card accounting for the new
  shelf
- repaired active adjacent links into the moved automation-readiness leaves
  and existing decision-routing leaves
- preserved all three bundles as `domain: agent-workflows`, `kind:
  assessment`, and `status: promoted`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no `governance/promotion-boundary`,
  `governance/practice-adoption-lifecycle`, or `tool-use/tool-gateway` shelf
  moved

## 2026-05-05 - Automation-readiness direct-read migration review

Changed:

- added
  [automation-readiness-direct-read-migration-review](parts/technique-reform-ingress/reviews/automation-readiness-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088`
- accepted `governance/automation-readiness` as the twenty-fifth bounded
  migration pilot without moving files
- kept the shelf centered on automation fit classification, first honest
  landing, and approval-sensitivity burden
- preserved all three bundles as `domain: agent-workflows`, `kind:
  assessment`, and `status: promoted`
- kept automation policy authority, seed canon, skill acceptance, skill
  activation, scheduler doctrine, hidden automation governance, route
  mutation, memory write, runtime behavior, KAG promotion, ToS canon, broad
  orchestration governance, Candidate B, Candidate C, and the tool-use
  singleton outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no frontmatter changed
- no bundle was promoted to canonical
- no `governance/promotion-boundary`,
  `governance/practice-adoption-lifecycle`, or `tool-use/tool-gateway` shelf
  moved

## 2026-05-05 - Automation-governance split expansion closeout

Changed:

- added
  [automation-governance-split-expansion-closeout](parts/technique-reform-ingress/reviews/automation-governance-split-expansion-closeout.md)
  as the route closeout for the rejected bulk automation-governance shelf
- activated Candidate A as `governance/automation-readiness` over
  `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088`
- kept Candidate B as `governance/promotion-boundary` over `AOA-T-0089`,
  `AOA-T-0090`, and `AOA-T-0102`
- kept Candidate C as `governance/practice-adoption-lifecycle` over
  `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104`
- preserved all nine bundles at current paths with no frontmatter changes

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle moved
- no split candidate was accepted or migrated yet
- no `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added
- no automation policy authority, skill acceptance, skill activation,
  Method-growth law, local owner consent, deletion, proof authority, memory
  truth, routing policy, runtime behavior, or broad orchestration governance
  moved

## 2026-05-05 - Automation-governance direct-read split review

Changed:

- added
  [automation-governance-direct-read-split-review](parts/technique-reform-ingress/reviews/automation-governance-direct-read-split-review.md)
  as the direct-read review over `AOA-T-0086`, `AOA-T-0087`, `AOA-T-0088`,
  `AOA-T-0089`, `AOA-T-0090`, `AOA-T-0101`, `AOA-T-0102`, `AOA-T-0103`, and
  `AOA-T-0104`
- rejected one bulk `governance/automation-governance` migration shelf before
  movement
- named `governance/automation-readiness`,
  `governance/promotion-boundary`, and
  `governance/practice-adoption-lifecycle` as split candidates
- preserved all nine bundles at their current `techniques/agent-workflows/`
  paths with frontmatter unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no automation-governance bundle moved
- no split candidate shelf was migrated yet
- no `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added
- no automation policy authority, seed canon, skill acceptance, skill
  activation, quest/playbook promotion doctrine, Method-growth law, local owner
  consent, deletion, deprecation execution, proof authority, memory truth,
  routing policy, runtime behavior, broad orchestration governance, or
  `tool-use/tool-gateway` singleton hold moved

## 2026-05-05 - Landed owner-truth-closeout pilot review

Changed:

- added
  [landed-owner-truth-closeout-pilot-review](parts/technique-reform-ingress/reviews/landed-owner-truth-closeout-pilot-review.md)
  as the landed review for the twenty-fourth tree pilot
- accepted `owner-truth-closeout` as a successful migrated shelf and the fifth
  proof trunk shelf
- confirmed ingress guard, audit closeout, remote owner endcap, generated
  publish validation, and mirror parity stayed separate one-use atoms under
  one owner-truth closeout shelf
- chose `governance/automation-governance` for direct-read split review before
  any twenty-fifth shelf movement
- preserved all five landed `owner-truth-closeout` bundles as promoted and
  kept their `domain`, `kind`, evidence, support files, and path receipt
  unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no `governance/automation-governance` bundle moved
- no `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added
- no automation policy authority, seed canon, skill acceptance, skill
  activation, quest/playbook promotion doctrine, route mutation, memory write,
  runtime behavior, KAG promotion, ToS canon, broad orchestration governance,
  or `tool-use/tool-gateway` singleton hold moved

## 2026-05-05 - Owner-truth-closeout tree pilot migration

Changed:

- moved exactly `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, `AOA-T-0096`, and
  `AOA-T-0094` into `techniques/proof/owner-truth-closeout/`
- kept `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, and `AOA-T-0096` as
  `domain: agent-workflows`
- kept `AOA-T-0094` as `domain: docs`
- kept `AOA-T-0091` as `kind: guardrail`, `AOA-T-0092` and `AOA-T-0095` as
  `kind: workflow`, `AOA-T-0096` as `kind: validation`, and `AOA-T-0094` as
  `kind: distribution`
- added
  [2026-05-05-owner-truth-closeout-tree-pilot](../../legacy/receipts/2026-05-05-owner-truth-closeout-tree-pilot.md)
  as the root legacy receipt for the twenty-fourth migration
- updated the proof route card to name `owner-truth-closeout/` as bounded
  owner-truth entry, closeout, remote-owner, generated-publish, and mirror
  validation support rather than owner law

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no AoA constitutional authority, root `AGENTS.md` law, workspace install
  doctrine, public-share approval policy, GitHub platform policy, release
  governance, cross-repo mirror co-ownership, skill activation, checkpoint
  automation, closeout automation, route mutation, memory write, runtime
  behavior, KAG promotion, ToS canon, `aoa-evals` verdict authority, or
  neighboring automation/tool-use shelf moved

## 2026-05-05 - Owner-truth-closeout direct-read migration review

Changed:

- added
  [owner-truth-closeout-direct-read-migration-review](parts/technique-reform-ingress/reviews/owner-truth-closeout-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`,
  `AOA-T-0096`, and `AOA-T-0094`
- accepted `proof/owner-truth-closeout` as the twenty-fourth bounded migration
  pilot without moving files
- kept the shelf centered on owner-truth entry, proof-backed finding closeout,
  GitHub-native owner endcaps, workflow-pinned generated publish validation,
  and canonical-owner mirror parity
- preserved `AOA-T-0091` as `kind: guardrail`, `AOA-T-0092` and
  `AOA-T-0095` as `kind: workflow`, `AOA-T-0096` as `kind: validation`,
  `AOA-T-0094` as `kind: distribution`, and all five bundles as `status:
  promoted`
- kept AoA constitutional authority, root `AGENTS.md` law, workspace install
  doctrine, public-share approval policy, GitHub platform policy, release
  governance, cross-repo mirror co-ownership, skill activation, checkpoint
  automation, closeout automation, route mutation, memory writes, runtime
  behavior, KAG promotion, ToS canon, `aoa-evals` verdict authority, and
  neighboring automation/tool-use shelves outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique paths changed
- no frontmatter changed
- no `proof/owner-truth-closeout` route card or receipt was created
- no `governance/automation-governance` or `tool-use/tool-gateway` shelf moved

## 2026-05-05 - Landed runtime-truth-lifecycle pilot review

Changed:

- added
  [landed-runtime-truth-lifecycle-pilot-review](parts/technique-reform-ingress/reviews/landed-runtime-truth-lifecycle-pilot-review.md)
  as the landed review for the twenty-third tree pilot migration
- validated `runtime-truth-lifecycle` as the fourth execution trunk shelf after
  migration
- kept render truth, local lifecycle, host readiness, and baseline-first
  comparison as distinct runtime-adjacent atoms
- chose `proof/owner-truth-closeout` for direct-read migration review before
  any twenty-fourth shelf movement

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique paths changed
- no frontmatter changed
- no `proof/owner-truth-closeout` route card or receipt was created
- no AoA constitutional authority, root `AGENTS.md` law, workspace install
  doctrine, public-share approval policy, GitHub platform policy, release
  governance, cross-repo mirror co-ownership, skill activation, checkpoint
  automation, closeout automation, or neighboring automation/tool-use shelf
  moved

## 2026-05-05 - Runtime-truth-lifecycle tree pilot migration

Changed:

- moved exactly `AOA-T-0036`, `AOA-T-0038`, `AOA-T-0037`, and `AOA-T-0039`
  into `techniques/execution/runtime-truth-lifecycle/`
- kept `AOA-T-0036` and `AOA-T-0038` as `domain: agent-workflows`
- kept `AOA-T-0037` and `AOA-T-0039` as `domain: evaluation`
- kept `AOA-T-0036` as `kind: composition`, `AOA-T-0038` as `kind:
  workflow`, and `AOA-T-0037` plus `AOA-T-0039` as `kind: validation`
- added
  [2026-05-05-runtime-truth-lifecycle-tree-pilot](../../legacy/receipts/2026-05-05-runtime-truth-lifecycle-tree-pilot.md)
  as the root legacy receipt for the twenty-third migration
- updated the execution route card to name `runtime-truth-lifecycle/` as local
  runtime truth, lifecycle, readiness, and baseline-first comparison
  discipline rather than runtime owner law

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no `abyss-stack` runtime law, deployment ownership, monitoring platform
  doctrine, host policy, smoke-test law, benchmark-suite governance, product
  scoring, `aoa-evals` verdict authority, or neighboring owner/governance/tool
  shelf moved

## 2026-05-05 - Runtime-truth-lifecycle direct-read migration review

Changed:

- added
  [runtime-truth-lifecycle-direct-read-migration-review](parts/technique-reform-ingress/reviews/runtime-truth-lifecycle-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0036`, `AOA-T-0038`, `AOA-T-0037`,
  and `AOA-T-0039`
- accepted `execution/runtime-truth-lifecycle` as the twenty-third bounded
  migration pilot without moving files
- kept the shelf centered on four runtime-adjacent execution moves: render
  actual runtime truth, operate one local lifecycle entrypoint, check
  selector-aware host readiness, and compare additive profiles against one
  stable baseline shape
- preserved `AOA-T-0036` as `kind: composition`, `AOA-T-0038` as `kind:
  workflow`, `AOA-T-0037` and `AOA-T-0039` as `kind: validation`, and all four
  bundles as `status: promoted`
- kept `abyss-stack` runtime law, deployment ownership, monitoring platform
  doctrine, host policy, smoke-test law, benchmark-suite governance, product
  scoring, `aoa-evals` verdict authority, route mutation, memory writes,
  runtime behavior, KAG promotion, ToS canon, skill activation, and neighboring
  owner/governance/tool-use shelves outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `execution/runtime-truth-lifecycle` route card or receipt was created

## 2026-05-05 - Landed review-evidence pilot review

Changed:

- added
  [landed-review-evidence-pilot-review](parts/technique-reform-ingress/reviews/landed-review-evidence-pilot-review.md)
  as the review over the landed `proof/review-evidence` migration
- validated the fourth successful proof trunk shelf after `skill-support`,
  `evaluation-chain`, and `published-summary`
- kept `AOA-T-0107` as one claim-locus challenge, `AOA-T-0105` as one
  missing-evidence request, and `AOA-T-0106` as one scoped evidence reference
- preserved `AOA-T-0107` and `AOA-T-0105` as `kind: guardrail`, `AOA-T-0106`
  as `kind: artifact`, and all three bundles as `status: promoted`
- chose `execution/runtime-truth-lifecycle` for direct-read review before any
  twenty-third shelf movement

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `execution/runtime-truth-lifecycle` route card or receipt was created
- no `abyss-stack` runtime law, deployment ownership, monitoring platform
  doctrine, host policy, smoke-test law, benchmark-suite governance, product
  scoring, or `aoa-evals` verdict authority was imported

## 2026-05-05 - Review-evidence tree pilot migration

Changed:

- moved exactly `AOA-T-0107`, `AOA-T-0105`, and `AOA-T-0106` into
  `techniques/proof/review-evidence/`
- kept `AOA-T-0107` and `AOA-T-0105` as `domain: agent-workflows`,
  `kind: guardrail`, `status: promoted`
- kept `AOA-T-0106` as `domain: docs`, `kind: artifact`,
  `status: promoted`
- added
  [2026-05-05-review-evidence-tree-pilot](../../legacy/receipts/2026-05-05-review-evidence-tree-pilot.md)
  as the root legacy receipt for the twenty-second migration
- updated the proof route card to name `review-evidence/` as bounded review
  evidence rather than proof verdict authority, eval-suite ownership,
  review-board workflow, Agon move law, actor eligibility, source-truth
  transfer, or evidence adequacy scoring

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no owner-truth, runtime, automation-governance, tool-use, or remaining
  `agent-workflows` and `docs` shelf moved

## 2026-05-05 - Review-evidence direct-read migration review

Changed:

- added
  [review-evidence-direct-read-migration-review](parts/technique-reform-ingress/reviews/review-evidence-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0107`, `AOA-T-0105`, and `AOA-T-0106`
- accepted `proof/review-evidence` as the twenty-second bounded migration
  pilot without moving files
- kept the shelf centered on three one-atom review-evidence moves: challenge
  one claim locus, request one missing evidence object, and offer one scoped
  evidence reference
- preserved `AOA-T-0107` and `AOA-T-0105` as `kind: guardrail`, `AOA-T-0106`
  as `kind: artifact`, and all three bundles as `status: promoted`
- kept proof verdict authority, eval-suite ownership, review-board workflow,
  Agon move law, actor eligibility, evidence adequacy scoring, source-truth
  transfer, route mutation, memory writes, runtime behavior, KAG promotion,
  ToS canon, skill activation, and neighboring proof/runtime/governance
  shelves outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `proof/review-evidence` route card or receipt was created

## 2026-05-05 - Landed approval-evidence pilot review

Changed:

- added
  [landed-approval-evidence-pilot-review](parts/technique-reform-ingress/reviews/landed-approval-evidence-pilot-review.md)
  as the review over the landed `governance/approval-evidence` migration
- validated the second successful governance trunk shelf after
  `decision-routing`
- preserved `AOA-T-0068` as the immediate fail-closed boundary gate and
  `AOA-T-0069` as the durable approval seam
- chose `proof/review-evidence` for direct-read review before any
  twenty-second shelf movement
- kept proof verdict authority, eval-suite ownership, review-board workflow,
  Agon move law, actor eligibility, route mutation, memory writes, runtime
  behavior, KAG promotion, ToS canon, skill activation, and neighboring
  runtime/owner/governance shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `proof/review-evidence` route card or receipt was created

## 2026-05-05 - Approval-evidence tree pilot migration

Changed:

- moved exactly `AOA-T-0068` and `AOA-T-0069` into
  `techniques/governance/approval-evidence/`
- kept `AOA-T-0068` as `domain: agent-workflows`, `kind: guardrail`,
  `status: promoted`
- kept `AOA-T-0069` as `domain: agent-workflows`, `kind: handoff`,
  `status: promoted`
- added
  [2026-05-05-approval-evidence-tree-pilot](../../legacy/receipts/2026-05-05-approval-evidence-tree-pilot.md)
  as the root legacy receipt for the twenty-first migration
- updated the governance route card to name `approval-evidence/` as boundary
  evidence rather than approval policy, security framework authority, runtime
  job-runner ownership, scheduler doctrine, queue ownership, or broad
  orchestration governance

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no frontmatter changed
- no bundle was promoted to canonical
- no proof, runtime, automation-governance, tool-use, or remaining
  `agent-workflows` shelf moved

## 2026-05-05 - Approval-evidence direct-read migration review

Changed:

- added
  [approval-evidence-direct-read-migration-review](parts/technique-reform-ingress/reviews/approval-evidence-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0068` and `AOA-T-0069`
- accepted `governance/approval-evidence` as the twenty-first bounded
  migration pilot without moving files
- kept the shelf centered on approval-shaped boundary evidence: one
  fail-closed execution gate and one approval-bound durable job seam
- preserved `AOA-T-0068` as `kind: guardrail`, `AOA-T-0069` as
  `kind: handoff`, and both bundles as `status: promoted`
- kept approval policy, security framework authority, trust-platform
  semantics, runtime job-runner ownership, scheduler doctrine, queue-product
  ownership, broad orchestration governance, and neighboring proof/runtime
  shelves outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `governance/approval-evidence` route card or receipt was created

## 2026-05-05 - Landed decision-routing pilot review

Changed:

- added
  [landed-decision-routing-pilot-review](parts/technique-reform-ingress/reviews/landed-decision-routing-pilot-review.md)
  as the landed review after the twentieth path migration
- validated `techniques/governance/decision-routing/` as the first successful
  governance trunk shelf
- confirmed the shelf remained local decision support rather than AoA
  constitutional authority, `aoa-routing` ownership, role contract law,
  runtime dispatch, approval policy, playbook design, hidden automation
  governance, risk scoring doctrine, or context-map doctrine
- chose `governance/approval-evidence` for the next direct-read migration
  review before any twenty-first shelf movement

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `governance/approval-evidence` route card or receipt was created
- no security framework authority, approval policy, runtime job-runner
  ownership, scheduler doctrine, trust-platform semantics, or broad
  orchestration governance was imported

## 2026-05-05 - Decision-routing tree pilot migration

Changed:

- moved exactly `AOA-T-0076`, `AOA-T-0078`, and `AOA-T-0079` into
  `techniques/governance/decision-routing/`
- added `techniques/governance/AGENTS.md` with compact governance trunk
  guidance
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-decision-routing-tree-pilot.md`
- repaired authored links from adjacent techniques and active mechanics or
  review sources to current paths
- kept `domain`, `kind`, status, IDs, evidence, relations, support files,
  maturity, validation-strength metadata, and public-safety posture unchanged
- preserved all three bundles as `status: promoted`; path movement did not
  imply canonical promotion

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no neighboring governance, proof, execution, tool-use, routing, role,
  approval, automation, or remaining `agent-workflows` shelf was moved
- no AoA constitutional authority, `aoa-routing` ownership, role contract law,
  runtime dispatch, approval policy, playbook design, hidden automation
  governance, risk scoring doctrine, or context-map doctrine was imported into
  the shelf

## 2026-05-05 - Decision-routing direct-read migration review

Changed:

- added
  [decision-routing-direct-read-migration-review](parts/technique-reform-ingress/reviews/decision-routing-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0076`, `AOA-T-0078`, and `AOA-T-0079`
- accepted `governance/decision-routing` as the twentieth bounded migration
  pilot without moving files
- kept the shelf centered on local decision support: one owner-layer verdict,
  explicit branch cards, and one small route-risk passport
- preserved all three bundles as `status: promoted` and kept `domain`, `kind`,
  IDs, evidence, relations, support files, maturity, validation-strength
  metadata, and public-safety posture unchanged
- kept AoA constitutional authority, `aoa-routing` ownership, role contract
  law, runtime dispatch, approval policy, playbook design, hidden automation
  governance, risk scoring doctrine, context-map doctrine, and neighboring
  boundary-watch shelves outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no governance route card was created
- no twentieth shelf migration landed from the review alone

## 2026-05-05 - Landed donor-harvest pilot review

Changed:

- added
  [landed-donor-harvest-pilot-review](parts/technique-reform-ingress/reviews/landed-donor-harvest-pilot-review.md)
  as the landed review after the nineteenth path migration
- validated `donor-harvest` as the third successful continuity trunk shelf
- confirmed the shelf remains reviewed-session continuity rather than memory
  authority, playbook quest authority, progression doctrine, owner routing,
  role progression, stats ownership, or session-closeout automation
- preserved `AOA-T-0077` as `kind: handoff` and `AOA-T-0075`, `AOA-T-0084`,
  and `AOA-T-0085` as `kind: lift`
- chose `governance/decision-routing` for the next direct-read migration
  review without moving files
- kept AoA constitutional authority, `aoa-routing` ownership, role contract
  law, runtime dispatch, approval policy, playbook design, hidden automation
  governance, and neighboring boundary-watch shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no governance route card was created
- no `tree_path` frontmatter was added

## 2026-05-05 - Donor-harvest tree pilot migration

Changed:

- moved exactly `AOA-T-0075`, `AOA-T-0077`, `AOA-T-0084`, and `AOA-T-0085`
  into `techniques/continuity/donor-harvest/`
- extended `techniques/continuity/AGENTS.md` with the third continuity shelf
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-donor-harvest-tree-pilot.md`
- repaired authored links from adjacent techniques and active review sources
  to current paths
- kept `domain`, `kind`, status, IDs, evidence, relations, support files,
  maturity, validation-strength metadata, and public-safety posture unchanged
- preserved all four bundles as `status: promoted`; path movement did not
  imply canonical promotion

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no neighboring continuity, governance, questbook, playbook, RPG, memory,
  stats, role, owner-route, or remaining `agent-workflows` shelf was moved
- no memory authority, playbook quest authority, progression doctrine, owner
  routing, role progression, stats ownership, or session-closeout automation
  was imported into the shelf

## 2026-05-05 - Donor-harvest direct-read migration review

Changed:

- added
  [donor-harvest-direct-read-migration-review](parts/technique-reform-ingress/reviews/donor-harvest-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0075`, `AOA-T-0077`, `AOA-T-0084`,
  and `AOA-T-0085`
- accepted `continuity/donor-harvest` as the nineteenth bounded migration
  pilot without moving files
- kept the shelf centered on reviewed-session continuity: donor candidates,
  one harvest packet contract, progression evidence, and an adjunct quest
  overlay
- preserved all four bundles as `status: promoted` and kept `domain`, `kind`,
  IDs, evidence, relations, support files, maturity, validation-strength
  metadata, and public-safety posture unchanged
- kept memory authority, playbook quest authority, progression doctrine, owner
  routing, role progression, stats ownership, session-closeout automation, and
  neighboring continuity or governance shelves outside the move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no nineteenth shelf migration landed from the review alone

## 2026-05-05 - Landed agent-workflows-core pilot review

Changed:

- added
  [landed-agent-workflows-core-pilot-review](parts/technique-reform-ingress/reviews/landed-agent-workflows-core-pilot-review.md)
  as the landed review after the eighteenth path migration
- validated `agent-workflows-core` as the third successful execution trunk
  shelf
- confirmed the shelf remains a bounded mixed-kind execution backbone rather
  than generic agent doctrine, shell policy, autonomous orchestration, or broad
  methodology
- preserved `AOA-T-0028` as `kind: guardrail` and `AOA-T-0031` as
  `kind: composition`
- chose `continuity/donor-harvest` for the next direct-read migration review
  without moving files
- kept memory authority, playbook quest authority, progression doctrine, owner
  routing, role progression, stats ownership, session-closeout automation, and
  neighboring continuity or governance shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `tree_path` frontmatter was added

## 2026-05-05 - Agent-workflows-core tree pilot migration

Changed:

- moved exactly `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`,
  and `AOA-T-0031` into
  `techniques/execution/agent-workflows-core/`
- extended the compact `techniques/execution/AGENTS.md` route card with the
  third execution shelf
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-agent-workflows-core-tree-pilot.md`
- repaired authored links from semantic reviews, audit evidence surfaces,
  active review sources, root docs, and current selection surfaces
- kept `domain`, `kind`, status, IDs, evidence, relations, support files,
  maturity, validation-strength metadata, and public-safety posture unchanged
- preserved `AOA-T-0028` as `kind: guardrail` and `AOA-T-0031` as
  `kind: composition`; path movement did not imply kind remap

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no remaining `agent-workflows` shelf was moved
- no generic agent doctrine, shell policy, product policy, approval policy,
  autonomous orchestration, hidden agent scheduling, runtime lifecycle law,
  broad methodology doctrine, or neighboring execution shelf was imported

## 2026-05-05 - Agent-workflows-core direct-read migration review

Changed:

- added
  [agent-workflows-core-direct-read-migration-review](parts/technique-reform-ingress/reviews/agent-workflows-core-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`,
  `AOA-T-0028`, and `AOA-T-0031`
- accepted `execution/agent-workflows-core` as the eighteenth bounded
  migration pilot without moving files
- kept the shelf centered on visible, bounded, reviewable agent work rather
  than hidden autonomous loops
- preserved `AOA-T-0028` as `kind: guardrail` and `AOA-T-0031` as
  `kind: composition`; path movement must not imply kind remap
- kept generic agent doctrine, shell policy, product policy, approval policy,
  autonomous orchestration, hidden agent scheduling, runtime lifecycle law,
  broad methodology doctrine, and neighboring execution shelves outside the
  shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no eighteenth shelf migration landed from the review alone

## 2026-05-05 - Landed intent-chain pilot review

Changed:

- added
  [landed-intent-chain-pilot-review](parts/technique-reform-ingress/reviews/landed-intent-chain-pilot-review.md)
  as the landed review after the seventeenth path migration
- validated `intent-chain` as the second successful execution trunk shelf
- confirmed both leaves remain `domain: agent-workflows` and `kind: workflow`
  even though they now live under the execution tree path
- preserved `AOA-T-0005` as `promoted`; path movement still does not imply
  canonical promotion
- chose `execution/agent-workflows-core` for the next direct-read migration
  review without moving files
- kept autonomous orchestration, hidden agent scheduling, runtime lifecycle
  law, shell doctrine, product policy, approval policy, broad methodology
  doctrine, and neighboring execution shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `tree_path` frontmatter was added

## 2026-05-05 - Intent-chain tree pilot migration

Changed:

- moved exactly `AOA-T-0004` and `AOA-T-0005` into
  `techniques/execution/intent-chain/`
- extended the compact `techniques/execution/AGENTS.md` route card with the
  second execution shelf
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-intent-chain-tree-pilot.md`
- repaired authored links from semantic reviews, audit evidence surfaces,
  long-gap reentry, active review sources, and root docs
- kept `domain`, `kind`, status, IDs, evidence, relations, support files,
  maturity, validation-strength metadata, and public-safety posture unchanged
- preserved `AOA-T-0005` as `promoted`; path movement did not imply canonical
  promotion

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no neighboring execution shelf was moved
- no router ownership, API contract authority, runtime dispatch, real-action
  permission, automation governance, CI policy, broad rollout doctrine, or
  proof of real-execution safety was imported into the shelf

## 2026-05-05 - Intent-chain direct-read migration review

Changed:

- added
  [intent-chain-direct-read-migration-review](parts/technique-reform-ingress/reviews/intent-chain-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0004` and `AOA-T-0005`
- accepted `execution/intent-chain` as the seventeenth bounded migration pilot
  without moving files
- kept `AOA-T-0004` as the base artifact-first intent chain and `AOA-T-0005`
  as the one-new-intent rollout checklist on top of that chain
- preserved `AOA-T-0005` as `status: promoted`; path movement must not imply
  canonical promotion
- kept router ownership, API contract authority, runtime dispatch, real-action
  permission, automation governance, CI policy, broad rollout doctrine, and
  neighboring execution shelves outside the shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no seventeenth shelf migration landed from the review alone

## 2026-05-05 - Landed ready-work-graphs pilot review

Changed:

- added
  [landed-ready-work-graphs-pilot-review](parts/technique-reform-ingress/reviews/landed-ready-work-graphs-pilot-review.md)
  as the landed review after the sixteenth path migration
- validated `ready-work-graphs` as the first successful execution trunk shelf
- confirmed all three leaves remain `domain: agent-workflows` and
  `kind: workflow` even though they now live under the execution tree path
- preserved `AOA-T-0055` as a watch-line readiness ladder rather than a graph
  database, methodology, or execution workflow
- chose `execution/intent-chain` for the next direct-read migration review
  without moving files
- kept router ownership, API contract authority, runtime dispatch, real-action
  permission, automation governance, CI policy, broad rollout doctrine, and
  neighboring execution shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `tree_path` frontmatter was added

## 2026-05-05 - Ready-work-graphs tree pilot migration

Changed:

- moved exactly `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055` into
  `techniques/execution/ready-work-graphs/`
- added the compact `techniques/execution/AGENTS.md` route card for the first
  execution trunk shelf
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-ready-work-graphs-tree-pilot.md`
- repaired authored links from ready-work notes, active review sources, audit
  readiness, and root docs
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- preserved `AOA-T-0055` as a readiness ladder rather than treating it as
  graph database doctrine, methodology, or execution workflow

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no neighboring execution shelf was moved
- no project-management, scheduling, staffing, dispatch, backlog governance,
  graph database, memory substrate, proof, validation, or hidden orchestration
  authority was imported into the shelf

## 2026-05-05 - Ready-work-graphs direct-read migration review

Changed:

- added
  [ready-work-graphs-direct-read-migration-review](parts/technique-reform-ingress/reviews/ready-work-graphs-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055`
- accepted `execution/ready-work-graphs` as the sixteenth bounded migration
  pilot without moving files
- kept `AOA-T-0055` as a watch-line readiness ladder rather than treating it
  as graph database doctrine, methodology, or execution workflow
- kept project-management doctrine, scheduling, staffing, dispatch policy,
  backlog governance, graph database doctrine, memory substrate, hidden
  orchestration, proof of readiness, and execution validation outside the shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no sixteenth shelf migration landed from the review alone

## 2026-05-05 - Landed antifragility-recovery pilot review

Changed:

- added
  [landed-antifragility-recovery-pilot-review](parts/technique-reform-ingress/reviews/landed-antifragility-recovery-pilot-review.md)
  as the landed review after the fifteenth path migration
- validated `antifragility-recovery` as the second successful recovery trunk
  shelf after `diagnosis-repair`
- confirmed `AOA-T-0098` remains `domain: validation-patterns` and
  `kind: validation` even though it now lives under the recovery tree path
- chose `execution/ready-work-graphs` for the next direct-read migration review
  without moving files
- kept project-management doctrine, scheduling, staffing, dispatch policy,
  memory substrate, graph database doctrine, hidden orchestration, proof
  authority, and neighboring execution shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no `tree_path` frontmatter was added

## 2026-05-05 - Antifragility-recovery tree pilot migration

Changed:

- moved exactly `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and `AOA-T-0098`
  into `techniques/recovery/antifragility-recovery/`
- extended `techniques/recovery/AGENTS.md` for the compact recovery shelf while
  keeping incident response doctrine, runtime self-healing, runtime ownership,
  proof authority, rollback policy, deployment lifecycle law, service catalog
  ownership, KAG authority, stats meaning, playbook choreography, generic
  resilience platform authority, and broad improvement doctrine outside the
  shelf
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-antifragility-recovery-tree-pilot.md`
- repaired authored links from Antifragility mechanics, audit readiness,
  experience overlap notes, active review sources, and root docs
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- preserved `AOA-T-0098` as `domain: validation-patterns` and
  `kind: validation`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no Agents-of-Abyss Antifragility doctrine, runtime, proof, KAG, stats,
  playbook, deployment, or service-catalog authority moved into the shelf
- no neighboring shelf moved

## 2026-05-05 - Antifragility-recovery direct-read migration review

Changed:

- added
  [antifragility-recovery-direct-read-migration-review](parts/technique-reform-ingress/reviews/antifragility-recovery-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`,
  and `AOA-T-0098`
- accepted `recovery/antifragility-recovery` as the fifteenth bounded
  migration pilot without moving files
- kept `AOA-T-0098` readable as a validation-shaped leaf even though the
  proposed path is under `recovery/`
- kept Agents-of-Abyss Antifragility doctrine, via negativa law,
  fragile-pattern source truth, incident response doctrine, runtime
  self-healing, runtime ownership, proof authority, rollback policy,
  deployment lifecycle law, service catalog ownership, KAG authority, stats
  meaning, playbook choreography, and generic resilience platform authority
  outside the shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fifteenth shelf migration landed from the review alone

## 2026-05-05 - Landed history-artifacts pilot review

Changed:

- added
  [landed-history-artifacts-pilot-review](parts/technique-reform-ingress/reviews/landed-history-artifacts-pilot-review.md)
  as the post-migration review over the fourteenth tree pilot
- accepted the landed `history-artifacts` shelf as clearer after validation
  and as the first successful history trunk shelf
- chose `recovery/antifragility-recovery` for the next direct-read migration
  review without moving a fifteenth shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept incident response doctrine, runtime ownership, validation-patterns
  erasure, proof authority, rollback policy, deployment lifecycle law, service
  catalog ownership, and generic resilience platform authority outside the
  next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fifteenth shelf migration was authorized without direct-read review

## 2026-05-05 - History-artifacts tree pilot migration

Changed:

- moved exactly `AOA-T-0044`, `AOA-T-0053`, `AOA-T-0026`, `AOA-T-0045`,
  `AOA-T-0066`, and `AOA-T-0067` into
  `techniques/history/history-artifacts/`
- extended `techniques/history/AGENTS.md` for the compact history shelf while
  keeping memory doctrine, instruction authority, private transcript
  publication, hidden capture policy, hosted viewer product doctrine, repo
  analytics, retention policy, recall substrate, and proof authority outside
  the shelf
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-history-artifacts-tree-pilot.md`
- repaired authored links from history-adjacent techniques, checkpoint
  provenance, active Distillation ledgers, and reform review sources
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept capture, transcript packaging, derivative local indexing, witness trace
  review, transcript replay, and code-lineage links as separate leaf bundles

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no memory, instruction, retention, recall, hosted-viewer, analytics, or proof
  authority moved into the shelf
- no neighboring shelf moved

## 2026-05-05 - History-artifacts direct-read migration review

Changed:

- added
  [history-artifacts-direct-read-migration-review](parts/technique-reform-ingress/reviews/history-artifacts-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0044`, `AOA-T-0053`, `AOA-T-0026`,
  `AOA-T-0045`, `AOA-T-0066`, and `AOA-T-0067`
- accepted `history-artifacts` as the fourteenth bounded migration pilot
  without moving files
- kept capture, transcript packaging, indexing, witness tracing, replay, and
  code lineage as six separate leaf moves under one history shelf
- kept memory doctrine, instruction authority, private transcript publication,
  hidden capture policy, hosted viewer product doctrine, repo analytics,
  retention policy, recall substrate, and proof authority outside the shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fourteenth shelf migration landed from the review alone

## 2026-05-05 - Landed published-summary pilot review

Changed:

- added
  [landed-published-summary-pilot-review](parts/technique-reform-ingress/reviews/landed-published-summary-pilot-review.md)
  as the post-migration review over the thirteenth tree pilot
- accepted the landed `published-summary` shelf as clearer after validation
  and as the third successful proof trunk shelf
- chose `history-artifacts` for the next direct-read migration review without
  moving a fourteenth shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept memory doctrine, instruction authority, private transcript
  publication, hosted viewer product doctrine, repo analytics, retention
  policy, recall substrate, and neighboring shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fourteenth shelf migration was authorized without direct-read review

## 2026-05-05 - Published-summary tree pilot migration

Changed:

- moved exactly `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011`
  into `techniques/proof/published-summary/`
- extended `techniques/proof/AGENTS.md` for the third proof trunk shelf
  without turning it into telemetry owner doctrine, dashboard ownership,
  runtime storage policy, archive governance, remediation execution, integrity
  verdict law, release policy, proof verdict law, or a generic reporting
  platform
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-published-summary-tree-pilot.md`
- repaired authored links from published-summary semantic and shadow reviews,
  evaluation-chain adjacency, active review sources, and incoming overlap notes
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept latest alias storage, remediation snapshot, integrity diagnosis, and
  required-versus-optional rendering as separate leaf bundles
- kept `AOA-T-0011` readable as reusable consumer policy, not only a package
  appendix

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no review-evidence, owner-truth-closeout, runtime, governance, or automation
  shelf moved
- no generated projection became authority

## 2026-05-05 - Published-summary direct-read migration review

Changed:

- added
  [published-summary-direct-read-migration-review](parts/technique-reform-ingress/reviews/published-summary-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`,
  and `AOA-T-0011`
- accepted `published-summary` as the thirteenth bounded migration pilot
  because direct reading confirmed the proof-facing package: latest/history
  storage, bounded remediation snapshot, diagnostic integrity snapshot, and
  required-versus-optional summary-source rendering
- kept the review non-mutating: no technique bundle moved, no frontmatter
  changed, and no generated projection became authority
- kept telemetry owner doctrine, dashboard ownership, runtime storage policy,
  archive governance, remediation execution, integrity verdict law, release
  policy, proof verdict law, generic reporting platform, and neighboring
  shelves outside the migration wave
- preserved the `AOA-T-0011` watch seam: rendering remains reusable consumer
  policy, not only a package appendix

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no thirteenth shelf migration happened from the review alone

## 2026-05-05 - Landed evaluation-chain pilot review

Changed:

- added
  [landed-evaluation-chain-pilot-review](parts/technique-reform-ingress/reviews/landed-evaluation-chain-pilot-review.md)
  as the post-migration review over the twelfth tree pilot
- accepted the landed `evaluation-chain` shelf as clearer after validation and
  as the second successful proof trunk shelf
- chose `published-summary` for the next direct-read migration review without
  moving a thirteenth shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept proof authority, release policy, remediation execution, integrity
  verdict law, telemetry platform, rendering product policy, archive
  governance, generic observability doctrine, and neighboring proof-side
  shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no thirteenth shelf migration was authorized without direct-read review

## 2026-05-05 - Evaluation-chain tree pilot migration

Changed:

- moved exactly `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032` into
  `techniques/proof/evaluation-chain/`
- extended `techniques/proof/AGENTS.md` for the second proof trunk shelf
  without turning it into CI ownership, release policy, eval-suite authority,
  proof verdict law, mandatory testing doctrine, generic quality gate
  doctrine, or owner acceptance
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-evaluation-chain-tree-pilot.md`
- repaired authored links from the direct-read review, evaluation-chain
  semantic review, active Distillation ledgers, and Agon handoff overlap notes
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept `AOA-T-0032` promoted rather than promoting it to canonical by path
  placement
- kept summary-contract generation, staged signal promotion, and read-only CI
  context reporting as separate leaf bundles

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no `published-summary`, `review-evidence`, `owner-truth-closeout`, runtime,
  governance, or automation shelf moved
- no generated projection became authority

## 2026-05-05 - Evaluation-chain direct-read migration review

Changed:

- added
  [evaluation-chain-direct-read-migration-review](parts/technique-reform-ingress/reviews/evaluation-chain-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0003`, `AOA-T-0007`, and
  `AOA-T-0032`
- accepted `evaluation-chain` as the twelfth bounded migration pilot because
  direct reading confirmed the proof-facing chain: machine-readable validation
  summary, staged signal promotion, and read-only CI context reporting
- kept the review non-mutating: no technique bundle moved, no frontmatter
  changed, and no generated projection became authority
- kept CI ownership, release policy, eval-suite authority, proof verdict law,
  mandatory testing doctrine, generic quality gate doctrine, owner
  acceptance, and neighboring proof-side shelves outside the migration wave
- kept `AOA-T-0032` promoted rather than treating path placement as canonical
  status promotion

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no twelfth shelf migration happened from the review alone

## 2026-05-05 - Landed skill-support pilot review

Changed:

- added
  [landed-skill-support-pilot-review](parts/technique-reform-ingress/reviews/landed-skill-support-pilot-review.md)
  as the post-migration review over the eleventh tree pilot
- accepted the landed `skill-support` shelf as clearer after validation and
  as the first successful proof trunk shelf
- chose `evaluation-chain` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept CI ownership, release policy, eval-suite authority, proof verdict law,
  mandatory testing doctrine, generic quality gate doctrine, and neighboring
  proof-side shelves outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no twelfth shelf migration was authorized without direct-read review

## 2026-05-05 - Skill-support tree pilot migration

Changed:

- moved exactly `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017` into
  `techniques/proof/skill-support/`
- added `techniques/proof/AGENTS.md` as a compact proof-trunk route card
  without turning the shelf into proof authority, eval-suite ownership,
  mandatory testing doctrine, DDD formalism, architecture taxonomy, runtime
  readiness, owner-truth law, policy enforcement, or a neighboring proof-side
  shelf
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-skill-support-tree-pilot.md`
- repaired authored links from semantic reviews, mechanics parts,
  review source rows, and adjacent-technique links
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept bounded-context vocabulary, consumer-visible contract validation, and
  invariant-oriented coverage as separate leaf bundles

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no evaluation-chain, published-summary, review-evidence,
  owner-truth-closeout, runtime, governance, or automation shelf moved
- no generated projection became authority

## 2026-05-05 - Skill-support direct-read migration review

Changed:

- added
  [skill-support-direct-read-migration-review](parts/technique-reform-ingress/reviews/skill-support-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0016`, `AOA-T-0015`, and
  `AOA-T-0017`
- accepted `skill-support` as the eleventh bounded migration pilot because
  direct reading confirmed the proof-side support triangle: bounded-context
  vocabulary, consumer-visible contract validation, and invariant-oriented
  coverage
- kept the review non-mutating: no technique bundle moved, no frontmatter
  changed, and no generated projection became authority
- kept proof authority, eval-suite ownership, mandatory testing doctrine,
  DDD formalism, architecture taxonomy, runtime readiness, owner-truth law,
  policy enforcement, and neighboring proof-side shelves outside the
  migration wave

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no eleventh shelf migration happened from the review alone

## 2026-05-05 - Landed skill-discovery pilot review

Changed:

- added
  [landed-skill-discovery-pilot-review](parts/technique-reform-ingress/reviews/landed-skill-discovery-pilot-review.md)
  as the post-migration review over the tenth tree pilot
- accepted the landed `skill-discovery` shelf as clearer after validation and
  as the fifth successful instruction trunk shelf
- chose `skill-support` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept proof authority, eval-suite ownership, mandatory testing doctrine,
  runtime, governance, owner-closeout, review-evidence, and
  automation-governance outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no eleventh shelf migration was authorized without direct-read review

## 2026-05-05 - Skill-discovery tree pilot migration

Changed:

- moved exactly `AOA-T-0041` and `AOA-T-0042` into
  `techniques/instruction/skill-discovery/`
- extended `techniques/instruction/AGENTS.md` for curated skill discovery and
  pre-surface upstream source readiness without turning the shelf into
  installer behavior, sync substrate, registry governance, trust scoring,
  security scanning, routing policy, runtime law, or agent-role authority
- preserved root legacy accounting in
  `legacy/receipts/2026-05-05-skill-discovery-tree-pilot.md`
- repaired authored links from active mechanics parts, review source rows,
  incoming staging notes, and adjacent-technique links
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept curated marketplace discoverability and upstream source-readiness as
  separate leaf bundles

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no proof, skill-support, governance, runtime, owner-closeout, or
  automation-governance shelf moved
- no generated projection became authority

## 2026-05-05 - Skill-discovery direct-read migration review

Changed:

- added
  [skill-discovery-direct-read-migration-review](parts/technique-reform-ingress/reviews/skill-discovery-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0041` and `AOA-T-0042`
- accepted `skill-discovery` as the tenth bounded migration pilot because
  direct reading confirmed the shared skill-surfacing shelf
- kept the review non-mutating: no technique bundle moved, no frontmatter
  changed, and no generated projection became authority
- kept proof, skill-support, governance, runtime, owner-closeout,
  automation-governance, and other skill-adjacent shelves outside the
  migration wave
- kept installer behavior, sync substrate, registry product doctrine, registry
  governance, access control, routing policy, recommendation ranking, trust
  scoring, security scanning, compliance review, generic monitoring,
  capability ownership, command doctrine, runtime law, and agent-role
  authority outside `skill-discovery`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no tenth shelf migration happened from the review alone

## 2026-05-05 - Landed capability-boundary pilot review

Changed:

- added
  [landed-capability-boundary-pilot-review](parts/technique-reform-ingress/reviews/landed-capability-boundary-pilot-review.md)
  as the post-migration review over the ninth tree pilot
- accepted the landed `capability-boundary` shelf as clearer after validation
  and as the fourth successful instruction trunk shelf
- chose `skill-discovery` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept proof, governance, runtime, owner-closeout, automation-governance, and
  other skill-adjacent shelves outside the next move
- kept registry product doctrine, routing policy, installer behavior, sync
  substrate, trust scoring, security scanning, generic monitoring, capability
  ownership, command doctrine, and agent-role authority outside
  `skill-discovery`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no tenth shelf migration was authorized without direct-read review

## 2026-05-04 - Capability-boundary tree pilot migration

Changed:

- moved exactly `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093` into
  `techniques/instruction/capability-boundary/`
- extended `techniques/instruction/AGENTS.md` for the fourth instruction trunk
  shelf without turning it into marketplace curation, upstream health
  validation, routing policy, KAG graph semantics, runtime law, host inventory,
  command product design, shell doctrine, registry product doctrine, or
  agent-role authority
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-capability-boundary-tree-pilot.md`
- repaired authored links from active mechanics parts, review source rows, and
  moved adjacent-technique links
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept skill-command ownership, primary source priority, and
  recommendation/actionability as separate guardrail leaves

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not changed:

- no `tree_path` frontmatter was added
- no `skill-discovery`, proof, governance, runtime, owner-closeout, or
  automation-governance shelf moved
- no generated projection became authority

## 2026-05-04 - Capability-boundary direct-read migration review

Changed:

- added
  [capability-boundary-direct-read-migration-review](parts/technique-reform-ingress/reviews/capability-boundary-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093`
- accepted `capability-boundary` as the ninth bounded migration pilot because
  direct reading confirmed the shared capability-boundary guardrail cluster
- kept the review non-mutating: no technique bundle moved, no frontmatter
  changed, and no generated projection became authority
- kept `skill-discovery`, proof, governance, runtime, owner-closeout,
  automation-governance, and other capability-adjacent shelves outside the
  migration wave
- kept marketplace curation, upstream health validation, routing policy,
  recommendation ranking, KAG graph semantics, runtime execution doctrine,
  host inventory policy, command product design, shell doctrine, registry
  product doctrine, and agent-role authority outside `capability-boundary`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no ninth shelf migration happened from the review alone

## 2026-05-04 - Landed capability-registry pilot review

Changed:

- added
  [landed-capability-registry-pilot-review](parts/technique-reform-ingress/reviews/landed-capability-registry-pilot-review.md)
  as the post-migration review over the eighth tree pilot
- accepted the landed `capability-registry` shelf as clearer after validation
  and as the third successful instruction trunk shelf
- chose `capability-boundary` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `skill-discovery`, proof, governance, runtime, owner-closeout, and
  other capability-adjacent shelves outside the next move
- kept skill marketplace curation, upstream health validation, routing policy,
  KAG graph semantics, runtime execution doctrine, host inventory policy, and
  agent-role authority outside `capability-boundary`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no ninth shelf migration was authorized without direct-read review

## 2026-05-04 - Capability-registry tree pilot migration

Changed:

- moved exactly `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064` from
  `techniques/docs/` into `techniques/instruction/capability-registry/`
- extended `techniques/instruction/AGENTS.md` for the third instruction trunk
  shelf without turning it into registry product doctrine, discovery ranking,
  marketplace curation, trust policy, graph semantics, runtime resolution,
  skill acceptance, or agent-role authority
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-capability-registry-tree-pilot.md`
- repaired authored links from Audit active parts, incoming staging notes,
  active adjacent techniques, and the reform review source rows
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept capability specs, registry-facing entries, and discovery queries as
  separate leaves rather than merging them into one registry framework bundle

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`
- capability-boundary, skill-discovery, proof, governance, runtime,
  owner-closeout, and knowledge-lift shelves stayed outside the migrated shelf

## 2026-05-04 - Capability-registry direct-read migration review

Changed:

- added
  [capability-registry-direct-read-migration-review](parts/technique-reform-ingress/reviews/capability-registry-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064`
- accepted `capability-registry` as the eighth bounded migration pilot because
  direct reading confirmed the spec-entry-query chain
- kept the review non-mutating: no technique bundle moved, no frontmatter
  changed, and no generated projection became authority
- kept `capability-boundary`, `skill-discovery`, proof, governance, runtime,
  and owner-closeout shelves outside the migration wave
- kept registry product doctrine, discovery ranking, marketplace curation,
  trust policy, graph semantics, runtime resolution, skill acceptance, and
  agent-role authority outside `capability-registry`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no eighth shelf migration happened from the review alone

## 2026-05-04 - Landed docs-boundary pilot review

Changed:

- added
  [landed-docs-boundary-pilot-review](parts/technique-reform-ingress/reviews/landed-docs-boundary-pilot-review.md)
  as the post-migration review over the seventh tree pilot
- accepted the landed `docs-boundary` shelf as clearer after validation and as
  the second successful instruction trunk shelf
- chose `capability-registry` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `capability-boundary`, `skill-discovery`, proof, governance, runtime,
  and owner-closeout shelves outside the next move
- kept registry product doctrine, discovery ranking, trust policy, marketplace
  curation, graph semantics, runtime resolution, and agent-role authority
  outside `capability-registry`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no eighth shelf migration was authorized without direct-read review

## 2026-05-04 - Docs-boundary tree pilot migration

Changed:

- moved exactly `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033`
  from `techniques/docs/` into `techniques/instruction/docs-boundary/`
- extended `techniques/instruction/AGENTS.md` for the second instruction trunk
  shelf without turning the route card into governance doctrine
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md`
- repaired authored links from docs guides, semantic review surfaces, Audit
  active parts, Experience candidate bridge notes, Agon candidate handoff
  notes, and the reform review source rows
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept `docs-boundary` bounded to document truth, status snapshots,
  public-share artifacts, and decision rationale rather than source-of-truth
  governance, approval policy, proof authority, runtime role law, or
  architecture taxonomy

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`
- capability, skill-discovery, proof, governance, runtime, owner-closeout, and
  knowledge-lift shelves stayed outside the migrated shelf

## 2026-05-04 - Docs-boundary direct-read migration review

Changed:

- added
  [docs-boundary-direct-read-migration-review](parts/technique-reform-ingress/reviews/docs-boundary-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`,
  and `AOA-T-0033`
- accepted `docs-boundary` as the seventh bounded tree migration pilot and the
  next instruction trunk shelf test
- recorded the exact next migration scope:
  `techniques/instruction/docs-boundary/`
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept capability, skill-discovery, proof, governance, runtime,
  owner-closeout, and knowledge-lift shelves outside the accepted move
- kept source-of-truth governance, approval policy, skill acceptance, proof
  authority, runtime role law, and architecture taxonomy outside the shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no seventh shelf migration happened before direct-read review

## 2026-05-04 - Landed kag-source-lift pilot review

Changed:

- added
  [landed-kag-source-lift-pilot-review](parts/technique-reform-ingress/reviews/landed-kag-source-lift-pilot-review.md)
  as the post-migration review over the sixth tree pilot
- accepted the landed `kag-source-lift` shelf as clearer after validation and
  as the first successful knowledge-lift trunk test
- chose `docs-boundary` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept capability, skill-discovery, proof, governance, runtime, and
  owner-closeout shelves outside the next move
- kept KAG owner authority, graph semantics, retrieval policy, scoring, proof
  authority, status automation, and automatic verdicts outside
  `knowledge-lift`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no seventh shelf migration was authorized without direct-read review

## 2026-05-04 - Kag-source-lift tree pilot migration

Changed:

- moved exactly `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`,
  `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048` from
  `techniques/docs/` into `techniques/knowledge-lift/kag-source-lift/`
- added `techniques/knowledge-lift/AGENTS.md` as the minimal route card for
  the knowledge-lift trunk
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-kag-source-lift-tree-pilot.md`
- repaired authored links from KAG/source-lift guides, Audit and Distillation
  active parts, Boundary-bridge active parts, incoming staging notes, and the
  reform review source rows
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged
- kept `knowledge-lift` bounded to reusable source-lift practice rather than
  KAG owner doctrine, graph semantics, retrieval policy, scoring, generated
  truth, or automatic verdicts

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`
- docs-boundary, capability, skill-discovery, proof, governance, runtime, and
  owner-closeout shelves stayed outside the migrated shelf

## 2026-05-04 - Kag-source-lift direct-read migration review

Changed:

- added
  [kag-source-lift-direct-read-migration-review](parts/technique-reform-ingress/reviews/kag-source-lift-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`,
  `AOA-T-0021`, `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048`
- accepted `kag-source-lift` as the sixth bounded tree migration pilot and the
  first `knowledge-lift` trunk test
- recorded the exact next migration scope:
  `techniques/knowledge-lift/kag-source-lift/`
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `docs-boundary`, capability, skill-discovery, proof, governance,
  runtime, and owner-closeout shelves outside the accepted move
- kept `knowledge-lift` bounded to source-lift technique placement rather than
  KAG owner doctrine, graph semantics, scoring, policy, or automatic verdicts

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no sixth shelf migration happened before direct-read review

## 2026-05-04 - Landed instruction-surface pilot review

Changed:

- added
  [landed-instruction-surface-pilot-review](parts/technique-reform-ingress/reviews/landed-instruction-surface-pilot-review.md)
  as the post-migration review over the fifth tree pilot
- accepted the landed `instruction-surface` shelf as clearer after validation
  and as the first successful instruction trunk test
- chose `kag-source-lift` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `docs-boundary`, capability, skill-discovery, proof, governance, and
  runtime-authority shelves outside the next move
- kept `knowledge-lift` bounded to technique-local source-lift rather than KAG
  owner authority, graph truth, scoring, policy, or automatic verdicts

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no sixth shelf migration was authorized without direct-read review

## 2026-05-04 - Instruction-surface tree pilot migration

Changed:

- moved exactly `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`,
  `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035` from `techniques/docs/` into
  `techniques/instruction/instruction-surface/`
- added `techniques/instruction/AGENTS.md` as the minimal route card for the
  instruction trunk
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-instruction-surface-tree-pilot.md`
- repaired authored links from semantic review, Audit and Distillation active
  parts, and reform review source rows
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`
- `kag-source-lift`, docs-boundary, capability, proof, governance, and
  runtime-authority shelves stayed outside the migrated shelf

## 2026-05-04 - Instruction-surface direct-read migration review

Changed:

- added
  [instruction-surface-direct-read-migration-review](parts/technique-reform-ingress/reviews/instruction-surface-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`,
  `AOA-T-0027`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035`
- accepted `instruction-surface` as the fifth bounded tree migration pilot and
  the next instruction trunk test
- recorded the exact next migration scope:
  `techniques/instruction/instruction-surface/`
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `kag-source-lift`, docs-boundary, capability, proof, governance, and
  runtime-authority shelves outside the accepted move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fifth shelf migration happened before direct-read review

## 2026-05-04 - Landed diagnosis-repair pilot review

Changed:

- added
  [landed-diagnosis-repair-pilot-review](parts/technique-reform-ingress/reviews/landed-diagnosis-repair-pilot-review.md)
  as the post-migration review over the fourth tree pilot
- accepted the landed `diagnosis-repair` shelf as clearer after validation and
  as the first successful recovery trunk test
- chose `instruction-surface` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `kag-source-lift`, boundary-watch proof shelves, and
  `automation-governance` outside the next move

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fifth shelf migration was authorized without direct-read review

## 2026-05-04 - Diagnosis-repair tree pilot migration

Changed:

- moved exactly `AOA-T-0080` through `AOA-T-0083` from
  `techniques/agent-workflows/` into
  `techniques/recovery/diagnosis-repair/`
- added `techniques/recovery/AGENTS.md` as the minimal route card for the
  recovery trunk
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-diagnosis-repair-tree-pilot.md`
- repaired authored links from mechanics anchors, Agon gate overlap notes, and
  reform review surfaces
- kept `domain`, `kind`, status, IDs, evidence, relations, and public-safety
  posture unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`
- recovery was not widened into self-improvement, role-law, proof-law, or
  scenario rollout

## 2026-05-04 - Diagnosis-repair direct-read migration review

Changed:

- added
  [diagnosis-repair-direct-read-migration-review](parts/technique-reform-ingress/reviews/diagnosis-repair-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0080` through `AOA-T-0083`
- accepted `diagnosis-repair` as the fourth bounded tree migration pilot and
  the next recovery trunk test
- recorded the exact next migration scope:
  `techniques/recovery/diagnosis-repair/`
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept self-improvement, hidden doctrine edits, role-law, proof-law, and
  scenario rollout outside the accepted shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fourth shelf migration happened before direct-read review

## 2026-05-04 - Landed media-ingest pilot review

Changed:

- added
  [landed-media-ingest-pilot-review](parts/technique-reform-ingress/reviews/landed-media-ingest-pilot-review.md)
  as the post-migration review over the third tree pilot
- accepted the landed `media-ingest` shelf as clearer after validation and as
  the first successful non-continuity trunk test
- chose `diagnosis-repair` for the next direct-read migration review without
  moving another shelf
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `telegram-account-auth-and-session-bridge` outside the migrated shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no fourth shelf migration was authorized without direct-read review

## 2026-05-04 - Media-ingest tree pilot migration

Changed:

- moved exactly `AOA-T-0070` through `AOA-T-0074` from
  `techniques/agent-workflows/` into `techniques/ingest/media-ingest/`
- added `techniques/ingest/AGENTS.md` as the minimal route card for the first
  non-continuity migrated trunk
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-media-ingest-tree-pilot.md`
- repaired authored links from media-ingest bundles, incoming staging surfaces,
  Audit promotion-readiness rows, and reform review surfaces
- kept `domain`, `kind`, status, IDs, evidence, and public-safety posture
  unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`
- `telegram-account-auth-and-session-bridge` stayed outside the migrated shelf

## 2026-05-04 - Media-ingest direct-read migration review

Changed:

- added
  [media-ingest-direct-read-migration-review](parts/technique-reform-ingress/reviews/media-ingest-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0070` through `AOA-T-0074`
- accepted `media-ingest` as the third bounded tree migration pilot and the
  first non-continuity trunk test
- recorded the exact next migration scope:
  `techniques/ingest/media-ingest/`
- kept `family`, `tree_path`, and scout topology axes out of frontmatter
- kept `telegram-account-auth-and-session-bridge` outside the accepted shelf

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no third shelf migration happened before direct-read review

## 2026-05-04 - Landed handoff-continuation pilot review

Changed:

- added
  [landed-handoff-continuation-pilot-review](parts/technique-reform-ingress/reviews/landed-handoff-continuation-pilot-review.md)
  as the post-migration review over the second tree pilot
- accepted the landed `handoff-continuation` shelf as clearer after validation
- chose `media-ingest` for the next direct-read migration review without moving
  another shelf
- repaired `incoming/` staging candidate links for `AOA-T-0056` through
  `AOA-T-0062` so landed-bundle references point at current authored paths
- kept `family`, `tree_path`, and scout topology axes out of frontmatter

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no third shelf migration was authorized without direct-read review

## 2026-05-04 - Handoff-continuation tree pilot migration

Changed:

- moved exactly `AOA-T-0056` through `AOA-T-0062` from
  `techniques/agent-workflows/` into
  `techniques/continuity/handoff-continuation/`
- updated `techniques/continuity/AGENTS.md` so the continuity trunk names both
  accepted pilot shelves
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md`
- repaired authored links from adjacent bundles, mechanics anchors, and reform
  review surfaces
- kept `domain`, `kind`, status, IDs, evidence, and public-safety posture
  unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`

## 2026-05-04 - Handoff-continuation direct-read migration review

Changed:

- added
  [handoff-continuation-direct-read-migration-review](parts/technique-reform-ingress/reviews/handoff-continuation-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0056` through `AOA-T-0062`
- accepted `handoff-continuation` as the second bounded tree migration pilot
  while keeping the review itself non-mutating
- recorded the exact next migration scope:
  `techniques/continuity/handoff-continuation/`
- kept `family`, `tree_path`, and scout topology axes out of frontmatter

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no second shelf migration happened before direct-read review

## 2026-05-04 - Landed review-compaction pilot review

Changed:

- added
  [landed-review-compaction-pilot-review](parts/technique-reform-ingress/reviews/landed-review-compaction-pilot-review.md)
  as the post-migration review over the first tree pilot
- accepted the landed `review-compaction` shelf as clearer after validation
- chose `handoff-continuation` for the next direct-read migration review
  without moving any new bundles
- kept `family`, `tree_path`, and scout topology axes out of frontmatter

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no frontmatter changed
- no second shelf migration was authorized without direct-read review

## 2026-05-04 - Review-compaction tree pilot migration

Changed:

- moved exactly `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054` from
  `techniques/agent-workflows/` into
  `techniques/continuity/review-compaction/`
- added `techniques/continuity/AGENTS.md` as the minimal tree-trunk route card
- preserved root legacy accounting in
  `legacy/receipts/2026-05-04-review-compaction-tree-pilot.md`
- repaired authored links from adjacent bundles and reform review surfaces
- kept `domain`, `kind`, status, IDs, evidence, and public-safety posture
  unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no other shelf migrated
- no `tree_path` frontmatter was added
- no `family` or scout topology axis became schema truth
- active bundles did not pass through root `legacy/`

## 2026-05-04 - Review-compaction direct-read migration review

Changed:

- added
  [review-compaction-direct-read-migration-review](parts/technique-reform-ingress/reviews/review-compaction-direct-read-migration-review.md)
  as the direct-read review over `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054`
- accepted `review-compaction` as the first migration pilot while keeping the
  review itself non-mutating
- recorded the migration blast radius and the next exact pilot scope:
  `techniques/continuity/review-compaction/`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no technique frontmatter changed
- no `tree_path`, `family`, or scout topology axis became schema truth
- no generated future path became a current valid link

## 2026-05-04 - Tree projection and first review pack

Changed:

- added generated
  [technique_tree_projection](parts/technique-reform-ingress/reports/technique_tree_projection.md)
  reports over all `107` bundles
- added `mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py` and validator parity for the
  projection surface
- added
  [first-tree-projection-review-pack](parts/technique-reform-ingress/reviews/first-tree-projection-review-pack.md)
  as the human review layer over the generated placement projection
- selected `review-compaction` for the next direct-read migration review

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no technique frontmatter changed
- no `tree_path`, `family`, or scout topology axis became required schema truth
- no future projected path became a current valid link

## 2026-05-04 - Family shelf review pack

Changed:

- added
  [first-family-shelf-review-pack](parts/technique-reform-ingress/reviews/first-family-shelf-review-pack.md)
  as the review layer over all `26` scout families before tree projection
- sorted families into stable shelf candidates, boundary-watch families,
  split pressure, and singleton hold posture without promoting `family` into
  frontmatter
- updated the technique reform ingress packet and Distillation roadmap so the
  next route is a non-authoritative tree projection over all `107` bundles

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique bundle was moved
- no technique frontmatter changed
- no `family`, `tree_path`, or scout topology axis became required schema truth
- no `domain`, `kind`, status, relation, owner, or generated catalog authority
  changed

## 2026-05-04 - Post-0054 kind-audit hold review

Changed:

- added
  [post-0054-kind-audit-hold-review](parts/technique-reform-ingress/reviews/post-0054-kind-audit-hold-review.md)
  as the explicit close of the current kind remap lane
- classified remaining generated audit pressure as already-reviewed holds or
  tie-break calibration rather than fresh remap candidates
- updated the technique reform ingress packet and Distillation roadmap so the
  next route is family shelf review before frontmatter, tree, or schema work

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique frontmatter changed
- no `kind` value was added, removed, or renamed
- no technique status, domain, owner, relation, or evidence surface changed
- no family, tree, schema, or path migration was claimed

## 2026-05-04 - AOA-T-0054 kind remap

Changed:

- remapped
  [compaction-resilient-skill-loading](../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md)
  from `handoff` to `recovery`
- kept the bundle at `domain: agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- added a destination-check review comparing `handoff`, `workflow`, and
  `recovery`
- added a decision note for the public kind-frontmatter correction

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no `kind` value was added, removed, or renamed
- no technique status changed
- no domain, relation, evidence note, or owner boundary changed
- no broad classification migration was claimed

## 2026-05-04 - Second kind ambiguity review pack

Changed:

- added
  [second-kind-ambiguity-review-pack](parts/technique-reform-ingress/reviews/second-kind-ambiguity-review-pack.md)
  as the updated-audit read after the first shortlist remap wave closed
- kept repeated audit candidates as review holds where direct bundle reading
  still supports `guardrail`, `lift`, or `assessment`
- routed `AOA-T-0054` to a destination check against `handoff`, `workflow`, and
  `recovery` before any frontmatter change

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no technique frontmatter changed
- no `kind` value was added, removed, or renamed
- no technique status, domain, owner, relation, or evidence surface changed
- no broad classification migration was claimed

## 2026-05-04 - AOA-T-0052 kind remap

Changed:

- remapped
  [review-findings-compaction](../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md)
  from `handoff` to `workflow`
- kept the bundle at `domain: agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- updated the technique reform ingress review pack so the first kind ambiguity
  shortlist is closed after three narrow remap waves
- added a decision note for the public kind-frontmatter correction

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no `kind` value was added, removed, or renamed
- no technique status changed
- no domain, relation, evidence note, or owner boundary changed
- no broad classification migration was claimed

## 2026-05-04 - AOA-T-0005 kind remap

Changed:

- remapped
  [new-intent-rollout-checklist](../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md)
  from `guardrail` to `workflow`
- kept the bundle at `domain: agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- updated the technique reform ingress review pack so `AOA-T-0005` is landed
  and `AOA-T-0052` becomes the next narrow destination-check candidate
- added a decision note for the public kind-frontmatter correction

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no `kind` value was added, removed, or renamed
- no technique status changed
- no domain, relation, evidence note, or owner boundary changed
- no broad classification migration was claimed

## 2026-05-04 - AOA-T-0085 kind remap

Changed:

- remapped
  [multi-axis-quest-overlay](../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md)
  from `artifact` to `lift`
- kept the bundle at `agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- updated the technique reform ingress review pack so `AOA-T-0085` is landed
  and `AOA-T-0005` becomes the next narrow remap candidate
- added a decision note for the public kind-frontmatter correction

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no `kind` value was added, removed, or renamed
- no technique status changed
- no domain, relation, evidence note, or owner boundary changed
- no broad classification migration was claimed

## 2026-05-04 - Technique topology scout review pack

Changed:

- added
  [first-topology-scout-review-pack](parts/technique-reform-ingress/reviews/first-topology-scout-review-pack.md)
  as the first human review layer over the generated topology scout
- linked the review pack from the technique reform ingress packet, Distillation
  part map, and part index
- recorded that the generated projection covers `107` techniques, with `52`
  `orchestration-required`, `36` `small-agent`, `19` `medium-agent`, `65`
  `read-only`, and `25` `mutating` readouts
- moved the next route from generated projection creation to direct bundle
  reading for the kind ambiguity review pack

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no generated scout axis became schema or frontmatter truth
- no technique bundle was remapped
- no `kind` registry value was added or changed
- no public, approval, security, or migration proof was claimed from the scout
  report

## 2026-05-04 - Kind ambiguity direct-read review pack

Changed:

- added
  [first-kind-ambiguity-review-pack](parts/technique-reform-ingress/reviews/first-kind-ambiguity-review-pack.md)
  as the first direct-read review over generated kind ambiguity pressure
- read the strongest generated remap and revisit candidates directly from their
  bundle files before naming a shortlist
- narrowed the later remap shortlist to `AOA-T-0085`, `AOA-T-0005`, and
  `AOA-T-0052`, while keeping generated false positives as current-kind holds
- updated the technique reform ingress packet and Distillation roadmap so the
  next route is one narrow remap wave rather than broad classification churn

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no bundle frontmatter changed
- no `kind` value was added, removed, or renamed
- no technique status changed
- no generated audit verdict became stronger than direct bundle meaning

## 2026-05-01 - Active parts split

Changed:

- added route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
  `LANDING_LOG.md`, and `ROADMAP.md`
- moved the five formerly flat distillation docs into part-local active homes
- added `parts/` and `legacy/` route cards
- preserved candidate verdicts and ledger counts without compaction
- added a decision record for the active/parts/legacy split

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no raw donor wave packet was copied into `legacy/raw/`
- no candidate verdict was promoted, dropped, or rewritten
- no technique bundle was minted by this structural pass

## 2026-05-01 - External candidate ledger source-status pass

Changed:

- preserved the active external candidate ledger as
  [legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md](legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md)
- marked `seed_4.txt` and `seed_6.txt` as historical source labels whose raw
  files are not present in the current checkout
- kept candidate verdicts, counts, and narrowing-lane posture unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

## 2026-05-01 - External candidate ledger compaction

Changed:

- compacted the active external candidate ledger into route, source-status,
  summary, candidate-accounting, landed-anchor, and reopen-rule sections
- kept the detailed wave execution notes and donor-read details in the preserved
  pre-prune receipt
- kept candidate verdicts, counts, and the `phase_sync_for_agents` narrowing
  lane unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

## 2026-05-01 - External candidate registry

Changed:

- added a part-local source registry, schemas, example, builder, validator, tests,
  and generated compact index for
  [parts/external-candidate-ledger](parts/external-candidate-ledger/README.md)
- kept all `13` candidate verdicts, status counts, and the
  `phase_sync_for_agents` active narrowing lane unchanged
- made atom/topology and boundary/portability gates explicit per candidate without
  promoting any candidate into a technique bundle

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no external candidate was promoted, dropped, or reclassified
- no raw donor source was treated as present when it was only a historical label
- no generated index became authority over the active part README or bundle
  review path

## 2026-05-01 - Cross-layer candidate registry

Changed:

- added a part-local source registry, schemas, example, builder, validator, tests,
  and generated compact index for
  [parts/cross-layer-candidate-ledger](parts/cross-layer-candidate-ledger/README.md)
- kept the `24` candidate universe, `6` already-staged rows, `10` landed wave
  imports, `0` future imports, `2` overlap holds, `3` layer-incubation lanes,
  and `3` architecture/substrate holds intact
- made landed, inherited, overlap, incubation, and architecture gates explicit
  per candidate without compacting the active README or promoting any candidate
  into a technique bundle
- corrected the active README arithmetic from `17` to `18` remaining
  non-inherited candidates so it matches the unchanged summary counts

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no cross-layer candidate was promoted, dropped, or reclassified
- no wave program was reopened
- no generated index became authority over the active part README, landed
  technique bundles, or recurrence review path

## 2026-05-01 - Cross-layer recurrence observation repoint

Changed:

- repointed technique recurrence observation to read both
  [parts/cross-layer-candidate-ledger](parts/cross-layer-candidate-ledger/README.md)
  and the generated
  [cross-layer registry index](parts/cross-layer-candidate-ledger/generated/cross_layer_candidate_registry.min.json)
- kept the active README as the decision route while treating the generated
  registry as observation evidence for counts, gates, waves, and holds
- made the recurrence stop line explicit: generated registry evidence cannot
  create candidates, release holds, authorize import, or promote techniques

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no recurrence manifest became candidate or promotion authority
- no candidate status changed
- no generated index became a decision surface

## 2026-05-01 - Distillation gate alignment

Changed:

- made the atom/topology and boundary/portability packet explicit in the donor
  refinery and external import runbook
- aligned external and cross-layer candidate-ledger reopen rules with the same
  packet before any future import wave
- kept generated registries as evidence only and kept candidate statuses
  unchanged

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no candidate moved out of hold, incubation, overlap, or landed status
- no technique bundle was drafted
- no future topology axis became current bundle frontmatter authority

## 2026-05-01 - Cross-layer candidate ledger compaction

Changed:

- preserved the active cross-layer candidate ledger as
  [legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md](legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md)
- compacted [parts/cross-layer-candidate-ledger](parts/cross-layer-candidate-ledger/README.md)
  so active route keeps current accounting, landed anchors, implementation
  rules, and reopen gates instead of detailed landed wave execution order
- updated provenance and legacy indexes so the preserved receipt is the place
  for exact Wave A/B/C order, worker-role notes, and seam rationale

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no cross-layer candidate was promoted, dropped, or reclassified
- no generated registry became authority
- no landed wave was reopened

## 2026-05-03 - Agon candidate handoff lanes

Changed:

- added [parts/agon-candidate-handoff](parts/agon-candidate-handoff/README.md)
  as the Distillation lane map for Agon requested-only practice candidates
- added a part-local source registry, schemas, example, builder, validator, tests,
  and generated compact index
- mapped all `22` current Agon technique-side candidates: `12` Wave IV
  move-binding candidates and `10` Wave XV epistemic candidates
- kept `first_narrowing_watch`, `source_boundary_hold`, and `owner_route_hold`
  as Distillation lanes, not technique statuses

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate status changed
- no Agon lawful move, proof, scar, rank, KAG, ToS, runtime, or skill authority
  moved into `aoa-techniques`

## 2026-05-03 - Request evidence gate card

Changed:

- added the first Agon handoff gate card for
  `candidate:aoa-techniques:agon/request-evidence-practice`
- registered the card in the part-local Agon candidate handoff seed and compact
  generated index
- kept the card as a one-candidate atom/topology check, not a technique bundle
  or Agon acceptance

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  or scar authority moved into `aoa-techniques`

## 2026-05-03 - Request evidence gate example

Changed:

- added a minimal public-safe gate example for
  `candidate:aoa-techniques:agon/request-evidence-practice`
- registered the example in the Agon candidate handoff seed and compact
  generated index
- kept the example as one gate artifact, not a technique bundle or Agon
  acceptance

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  or scar authority moved into `aoa-techniques`

## 2026-05-03 - Request evidence gate checklist and evidence note

Changed:

- added a checklist and evidence note for
  `candidate:aoa-techniques:agon/request-evidence-practice`
- registered both artifacts in the Agon candidate handoff seed and compact
  generated index
- kept the artifacts as gate evidence for bundle-readiness review, not a
  technique bundle or Agon acceptance

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  or scar authority moved into `aoa-techniques`

## 2026-05-03 - Request evidence bundle-readiness review

Changed:

- added a bundle-readiness review for
  `candidate:aoa-techniques:agon/request-evidence-practice`
- registered the review in the Agon candidate handoff seed and compact
  generated index
- aligned the candidate's current bundle-facing `primary_kind` from
  `evidence-request` to the registry-backed `guardrail`, leaving
  evidence-request as family/capability posture
- kept the review as draft-readiness evidence, not as bundle acceptance or
  Agon source acceptance

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  or scar authority moved into `aoa-techniques`
- no current `kind` registry value was added or changed

## 2026-05-03 - Request evidence technique bundle

Changed:

- added
  [single-missing-evidence-request](../../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md)
  as the first normal technique bundle grown from the Agon candidate handoff
- registered a traceability pointer from
  `candidate:aoa-techniques:agon/request-evidence-practice` to the landed
  bundle in the part-local seed and generated compact index
- kept the bundle at `promoted`, `guardrail`, and `source_backed` posture with
  origin evidence and a non-canonical readiness note

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  scar, or skill authority moved into the technique bundle
- no canonical promotion was claimed

## 2026-05-03 - Offer evidence reference gate packet

Changed:

- added a gate card, public-safe example, checklist, and evidence note for
  `candidate:aoa-techniques:agon/offer-evidence-reference-practice`
- registered the packet in the Agon candidate handoff seed and compact
  generated index
- aligned the candidate's current bundle-facing `primary_kind` from
  `evidence-reference` to the registry-backed `artifact`, leaving
  evidence-reference as family/capability posture under `review-evidence`

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  scar, or skill authority moved into `aoa-techniques`
- no current `kind` registry value was added or changed

## 2026-05-03 - Challenge claim gate packet

Changed:

- added a gate card, public-safe example, checklist, and evidence note for
  `candidate:aoa-techniques:agon/challenge-claim-practice`
- registered the gate packet in the Agon candidate handoff seed and compact
  generated index
- kept `challenge` as handoff-facing posture only, with a future bundle required
  to map the atom to a registry-backed kind before promotion
- recorded the next move as a bundle-readiness review, not an immediate
  technique draft

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime,
  rank, scar, or skill authority moved into `aoa-techniques`
- no current `kind` registry value was added or changed

## 2026-05-03 - Technique reform ingress packet

Changed:

- added `technique-reform-ingress` as the Distillation entry packet for future
  classification reform
- gathered the atom/topology contracts, kind registry, family scout, kind
  ambiguity audit, and Agon first-narrowing frontier into one route
- updated Distillation direction, part map, provenance, roadmap, root roadmap,
  and Start Here so broad reform starts from evidence instead of a schema jump
- recorded the structural decision in
  [Technique Reform Ingress Packet](../../docs/decisions/AOA-TECH-D-0035-technique-reform-ingress-packet.md)

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no schema, template, or validator contract changed
- no bundle frontmatter was remapped
- no new `kind`, `family`, capability, substrate, execution, or risk axis became
  required
- no generated report gained authority over authored bundle meaning

## 2026-05-03 - Agon first-narrowing frontier review

Changed:

- added a frontier review for the remaining `8` ungated Agon first-narrowing
  candidates after the request, offer, and challenge gate-to-bundle paths landed
- extended the part-local generated index with `first_narrowing_frontier`,
  `first_narrowing_frontier_counts`, and `gate_pipeline_counts`
- exposed family, capability, substrate, execution profile, and risk posture in
  the frontier lens as evidence for the later technique classification reform
- updated the handoff README, gates README, Distillation parts/provenance/roadmap
  surfaces, and schema example so future passes choose the next gate from
  current evidence rather than memory

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no new gate card or technique bundle was drafted
- no Agon candidate source status changed
- no `kind` registry value was added or changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime,
  rank, scar, or skill authority moved into `aoa-techniques`

## 2026-05-03 - Challenge claim technique bundle

Changed:

- added
  [single-locus-claim-challenge](../../techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md)
  as the third normal technique bundle grown from the Agon candidate handoff
- added the challenge-claim bundle-readiness review and registered the bundle
  pointer in the part-local seed and generated compact index
- mapped `challenge` from handoff-facing posture to the registry-backed
  `guardrail` kind for the public technique bundle
- updated the offer-evidence and challenge gate cards so their landed bundle
  bridges are visible from the gate packet itself
- extended the Audit promotion-readiness matrix so the new bundle enters the
  fresh extraction lane instead of becoming hidden corpus drift

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime,
  rank, or scar authority moved into `aoa-techniques`
- no canonical promotion was claimed

## 2026-05-03 - Offer evidence reference technique bundle

Changed:

- added
  [single-scoped-evidence-reference](../../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md)
  as the second normal technique bundle grown from the Agon candidate handoff
- registered a traceability pointer from
  `candidate:aoa-techniques:agon/offer-evidence-reference-practice` to the
  landed bundle in the part-local seed and generated compact index
- kept the bundle at `promoted`, `artifact`, and `source_backed` posture with
  origin evidence and a non-canonical readiness note
- extended the Audit promotion-readiness matrix so the new bundle enters the
  fresh extraction lane instead of becoming hidden corpus drift

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime,
  rank, or scar authority moved into `aoa-techniques`
- no canonical promotion was claimed

## 2026-05-03 - Offer evidence reference bundle-readiness review

Changed:

- added a bundle-readiness review for
  `candidate:aoa-techniques:agon/offer-evidence-reference-practice`
- registered the review in the Agon candidate handoff seed and compact
  generated index
- kept the candidate's bundle-facing `primary_kind` at the registry-backed
  `artifact`, leaving evidence-reference as family, capability, substrate, and
  reform-thread posture
- marked the next move as one technique bundle draft around a single scoped
  evidence reference

Verification lane:

Verification covered the targeted owner checks and repository validation lanes recorded for this landing.

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  scar, or skill authority moved into `aoa-techniques`
- no current `kind` registry value was added or changed
