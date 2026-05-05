# Second Context Adaptation

## Technique
- id: AOA-T-0067
- name: transcript-linked-code-lineage

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded code-to-evidence lineage seam rather than shipping the donor's blame tooling, analytics, or retrieval UX

## What changed

- paths: the donor ships concrete blame, notes, and `/ask` behavior; this adaptation keeps the generic code-anchor-to-evidence link without requiring one implementation surface
- services: dashboards, metrics, analytics summaries, and broader retrieval-product features were removed from the reusable contract
- dependencies: the adaptation depends on already-saved evidence artifacts plus stable code anchors, not on the donor CLI or analytics stack
- operating assumptions: contributors should read the technique as provenance lookup from code back to saved evidence, not as a scorecard or Q and A platform

## What stayed invariant

- contract: code anchors keep stable pointers back to saved session evidence
- validation logic: later reviewers can reopen evidence from the lineage surface
- safety rules: saved evidence remains authoritative and the lineage seam stays outside dashboard, ranking, and retrieval-product doctrine

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0045](../witness-trace-as-reviewable-artifact/TECHNIQUE.md) if repositories expect a full run artifact instead of one bounded provenance link
- the public bundle could drift into analytics product behavior if dashboards or scorecards become more prominent than the lineage seam
- teams may over-associate lineage with why-retrieval features because the donor bundles the two closely

## Evidence

- the donor README says every AI-written line can be linked back to the session that produced it
- the public spec defines provenance structures that connect code changes to session metadata and evidence
- the donor `/ask` skill demonstrates a later inspection surface that reopens original prompts or conversations from selected code, which confirms the importance of the code-to-evidence link while also showing why retrieval UX should stay outside the invariant core
- together these sources show that provenance links can be extracted cleanly without importing the donor's wider analytics stack

## Result

- works as a documentation-first second context and preserves one bounded code-lineage contract without carrying over the donor's analytics, dashboards, or retrieval-product breadth
