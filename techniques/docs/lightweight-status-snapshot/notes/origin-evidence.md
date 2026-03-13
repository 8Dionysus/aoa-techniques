# Origin Evidence

## Technique
- id: AOA-T-0009
- name: lightweight-status-snapshot

## Source project
- name: atm10-agent
- source files:
  - `docs/SOURCE_OF_TRUTH.md`
  - `README.md`
  - `MANIFEST.md`
  - `docs/DECISIONS.md`

## Evidence
- `docs/SOURCE_OF_TRUTH.md` assigns `README.md` the role of short human-facing entrypoint and `MANIFEST.md` the role of short machine/human snapshot, while routing long chronology to `docs/SESSION_*.md`
- the same source file explicitly says test counters should not be duplicated everywhere and that current-state truth should live in CI plus the latest `docs/SESSION_*.md`
- `README.md` keeps quick links to canonical docs and points current-state evidence to CI plus `docs/SESSION_2026-03-13.md`
- `MANIFEST.md` stays in snapshot form: current date, active capabilities, and canonical doc links without long historical logs
- `docs/DECISIONS.md` records the doc-hygiene transition explicitly: `README.md` and `MANIFEST.md` were moved to lightweight snapshot form with links to `TODO/PLANS/RUNBOOK/SESSION`

## Interpretation
- this origin is not only descriptive; it shows the technique as an active policy, a recorded transition decision, and a live repository state
