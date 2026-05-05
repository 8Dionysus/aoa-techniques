# Origin Evidence

## Technique
- id: AOA-T-0047
- name: github-review-template-lift

## Source project
- name: aoa-techniques
- source files:
  - `generated/github_review_template_manifest.json`
  - `.github/ISSUE_TEMPLATE/canonical-promotion.md`
  - `.github/ISSUE_TEMPLATE/external-import-review.md`
  - `.github/ISSUE_TEMPLATE/technique-proposal.md`
  - `.github/PULL_REQUEST_TEMPLATE.md`
  - `docs/KAG_SOURCE_LIFT_GUIDE.md`

## Evidence
- `generated/github_review_template_manifest.json` already projects the authored template shapes into a bounded derived intake surface
- the `.github` issue and pull-request templates already carry review prompts that are useful as an intake inventory without becoming workflow policy
- `docs/KAG_SOURCE_LIFT_GUIDE.md` explicitly frames GitHub review templates as a bounded source-class pilot and keeps policy or state behavior deferred

## Interpretation
- the reusable pattern already exists in the live repository as a review-intake surface, not as a review-state machine
- the technique generalizes that pattern into a public bounded intake-lift contract while keeping the authored templates authoritative
