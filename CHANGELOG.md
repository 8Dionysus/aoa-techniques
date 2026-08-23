# Changelog

All notable changes to `aoa-techniques` will be documented in this file.

The format is intentionally simple and human-first.

## [Unreleased]

### Postpublish release-audit follow-up

- repaired the release-audit and nightly sentinel artifact-tool pin to the
  exact current `abyss-machine` commit
  `a9f52d8bfe23e28167c01dd2a059af231fff77a0`, which exposes the subject-root
  API required by the exact KAG evidence contract
- added an optional `release_ref` input to release-audit so an immutable tag
  can be re-audited from the current workflow without moving or rewriting the
  tag or GitHub Release

## [0.6.1] - 2026-08-23

### Summary

- this is a corrective patch after `v0.6.0`'s post-audit: direct KAG and
  stats provider body pins now name the exact published provider commits, and
  the KAG export artifact contract binds durable evidence to the exact
  Techniques release commit and intended consumer trust boundary
- the public technique canon and authored technique bundles are unchanged;
  this release repairs dependency currentness, artifact identity, generated
  parity, and release evidence without claiming a new technique corpus
- `v0.6.0` remains an immutable historical release and is not rewritten

### Added

- added an exact `commit:<40-hex-git-SHA>` source-ref contract for KAG export
  artifact sidecars, registry records, subject materialization, and trust
  gates
- added explicit release-evidence guidance distinguishing the intended local
  `consumer_intent=agent` / `trust_root_mode=host_managed` boundary from the
  separate `release_consumer` and `public_release` production boundaries
- added a durable decision record for immutable provider pins and exact KAG
  release evidence

### Changed

- changed repo-validation, release-audit, nightly-sentinel, and local KAG
  guard surfaces to use published `aoa-kag@v0.5.0` commit
  `813a7f69dc96ec031dad9b897a6991792cc48b7a` and published
  `aoa-stats@v0.2.0` commit
  `dc608fd5de3fcaf0301f356c9efd52e2bdd350ce`; these replace the historical
  ancestor-only body pins recorded in `v0.6.0`
- changed the KAG export validator to resolve the checked-out `HEAD`, reject
  a mismatched requested source ref, and pass the exact ref through sidecars,
  the registry, subject-store verification, and trust-gate calls
- refreshed the source-owned portable KAG family and generated export
  readers from the exact provider source after the evidence contract change

### Fixed

- fixed consumer/provider currentness so a green ancestor-only ref cannot be
  mistaken for the exact published provider commit
- fixed the KAG export manifest and validator path-source ambiguity: a
  manifest path is descriptive only, while artifact evidence carries the
  immutable release commit
- fixed pre-materialization handling so the raw
  `required_artifact_subject_store_not_verified` `deny` remains a deny until
  subject materialization is complete; wrappers do not rewrite it to `allow`
- fixed trust-boundary reporting so `allow`, `manual_review_required`,
  `deny`, `warn`, and `unknown` remain separate outcomes

### ABI, schemas, evidence, and generated consumers

- the `aoa_techniques_kag_export_v1` envelope remains the source-owned KAG
  export ABI; generated identity and evidence-contract text are refreshed,
  while authored technique meaning remains authoritative
- the content-addressed generated capsule does not embed a self-referential
  release SHA; the artifact owner binds `source_ref=commit:<exact-release-SHA>`
  when sidecars, registry evidence, subject materialization, and trust gates
  are prepared
- the intended local consumer contract is `agent` with `host_managed` trust;
  a production `release_consumer` or `public_release` result is independently
  evaluated and is not promoted to allow by this source release
- the public publication artifact is the annotated Git tag and matching
  GitHub Release; no PyPI, npm, package-registry, or GitHub asset publication
  is implied

### Compatibility and migration

- current exact prerequisites are published `aoa-kag@v0.5.0` containing
  `813a7f69dc96ec031dad9b897a6991792cc48b7a` and `aoa-stats@v0.2.0`
  containing `dc608fd5de3fcaf0301f356c9efd52e2bdd350ce`
- consumers staying on `v0.6.0` retain its historical provider-pin claims and
  artifact path reference; they should upgrade to `v0.6.1` for exact provider
  currentness and exact release-commit evidence
- the KAG export ABI and technique-bundle layout remain compatible; generated
  KAG family and export identities change because their source/evidence
  contract is refreshed

### Security and privacy

- public source, generated, and artifact evidence surfaces remain limited to
  sanitized metadata, public commits, and public trust claims; secrets,
  private transcripts, host internals, and raw sensitive logs are excluded
- artifact admission remains fail-closed on ABI identity, provenance,
  durable evidence, subject-store state, source identity, trust-root mode,
  and the exact raw trust-gate result
- a missing public-release trust root remains `manual_review_required`; it is
  not relabeled as an allow, and unknown/deny/warn outcomes are not collapsed
- these are source, CI, artifact-admission, and public-hygiene claims, not a
  general runtime-security certification

### Deployment, observability, recovery, and rollback

- no service, deployment, storage, host, runtime, activation, or sibling
  repository path changed
- owner-local stats and observability meaning remain separate from the
  central `aoa-stats` protocol and cross-owner aggregation owner; no adoption,
  quality, power, or universal score claim is made
- rollback remains Git based: retain `v0.6.0`, retain its Release and tag,
  and move consumers back to that immutable source only through an explicit
  owner decision

### First-Parent Reconciliation

The product-change range is
`v0.6.0..0f981adfcd37b74800db701dab73dbe842296329`.
It contains one landed one-parent squash commit. The release-preparation
commit that introduces this section is publication bookkeeping and is
intentionally outside the product-change ledger, following the repository's
prior release tradition.

1. `0f981adfcd37b74800db701dab73dbe842296329` — PR #502, repaired exact
   published KAG/stats provider pins, bound KAG export evidence to an exact
   source commit and consumer boundary, preserved raw artifact verdicts, and
   refreshed the generated KAG family. All generated shard/index churn is
   accounted for under this single landed corrective commit; no authored
   technique bundle change is omitted or duplicated.

There are no additional internal/noise commits, duplicate product entries,
or intentional exclusions in this product range.

