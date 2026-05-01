# Distillation Landing Log

This log records structural landings for the `aoa-techniques` Distillation
mechanic.

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
- made atom/topology and law/local/bridge gates explicit per candidate without
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

- made the atom/topology and law/local/bridge packet explicit in the donor
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
