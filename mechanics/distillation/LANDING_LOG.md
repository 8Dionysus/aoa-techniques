# Distillation Landing Log

This log records structural landings for the `aoa-techniques` Distillation
mechanic.

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

Not moved:

- no technique frontmatter changed
- no `kind` value was added, removed, or renamed
- no technique status, domain, owner, relation, or evidence surface changed
- no family, tree, schema, or path migration was claimed

## 2026-05-04 - AOA-T-0054 kind remap

Changed:

- remapped
  [compaction-resilient-skill-loading](../../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md)
  from `handoff` to `recovery`
- kept the bundle at `agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- added a destination-check review comparing `handoff`, `workflow`, and
  `recovery`
- added a decision note for the public kind-frontmatter correction

Verification lane:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python scripts/release_check.py
```

Not moved:

- no technique frontmatter changed
- no `kind` value was added, removed, or renamed
- no technique status, domain, owner, relation, or evidence surface changed
- no broad classification migration was claimed

## 2026-05-04 - AOA-T-0052 kind remap

Changed:

- remapped
  [review-findings-compaction](../../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md)
  from `handoff` to `workflow`
- kept the bundle at `agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- updated the technique reform ingress review pack so the first kind ambiguity
  shortlist is closed after three narrow remap waves
- added a decision note for the public kind-frontmatter correction

Verification lane:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

Not moved:

- no `kind` value was added, removed, or renamed
- no technique status changed
- no domain, relation, evidence note, or owner boundary changed
- no broad classification migration was claimed

## 2026-05-04 - AOA-T-0005 kind remap

Changed:

- remapped
  [new-intent-rollout-checklist](../../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
  from `guardrail` to `workflow`
- kept the bundle at `agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- updated the technique reform ingress review pack so `AOA-T-0005` is landed
  and `AOA-T-0052` becomes the next narrow destination-check candidate
- added a decision note for the public kind-frontmatter correction

Verification lane:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

Not moved:

- no `kind` value was added, removed, or renamed
- no technique status changed
- no domain, relation, evidence note, or owner boundary changed
- no broad classification migration was claimed

## 2026-05-04 - AOA-T-0085 kind remap

Changed:

- remapped
  [multi-axis-quest-overlay](../../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md)
  from `artifact` to `lift`
- kept the bundle at `agent-workflows`, `promoted`, and `source_backed`
  posture with the same ID, evidence, relations, and public-safety state
- updated the technique reform ingress review pack so `AOA-T-0085` is landed
  and `AOA-T-0005` becomes the next narrow remap candidate
- added a decision note for the public kind-frontmatter correction

Verification lane:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
```

## 2026-05-01 - External candidate ledger compaction

Changed:

- compacted the active external candidate ledger into route, source-status,
  summary, candidate-accounting, landed-anchor, and reopen-rule sections
- kept the detailed wave execution notes and donor-read details in the preserved
  pre-prune receipt
- kept candidate verdicts, counts, and the `phase_sync_for_agents` narrowing
  lane unchanged

Verification lane:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

## 2026-05-01 - External candidate registry

Changed:

- added a part-local seed registry, schemas, example, builder, validator, tests,
  and generated compact index for
  [parts/external-candidate-ledger](parts/external-candidate-ledger/README.md)
- kept all `13` candidate verdicts, status counts, and the
  `phase_sync_for_agents` active narrowing lane unchanged
- made atom/topology and boundary/portability gates explicit per candidate without
  promoting any candidate into a technique bundle

Verification lane:

```bash
python mechanics/distillation/parts/external-candidate-ledger/scripts/build_external_candidate_registry.py --check
python mechanics/distillation/parts/external-candidate-ledger/scripts/validate_external_candidate_registry.py
python -m pytest -q mechanics/distillation/parts/external-candidate-ledger/tests/test_external_candidate_registry.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no external candidate was promoted, dropped, or reclassified
- no raw donor source was treated as present when it was only a historical label
- no generated index became authority over the active part README or bundle
  review path

## 2026-05-01 - Cross-layer candidate registry

Changed:

- added a part-local seed registry, schemas, example, builder, validator, tests,
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

```bash
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/build_cross_layer_candidate_registry.py --check
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/validate_cross_layer_candidate_registry.py
python -m pytest -q mechanics/distillation/parts/cross-layer-candidate-ledger/tests/test_cross_layer_candidate_registry.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python -m unittest tests.test_recurrence_manifest_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python mechanics/distillation/parts/external-candidate-ledger/scripts/validate_external_candidate_registry.py
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/validate_cross_layer_candidate_registry.py
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python -m unittest tests.test_distillation_mechanics_topology
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/build_cross_layer_candidate_registry.py --check
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/validate_cross_layer_candidate_registry.py
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no cross-layer candidate was promoted, dropped, or reclassified
- no generated registry became authority
- no landed wave was reopened

## 2026-05-03 - Agon candidate handoff lanes

Changed:

- added [parts/agon-candidate-handoff](parts/agon-candidate-handoff/README.md)
  as the Distillation lane map for Agon requested-only practice candidates
- added a part-local seed registry, schemas, example, builder, validator, tests,
  and generated compact index
- mapped all `22` current Agon technique-side candidates: `12` Wave IV
  move-binding candidates and `10` Wave XV epistemic candidates
- kept `first_narrowing_watch`, `source_boundary_hold`, and `owner_route_hold`
  as Distillation lanes, not technique statuses

Verification lane:

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology tests.test_agon_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  or scar authority moved into `aoa-techniques`
- no current `kind` registry value was added or changed

## 2026-05-03 - Request evidence technique bundle

Changed:

- added
  [single-missing-evidence-request](../../techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md)
  as the first normal technique bundle grown from the Agon candidate handoff
- registered a traceability pointer from
  `candidate:aoa-techniques:agon/request-evidence-practice` to the landed
  bundle in the part-local seed and generated compact index
- kept the bundle at `promoted`, `guardrail`, and `source_backed` posture with
  origin evidence and a non-canonical readiness note

Verification lane:

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
```

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
  [Technique Reform Ingress Packet](../../docs/decisions/2026-05-03-technique-reform-ingress-packet.md)

Verification lane:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no new gate card or technique bundle was drafted
- no Agon candidate source status changed
- no `kind` registry value was added or changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime,
  rank, scar, or skill authority moved into `aoa-techniques`

## 2026-05-03 - Challenge claim technique bundle

Changed:

- added
  [single-locus-claim-challenge](../../techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md)
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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology tests.test_roadmap_parity tests.test_audit_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime,
  rank, or scar authority moved into `aoa-techniques`
- no canonical promotion was claimed

## 2026-05-03 - Offer evidence reference technique bundle

Changed:

- added
  [single-scoped-evidence-reference](../../techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md)
  as the second normal technique bundle grown from the Agon candidate handoff
- registered a traceability pointer from
  `candidate:aoa-techniques:agon/offer-evidence-reference-practice` to the
  landed bundle in the part-local seed and generated compact index
- kept the bundle at `promoted`, `artifact`, and `source_backed` posture with
  origin evidence and a non-canonical readiness note
- extended the Audit promotion-readiness matrix so the new bundle enters the
  fresh extraction lane instead of becoming hidden corpus drift

Verification lane:

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology tests.test_roadmap_parity
python scripts/validate_repo.py
python -m unittest discover -s tests
```

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

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
```

Not moved:

- no Agon candidate became a technique bundle
- no Agon candidate source status changed
- no Agon law, proof, workflow, routing, actor, memory, KAG, ToS, runtime, rank,
  scar, or skill authority moved into `aoa-techniques`
- no current `kind` registry value was added or changed