### Validation

- exact clean provider checkouts passed the manifest-owned `source-fast` lane;
  generated parity, public hygiene, AGENTS mesh, and focused contract tests
  passed
- the exact-source release lane completed repository, mechanics, part-local,
  generated-parity, KAG export, stats-federation, and artifact-validator
  coverage before release preparation
- PR #502 passed GitHub `Repo Validation`; merge, tag identity, GitHub
  Release identity, artifact admission, and tag-scoped Release Audit remain
  separate checks rather than one substituted claim
- provider currentness is checked against exact published tag targets, not
  moving branches or ancestor-only acceptance

### Notes

- this release does not claim runtime health, deployment, service activation,
  consumer-zero, measured routing benefit, cross-owner adoption, proof or eval
  verdicts, durable memory promotion, rollback execution, or human acceptance
- the artifact owner preserves its raw local and production-boundary results;
  the release does not manufacture a public-release trust-root decision
- the final release evidence must point to the exact immutable `v0.6.1` tag
  commit; a source checkout, CI pass, tag, Release, artifact admission,
  runtime state, proof, delivery, closure, and acceptance remain distinct
  claims

## [0.6.0] - 2026-08-22

### Summary

- this release reconstructs the complete `v0.5.0..2b70fddc` landed source
  range: five first-parent commits across the public technique canon, KAG
  export, owner-routing references, generated readers, and release/nightly
  reproducibility surfaces
- the version remains `0.6.0` under the repository's early `0.x` policy
  because the range changes public owner boundaries and generated KAG schema
  topology, not because of commit count
- `aoa-techniques` remains a standalone public canon of small, sanitized,
  bounded, reviewable engineering techniques; this release does not turn it
  into a skill runtime, proof authority, routing engine, KAG substrate, stats
  aggregator, package registry, or deployment runtime

### Added

- added an explicit owner decision and route law stating that this repository
  currently has no repository-local skill home; discovery returns to authored
  technique bundles and derived readers, while shared skills arrive through
  the user/profile surface
- added the portable v3 KAG family manifest, content-addressed JSONL shard
  topology, deterministic v2 compatibility assembly, and digest-bound
  migration and budget receipts
- added release/nightly dependency setup for the pinned `aoa-stats` validator
  and the bounded `pytest>=8.0,<9.0` test dependency

### Changed

- changed active dispatch, selection, and intelligence ownership references
  to canonical `aoa-sdk`; retained `aoa-routing` only in dated donor,
  provenance, review, and legacy compatibility evidence
- changed latest-release reproduction so foreign `.deps/` checkouts live
  outside the tagged owner checkout and cannot be misclassified as
  repository-owned tests, scripts, or command-authority inputs
- changed the tracked KAG read-model surface from v2 monoliths to the v3
  manifest/shard family while preserving deterministic v2 compatibility
  assembly for consumers that still require that view
- refreshed KAG family shards, generated route/read models, mechanics handoff
  projections, owner inventories, and repository-document readers from their
  authored sources

### Fixed

- fixed the historical release/nightly dependency split where latest-release
  reproduction lacked the pinned `aoa-stats` validator and the moving-main
  part-local lane lacked `pytest`
- fixed the post-merge latest-release reproduction false failure caused by
  foreign dependency checkouts being discovered as owner files
- fixed route, generated-projection, source-contract, and topology
  expectations required by the no-skill-home and `aoa-sdk` succession
  boundaries

### Deprecated

- deprecated direct active dispatch ownership references to `aoa-routing`;
  the namespace remains available for compatibility and historical evidence
  but is no longer the active route owner
- deprecated direct consumers of the removed tracked KAG v2 monolith paths;
  consumers should use the v3 manifest/shard/compatibility route

### Removed

- removed the foreign `.agents/skills/` cache: 25 shared bundles, 212 copied
  paths, and six copied helper scripts
- removed the active direct predecessor checkout dependency from the current
  `aoa-techniques` routing surface
- removed tracked KAG v2 monolith index files as storage representations;
  this does not remove the v2 compatibility view

### ABI, schemas, evidence, and generated consumers

- the KAG family manifest remains
  `kag/indexes/index_family.manifest.json` with schema
  `aoa-repo-local-kag-family-manifest-v3`; its content-addressed family
  identity is regenerated and checked by the pinned `aoa-kag` builder
- the `aoa_techniques_kag_export_v1` export ABI remains unchanged, while the
  v3 family manifest, shards, receipts, source-return records, and consumer
  routes change their generated identity and therefore require fresh parity
  and trust checks
- generated catalogs, capsules, section/checklist/example/evidence/review
  manifests, AGENTS mesh, mechanics projections, KAG exports, Technique
  Intelligence, questbook readers, and repository-document readers remain
  derived companions; authored technique bundles, contracts, route cards,
  decisions, and owner-local source packets remain the authorities
- the public artifact is the annotated Git tag and matching GitHub Release;
  no PyPI, npm, package-registry, or GitHub asset publication is implied

### Compatibility and migration

- consumers that opened deleted v2 monolith paths must migrate to the v3
  manifest, shard, and deterministic compatibility routes
- consumers that treated `aoa-routing` as the active dispatch owner must
  follow the `aoa-sdk` route; dated donor, provenance, review, and legacy
  evidence remains available for reconciliation
- the exact provider prerequisites used for this release are published
  `aoa-kag@v0.5.0` containing commit
  `b28f64a497fd440dd58cbaae90d655da46224d8c` and `aoa-stats@v0.2.0`
  containing commit `25ebfb784f01d3b93f62994908579c4a2c5d87b1`; unmerged
  `aoa-kag` PR #219 is not part of this consumer release contract

### Security and privacy

- public technique and KAG-export surfaces remain limited to sanitized public
  metadata and source references; secrets, private transcripts, private
  infrastructure, runtime state, and raw sensitive logs are excluded
- GitHub Actions and cross-repository validation checkouts remain pinned to
  exact immutable refs in workflow source
- KAG-adjacent consumer admission remains fail-closed on ABI identity,
  generated provenance, materialized subjects, source/trust-root matching,
  and the exact artifact trust-gate result
