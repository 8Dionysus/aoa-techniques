# Frontmatter To Catalog Entry

This example shows how bounded frontmatter can act as a metadata spine while the technique body still carries the real meaning.

## Source frontmatter

```yaml
id: AOA-T-0019
name: frontmatter-metadata-spine
domain: docs
status: promoted
summary: Treat bounded frontmatter and derived catalog outputs as a metadata spine.
validation_strength: source_backed
relations:
  - type: used_together_for
    target: AOA-T-0020
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
```

## Derived catalog excerpt

```json
{
  "id": "AOA-T-0019",
  "domain": "docs",
  "status": "promoted",
  "summary": "Treat bounded frontmatter and derived catalog outputs as a metadata spine.",
  "validation_strength": "source_backed",
  "relations": [
    {
      "type": "used_together_for",
      "target": "AOA-T-0020"
    }
  ],
  "evidence": [
    {
      "kind": "origin_evidence",
      "path": "notes/origin-evidence.md"
    }
  ]
}
```

## Anti-drift rule

If the catalog must duplicate section prose to stay useful, the metadata problem is no longer bounded and the spine should not be widened casually.
