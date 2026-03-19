# Evidence Note To Manifest

This example shows how one bundle can expose supporting provenance notes through explicit handles and a derived manifest without flattening the notes into one merged schema.

## Source frontmatter excerpt

```yaml
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
```

## Supporting note roles

- `notes/origin-evidence.md` explains where the technique was born and what in the source project proves the pattern is real.
- `notes/second-context-adaptation.md` explains what changed in a second context and what stayed invariant.

## Derived manifest excerpt

```json
{
  "technique_id": "AOA-T-0020",
  "notes": [
    {
      "kind": "origin_evidence",
      "path": "notes/origin-evidence.md",
      "shape": "typed_sections"
    },
    {
      "kind": "second_context",
      "path": "notes/second-context-adaptation.md",
      "shape": "typed_sections"
    }
  ]
}
```

## Anti-drift rule

If the manifest must summarize the argument well enough that nobody needs to open the supporting note, the provenance lift has widened too far.
