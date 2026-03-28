# minimal versioned agent-registry contract

```yaml
named_record_ref:
  name: weather-agent
  version: v1.2.0
  cid: bafybeigdyrztl6examplecidweatheragentv120

record_meta:
  schema_version: 1.0.0
  created_at: 2026-03-28T14:00:00Z
  annotations:
    capability_family: weather
    surface: public-registry
```

Why this example stays bounded:

- it makes the published entry identity explicit without redefining the capability contract itself
- it does not become a discovery query, marketplace page, or trust policy surface
- it keeps record reference and metadata reviewable without importing registry runtime semantics