- these are source/public-hygiene and artifact-admission claims, not a general
  runtime-security certification

### Deployment, observability, recovery, and rollback

- no service, deployment, storage, host, runtime, or activation path changed
- owner-local stats and observability meaning remains separate from the
  central `aoa-stats` protocol and cross-owner aggregation owner; no adoption,
  quality, power, or universal score claim is made
- rollback remains source/Git based: retain `v0.5.0`, retain the v2
  compatibility assembly and `aoa-routing` legacy references, and keep the
  no-skill-home boundary reversible through a separately admitted future trial

### First-Parent Reconciliation

The product-change range is `v0.5.0..2b70fddcefe17bb4d02584a84997011d69964f24`.
It contains five landed one-parent squash commits. Each is listed exactly once;
no commit in this source range is internal-only noise or intentionally omitted.
The release-preparation commit that introduces this section is publication
bookkeeping and is intentionally outside the product-change ledger, following
the repository's prior release tradition.

1. `9364662c7bde35b87fc67e17502f9c78f5934b64` — PR #495, removed the foreign
   `.agents/skills/` cache and recorded the no-skill-home owner decision. This
   is a changelog-worthy owner-boundary change, not generated noise.
2. `e842c0d0156c58cfb9020b636e81134e96fc8cfb` — PR #496, migrated the KAG
   family from tracked v2 monoliths to the portable v3 manifest and
   content-addressed shards while retaining v2 compatibility. This is a
   changelog-worthy schema/read-model migration and is not folded into a CI
   bullet.
3. `9a5222cc6a6b1fdc52b4df906f49dadfd0383c71` — PR #497, moved active
   dispatch and selection ownership to `aoa-sdk` while retaining
   `aoa-routing` compatibility/provenance/history. Consumer-zero,
   observation-cycle, rollback-rehearsal, and measured-net-benefit outcomes
   remain explicitly unclaimed.
4. `cf2756912d7c60fbedc06bd85e459e6e451efe7d` — PR #498, repaired release and
   nightly dependency provisioning and topology coverage. The temporary
   generated receipt it introduced was replaced by the current receipt in
   #499, so that receipt replacement is generated churn, not a second feature.
5. `2b70fddcefe17bb4d02584a84997011d69964f24` — PR #499, isolated foreign
   `.deps/` checkouts outside tagged owner topology and refreshed the current
   KAG family receipt. It is distinct from #498: path isolation and dependency
   provisioning close different failure modes.

Generated shard files and index churn are accounted for under their owning
landings above, not promoted to duplicate release bullets. There are no
additional internal/noise commits, duplicate product entries, or intentional
exclusions in the five-commit product range.

### Validation

- the release-prep route uses the manifest-owned `source-fast`, `generated`,
  `mechanics/part-local`, and `release` lanes; `scripts/release_check.py`
  stabilizes the generated snapshot and fails if a clean source tree drifts
- the release surface includes repo-local KAG full/incremental/family and
  event-history parity, generated-doc and AGENTS-mesh freshness, public
  hygiene, mechanics tests, full repository tests, and the KAG artifact bundle
  validator
- provider currentness is bound to exact published tags rather than moving
  branches: `aoa-kag@v0.5.0` and `aoa-stats@v0.2.0` contain the exact consumer
  pins above
- GitHub Repo Validation, the exact landed-commit release lane, the annotated
  tag identity, and the tag-scoped Release Audit are separate checks; a green
  PR or CI result is not publication, artifact admission, runtime health,
  proof, or human acceptance

### Notes

- this release does not claim runtime health, deployment, service activation,
  consumer-zero, measured routing cost benefit, cross-owner adoption, proof or
  eval verdicts, durable memory promotion, rollback execution, or human
  acceptance
- there is no `1.0.0` claim: structure, contribution, and validation posture
  remain early public shaping under `docs/RELEASING.md`
- local ignored `dist/` files are evidence inputs only and are not GitHub
  Release assets; artifact receipts, trust-gate admission, runtime status,
  proof, and publication acceptance remain separate claims

## [0.5.0] - 2026-07-13

### Summary

- this release reconstructs the complete post-`v0.4.5` delta from Git history
  and source diffs: `37` first-parent commits across `366` paths, with `98,241`
  additions and `22,697` deletions; `31` of those commits did not edit this
  changelog and are therefore accounted for explicitly below
- validation now has manifest-owned source-fast, generated, part-local,
  release, nightly, and advisory lanes, with owner-split validators, test and
  script topology inventories, dedicated GitHub workflows, and a stabilizing
  release entrypoint
- the repository now carries bounded local memo, eval, KAG, and stats ports
  while preserving `aoa-memo`, `aoa-evals`, `aoa-kag`, and `aoa-stats` as the
  stronger owners of their respective cross-repository semantics
- KAG export and repo-local indexes now carry artifact identity, trust-root and
  subject-store admission, canonical index-family parity, squash-stable event
  history, and fail-closed consumer verdicts
- this remains a public technique canon and generated companion surface, not a
  skill runtime, proof authority, routing engine, memory owner, KAG substrate,
  cross-owner stats layer, or package-registry artifact

### Added

- added the root `memo/` port, portable validation route, reviewed-memory route
  labels, and memory-trigger guidance without turning session evidence into
  technique truth
- added canonical decision indexes plus modeled-surface contracts that reject
  implicit, unlisted, or unmodeled decision-lane inputs
- added the manifest-backed validation topology, source-only PR gate,
  generated projection groups, part-local discovery runner, release/nightly
  workflows, and explicit test and script inventories
- added the root `evals/` skeleton for technique-local eval pressure while
  keeping verdict, scoring, regression, and proof doctrine with `aoa-evals`
- added artifact identity and OS Abyss trust-envelope validation for the KAG
  export, including durable evidence promotion and subject-store admission
- added the root `kag/` provider home, source-return packet, provider readiness
  surface, repo-local indexes, canonical seven-index family, and downstream
  parity validation
- added the root `stats/` owner port with a revision-bound
  promotion-readiness pass ratio, central protocol validation, and coverage
  that rejects a false numerator while preserving technique and audit authority

