# Canonical Owner With Validated Mirror Checklist

- Name exactly one canonical owner for the shared contract.
- Keep each local mirror subordinate to the canonical owner rather than independently editable by default.
- Preserve explicit canonical-reference metadata in every mirror.
- Validate parity for owner metadata and bounded vocabulary, not only loose shape.
- Reject unknown contract tokens in consumer intake before derived outputs are built.
- Land migrations in the canonical owner first and update mirrors through parity-preserving sync.
- Keep local wrapper or packaging logic outside the mirrored contract payload.
