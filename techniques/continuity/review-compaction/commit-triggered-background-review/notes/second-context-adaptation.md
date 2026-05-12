# Second Context Adaptation

## Technique

- id: AOA-T-0051
- name: commit-triggered-background-review

## Target project

- name: aoa-techniques
- environment: public library repository with staged external-import waves, technique bundles, and generated catalog surfaces
- runtime: documentation-first repository where a commit-triggered background review can be described as a bounded artifact loop without shipping the donor review daemon itself

## What changed

- paths: donor daemon, hook, and queue paths were replaced by markdown candidate bundles, landing notes, and the published technique bundle
- services: this adaptation does not ship a background review service, TUI, or fix loop
- dependencies: the review artifact now exists as a documentation-first reusable contract rather than as a donor runtime feature
- operating assumptions: the technique is read as one bounded post-commit review artifact pattern, not as a full review platform

## What stayed invariant

- contract: a visible commit boundary triggers background review and yields an inspectable findings artifact
- validation logic: the artifact names the reviewed commit or scope and stays distinct from any later remediation step
- safety rules: review, remediation, and policy enforcement remain separate surfaces

## Risks introduced by adaptation

- a documentation-first artifact loop can look stronger than the live runtime evidence if readers forget that this repo is recording the pattern, not running it
- some repositories may widen the contract into full CI governance if they ignore the remediation boundary

## Evidence

- source family: Qodo / open-source PR-Agent
- public repository: `https://github.com/The-PR-Agent/pr-agent`
- observed revision: `9ab2636f89952c69600dc2038d39f468de699fd0`
- public docs: `https://docs.qodo.ai/code-review/get-started/use-qodo-in-prs/code-review/persistent-review-comments`, `https://docs.pr-agent.ai/installation/github/`, and `https://docs.pr-agent.ai/usage-guide/automations_and_usage/`
- source surfaces inspected: `README.md`, `docs/docs/installation/github.md`, `docs/docs/usage-guide/automations_and_usage.md`, `pr_agent/settings/configuration.toml`, `pr_agent/tools/pr_reviewer.py`, and `pr_agent/git_providers/github_provider.py`

Qodo / PR-Agent closes the live-adopter gap because it exposes a public
workflow where pull request or push-trigger events launch review work and
publish inspectable review output. The open-source PR-Agent GitHub Action
examples run on `pull_request` events, including `synchronize` in the quick
start, and the configuration surface keeps automatic review as a named command
rather than an implicit merge or rewrite path. Qodo's persistent review comment
docs also show that new commits update an existing review comment while
keeping findings visible in the pull request review.

The exact reusable proof is the trigger-and-artifact seam: a visible commit or
push boundary causes background review output to be refreshed as an inspectable
review surface. The boundary remains strict: Qodo / PR-Agent also has adjacent
auto-improve, auto-approval, chat, and broader platform behavior, but those are
not part of this technique's canonical default.

- source paths: `incoming/chat-graph-review-mailbox/candidate_bundles/agent-workflows/commit-triggered-background-review/TECHNIQUE.candidate.md`, `incoming/chat-graph-review-mailbox/docs/CHAT_GRAPH_REVIEW_MAILBOX_PLANTING_ORDER.md`, and `techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md`
- review surface or generated output touched: `TECHNIQUE_INDEX.md`, generated catalog and capsule surfaces, and the Wave 2 staging registry after landing

## Result

- works as a documentation-first second context and now has external
  reinforcement from Qodo / PR-Agent, preserving the commit-bound review
  artifact contract without importing the donor review daemon, remediation
  breadth, auto-approval, or CI-governance behavior