### Changed

- changed root and generated agent guidance to use the canonical `aoa-memo`
  route label and explicit memory-route trigger law
- moved executable validation command authority into
  `config/validation_lanes.json`; active docs and decisions now name lane ids
  and nearest owner cards rather than copying release command sequences
- split the former repo validator and its monolithic test into owner-local
  source, generated, AGENTS-mesh, hygiene, questbook, intelligence, and
  compatibility modules, and similarly split Distillation topology coverage
  into phase-, part-, and surface-owned suites
- separated ordinary PR growth validation from release-freeze and nightly
  reproduction, while keeping latest-tag reproduction and generated drift
  checks explicit
- keyed live recurrence receipts by event id and sanitized owner-local evidence
  and workspace-origin paths before they enter public technique surfaces
- aligned KAG provider validation with the canonical shared contract, then
  adopted pinned, lineage-aware, streamable, squash-stable repository index
  generation and event-history propagation
- tightened KAG export admission so materialized subjects, source and trust-root
  identity, evidence state, and allow/deny consumer verdicts must agree before
  agent consumption

### Fixed

- restored Spark center-decision references and made the local memo validator
  route portable
- enforced CSV parity for the kind overlay and repaired the Distillation reform
  context guard, Wave A anatomy counts, and promotion-evidence hold label
- repaired owner-truth closeout and technique-tree relative links across source
  bundles and their generated companions
- enforced bundle-review draft kind, hardened antifragility and recurrence
  owner-request receipt tests, and retained wrapped rubric finding tokens
- aligned the published-summary remediation snapshot cap policy with its
  checklist, generated readers, and regression coverage

### Included changes

Every first-parent commit from `v0.4.5` through the pre-release base
`e45b41f5` is listed exactly once, in landing order:

- `5d73dfa3` — `[codex] Add memory route trigger law (#457)`
- `c030988e` — `Use canonical aoa-memo route label (#458)`
- `9a0ac2ba` — `Add local memo port (#459)`
- `b8aeb335` — `Canonicalize technique decision indexes (#460)`
- `5a733764` — `[codex] Close validation lane coverage gaps (#461)`
- `4e3ceb77` — `[codex] Add script topology coverage`
- `3df26cb3` — `Detect unmodeled decision lane surfaces (#463)`
- `a0263cd4` — `Honor modeled decision lane surfaces (#464)`
- `01461d6b` — `Require modeled surfaces to be explicit lists (#465)`
- `1a7d1469` — `Add local eval port skeleton`
- `ad926b20` — `Restore Spark center decision references (#467)`
- `7c327f0e` — `Require portable memo validation route (#468)`
- `60e8edee` — `Validate kind overlay CSV parity (#469)`
- `b008e207` — `Fix distillation reform context guard (#470)`
- `1fdf90ab` — `Fix bundle anatomy Wave A counts`
- `e30e26fa` — `Define promotion evidence hold rubric label`
- `9c28aab7` — `Fix owner truth closeout links`
- `0d56be3b` — `Fix stale technique tree relative links (#474)`
- `6b51b6ea` — `Enforce bundle review draft kind (#475)`
- `8b2ad2de` — `Harden antifragility ORQ receipt test (#476)`
- `1fdf9849` — `Harden recurrence ORQ receipt test (#477)`
- `30a70271` — `Capture wrapped rubric finding tokens (#478)`
- `15bafd85` — `[codex] Add artifact identity to KAG export (#479)`
- `5fc1c0c2` — `Add OS Abyss trust gate for KAG export (#480)`
- `b5e38e08` — `Require subject-store trust gate for KAG export (#481)`
- `8ab16bc8` — `Add local KAG provider home (#482)`
- `50f14c92` — `Align KAG provider validation route (#483)`
- `326f70bf` — `Add repo-local KAG indexes (#484)`
- `89432bbc` — `Key live receipt hooks by event id (#485)`
- `a1918b54` — `Sanitize promotion incubation evidence handles (#486)`
- `e432adac` — `Sanitize workspace ingress origin path (#487)`
- `98a5533f` — `Align remediation snapshot cap policy (#488)`
- `67f90cc7` — `Enforce repo-local KAG index parity (#489)`
- `d58fd66c` — `Adopt repository KAG index family (#490)`
- `5fa63ab7` — `Publish canonical repository KAG indexes (#491)`
- `090440b5` — `Add aoa-techniques stats port (#492)`
- `e45b41f5` — `Harden KAG export artifact admission (#493)`

### Validation

- exact `37`-of-`37` first-parent inventory parity against the tagged range
- complete `366`-path source-diff accounting, including the `31` commits that
  did not edit the prior changelog
- source-fast, generated, mechanics/part-local, and release validation lanes
- repository tests, public-hygiene checks, and diff hygiene
- repo-local KAG full, incremental, family, and event-history parity
- landed-main GitHub validation and post-merge release-lane reproduction

### Notes

- generated outputs remain derived companions; authored technique bundles,
  route cards, contracts, decisions, mechanic-owned packets, and local port
  sources remain authoritative
- package publication to PyPI, npm, or another registry remains out of scope;
  the public artifact is the tagged corpus and its GitHub release

## [0.4.5] - 2026-05-18

### Summary

- this release carries the post-`v0.4.2` repo-shaping pass from a
  mostly-flat public technique corpus into a canonical technique tree with
  `107` authored bundles across `10` trunks and `28` shelves
- the corpus now publishes `98` canonical techniques and `9` promoted
  techniques, with promotion evidence, audit posture, generated readers, and
  route surfaces aligned to that current state
- root, docs, mechanics, generated, agent-facing, Spark, and release surfaces
  were reorganized so source truth, generated companions, historical
  provenance, and executable command lanes each have a clear owner
- this remains a curated public technique corpus and validated documentation
  surface, not a package registry artifact, runtime owner, skill workflow, eval
  verdict layer, routing policy, memory substrate, playbook, or agent identity

### Added

- added a source-derived Technique Intelligence layer with registry and DAG
  schemas, builder, CLI `query`/`explain`/`pack`/`status` commands, generated
  full/min JSON companions, a generated reader, validation/release wiring, and
  a decision record that keeps the layer focused on atomic moves rather than
  execution workflow or graph authority
