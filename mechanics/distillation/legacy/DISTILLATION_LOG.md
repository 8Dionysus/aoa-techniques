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
