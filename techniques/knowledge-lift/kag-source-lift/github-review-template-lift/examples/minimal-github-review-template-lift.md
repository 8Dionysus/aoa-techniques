# Minimal GitHub Review Template Lift

This example shows how authored GitHub review templates can become a bounded derived intake surface without turning the manifest into workflow policy.

## Source template excerpt

```md
## Review Contract

- proposed outcome: approve for canonical promotion or defer for now
- bounded scope where this would be the default:

## Public-Safety Recheck

- sanitization still holds:
- private paths, URLs, or operational details removed:
- remaining public-safety concerns:
```

## Derived manifest excerpt

```json
{
  "template_id": "canonical-promotion",
  "template_type": "issue_template",
  "section_scope": [
    "Technique",
    "Review Contract",
    "Default-Use Rationale",
    "Reuse Beyond Origin",
    "Stronger Validation Than Initial Promotion Baseline",
    "Adaptation Boundary Check",
    "Public-Safety Recheck",
    "Recommendation"
  ]
}
```

The same pattern can cover pull-request templates and external-import review templates, but the derived surface should stay inventory-first. If the manifest needs to decide the outcome, the technique has crossed into workflow policy.
