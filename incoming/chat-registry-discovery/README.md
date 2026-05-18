# chat-registry-discovery

This is a repo-native evidence packet for the registry and discovery slice from
the external chat wave pack.

It exists to keep the donor verdicts reviewable inside `incoming/` without
revisiting the already-landed registry and discovery bundles. It is not an
active landing lane.

## Activation state

- `evidence-only`
- registry-first on the first pass
- two landed candidates, no remaining staged landing candidates
- one closed non-import candidate with a closeout memo
- no active non-landed tail remains in this packet
- no candidate bundles in this packet

## What this shard tracks

- landed from this shard:
  - `AOA-T-0063` / `versioned-agent-registry-contract`
  - `AOA-T-0064` / `capability-discovery`
- seed lane:
  - none
- closed non-import:
  - `semantic-linkage-records` with final rationale in `docs/SEMANTIC_LINKAGE_RECORDS_CLOSEOUT_MEMO.md`
- explicit exclusions routed out of first-pass landing:
  - `well-known-skill-discovery`
  - `versioned-skill-package-manifest`
  - `source-manifest-sync`
  - `universal-skill-loader`
  - `progressive-skill-loading`

## Operating posture

- keep the packet as evidence, not merge authority
- keep `semantic-linkage-records` closed unless fresh evidence proves a smaller atom than graph or registry-product doctrine
- do not move a closed candidate into `techniques/` from this packet
- keep marketplace, registry governance, and graph doctrine out unless a later narrowing pass proves a smaller reusable contract
