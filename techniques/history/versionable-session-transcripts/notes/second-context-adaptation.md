# Second Context Adaptation

## Technique
- id: AOA-T-0044
- name: versionable-session-transcripts

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records bounded transcript-export meaning rather than shipping the donor extension, CLI wrapper, or hosted review service

## What changed
- paths: the donor surfaces use `.specstory/history/` plus editor and CLI export flows; this adaptation keeps the already-saved-artifact idea generically without depending on one product path
- services: hosted sharing, search and organization, sign-in, support flows, and rule derivation are removed from the reusable contract
- dependencies: the adaptation depends on an existing saved history layer and one readable export path, not on the donor platform stack
- operating assumptions: contributors should read the technique as post-capture transcript packaging for reviewable history, not as product installation guidance

## What stayed invariant
- contract: transcript export begins from already-saved session artifacts
- validation logic: selected conversations can be packaged into one readable Markdown review unit with versionable cues such as timestamps or metadata
- safety rules: transcript history stays separate from authored instructions, summary distillation, and memory recall semantics

## Risks introduced by adaptation
- the pattern can collapse back into `AOA-T-0026` if repositories cannot say what transcript export adds after the first save
- teams may over-associate transcript packaging with rule derivation or hidden instruction authority because the donor product also exposes those adjacent features

## Evidence
- the public `Quickstart` doc says `SpecStory: Save AI Chat History` can save curated conversations into one Markdown document and open the file immediately for review or editing before saving
- the public `Features` doc says manual save and export can combine multiple conversations into a single Markdown file and the share flow can add extra Markdown sections and related links before publication
- the public terminal-agent overview says transcripts land under `.specstory/history/` with timestamps and metadata ready for code review or knowledge sharing

## Result
- works as a documentation-first second context and preserves a bounded post-capture transcript-export contract without carrying over donor wrapper, cloud, or rule-derivation breadth
