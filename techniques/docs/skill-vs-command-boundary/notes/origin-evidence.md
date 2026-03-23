# Origin Evidence

## Technique
- id: AOA-T-0040
- name: skill-vs-command-boundary

## Source project
- name: agentic-dev-team
- source files:
  - `README.md`
  - `docs/skills.md`
  - `skills/test-driven-development.md`
  - `commands/plan.md`

## Evidence
- the donor README says skills provide reusable knowledge modules while slash commands invoke agents and skills directly as user-facing entrypoints
- `docs/skills.md` names two separate reusable capability kinds: skills under `skills/` as agent-agnostic knowledge modules and slash commands under `commands/` as user-invocable workflows with numbered steps, argument parsing, and structured output
- `docs/skills.md` says agent references explain when and why a skill is used, while the skill artifact itself defines how the capability works
- the donor skill example `skills/test-driven-development.md` stores reusable discipline, constraints, and verification gates as a capability artifact rather than as one command's argument surface
- the donor command example `commands/plan.md` stores invocation syntax, arguments, role, numbered steps, and approval/output behavior as a command artifact rather than as the reusable skill definition

## Interpretation
- the reusable object is the ownership boundary between reusable skill meaning and user-facing command invocation
- the public technique can stay bounded to that artifact split without importing plugin install flows, orchestrator policy, model routing tables, review-agent catalogs, or broader slash-command product doctrine
