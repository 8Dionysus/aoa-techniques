# Second Context Adaptation

## Technique
- id: AOA-T-0055
- name: requirements-design-tasks-ladder

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded pre-execution planning ladder rather than shipping the donor's command set, templates, or methodology framework
- external reinforcement:
  - name: SpecForge-Agent
  - repository: `wirelessr/SpecForge-Agent`
  - observed revision: `bfbc98f7be766b36e7979fb5fd9472d69a3d0c48`
  - public surfaces: `README.md`, `autogen_framework/README.md`, `autogen_framework/workflow_manager.py`, `autogen_framework/agents/plan_agent.py`, `autogen_framework/agents/design_agent.py`, `autogen_framework/agents/tasks_agent.py`, `tests/e2e/workflow_test.sh`, and `tests/e2e/simple_workflow_test.sh`
  - supporting contrast: `github/spec-kit` at `765e60f1c46a242b44238ce1fc7bdd2a5e9cd1ab`, using only the visible `spec.md` -> `plan.md` -> `tasks.md` surface as a boundary check rather than importing its full SDD method

## What changed
- paths: the donor uses slash-command workflows, `.kiro/specs/` artifacts, and template-driven generation; this adaptation keeps the generic requirement -> design -> task ladder without depending on one command host
- services: steering, project memory, validation commands, multi-agent orchestration, and template ecosystems were removed from the reusable contract
- dependencies: the adaptation depends on three explicit planning layers, not on the donor tooling stack
- operating assumptions: contributors should read the technique as a bounded planning seam before execution, not as product setup or methodology adoption guidance

## What stayed invariant
- contract: requirements, design, and tasks remain distinct layers that constrain one another in order
- validation logic: the task layer can be traced back to visible design, and design can be traced back to visible requirements
- safety rules: the technique remains outside implementation workflow, runtime coordination, and wider methodology doctrine
- external reinforcement: SpecForge-Agent keeps `requirements.md`, `design.md`, and `tasks.md` as explicit workflow artifacts, generates design from approved requirements, generates tasks from design plus requirements, and tests the sequence before implementation

## Risks introduced by adaptation
- the pattern can collapse back into [AOA-T-0001](../../../../agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) if repositories cannot explain what this ladder adds before apply/verify/report starts
- teams may over-associate the ladder with a whole methodology because the donor also bundles steering, validation, templates, and multi-agent support
- the public bundle could drift into command or template doctrine if layer boundaries stop being the real center of gravity

## Evidence
- the donor README states `Requirements -> Design -> Tasks -> Implementation` as the core spec-driven workflow
- the same README shows separate commands for `spec-requirements`, `spec-design`, and `spec-tasks`, reinforcing visible movement down the ladder instead of one merged planning blob
- the donor example spec stores `requirements.md`, `design.md`, and `tasks.md` as separate artifacts for the same feature
- the sample `tasks.md` includes requirement coverage notes, which shows the task layer remains traceable back to the earlier planning layers
- SpecForge-Agent's public documentation names a complete `Requirements -> Design -> Tasks -> Execution` workflow with phased review and approval, keeping the first three layers separate before execution begins.
- SpecForge-Agent's `PlanAgent` creates `requirements.md`, `DesignAgent` builds `design.md` from approved requirements, and `TasksAgent` reads both `design.md` and `requirements.md` before writing `tasks.md`.
- SpecForge-Agent's end-to-end tests check that `requirements.md`, `design.md`, and `tasks.md` are generated in order before implementation.
- GitHub Spec Kit independently exposes the same visible planning spine as `spec.md` -> `plan.md` -> `tasks.md`, but its broader SDD command suite, constitution gates, hooks, research documents, and implementation flow remain out of scope for this technique.

## Result
- works across donor, documentation-first, SpecForge-Agent, and Spec Kit planning-spine contexts while preserving one bounded requirement-to-design-to-task ladder without carrying over command suites, template systems, approvals, agent orchestration, memory layers, implementation execution, or wider methodology stacks