- added canonical `AGENTS.md` cards for the Distillation
  `technique-reform-ingress` part root and its `reviews/` district so reform
  review packets preserve historical validation evidence without becoming
  current command-law surfaces
- added canonical `AGENTS.md` cards for root legacy subdistricts
  (`legacy/raw`, `legacy/archive`, `legacy/receipts`) and quest lanes
  (`quests/techniques`, `quests/agon`), with mesh config and validation
  coverage so nearby README files stay descriptive instead of carrying agent
  command law
- expanded `.agents/spark/` into a registry-backed Codex Spark lane for
  technique-canon work, with technique-specific scenarios, result/handoff
  templates, schemas, validator, tests, release-check wiring, and a decision
  record for the lane contract
- added repo-local `DESIGN.md`, `DESIGN.AGENTS.md`, AGENTS mesh guardrails,
  `config/agents_mesh.json`, generated `agents_mesh.min.json`, validators, and
  tests so the Agents-of-Abyss agent-surface principle is adapted into a
  checkable `aoa-techniques` mesh with canonical and migration card statuses
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

- tightened root-document roles across [README](README.md), [CHARTER](CHARTER.md),
  [DESIGN](DESIGN.md), [DESIGN.AGENTS](DESIGN.AGENTS.md), [ROADMAP](ROADMAP.md),
  [CONTRIBUTING](CONTRIBUTING.md), and [QUESTBOOK](QUESTBOOK.md) so root stays
  link-driven, owner-routed, and free of avoidable duplicated doctrine
- normalized every discovered local `AGENTS.md` card to the canonical mesh
  shape, registered all `87` cards as canonical, disabled migration drift in
  `config/agents_mesh.json`, and recorded the closure decision
- moved closed root `incoming/` packets into the Distillation legacy archive
  after their first-pass landing queues were exhausted, removed duplicate
  packet-local seed bundles for already landed techniques, and moved active
  packet intake into the Distillation `candidate-intake` part
- moved agent-only read order, validation command lanes, closeout expectations,
  and editing stop-lines from neighboring README/guide surfaces into the
  nearest `AGENTS.md`, including the mechanic package-card standard, Spark
  lane, examples, root legacy, source-lift, review, selection, decisions, and
  guardrail districts
- extended command-lane ownership across reader, generated-reader, guardrail,
  topology, runbook, quest, and Technique Intelligence surfaces: route docs now
  link to the owning `AGENTS.md` or release surface instead of embedding
  executable install, build, validation, or closeout lanes
- slimmed old root Markdown entry surfaces by turning `README.md` back into a
  compact public front door and reducing `ROADMAP.md` to live repo direction;
  detailed mechanic runbooks, generated readers, semantic/shadow reviews, tree
  migration breadcrumbs, and audit ledgers now route through owner surfaces
  instead of being re-indexed from root
- tightened [README](README.md) again after GitHub review so it no longer duplicates
  license, contribution, security, conduct, or validation-command surfaces
- added a local `docs/decisions/AGENTS.md` and `docs/decisions/TEMPLATE.md`,
  and reshaped current decision notes toward the Agents-of-Abyss decision
  pattern: decisions explain why, current source surfaces define what
- continued root/docs topology cleanup by moving semantic/shadow review packets
  and technique-reform scout reports into the owning Distillation
  `technique-reform-ingress` mechanic route, keeping root/docs surfaces as
  readers and generated reports as evidence rather than technique authority
- moved the root `Spark/` agent lane under `.agents/spark/` so fast-loop agent
  guidance lives in the agent district instead of a standalone root directory
- moved root `manifests/recurrence/` into the Recurrence
  `live-observation-producers` part so beacon manifests and hook bindings stay
  beside the mechanic route that constrains them
- moved mechanic-local schema/example contract packets from root `schemas/` and
  `examples/` into owning Experience, Method-growth, and Release-support parts;
  root contract districts now stay repo-wide, and part-local JSON identifiers
  now use public part-local schema URLs instead of the old internal local host
- moved Distillation technique-reform scout input registries and kind-overlay
  data from root `config/` and `data/` into the owning
  `technique-reform-ingress` part while keeping the root kind registry as the
  repo-wide `kind` contract
- moved one-owner mechanic scripts out of root `scripts/`: technique-reform
  scout/tree report builders now live under the Distillation
  `technique-reform-ingress` part, and live receipt publishing now lives under
  the Recurrence `live-observation-producers` part
- moved mechanic-owned tests out of root `tests/` into `mechanics/<slug>/tests/`
  and `mechanics/tests/`, adding `scripts/run_tests.py` so release validation
  still runs root-owned and mechanic-owned unittest suites together
- retired the empty root `data/` district after all active data moved to owner
  homes; future root data now requires a concrete repo-wide data contract and a
  decision rather than a placeholder shelf
- moved the KAG/source-lift authored guide family under `docs/source-lift/`
  with local route guidance, keeping repeated section, checklist, example,
  evidence-note, metadata, relation, caution, repo-doc, and export contracts
  out of flat `docs/` while preserving generated readers under `docs/readers/`
- moved review, maturity, semantic-review, and caution guide contracts under
  `docs/review/` with local route guidance, keeping review-family contracts
  out of flat `docs/` while preserving mechanic-owned review packets and
  generated readers in their own districts
- moved selection, kind, handoff, and capsule guide contracts under
  `docs/selection/` with local route guidance, keeping chooser and compact-use
  contracts out of flat `docs/` while preserving generated readers under
  `docs/readers/`
- archived the old `docs/AGENTS_ROOT_REFERENCE.md` under `legacy/archive/`
  after lifting current route reliance into root and local `AGENTS.md`
  surfaces
- added link and shape hygiene guardrails under `docs/guardrails/`, with a
  root/docs Markdown link check in `tests/test_docs_surface_guardrails.py`
- moved the old root `WALKTHROUGH.md` into `examples/` with a local examples
  index and required example shape, narrowing repo-doc routing back to
  `20` public route/canon/status files instead of treating an example as a
  root authority surface
