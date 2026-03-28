# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/git-ai-project/git-ai`
- source_license: `Apache-2.0`
- inspired_by: not used in this import
- adapted_from: `README.md`, `specs/git_ai_standard_v3.0.0.md`, and `skills/ask/SKILL.md`

## What changed

- what_changed: narrowed the donor to one bounded seam: code anchors can link back to saved session evidence so provenance stays reviewable
- invariant core kept: code history keeps stable references to prior session evidence and later reviewers can reopen that evidence from a code-inspection surface
- project-shaped details removed or generalized: contributor scorecards, deployment metrics, dashboards, analytics summaries, Git Notes implementation specifics, and broader retrieval-product semantics

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: repo-specific notes storage, internal dashboards, and environment-specific metric paths were omitted
- environment-specific assumptions generalized: the public technique does not depend on one blame UI, one notes backend, or one analytics dashboard
- remaining public-safety concerns: the main risks are drift into repo analytics on one side and drift into retrieval-product doctrine on the other

## Review notes

- why this adaptation is reusable here: AI-assisted repositories often need a bounded provenance seam from code back to saved session evidence without importing an entire analytics or retrieval stack
- primary evidence used: the donor README describes linking AI-written code lines back to sessions, the public spec defines code-to-session provenance structures, and the `/ask` skill shows how later inspection reopens evidence linked to code
- limits or follow-up review concerns: dashboards, metrics, why-retrieval UX, and broader provenance or governance systems remain intentionally outside this import
