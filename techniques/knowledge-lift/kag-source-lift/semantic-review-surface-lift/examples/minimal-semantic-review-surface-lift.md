# Minimal Semantic Review Surface Lift

This example shows how an authored semantic-review doc can be surfaced as a bounded derived lookup aid without making the derived view the source of review meaning.

## Source review excerpt

```md
## Cluster Map

| technique | current role |
|---|---|
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | repository-wide document-role layout and update-routing pattern |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | narrow discipline for keeping top-level status docs short, link-driven, and non-duplicative |

## Seam Review

### `AOA-T-0002` vs `AOA-T-0009`

Question: where does the broader document-role layout stop and the narrower snapshot discipline begin?

- Invariant boundary: [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) owns the full document-role map.
- Default-use trigger: use `0002` when a repository needs one canonical home per recurring information class.
```

## Derived lookup excerpt

```json
{
  "review_id": "docs_boundary",
  "review_path": "docs/DOCS_BOUNDARY_SEMANTIC_REVIEW.md",
  "title": "Docs Boundary Semantic Review",
  "findings": [
    "`AOA-T-0002` is semantically distinct as the broader source-of-truth layout pattern.",
    "`AOA-T-0009` is semantically distinct as a lighter snapshot discipline layered on top of a broader document map."
  ],
  "overall_outcome": "`clear`"
}
```

The derived excerpt is intentionally routing-first. It helps a reader find the right authored review doc, but the meaning of the review still lives in that authored markdown.

## Anti-Drift Rule

If maintainers need to edit the manifest directly to correct review meaning, the lift has stopped being markdown-first.
If the next question is scoring, status changes, or relation cleanup, this technique has been asked to do too much.
