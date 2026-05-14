# Distillation Legacy Log

## 2026-05-01 - Flat files moved into active parts

The five pre-split distillation files were moved into active part homes:

- `DONOR_REFINERY_RUBRIC.md` -> `parts/donor-refinery/README.md`
- `EXTERNAL_IMPORT_RUNBOOK.md` -> `parts/external-import-runbook/README.md`
- `EXTERNAL_TECHNIQUE_CANDIDATES.md` -> `parts/external-candidate-ledger/README.md`
- `CROSS_LAYER_TECHNIQUE_CANDIDATES.md` -> `parts/cross-layer-candidate-ledger/README.md`
- `LONG_GAP_CANON_DESIGN.md` -> `parts/long-gap-reentry/README.md`

No ledger was shortened in this slice, so no raw pre-prune receipt was added.

## 2026-05-01 - External candidate ledger receipt and source status

Preserved the active external candidate ledger before source-status edits:

- `parts/external-candidate-ledger/README.md` -> `legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md`

The active ledger now states that `seed_4.txt` and `seed_6.txt` are historical
source labels whose raw files are not present in the current checkout. Candidate
counts and verdicts were not changed.

## 2026-05-01 - External candidate ledger active compaction

Compacted `parts/external-candidate-ledger/README.md` after preserving the
pre-prune receipt. The active surface now keeps current route accounting,
candidate tables, landed anchors, and reopen rules. The preserved receipt keeps
the detailed wave execution notes, public donor-read details, and old expected
first import package.

Candidate counts and verdicts were not changed.

## 2026-05-01 - Cross-layer candidate ledger active compaction

Preserved the active cross-layer candidate ledger before compaction:

- `parts/cross-layer-candidate-ledger/README.md` -> `legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md`

Compacted the active surface so it keeps current route accounting, all `24`
candidate rows, landed wave anchors, implementation rules, and the reopen gate.
The preserved receipt keeps detailed Wave A/B/C execution order, worker-role
notes, and seam rationale.

Candidate counts, verdicts, landed anchors, and registry authority did not
change.

## 2026-05-14 - Root roadmap breadcrumb receipt

Preserved the old root roadmap before slimming it back to live repo direction:

- `ROADMAP.md` -> `legacy/raw/ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md`

The active root roadmap now points to owner surfaces instead of carrying the
tree-migration breadcrumb chain. Distillation tests read this raw receipt for
historical migration assertions.
