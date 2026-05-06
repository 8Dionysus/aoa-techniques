# Origin Evidence

## Technique
- id: AOA-T-0091
- name: workspace-root-ingress-and-mutation-gate

## Source project
- name: aoa-sdk + 8Dionysus
- source files:
  - `src/aoa_sdk/skills/detector.py`
  - `src/aoa_sdk/cli/main.py`
  - `docs/session-closeout.md`
  - `docs/WORKSPACE_INSTALL.md`
  - `/srv/AGENTS.md`

## Evidence
- the workspace root now defines an explicit session-start contract that requires one ingress pass before substantial work
- the same root contract requires one guard pass before risky, mutating, infra, runtime, repo-config, or public-share actions
- the detector output keeps `activate_now`, `must_confirm`, `suggest_next`, and `blocked_actions` visible instead of hiding posture in free-form memory
- the route was used as part of the real workspace-foundation landing wave rather than being invented as a template-only abstraction

## Interpretation
- the surviving reusable object is one workspace-root operating law for entering and gating federated work
- the public technique can stay bounded around ingress-plus-guard posture without importing workspace install, bootstrap, or closeout doctrine
