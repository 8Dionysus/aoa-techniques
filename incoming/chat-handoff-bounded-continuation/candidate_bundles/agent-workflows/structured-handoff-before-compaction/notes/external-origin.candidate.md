# external-origin seed - structured-handoff-before-compaction

## Donor spine

- yan5xu/code-relay
- thebasedcapital/nightcrawler

## Bounded pattern extracted

- Create one structured handoff artifact before compaction or session rollover so context transfer stays reviewable.

## What stays out

- generic transcript export
- broad orchestration frameworks
- memory writeback
- donor platform semantics

## Why narrower than the donors

- this seed isolates one pre-compaction transfer contract
- it leaves orchestration stacks and broader runtime behavior behind
- it does not claim the donor repos should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
