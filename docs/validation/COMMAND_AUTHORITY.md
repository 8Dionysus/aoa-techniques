# Validation Command Authority

`aoa-techniques` uses a lane-owned command model:

- `config/validation_lanes.json` is the canonical storage surface for lane
  definitions, blocking command sequences, generated drift paths, and advisory
  boundary notes.
- `scripts/validation_lanes.py` is the loader/API for Python callers.
- `scripts/ci_gate.py` executes CI lane modes.
- `scripts/run_part_local_tests.py` discovers mechanic part-local pytest homes
  and their related builder `--check` / validator scripts for the
  `mechanics/part-local` lane.
- `scripts/validate_source_contracts.py` is the source-only technique contract
  entrypoint for `source-fast`; it must not check generated freshness.
- `scripts/release_check.py` remains the release entrypoint and worktree
  stabilizer, but it asks the loader for the `release` lane from the manifest.
- `scripts/validate_repo.py` remains the compatibility CLI and import adapter;
  rule implementation lives in `scripts/validators/` owner modules.
- Generated/read-model command groups live under `command_groups.generated_check`
  in the lane manifest and map to explicit projection validator modules.
- `docs/validation/script_inventory.json` describes every active script's
  owner, lane, side effects, and test target. It is inventory only, not a
  place to store executable lane sequences.
- GitHub workflow YAML calls lane entrypoints. It must not rebuild lane meaning
  inline.
- `.github/workflows/repo-validation.yml` owns the PR and moving-main
  `source-fast` growth gate, with generated checks only on pushes to `main`.
- `.github/workflows/release-audit.yml` owns tag/manual release checks through
  the `release` lane.
- `.github/workflows/nightly-sentinel.yml` owns scheduled/manual moving-main
  drift checks through the `nightly` lane and latest
  release reproduction on the latest `v*` tag.
- `AGENTS.md` cards may name focused local checks, lane ids, and nearby owner
  routes. They should not copy the full release or generated command sequence.
- Active docs and decision guidance name lane ids and nearest owner
  `AGENTS.md` checks. Exact executable sequences stay in
  `config/validation_lanes.json` or a focused `AGENTS.md` when a local command
  is genuinely useful there.
- Decision records, changelogs, receipts, landing logs, and review ledgers
  preserve verification scope or outcome, not executable command snippets.

The manifest defines the `source-fast`, `generated`, `mechanics/part-local`,
`release`, `nightly`, and `advisory` routes. Workflow YAML and release tooling
invoke those routes without making this Markdown file a second command store.

## Promotion Rule

Advisory boundary notes become hard gates only when a current source owner,
runtime owner, or decision record proves that `aoa-techniques` owns the
behavior being checked.

Until then, export/runtime, trace/eval, and security/adversarial topics stay as
route boundaries. This repository can check public hygiene, generated parity,
mechanic-local candidate packets, and technique-canon shape; it does not become
the skill export owner, eval verdict layer, or runtime policy engine.

## Failure Route

When a lane fails:

1. Fix the source owner that the failing command names.
2. Rebuild generated companions only from their source builders.
3. Keep `config/validation_lanes.json` as the command store if the command
   route itself moved.
4. Update `docs/validation/validator_inventory.json` when owner, lane, mode, or
   failure route changes.
5. Update `docs/validation/script_inventory.json` when a script is added,
   moved, removed, or changes owner, lane, side-effect posture, CI inclusion,
   or focused test target.
