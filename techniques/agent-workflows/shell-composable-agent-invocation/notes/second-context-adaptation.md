# Second Context Adaptation

## Technique
- id: AOA-T-0031
- name: shell-composable-agent-invocation

## Target project
- name: OpenAI Codex CLI `codex exec`
- environment: official public CLI docs for non-interactive Codex runs, scripted execution, and CI-style shell usage
- runtime: one-shot terminal invocation that can read prompts from stdin, stream output to stdout or JSONL, and write the final message to a file for downstream scripting

## What changed

- paths: the donor exposes shell-friendly one-shot commands, while the second context uses `codex exec` or `codex e` rather than donor-specific command names
- services: the wider Codex family includes interactive sessions, resume flows, and approval controls, but this adaptation narrows to the one-shot scripted run surface only
- dependencies: the adaptation depends on explicit stdin, stdout, JSONL, and file output boundaries rather than on the donor CLI layout
- operating assumptions: operators use the non-interactive exec path when the value is shell composition, and widen into interactive sessions only when the task has clearly outgrown the bounded one-shot contract

## What stayed invariant

- contract: one agent run stays one-shot and shell-composable
- validation logic: stdin, stdout, files, or pipes still define the observable composition boundary
- safety rules: the run ends after the current result instead of drifting into a hidden session

## Risks introduced by adaptation

- resume and interactive continuation features can blur the line between a shell-composable one-shot run and a longer-lived session contract
- file-output and JSON-event options can still become vague if the shell-visible I/O boundaries stop being the thing reviewers actually rely on
- automation flags or approval bypasses can tempt teams to treat one-shot scripting as if it already covered broader workflow safety

## Evidence

- the official Codex CLI docs say `codex exec` is for scripted or CI-style runs that should finish without human interaction
- the same docs keep shell composition explicit by allowing the prompt to come from stdin, the final message to be written to a file, and JSONL events to stream to stdout
- those public surfaces preserve the same reusable core: one visible shell invocation with explicit I/O boundaries, not a hidden long-lived session

## Result

- works as a real public second context and preserves the bounded core without carrying over donor-specific CLI breadth
