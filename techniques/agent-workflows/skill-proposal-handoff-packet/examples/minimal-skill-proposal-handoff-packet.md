# Minimal skill-proposal handoff packet

```yaml
packet_type: skill_proposal_handoff
proposal_name: reviewed-diff-closeout-skill
receiving_owner: skill-owning repository
source_practice:
  technique_refs:
    - AOA-T-0001
    - AOA-T-0033
execution_pressure: >
  Review sessions repeatedly need the same closeout move: summarize the diff,
  name validation, record one decision if the boundary changed, and stop before
  merge authority.
proposed_trigger_boundary: >
  Use when a bounded repository change is complete and the agent needs a
  reviewable closeout workflow.
inputs:
  - changed files or diff summary
  - validation results
  - known unresolved risks
outputs:
  - closeout summary
  - validation statement
  - optional decision-note request
workflow_shape:
  - read current diff
  - compare against requested scope
  - report validation and unresolved risks
  - route decision-note need without writing it automatically
risks:
  - packet could be mistaken for merge approval
  - decision notes could be created for trivial edits
verification_hints:
  - check that the final skill keeps merge, release, and decision authority out
    of the workflow unless explicitly owned
nearest_wrong_targets:
  - proof verdict
  - playbook scenario
  - runtime command
non_acceptance_stop_line: >
  This packet is only a proposal for owner review. It does not create, accept,
  install, or activate a skill.
```

Accept the packet only as a handoff object. The receiving owner must still
decide whether a real skill should exist, what its trigger should be, and how it
is verified.
