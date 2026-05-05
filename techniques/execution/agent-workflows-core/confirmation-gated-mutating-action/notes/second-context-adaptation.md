# Second Context Adaptation

## Technique
- id: AOA-T-0028
- name: confirmation-gated-mutating-action

## Target project
- name: GitHub Copilot coding-agent approval surfaces
- environment: official public docs for GitHub Copilot agent mode in IDEs plus GitHub Copilot CLI tool-approval flows
- runtime: interactive coding-agent surfaces where terminal commands or tool invocations are proposed first and only execute after explicit operator approval

## What changed
- paths: the donor splits read-only and action paths with `qq` and `qa`, while the second context uses Copilot agent-mode terminal-command confirmation and Copilot CLI tool approvals instead of donor-specific command names
- services: the broader Copilot product family includes planning, chat, custom agents, and approval presets, but this adaptation narrows to the one explicit confirmation seam before command or tool execution
- dependencies: the adaptation depends on visible operator approval before mutation, not on the donor's stateless fast-path shell split
- operating assumptions: operators review the proposed command or tool use and either approve, reject, or redirect it before any mutating step runs

## What stayed invariant
- contract: one explicit confirmation is required before a bounded mutation runs
- validation logic: read or plan work and mutation stay distinct, and the workflow should stop after the confirmed action
- safety rules: the confirmation must name the mutation clearly and should not collapse into a weak or implicit approval

## Risks introduced by adaptation
- broad auto-approval settings can widen the operating surface beyond the bounded confirmation seam that makes the pattern reviewable
- the pattern can still become vague if a tool-approval prompt exists but does not make the actual mutation clear enough to review
- some teams may mistake workspace-trust prompts or session-wide permission toggles for the reusable core instead of the per-action gate

## Evidence
- the GitHub Copilot IDE docs say agent mode suggests terminal commands and then asks the operator to confirm whether Copilot can run them before continuing the task
- the GitHub Copilot CLI docs say tools that could modify or execute files ask for approval before running, and rejection stops the current operation so the operator can redirect the approach
- those public surfaces preserve the same reusable core: mutation stays behind one explicit approval seam instead of hiding inside a generic autonomous loop

## Result
- works as a real public second context and preserves the bounded core without carrying over donor-specific shell fast-path breadth