- tightened `docs/README.md` into a route map and expanded
  `docs/decisions/README.md` into an active decision-record index, with tests
  covering examples shape, docs links, and decision index coverage
- added a Canonical Retro Audit part and rechecked all `98` canonical
  techniques for metadata, evidence-declaration, and bundle-local verdict
  coherence; no canonical downgrade was justified, and stale metadata was
  aligned for `AOA-T-0003`, `AOA-T-0007`, `AOA-T-0008`, `AOA-T-0010`, and
  `AOA-T-0012`
- promoted `AOA-T-0046 repo-doc-surface-lift` to `canonical` after the Nuxt
  LLMs docs reader and the 8Dionysus public route-map manifest closed the
  repo-owned docs route-manifest evidence gap, moving Audit queue posture from
  `11` promoted techniques to `10` while keeping route readers subordinate to
  authored docs and outside docs taxonomy, status policy, release authority,
  and sibling-owner truth
- promoted Packs 35 through 41 to `canonical`, moving `AOA-T-0084` through `AOA-T-0107` except already-closed `AOA-T-0090` after exact-fit sibling downstream or second-context evidence landed across progression, automation, quest review, workspace boundary, proof-loop, recovery, Method-growth adoption, and Agon review-evidence families. The pass updates bundle-local canonical-readiness, second-context, and adverse-effects notes, closes the fresh-extraction tail, records the long-pass closeout in Audit, and moves Audit queue posture from `34` promoted techniques to `11` while keeping skill execution, SDK runtime, playbook law, AoA center law, eval verdicts, runtime repair, routing/KAG, memo writeback, and owner acceptance outside the bundles
- promoted `AOA-T-0080 session-drift-taxonomy`, `AOA-T-0081
  diagnosis-from-reviewed-evidence`, `AOA-T-0082
  repair-shape-from-diagnosis`, and `AOA-T-0083
  checkpoint-bound-self-repair` to `canonical` after sibling downstream
  evidence showed the diagnosis-and-repair loop in real use: `aoa-skills`
  `abyss-self-diagnostic-spine` consumes drift taxonomy and read-only
  diagnosis for runtime-body evidence before repair; `aoa-sdk` closeout rules
  surface bounded self-repair only when diagnosis exists and no repair-cycle
  receipt has landed; `aoa-skills` growth-cycle examples preserve repair
  packets with owner target, validation, rollback, approval, iteration, stop,
  and escalation posture; and `aoa-agents` plus `aoa-playbooks` keep
  checkpoint posture explicit without giving techniques role-law, proof,
  playbook, runtime, memory, or autonomous self-modification authority,
  updating Audit queue posture from `38` promoted techniques to `34`
- promoted `AOA-T-0076 owner-layer-triage`, `AOA-T-0078
  decision-fork-cards`, `AOA-T-0079 risk-passport-lift`, and `AOA-T-0090
  nearest-wrong-target-rejection` to `canonical` after sibling downstream
  evidence from `aoa-playbooks`, `aoa-summon`, `aoa-sdk`, and supporting
  `aoa-evals` owner-fit surfaces showed the owner/fork/passport/rejection
  discipline changing real follow-through posture: owner-followthrough and
  session-growth routes require owner repo, owner shape, nearest-wrong target,
  branch decisions, stop/defer/drop/reanchor posture, and route artifacts
  before action; real quest entries reanchored seed-wave and recurrence
  archive survivors instead of promoting them into skills, proof, memo, stats,
  runtime, or premature playbook authority; summon routes unresolved competing
  branches back to route-forks; and SDK A2A passport assessment uses
  difficulty, risk, control mode, delegate tier, split, reviewed-lane, and
  human-gate posture to choose, narrow, or block child routes. This remains
  sibling downstream evidence, not external import proof, while playbook
  scenario design, summon authorization, SDK execution, eval verdicts,
  routing/KAG, memo writeback, stats refresh, final promotion review, and
  owner-object authorship stay outside the bundles, updating Audit queue
  posture from `42` promoted techniques to `38`
- promoted `AOA-T-0075 session-donor-harvest` and `AOA-T-0077
  harvest-packet-contract` to `canonical` after `aoa-sdk`'s checkpoint-closeout
  bridge showed exact-fit live reinforcement for reviewed session harvest:
  reviewed closeout rereads reviewed artifacts, blocks pending checkpoint
  reviews, carries semantic checkpoint-review evidence forward, builds bounded
  donor candidates, writes `HARVEST_PACKET.json`, emits harvest packet and core
  skill receipts, and lets the closeout API consume accepted candidates as
  owner follow-through briefs. LangSmith annotation queues and dataset docs
  were checked as supporting public reviewed-run curation evidence, not primary
  packet proof, while checkpoint capture, transcript packaging, local `.aoa`
  storage, exact SDK command wrappers, memory writeback, stats refresh, owner
  placement, progression, quest promotion, evaluation dataset governance, and
  final promotion verdicts stay outside the bundles, updating Audit queue
  posture from `44` promoted techniques to `42`
- promoted `AOA-T-0074 telegram-export-normalization-to-local-store` to
  `canonical` after `3bl3gamer/tg_history_dumper` showed exact-fit public
  reinforcement for bounded Telegram-source normalization: messages are saved
  as local JSON Lines, media files stay linked to chat and message ids, related
  users and chats remain visible as JSONL peer surfaces, the last saved message
  id drives incremental continuation, interrupted file downloads can resume,
  and account/auth/session dumps stay optional adjacent surfaces rather than
  the normalized message-store contract. `GeiserX/Telegram-Archive`,
  `jackwener/tg-cli`, `groupultra/telegram-search`, HTML/CSV/Markdown
  converters, and marketing/member-scraper projects were checked as wider,
  adjacent, lossy, or out of scope, while auth bootstrap, session conversion,
  account/session dumps, live control, archive presentation, search products,
  deletion/edit sync, routing, recall, and memory writeback stay outside the
  bundle, updating Audit queue posture from `45` promoted techniques to `44`
