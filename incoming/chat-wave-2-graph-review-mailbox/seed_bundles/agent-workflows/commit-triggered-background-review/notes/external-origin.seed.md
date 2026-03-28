# external-origin seed - commit-triggered-background-review

## Donor spine

- roborev-dev/roborev

## Bounded pattern extracted

- Trigger a bounded background review after a commit and emit findings as a review artifact.

## What stays out

- autonomous merge behavior
- unsupervised code rewriting
- full CI governance
- product-specific review UX

## Why narrower than the donor

- this seed keeps only the commit-bound review artifact loop
- it leaves product workflow, remediation systems, and broader automation behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
