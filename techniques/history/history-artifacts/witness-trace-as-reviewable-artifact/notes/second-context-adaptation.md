# Second Context Adaptation

## Technique
- id: AOA-T-0045
- name: witness-trace-as-reviewable-artifact

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over portable, reviewable technique bundles
- external reinforcement:
  - name: Maida / AgentDbg
  - repository: `AgentDbg/AgentDbg`
  - observed revision: `8a14dad4ee9bd1c45a354bf2f0b497f8e3f30273`
  - public surfaces: `README.md`, `docs/reference/trace-format.md`, `schemas/run.schema.json`

## What changed
- donor-specific pilot roles, eval anchor names, and compost promotion steps were rewritten as a reusable history-artifact contract
- memo taxonomy mapping remains a boundary note instead of part of the invariant core
- the paired trace-plus-summary posture became public-safe artifact language rather than witness-route operating instructions
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes
- the external Maida reinforcement proves the same non-transcript trace-artifact shape in a local-first agent debugger: one run has `run.json` metadata, `events.jsonl` event stream, ordered LLM/tool/error/state events, redaction/truncation, and a human-readable timeline / summary panel for review

## What stayed invariant
- the trace remains a reviewable export artifact rather than a memory object
- run identity, ordered steps, tool visibility, state deltas, and summary posture remain visible
- redaction-first and failure-path preservation remain part of the contract
- writeback and promotion stay downstream of the trace rather than inside it
- external trace storage remains local and review-first rather than becoming memory authority, hosted observability doctrine, or promotion policy

## Risks introduced by adaptation
- the public wording can drift into generic workflow logging if state-delta and review posture are not kept explicit
- the bundle can widen into runtime witness behavior, memory writeback, or canon routing if the donor pilot shape is not carefully stripped away
- a minimal example can feel too abstract if it does not show both the structured trace and the human-readable summary
- a debugger timeline can be mistaken for this whole technique unless the state-delta and pre-downstream-review boundary stay explicit

## Evidence
- the public technique stays in `history` because the reusable object is a surviving review artifact for a bounded run rather than a memory-object taxonomy or playbook route
- the bundle now has explicit neighboring seams for capture and transcript packaging so this technique can stay narrow
- the donor evidence remains strong enough to support a bounded promoted bundle without importing pilot-only role or runtime detail
- Maida's public trace-format contract keeps one local run directory with `events.jsonl` and `run.json`, ordered events, `STATE_UPDATE` snapshots or diffs, `TOOL_CALL` and `LLM_CALL` payloads, `ERROR` and loop-warning evidence, redaction/truncation rules, and a run summary panel in the local viewer

## Result
- verdict: works across origin and external trace-artifact contexts
- note: the adapted bundle now has exact-fit external reinforcement for reviewable witness trace export without widening into transcript packaging, memory writeback, hosted observability, or promotion policy
