# dual-write-history-checklist

- latest alias exists at the stable expected path
- history copy exists under `run_dir`
- history copy differs from latest alias
- emitted `summary_json` and `history_summary_json` match actual files when present
- schema and status match between latest alias and history copy
- readers exclude the alias when nested history rows exist
- the same alias and history invariants still hold when the published paths are object-store keys instead of local filesystem paths
- legacy fallback is explicit and only used when no nested rows exist
