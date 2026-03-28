# Narrowing Memo - semantic-linkage-records

This memo records the current narrowing result for the remaining Wave 1A candidate `semantic-linkage-records`.

It is a staging note only.
It does not create a canonical bundle or authorize import by itself.

## Candidate chosen

- `semantic-linkage-records`
- donor: `agntcy/dir`

## Overlap watch

- [AOA-T-0021](../../../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
- [AOA-T-0063](../../../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md)
- [AOA-T-0064](../../../techniques/docs/capability-discovery/TECHNIQUE.md)

## Boundary statement

The current donor evidence does not yet expose one standalone semantic-linkage record contract.

What is public today is a mixed cluster:

- the donor README promises `Semantic Linkage` as a platform capability
- `RecordReferrer` in `record.proto` exposes a generic-looking record-attached association object
- `store_service.proto` exposes push, pull, and delete operations for referrers
- `rules.proto` and `referrer_types.go` currently validate only signature and public-key referrer types
- `tests/e2e/local/10_referrers_test.go` exercises referrers only through signing and key-verification examples

That is useful platform substrate, but it is not yet one sharply bounded semantic-link technique in the `aoa-techniques` sense.

The narrowest plausible extraction target is:

- a typed record-attached association object with its own content ID, target record reference, bounded annotations, and payload

Even that smaller target is not stable enough yet, because the donor still presents the live validated surface mainly as trust/signature referrers rather than as one reusable semantic-linkage contract for version lineage, dependency chains, or collaborative relationships.

## What stays out

- broad graph semantics, ontology expansion, and KAG architecture
- generic relation doctrine already covered by [AOA-T-0021](../../../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
- trust, signature, and public-key verification flows
- directory product semantics, runtime routing, and distributed-network claims
- speculative claims that semantic linkage is already a reusable public contract when the donor surface is still mostly platform substrate

## Evidence snapshot

- `README.md` frames semantic linkage as a directory feature for version history, collaborative partnerships, and dependency chains
- `proto/agntcy/dir/core/v1/record.proto` defines `RecordReferrer` as a record-attached association object with `type`, `record_ref`, `annotations`, `created_at`, `data`, and `referrer_ref`
- `proto/agntcy/dir/store/v1/store_service.proto` exposes storage operations for pushing, pulling, and deleting referrers
- `proto/agntcy/dir/core/v1/rules.proto` currently validates only `agntcy.dir.sign.v1.PublicKey` and `agntcy.dir.sign.v1.Signature`
- `api/core/v1/referrer_types.go` reflects the same narrow live type set
- `tests/e2e/local/10_referrers_test.go` demonstrates the current surface only through public-key and signature referrers

## Verdict

- keep `semantic-linkage-records` in the `narrowing-only` lane
- do not create a bundle yet
- do not assign a technique ID yet

## Honest reopen trigger

Reopen this candidate only if the donor or a second public context can say, in plain language:

- what the reusable semantic-link object is
- which link types are actually part of the bounded contract
- how the link object stays distinct from trust referrers and from graph doctrine
- why the reusable center is a semantic-link record contract rather than a generic registry-platform substrate

## Files touched or proposed

- touched: this memo
- touched: Wave 1A staging docs and registry to link the memo and keep the narrowing lane honest
- not proposed yet: no `TECHNIQUE.md`, no bundle-local example, no checklist seed, no note package

## Whether operator approval is needed

- no operator approval needed to keep this candidate in narrowing-only state
- operator approval is required before any future move from this memo into a real technique bundle
