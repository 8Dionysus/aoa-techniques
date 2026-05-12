# Second Context Adaptation

## Technique
- id: AOA-T-0039
- name: baseline-first-additive-profile-benchmarks

## Target project
- name: LOCOMO Benchmark for OpenClaw Memory
- environment: public benchmark harness comparing OpenClaw memory backends on the LOCOMO dataset
- runtime: backend-specific memory benchmark runs that start with `memory-core`, then compare `memory-lancedb` and `memory-lancedb-pro` on the same selected rows, gateway, judge path, and output artifact family

## What changed
- the donor's `baseline_first` profile maps to LOCOMO/OpenClaw's `memory-core` backend baseline
- the donor's additive profile maps to LOCOMO/OpenClaw's `memory-lancedb` and `memory-lancedb-pro` backend legs
- the donor's normalized suite summary maps to each LOCOMO run directory with `summary.json`, `selected_rows.jsonl`, `qa_results.jsonl`, `judged_results.jsonl`, and memory status artifacts
- the donor's isolated additive prework maps to prebuilt-store and plugin setup paths, especially the `memory-lancedb-pro` leg that builds from the existing `memory-lancedb` corpus rather than changing the baseline path

## What stayed invariant
- the baseline still runs first
- additive profiles still reuse the same measurement surface
- the artifact shape still stays consistent across compared runs
- additive prework still stays off the default path
- the result still reports comparison discipline rather than product scoring

## Risks introduced by adaptation
- LOCOMO/OpenClaw is a full benchmark harness, so the technique must not absorb benchmark-suite ownership, LLM judge policy, memory backend design, leaderboard logic, or product scoring
- `memory-lancedb-pro` has plugin-specific setup and tuning, so the transferable evidence is isolated additive prework over the same corpus and artifact family rather than one plugin's retrieval settings
- parallel execution is supported, but it remains an execution optimization only because the output format is kept identical

## Evidence
- LOCOMO/OpenClaw README describes three backends: `memory-core`, `memory-lancedb`, and `memory-lancedb-pro`, with LanceDB legs reusing the same LOCOMO markdown and exact `memory-core` indexed chunks or chunk-aligned corpus.
- The README explicitly says to start with `memory-core` as the baseline, then compare it against `memory-lancedb` and `memory-lancedb-pro`.
- The README defines the same output family for each run, including `summary.json`, selected rows, QA results, judged results, memory status before/after, and ingest logs.
- The runner writes the same `summary.json` shape for each backend using the selected rows, QA results, judged results, run label, input path, and limit.
- `run_parallel.py` preserves the same output format while splitting work across workers, then merges JSONL files and recomputes `summary.json`.

## Result
- verdict: exact-fit second context
- note: LOCOMO/OpenClaw proves the same reusable move outside the donor lineage: run the baseline backend first, compare additive backends on the same benchmark surface and artifact shape, isolate additive prework, and keep the result as comparison evidence rather than suite governance or product scoring
