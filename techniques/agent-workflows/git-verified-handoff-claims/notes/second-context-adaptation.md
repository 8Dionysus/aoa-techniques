# Second Context Adaptation

## Technique
- id: AOA-T-0059
- name: git-verified-handoff-claims

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded handoff-verification seam rather than shipping the donors' episode runners, snapshot tooling, or coordination logs

## What changed

- paths: Nightcrawler uses a mandatory session-opening ritual and AGOR uses snapshot-receiver verification guidance; this adaptation keeps the generic handoff-claims-versus-git-state contract without requiring one file layout or one snapshot path
- services: orchestrator loops, mission state tracking, receipt logs, version checks, and broader snapshot machinery were removed from the reusable contract
- dependencies: the adaptation depends on an existing handoff packet plus visible local git evidence, not on a specific runtime shell, task tracker, or coordination platform
- operating assumptions: contributors should read the technique as a bounded verification seam layered after packet creation and before continued work

## What stayed invariant

- contract: concrete handoff claims are checked against visible git state before they are trusted for continuation
- validation logic: the receiver can name the git evidence used and can surface mismatches explicitly
- safety rules: the technique remains outside packet authoring, receipt semantics, witness export, and broad review-policy doctrine

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0057](../structured-handoff-before-compaction/TECHNIQUE.md) if repositories stop separating packet creation from claim verification
- the public bundle could drift into [AOA-T-0045](../../history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) if teams expect a full run artifact instead of one bounded trust check
- the technique could widen into generic code review if every code change is routed through it instead of only handoff claims that matter for immediate continuation

## Evidence

- the Nightcrawler session-opening ritual explicitly requires reading the handoff and then running `git log --oneline -5` to cross-check what the handoff claims versus what actually happened
- the Nightcrawler README describes git diff verification as protection against hallucinated progress and says the next episode can cross-check handoff claims against git history
- the AGOR snapshot docs require the receiving side to review commits and file changes, verify current repository state, and confirm described changes are present before continuation
- both donors frame verification as a receiving-side trust check rather than as generic code review

## Result

- works as a documentation-first second context and preserves one bounded handoff-verification contract without carrying over the donors' orchestration loops, snapshot tooling, or broader review semantics
