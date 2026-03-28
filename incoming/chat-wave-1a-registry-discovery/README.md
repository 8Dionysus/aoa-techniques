# chat-wave-1a-registry-discovery

This is a repo-native active staging shard for the registry and discovery slice from the external chat wave pack.

It exists to keep the donor queue reviewable inside `incoming/` without reopening the already-landed repo Waves A/B/C.

## Activation state

- `active`
- registry-first on the first pass
- two landed candidates, no remaining staged landing candidates
- one narrowing-only candidate with a current memo
- no seed bundles yet

## What this shard tracks

- landed from this shard:
  - `AOA-T-0063` / `versioned-agent-registry-contract`
  - `AOA-T-0064` / `capability-discovery`
- active seed lane:
  - none
- narrowing-only lane:
  - `semantic-linkage-records` with a current memo in `docs/SEMANTIC_LINKAGE_RECORDS_NARROWING_MEMO.md`
- explicit exclusions routed out of first-pass landing:
  - `well-known-skill-discovery`
  - `versioned-skill-package-manifest`
  - `source-manifest-sync`
  - `universal-skill-loader`
  - `progressive-skill-loading`

## Operating posture

- keep the shard as staging soil, not merge authority
- keep the remaining candidate in narrowing-only state until its contract is narrower than graph or registry-product doctrine
- do not move the remaining staged candidates into `techniques/` without operator approval
- keep marketplace, registry governance, and graph doctrine out unless a later narrowing pass proves a smaller reusable contract
