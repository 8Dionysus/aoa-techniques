# Origin Evidence

## Technique
- id: AOA-T-0039
- name: baseline-first-additive-profile-benchmarks

## Source project
- name: atm10-agent
- source files:
  - `README.md`
  - `docs/RUNBOOK.md`
  - `src/agent_core/combo_a_profile.py`
  - `scripts/cross_service_benchmark_suite.py`
  - `.github/workflows/combo-a-profile-smoke.yml`
- supporting posture:
  - `abyss-stack/docs/FIRST_RUN.md`
  - `abyss-stack/docs/PROFILES.md`

## Evidence
- the donor README describes a baseline-first benchmark suite and a richer `combo_a` profile that stays additive rather than replacing the default path
- the donor runbook keeps `baseline_first` as the default benchmark profile and routes additive `combo_a` parity checks through a separate nightly/manual path
- the donor benchmark script accepts `baseline_first` and `combo_a`, produces one normalized cross-service suite summary shape, and seeds additive fixtures only when the richer profile is selected
- the donor workflow keeps baseline-first checks on the main smoke path and separates the additive `combo_a` parity flow into its own nightly/manual sequence
- the supporting `abyss-stack` docs reinforce the same general posture: profiles are ordered, composed in declaration order, and richer profiles should layer on top of a base path instead of replacing it

## Interpretation
- the reusable object is baseline-first comparison discipline with additive profiles
- the public technique can stay bounded to normalized comparison surfaces without importing benchmark-suite ownership, promotion policy, rolling baseline logic, or runtime lifecycle control
