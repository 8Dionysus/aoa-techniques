# Origin Evidence

## Technique
- id: AOA-T-0093
- name: recommendation-truth-vs-host-actionability

## Source project
- name: aoa-sdk + Dionysus
- source files:
  - `src/aoa_sdk/skills/detector.py`
  - `src/aoa_sdk/models.py`
  - `src/aoa_sdk/cli/main.py`
  - `docs/skill-runtime-recommendation-gap.md`
  - `docs/skill-runtime-recommendation-gap-fix-spec.md`
  - `reports/ecosystem-audits/2026-04-06.aoa-sdk.skill-runtime-recommendation-gap-fix-session-harvest.md`

## Evidence
- the live repair kept router recommendation truth intact while annotating host actionability separately
- host executability now resolves from explicit host manifests or canonical repo, workspace, and user install roots
- non-executable auto-actions are demoted out of `activate_now` instead of being treated as runnable
- router-only items stay visible so the report can still explain relevance and manual fallback posture
- the seam was hardened in real code and verified through full `pytest`, `ruff`, and live `skills detect` and `skills guard` checks

## Interpretation
- the surviving reusable object is one control-plane law for separating semantic recommendation from runtime executability
- the public technique can stay bounded around recommendation truth, host inventory precedence, and executable-action honesty without widening into discovery, marketplace, or upstream-health doctrine
