# Second Context Adaptation

## Technique
- id: AOA-T-0023
- name: stateless-single-shot-agent

## Target project
- name: GitHub Copilot CLI programmatic mode
- environment: official terminal-agent documentation for a CLI that supports both interactive sessions and one-prompt programmatic invocations
- runtime: shell-side single-prompt invocation path where the CLI completes the task and exits, with explicit tool approval or allow/deny flags around mutating or command-executing tools

## What changed
- paths: the donor exposes `qq` and `qa`, while this second context uses `copilot -p` and approval flags rather than donor-specific command names
- services: the target family exposes broader interactive features and product integration, but this adaptation narrows to the programmatic one-prompt path only
- dependencies: the confirmation seam moves from donor command split to per-tool approval prompts plus explicit allow/deny flags
- operating assumptions: operators use the single-prompt path for quick terminal work and widen into interactive mode only when the task has clearly outgrown the bounded fast path

## What stayed invariant
- contract: one shell-side invocation stays mostly independent and exits after handling one prompt
- validation logic: quick question flows remain distinct from confirmed tool-using action flows, and the fast path does not require hidden continuity across runs
- safety rules: mutating or command-executing tools stay behind explicit approval unless the operator deliberately widens permissions

## Risks introduced by adaptation
- broad auto-approval flags can widen the surface beyond the bounded confirmation seam that makes the fast path reviewable
- interactive continuation can blur the line between a one-prompt fast path and a longer-lived session contract
- tool allowlists scoped too broadly can weaken the practical discipline of one confirmed shell-side step

## Evidence
- the official Copilot CLI docs say the CLI has interactive and programmatic interfaces, and the programmatic interface lets an operator pass a single prompt directly on the command line
- the same docs say the CLI completes the task and then exits in that programmatic path, which preserves the mostly stateless one-invocation contract
- the security and approval docs say tools that could modify files or execute commands ask for approval by default, and one approval option allows a particular command this time only
- the docs also keep the boundary visible by warning that broader automatic approval flags widen risk and should be used deliberately

## Result
The same shell-side fast path survives in an independent public terminal-agent family: one prompt, one invocation, explicit approval before mutating tool use, and a clear boundary from broader interactive sessions.
