# Concrete Repo-Validation Rollout

This example shows one concrete public-safe adaptation of `signal-first-gate-promotion` for a repository validation signal.

## Scenario

A repository already publishes one machine-readable validation summary on every pull request. The team wants to move that signal toward strict enforcement, but only on one narrow nightly surface until the rollout proves stable.

## 1. Keep pull requests observational

Run the validation check in observational mode on pull requests:

```bash
python scripts/check_repo_contracts.py --policy signal_only --summary-json runs/repo-validation/pr_summary.json
```

- the summary still publishes on failure
- pull requests stay reviewable without turning every unstable failure into an immediate hard block

## 2. Publish readiness from recent runs

Build a readiness summary from recent validation history:

```bash
python scripts/check_repo_contracts_readiness.py --history-dir runs/repo-validation-history --policy report_only --summary-json runs/repo-validation-readiness/readiness_summary.json
```

The readiness summary should answer whether the signal is stable enough to consider narrow strict enforcement.

## 3. Make governance explicit

Turn readiness history into one visible promotion decision:

```bash
python scripts/check_repo_contracts_governance.py --readiness-dir runs/repo-validation-readiness --policy report_only --summary-json runs/repo-validation-governance/governance_summary.json
```

The output should be one explicit `go` or `hold`, plus reason codes when promotion is still blocked.

## 4. Publish progress and transition summaries

Keep rollout telemetry visible even before strict activation:

- `runs/repo-validation-progress/progress_summary.json`
- `runs/repo-validation-transition/transition_summary.json`

These summaries should publish:

- remaining stable runs needed
- remaining streak needed
- current strict-surface choice
- any reasons why promotion is still incomplete

## 5. Activate one narrow strict surface only

When governance says `go`, switch only the nightly validation surface to strict mode:

```bash
python scripts/check_repo_contracts.py --policy fail_nightly --summary-json runs/repo-validation/nightly_summary.json
```

Keep other surfaces observational:

- pull requests: `signal_only`
- local debugging: `signal_only`
- ad hoc triage runs: observational unless explicitly promoted later

## 6. Preserve diagnostics after strict failure

Even if the nightly strict run fails:

- `nightly_summary.json` still publishes
- readiness/governance/progress/transition summaries still publish
- operators can see why the signal went red without scraping logs

## Anti-drift rule

If the repository silently turns multiple surfaces strict at once, or stops publishing summaries once strict mode starts failing, the rollout is no longer following `signal-first-gate-promotion`.
