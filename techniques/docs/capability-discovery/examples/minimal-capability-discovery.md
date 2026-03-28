# minimal capability discovery

```yaml
search_request:
  queries:
    - type: name
      value: "weather-*"
    - type: skill_name
      value: "*forecast*"
  limit: 10
  offset: 0

search_response:
  record_cids:
    - bafybeigdyrztl6examplecidweatheragentv120
    - bafybeih2examplecidforecasthelperv110
```

Why this example stays bounded:

- it makes the discovery fields and result shape explicit without redefining the capability contract itself
- it keeps lookup smaller than marketplace ranking, recommendation, or editorial curation
- it does not import trust policy, graph semantics, or registry runtime behavior
