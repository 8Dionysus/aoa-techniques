# Second Context Adaptation

## Technique
- id: AOA-T-0044
- name: versionable-session-transcripts

## Target project
- name: claude-code-log
- environment: open-source CLI tooling that converts already-saved Claude Code transcript JSONL files into readable HTML and Markdown review artifacts
- runtime: local post-capture transcript conversion and export over saved session files, with portable Markdown output, session navigation, and summary-bearing transcript views

## What changed
- paths: the donor surfaces use `.specstory/history/` plus editor and CLI export flows, while the second context starts from saved Claude Code transcript JSONL files and converts them into Markdown or HTML
- services: the target also offers navigation, filtering, and HTML rendering, but this adaptation narrows to the readable Markdown transcript artifact rather than viewer product breadth
- dependencies: the adaptation depends on an existing saved transcript layer and one readable export path, not on the donor extension, hosted sharing, or account stack
- operating assumptions: contributors should read the technique as post-capture transcript packaging for reviewable history, not as product installation or transcript-viewer doctrine

## What stayed invariant
- contract: transcript export begins from already-saved session artifacts
- validation logic: selected conversations can be packaged into one readable Markdown review unit with versionable cues such as timestamps or metadata
- safety rules: transcript history stays separate from authored instructions, summary distillation, and memory recall semantics

## Risks introduced by adaptation
- the pattern can collapse back into `AOA-T-0026` if repositories cannot say what transcript export adds after the first save
- teams may over-associate transcript packaging with log viewing or transcript analytics because the second context also exposes richer viewer features alongside export
- teams may still confuse transcript packaging with witness tracing if detailed logs or summaries are mistaken for the same artifact contract

## Evidence
- the public `claude-code-log` README says the tool converts already-saved transcript JSONL files into readable HTML and Markdown
- the same README says Markdown export is a lightweight, portable alternative to HTML with session summaries, headers, collapsible details, and code-preserving fenced blocks
- those public surfaces preserve the same reusable core: start after capture, package transcript history into a readable Markdown review artifact, and keep the artifact portable enough for commit, handoff, or later review

## Result
- works as a real public second context and preserves a bounded post-capture transcript-export contract without carrying over donor wrapper, cloud, or transcript-viewer breadth
