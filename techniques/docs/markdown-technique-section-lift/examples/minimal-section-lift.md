# Minimal Section Lift

This example shows how a markdown-first technique bundle can expose a bounded section-level view without making the derived manifest the new source of truth.

## Source bundle excerpt

```md
## Intent

Keep the pattern bounded and reviewable.

## Contracts

- markdown stays authoritative
- derived output stays rebuildable

## Risks

### Failure modes
- consumers trust the manifest more than the bundle

## Validation

- rebuild the manifest from markdown
```

## Derived section-manifest excerpt

```json
{
  "id": "AOA-T-0018",
  "technique_path": "techniques/docs/markdown-technique-section-lift/TECHNIQUE.md",
  "sections": [
    {
      "heading": "Intent",
      "order": 1
    },
    {
      "heading": "Contracts",
      "order": 2
    },
    {
      "heading": "Risks",
      "order": 3
    },
    {
      "heading": "Validation",
      "order": 4
    }
  ]
}
```

This excerpt is intentionally routing-first. A full manifest may preserve more payload, but a reader-facing or review-facing projection should still route back to the authored bundle instead of becoming the place where section meaning is edited.

## Anti-drift rule

If maintainers need to edit the manifest directly to correct section meaning, the lift has stopped being markdown-first.
If bundle-level metadata already answered the question, section lift should not have been opened in the first place.
