# Second Context Adaptation

## Technique
- id: AOA-T-0055
- name: requirements-design-tasks-ladder

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded pre-execution planning ladder rather than shipping the donor's command set, templates, or methodology framework

## What changed
- paths: the donor uses slash-command workflows, `.kiro/specs/` artifacts, and template-driven generation; this adaptation keeps the generic requirement -> design -> task ladder without depending on one command host
- services: steering, project memory, validation commands, multi-agent orchestration, and template ecosystems were removed from the reusable contract
- dependencies: the adaptation depends on three explicit planning layers, not on the donor tooling stack
- operating assumptions: contributors should read the technique as a bounded planning seam before execution, not as product setup or methodology adoption guidance

## What stayed invariant
- contract: requirements, design, and tasks remain distinct layers that constrain one another in order
- validation logic: the task layer can be traced back to visible design, and design can be traced back to visible requirements
- safety rules: the technique remains outside implementation workflow, runtime coordination, and wider methodology doctrine

## Risks introduced by adaptation
- the pattern can collapse back into [AOA-T-0001](../../plan-diff-apply-verify-report/TECHNIQUE.md) if repositories cannot explain what this ladder adds before apply/verify/report starts
- teams may over-associate the ladder with a whole methodology because the donor also bundles steering, validation, templates, and multi-agent support
- the public bundle could drift into command or template doctrine if layer boundaries stop being the real center of gravity

## Evidence
- the donor README states `Requirements -> Design -> Tasks -> Implementation` as the core spec-driven workflow
- the same README shows separate commands for `spec-requirements`, `spec-design`, and `spec-tasks`, reinforcing visible movement down the ladder instead of one merged planning blob
- the donor example spec stores `requirements.md`, `design.md`, and `tasks.md` as separate artifacts for the same feature
- the sample `tasks.md` includes requirement coverage notes, which shows the task layer remains traceable back to the earlier planning layers

## Result
- works as a documentation-first second context and preserves one bounded requirement-to-design-to-task ladder without carrying over the donor's command suite, template system, or wider methodology stack
