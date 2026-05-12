# Second Context Adaptation

## Technique
- id: AOA-T-0037
- name: contextual-host-doctor

## Target project
- name: Get Physics Done
- environment: public multi-runtime agentic research CLI and runtime-integration package
- runtime: terminal-side readiness flow for selected AI runtimes such as Claude Code, Codex, Gemini CLI, GitHub Copilot CLI, and OpenCode

## What changed
- the donor's profile or preset selector maps to GPD's `--runtime`, `--local`, `--global`, and optional `--target-dir` readiness target
- the donor's host-readiness script maps to GPD's `gpd doctor --runtime <runtime>` runtime-readiness mode
- the donor's `ok`, `warn`, and `fail` rows map to GPD's structured check statuses, blockers, advisories, and `overall` verdict
- the donor's pre-start boundary maps to GPD's installer and operator preflight before runtime-owned installation, unattended permission alignment, plan preflight, or paper build truth

## What stayed invariant
- the diagnostic still runs before the selected runtime path is treated as ready
- the selected runtime and install target still change which checks are relevant
- item-level readiness checks still remain visible as separate statuses
- warning/advisory output remains distinct from blocking failure
- the doctor remains diagnostic and hands off to sibling readiness, permission, plan, or build checks instead of absorbing them

## Risks introduced by adaptation
- GPD is a broader agentic research workflow package, so the technique must not absorb command orchestration, permission synchronization, plan validation, manuscript build, or physics-review doctrine
- GPD's doctor is runtime-target readiness rather than container-stack readiness, so the transferable evidence is the selected-target diagnostic contract rather than a particular substrate
- GPD also has `validate unattended-readiness`, `validate plan-preflight`, and `paper-build` surfaces, so later reuse must keep doctor output separate from permission, plan, and build verdicts

## Evidence
- GPD README documents `gpd doctor --runtime <runtime> --local` and `gpd doctor --runtime <runtime> --global` as runtime-readiness checks for a selected runtime target.
- GPD README treats `Workflow Presets` and `LaTeX Toolchain` doctor rows as readiness signals that can be warnings rather than full install blockers, while `paper-build` remains the build truth.
- GPD CLI routes `doctor --runtime` into `run_doctor(..., runtime=..., install_scope=..., target_dir=..., cwd=...)` and defaults the target to local readiness unless a global or explicit target is selected.
- GPD health code normalizes runtime, scope, and target into one readiness context, checks runtime launcher, runtime config target, provider/auth guidance, optional live executable probes, LaTeX toolchain, and workflow presets, and returns `mode="runtime-readiness"` when a runtime is selected.
- GPD installer preflight consumes the structured doctor report, collects `fail` checks as blockers, keeps warning/advisory messages separate, and tells the operator to rerun the exact `gpd doctor --runtime ...` command before continuing.

## Result
- verdict: exact-fit second context
- note: Get Physics Done proves the same reusable move outside the donor lineage: run a selected-target doctor before treating a runtime path as ready, keep item-level readiness statuses visible, separate warnings from blockers, and hand off to sibling permission, plan, build, or runtime workflows after the diagnostic verdict