- promoted `AOA-T-0073 semantic-media-bucketing-with-vision-plus-ocr` to
  `canonical` after `end1989/ai-image-classification` showed exact-fit public
  reinforcement for bounded semantic media bucketing: configured mixed-media
  labels stay explicit, CLIP image embeddings score those labels, OCR text and
  confidence stay a separate side result, OCR text only boosts text-heavy
  labels such as receipt, chat, and work, review and auto-move thresholds
  remain distinct, user corrections stay visible, and file actions plus undo
  stay outside classification. `chintan-projects/photo-triage-agent`,
  `Aditya-Vasipalli/screensort` / Fragmenta, receipt-only extractors, and
  broad cleanup products were checked as adjacent or too wide, while OCR
  pipeline ownership, duplicate grouping, moderation or NSFW policy,
  face/person identification, deletion, archive/move policy, UI workflows,
  database schemas, model-serving detail, and full media-management behavior
  stay outside the bundle, updating Audit queue posture from `46` promoted
  techniques to `45`
- promoted `AOA-T-0072 perceptual-media-dedupe-with-threshold-review` to
  `canonical` after `qarmin/czkawka` showed exact-fit public reinforcement for
  thresholded perceptual media dedupe: Similar Images finds visually similar
  rather than byte-identical images, `max_difference` keeps strictness explicit,
  hash algorithm and hash size remain tunable, grouped output preserves
  difference-derived similarity labels and can be printed or saved as JSON, and
  deletion stays a separate default-off option. Czkawka's relevant core and CLI
  surfaces are MIT licensed and are used as evidence only; GUI/product workflow,
  mixed-license assets, cache layout, delete method names, hardlink strategy,
  semantic media taxonomy, archive policy, quality ranking, and full
  media-management behavior stay outside the bundle, updating Audit queue
  posture from `47` promoted techniques to `46`
- promoted `AOA-T-0071 template-backed-field-extraction-after-ocr` to
  `canonical` after `kotaro-kinoshita/yomitoku` showed exact-fit public
  reinforcement for schema-backed post-OCR field extraction: YAML schemas name
  explicit field targets, rule-based extraction uses visible `cell_id`, `bbox`,
  `description`, and `regex` methods, JSON output preserves normalized value,
  raw text, source, cell ids, bounding boxes, and confidence, and missed fields
  remain visible through `source: not_found` plus low confidence. YomiToku is
  CC BY-NC-SA 4.0 licensed and is used as evidence only; OCR engines, layout
  analyzers, LLM extraction services, schema products, locale doctrine,
  bookkeeping flows, receipt or invoice apps, and total document-understanding
  stacks stay outside the bundle, updating Audit queue posture from `48`
  promoted techniques to `47`
- promoted `AOA-T-0070 two-stage-document-ocr-pipeline` to `canonical` after
  `JaidedAI/EasyOCR` showed exact-fit public reinforcement for staged OCR:
  `readtext()` derives text regions through a separate detection step before
  recognition, public results preserve bounding boxes, recognized text, and
  confidence, and dictionary or JSON modes keep those fields as a structured
  handoff, while OCRmyPDF, Tesseract.js, Surya, PaddleOCR, and docTR were kept
  out of the primary proof as searchable-PDF, engine-packaging, full
  document-understanding, or donor-family lanes; serving, training, benchmark
  doctrine, searchable-PDF generation, receipt schema law, template extraction,
  semantic media bucketing, and automation stacks stay outside the bundle,
  updating Audit queue posture from `49` promoted techniques to `48`
- promoted `AOA-T-0069 approval-bound-durable-jobs` to `canonical` after
  `pydantic/pydantic-ai` showed exact-fit public reinforcement for deferred
  approval and external-tool calls that preserve pending call identity, return
  `DeferredToolRequests`, gather approval or result input outside the agent
  run, and resume with original message history plus `DeferredToolResults`,
  while its durable-execution surface supports long-running asynchronous and
  human-in-the-loop workflows; LangGraph interrupts were used only as
  supporting checkpoint/thread/resume semantics and scheduler products, queue
  platforms, workflow governance, fleet control, retry doctrine, generic
  confirmation prompts, and full durable-execution product behavior stay
  outside the bundle, updating Audit queue posture from `50` promoted
  techniques to `49`
- promoted `AOA-T-0068 fail-closed-evidence-gate` to `canonical` after
  `mvar-security/clawzero` showed exact-fit public reinforcement for a
  deterministic execution boundary between model output and tool/process
  execution, with explicit allow or block decisions, adapter-level blocked
  execution, and witness artifacts preserving reviewable verdict evidence,
  while OpenAI Agents SDK guardrails were used only as supporting boundary
  semantics and human approval, durable jobs, signed-witness infrastructure,
  attack packs, policy authoring, gateway products, sandboxing, compliance
  export, budget controls, and total trust governance stay outside the bundle,
  updating Audit queue posture from `51` promoted techniques to `50`
- promoted `AOA-T-0067 transcript-linked-code-lineage` to `canonical` after
  `ai4curation/ai-blame` showed exact-fit public reinforcement for deriving
  line- and block-level attribution from AI agent execution traces with
  timestamp, model, session id, and agent-tool metadata, then reopening saved
  transcripts from the code inspection path, while `empathic/toolpath` was
  used only as supporting provenance-document shape evidence and AI-percentage
  scoring, policy gates, review enforcement, transcript indexing, hosted
  search, dashboards, telemetry, repository analytics, and memory recall stay
  outside the bundle, updating Audit queue posture from `52` promoted
  techniques to `51`
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
  but insufficient, narrowing the next honest search shape without changing
  status, frontmatter, or technique meaning, and refreshing the generated
  evidence-note manifest surfaces
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

### Included in this release

- the current `107`-bundle technique corpus under `techniques/`, the refreshed
  [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md), generated catalog, capsules,
  source-lift manifests, KAG export, selection readers, shadow/semantic review
  manifests, and Technique Intelligence registry/DAG surfaces
- the canonical `10`-trunk / `28`-shelf tree topology, tree migration ledgers,
  reform review packets, owner-boundary, portability, selector/relation,
  execution-profile, bundle-anatomy, template-modernization, and
  technique-reform generated reports under the owning Distillation part
