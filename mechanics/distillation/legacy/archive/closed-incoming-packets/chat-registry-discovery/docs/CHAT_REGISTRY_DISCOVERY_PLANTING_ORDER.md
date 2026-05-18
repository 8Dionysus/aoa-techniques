# Chat Registry Discovery - Planting Order

This note is for operator-guided staging inside `aoa-techniques`.

## Hard rules

- keep Wave 1A registry-first on the first pass
- do not create candidate bundles from this closed packet
- do not assign `AOA-T-XXXX` ids from worker-owned wave tasks
- do not revisit marketplace curation, spec versioning, or graph semantics from this packet

## Landed first

1. `versioned-agent-registry-contract` is now landed as `AOA-T-0063` by the main agent
2. `capability-discovery` is now landed as `AOA-T-0064` by the main agent

## Preferred sequence

3. `semantic-linkage-records` is closed without import

Why this order:

- the registry contract was the cleanest anchor
- capability discovery could be landed only after the registry contract was named clearly and kept separate from curation or product semantics
- semantic linkage stayed last because it has the strongest graph-creep risk and the current donor still does not expose one live semantic-link contract cleanly enough to land

Current closeout verdict:

- keep `semantic-linkage-records` out of `techniques/` for now
- use `docs/SEMANTIC_LINKAGE_RECORDS_CLOSEOUT_MEMO.md` as the final packet rationale
- do not assign `AOA-T-XXXX` from this packet; a future attempt needs a new intake with a real semantic-link object smaller than graph doctrine and smaller than trust-referrer substrate

## Explicit exclusions to leave closed

- `well-known-skill-discovery`
- `versioned-skill-package-manifest`
- `source-manifest-sync`
- `universal-skill-loader`
- `progressive-skill-loading`

## Stop conditions

Stop and leave the shard staged if:

- a candidate still sounds like registry product doctrine
- the contract needs a new schema or new domain to stay coherent
- the candidate collapses into an already-landed docs technique
- the record shape still depends on graph semantics rather than one bounded reusable object
