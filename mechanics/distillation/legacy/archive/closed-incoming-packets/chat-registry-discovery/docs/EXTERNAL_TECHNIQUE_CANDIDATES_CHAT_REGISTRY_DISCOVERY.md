# External Technique Candidates - Chat Registry Discovery

This doc records the registry and discovery shard staged from the external chat wave pack.

Use it when the question is not "which landed technique should I open?", but
"which registry or discovery-shaped candidate from chat wave 1A is already
landed, which closed without import, and which should remain explicitly
excluded on the first pass?"

This is a staging and decision surface.
It does not create a canonical bundle or authorize import by itself.
The first-pass landing queue is exhausted; this packet now serves as evidence
and closed-verdict accounting.

## Scope

- this shard tracks `8` source-pack candidates
- `2` are already landed
- `0` remain staged for later triage
- `1` is closed without import
- `5` are explicit first-pass exclusions
- this shard is registry-only on the first pass
- no candidate bundles are created in this packet

## Landed From This Shard

| candidate | landed bundle | boundary kept | what stayed out |
|---|---|---|---|
| `versioned-agent-registry-contract` | [AOA-T-0063](../../../../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md) | reviewable contract for named versioned registry entries with explicit references and metadata | discovery queries, marketplace curation, semantic linkage, and registry product doctrine |
| `capability-discovery` | [AOA-T-0064](../../../../../../../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md) | bounded discovery-query contract for looking up published capability records through explicit fields and result shape | ranking policy, marketplace curation, trust semantics, semantic linkage, and registry product doctrine |

No remaining staged landing candidates in Wave 1A.

## Closed Non-Import Verdict

| candidate | why closed | next honest move |
|---|---|---|
| `semantic-linkage-records` | current donor evidence still reads as semantic-linkage promises plus a generic referrer substrate whose validated live types are mostly trust-oriented | keep it closed in this packet; a future attempt needs a new Distillation intake and the smaller semantic-link record contract described in [SEMANTIC_LINKAGE_RECORDS_CLOSEOUT_MEMO.md](SEMANTIC_LINKAGE_RECORDS_CLOSEOUT_MEMO.md) |

## Explicit Exclusions

| candidate | why excluded now | next honest move |
|---|---|---|
| `well-known-skill-discovery` | too close to `AOA-T-0041 skill-marketplace-curation` unless discovery itself becomes the invariant | keep closed unless a new intake proves a bounded discovery contract separated from curation |
| `versioned-skill-package-manifest` | too close to `AOA-T-0025 capability-spec-versioning` unless the package contract becomes sharper than spec versioning | keep excluded until the package boundary is independent of spec ownership |
| `source-manifest-sync` | already overlapped by `AOA-T-0024 upstream-mirroring-with-provenance` | leave closed unless sync control separates from provenance-backed mirroring |
| `universal-skill-loader` | currently collapses into `AOA-T-0027` and `AOA-T-0030` style rule or skill loading surfaces | keep closed unless a new intake proves a loader contract without restating propagation or fragmentation |
| `progressive-skill-loading` | too close to `AOA-T-0029 nested-rule-loading` plus fragmented context posture | keep excluded unless staged loading becomes a distinct reusable rule contract |

## Notes

- treat the zip as donor soil only
- `versioned-agent-registry-contract` now exits the staged lane as landed `AOA-T-0063`
- `capability-discovery` now exits the staged lane as landed `AOA-T-0064`
- keep `semantic-linkage-records` closed until fresh evidence shows a live semantic-link object smaller than graph doctrine and smaller than the existing registry/discovery siblings
- do not use this shard to revive already-landed skill curation or source-mirroring families
