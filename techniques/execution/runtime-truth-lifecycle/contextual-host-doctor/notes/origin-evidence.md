# Origin Evidence

## Technique
- id: AOA-T-0037
- name: contextual-host-doctor

## Source project
- name: abyss-stack
- source files:
  - `docs/DOCTOR.md`
  - `docs/FIRST_RUN.md`
  - `docs/LIFECYCLE.md`
  - `docs/DEPLOYMENT.md`
  - `scripts/aoa-doctor`

## Evidence
- the donor defines `aoa-doctor` as a host-readiness and runtime-readiness probe whose purpose is to answer whether the current environment is shaped enough for the selected stack path before startup
- the donor makes the doctor selector-aware: the same `--preset` and `--profile` inputs used by runtime wrappers determine whether checks such as Intel-device availability or internal-only reminders are relevant
- the donor emits explicit `ok`, `warn`, and `fail` signals and keeps a separate strict mode that can promote warnings into failure without erasing the default advisory distinction
- the donor places `aoa-doctor` in first-run and deployment flows as a pre-start readiness surface rather than as startup, smoke, or continuous monitoring logic

## Interpretation
- the reusable object is a selector-aware preflight verdict with explicit item-level severity
- the public technique can stay bounded to contextual host readiness without importing donor-specific runtime roots, command names, or post-start health checks
