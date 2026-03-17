# Docs Boundary Semantic Review

This review-only pilot checks whether the docs pair still reads as two distinct techniques rather than one broad "good docs hygiene" pattern.

Why this pair was chosen now:

- it is the next nearest-neighbor docs pair after the two evaluation pilots
- both techniques already point to each other through current `relations`
- the main question is whether repository-wide document-role layout stays distinct from top-level snapshot trimming discipline
- this pair is a good boundary test before moving from semantic pilots toward richer navigation work

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Pair Map

| technique | current role |
|---|---|
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | repository-wide document-role layout and update-routing pattern |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | narrow discipline for keeping top-level status docs short, link-driven, and non-duplicative |

## Seam Review

### `AOA-T-0002` vs `AOA-T-0009`

Question: where does the broader document-role layout stop and the narrower snapshot discipline begin?

- Invariant boundary: [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) owns the full document-role map, update-routing rules, and separation of active work, decisions, runbooks, and long history. [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) begins only after that broader layout exists and constrains how `README` and optional `MANIFEST` stay short, readable, and link-driven.
- Default-use trigger: use `0002` when a repository needs one canonical home per recurring information class and explicit routing rules for updates. Use `0009` when those canonical homes already exist and the remaining problem is that top-level status docs are growing into mini-archives or duplicate summaries.
- Relation check: mutual `complements` is appropriate and still bounded. It communicates that the snapshot discipline strengthens the broader layout without replacing it. A stronger relation such as `requires` would overstate dependency because a repository can apply lightweight snapshot discipline in a simpler form without adopting the full role map verbatim.
- Evidence check: `0002` checklist remains role-map centric, covering document roles, routing, and keeping long history out of `README` and `TODO`. `0009` checklist remains snapshot centric, covering short entrypoints, outward links, absent run-history blocks, and one-screen readability. The pair's support surfaces reinforce separation rather than blur it. Outcome: `clear`.

## Findings

- `AOA-T-0002` is semantically distinct as the broader source-of-truth layout pattern. No drift signal found.
- `AOA-T-0009` is semantically distinct as a lighter snapshot discipline layered on top of a broader document map.
- Current `relations` for this pair are helpful and still minimal. No cleanup is justified in this pilot.
- Current `examples/` and `checks/` support the claimed contracts well enough for a review-only docs semantic surface.

Overall outcome: `clear`

## Next Step

No narrow docs remediation wave is justified from this pilot alone.

With the first three bounded semantic pilots now complete, the next step should shift from semantic review toward the first richer relation consumer or another bounded navigation surface built on the existing catalog and review corpus.