- the repo-local agent surface system: `DESIGN.md`, `DESIGN.AGENTS.md`,
  canonical `AGENTS.md` mesh, generated AGENTS mesh index, `.agents/spark/`
  registry-backed Codex Spark lane, and installed portable AoA skill surfaces
- the reshaped public route and docs system: compact root README, CHARTER,
  START_HERE, ROOT_SURFACE_LAW, docs districts for source-lift, review,
  selection, readers, decisions, and guardrails, plus root legacy/archive
  provenance homes
- mechanics topology updates across Distillation, Audit, Agon, Recurrence,
  Experience, Method-growth, Growth-cycle, Release-support, Checkpoint,
  Boundary-bridge, Antifragility, Questbook, and RPG package routes, including
  active/legacy splits, candidate intake, moved scripts/tests/schemas/examples,
  and closed incoming packet handling
- release-visible validation support: `scripts/run_tests.py`, release-check
  generated-parity behavior, AGENTS mesh validators, docs/shape/link guardrails,
  Technique Intelligence validation, Spark lane validation, and tests that
  prevent route/reader docs from re-owning executable command lanes

### Validation

- repository validation
- the repository test runner
- the release lane
- the diff hygiene check

### Notes

- `v0.4.5` intentionally skips public tags `v0.4.3` and `v0.4.4` because the
  previous published GitHub release and fetched tag set ended at `v0.4.2`; this
  tag records the full accumulated release surface from `v0.4.2` to current
  `main`
- generated outputs remain derived companions; authored technique bundles,
  route cards, contracts, decisions, and mechanic-owned review packets remain
  the authority surfaces
- exact executable command lanes now live in
  `config/validation_lanes.json`, with focused local commands only in the
  owning `AGENTS.md`, rather than public route or reader docs
- package publishing to PyPI, npm, or other registries remains out of scope for
  this release

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

- the release lane
- the owning part builder
- the owning part validator
- the targeted part-local tests

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

- the release lane

### Notes

- this patch extends technique guidance and validation posture without turning
  the repository into a package registry or runtime authority

## [0.4.0] - 2026-04-10

### Summary

- this release adds workspace ingress and mutation-gate techniques, audit-to-closeout proof loops, promotion-readiness surfaces, live technique receipt publishing, and antifragility/via-negativa guidance
- pinned validation evidence, repo/root scouting, and current-practice posture are strengthened while new shared-substrate and owner-sync techniques are promoted into the public set
- `aoa-techniques` remains a curated public corpus and documentation surface rather than a package or registry authority

### Validation

- the release lane

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

- the release lane

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
- new repo-owned maintainer and navigation docs, including `docs/START_HERE.md`, `docs/selection/TECHNIQUE_SELECTION_GUIDE.md`, `docs/review/SEMANTIC_REVIEW_GUIDE.md`, `docs/EXTERNAL_IMPORT_RUNBOOK.md`, `docs/DONOR_REFINERY_RUBRIC.md`, `docs/LONG_GAP_CANON_DESIGN.md`, the roadmap now kept at `ROADMAP.md`, `docs/EXTERNAL_TECHNIQUE_CANDIDATES.md`, and `docs/CROSS_LAYER_TECHNIQUE_CANDIDATES.md`
- new derived surface families for technique capsules, repo-doc routing, technique sections, checklists, examples, evidence notes, GitHub review templates, semantic reviews, and shadow reviews

### Changed

- public corpus status is now `21` `canonical` techniques and `27` `promoted` techniques, up from `9` `canonical` and `4` `promoted` in `v0.1.0`
- the canonical default set expanded across agent workflows, docs, evaluation, and KAG/source-lift surfaces, including `AOA-T-0004`, `AOA-T-0013` through `AOA-T-0019`, `AOA-T-0021`, `AOA-T-0023`, and `AOA-T-0034`
- evidence and review posture is stronger across the corpus through broader `second-context-adaptation`, `canonical-readiness`, `external-origin`, `external-import-review`, and canonical-only `adverse-effects-review` coverage
- repo routing now centers on `docs/START_HERE.md` and the bounded `pick -> inspect -> expand -> object use` operating path
- release and validation posture now centers on the release lane, with tighter generator-drift checks, repo-doc and review-surface validation, broader public-hygiene URL scanning, and cleaner worktree behavior

### Included in this release

- technique bundles under `techniques/` plus the expanded [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md)
- capsule surfaces: `docs/readers/runtime/TECHNIQUE_CAPSULES.md`, `docs/selection/TECHNIQUE_CAPSULE_GUIDE.md`, `generated/technique_capsules.json`, and `generated/technique_capsules.min.json`
- repo-doc routing surfaces: `docs/readers/repo/REPO_DOC_SURFACES.md`, `generated/repo_doc_surface_manifest.json`, and `docs/source-lift/REPO_DOC_SURFACE_LIFT_GUIDE.md`
- source-lift reader and guide surfaces: `docs/readers/source-lift/TECHNIQUE_SECTIONS.md`, `docs/source-lift/TECHNIQUE_SECTION_LIFT_GUIDE.md`, `docs/readers/source-lift/TECHNIQUE_CHECKLISTS.md`, `docs/source-lift/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, `docs/readers/source-lift/TECHNIQUE_EXAMPLES.md`, `docs/source-lift/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`, `docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md`, and `docs/source-lift/EVIDENCE_NOTE_PROVENANCE_GUIDE.md`
- review routing surfaces: `docs/readers/review/SHADOW_PATTERNS.md`, `mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/PUBLISHED_SUMMARY_SHADOW_REVIEW.md`, `mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/EVALUATION_CHAIN_SHADOW_REVIEW.md`, `generated/shadow_review_manifest.json`, `generated/semantic_review_manifest.json`, and `generated/github_review_template_manifest.json`
- governance and intake surfaces under `.github/` plus the release and validation helpers under `scripts/`

### Validation

- the release lane
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

- the repository test suite
- repository validation

### Notes

- this is the first public baseline release for the repository
- package publishing to PyPI, npm, or other registries is out of scope for `v0.1.0`
- release emphasis is the curated public technique corpus and its repo-level validation/documentation surface
