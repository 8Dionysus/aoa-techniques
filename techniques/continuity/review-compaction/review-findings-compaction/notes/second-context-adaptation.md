# Second Context Adaptation

## Technique

- id: AOA-T-0052
- name: review-findings-compaction

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where multiple review findings can be compacted into a cleaner current surface without shipping the donor daemon or synthesis runtime

## What changed

- paths: donor daemon, compact job, and synthesis paths were replaced by markdown candidate bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a compact command, daemon worker, or fix loop
- dependencies: the compaction pass now exists as a documentation-first reusable contract rather than as a donor runtime feature
- operating assumptions: the technique is read as one bounded findings-hygiene pass, not as a full review platform

## What stayed invariant

- contract: duplicate or stale findings are revalidated and compacted against current code before they survive as the active review surface
- validation logic: grouped findings remain traceable and invalidated findings do not silently persist
- safety rules: compaction remains separate from review triggering, remediation, and backlog policy

## Risks introduced by adaptation

- a documentation-first compaction pass can look stronger than the live runtime evidence if readers forget that this repo is recording the pattern, not running it
- some repositories may widen the contract into issue triage if they ignore the boundary from prioritization

## Evidence

- source family: Qodo / open-source PR-Agent
- public repository: `https://github.com/The-PR-Agent/pr-agent`
- observed revision: `9ab2636f89952c69600dc2038d39f468de699fd0`
- public docs: `https://docs.qodo.ai/code-review/get-started/use-qodo-in-prs/code-review/persistent-review-comments` and `https://docs.qodo.ai/v1/tools/tools-list/improve`
- source surfaces inspected: `pr_agent/tools/pr_code_suggestions.py`, `pr_agent/tools/pr_reviewer.py`, `pr_agent/git_providers/github_provider.py`, `pr_agent/settings/configuration.toml`, `docs/docs/tools/improve.md`, and `docs/docs/tools/review.md`

Qodo / PR-Agent closes the live-adopter gap because it keeps repeated review
output compact during iterative pull request work. Qodo's persistent review
comments update an existing review comment when new commits are pushed instead
of posting a fresh review every time, keep findings visible in the pull
request review, and maintain an audit trail of findings added and resolved per
commit. Its update flow detects the latest delta, generates suggestions from
recent changes, merges them with overall PR feedback, and marks recent findings
distinctly.

The open-source PR-Agent implementation reinforces the same shape: persistent
suggestion comments keep the newest findings at the top, fold previous
suggestions into bounded history, trim older history by configuration, validate
suggestions against current diff hunks, and use incremental review state to
find commits since the previous review. The boundary remains strict:
auto-fix, auto-approval, chat, issue triage, and merge policy are adjacent
provider features, not part of this technique's canonical default.

- source paths: `mechanics/distillation/legacy/archive/closed-incoming-packets/chat-graph-review-mailbox/docs/CHAT_GRAPH_REVIEW_MAILBOX_PLANTING_ORDER.md` and `techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing

## Result

- works as a documentation-first second context and now has external
  reinforcement from Qodo / PR-Agent, preserving the findings-compaction
  contract without importing donor compact runtime, remediation, backlog
  policy, or auto-approval breadth
