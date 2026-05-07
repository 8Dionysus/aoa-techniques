# Capability Media Direct Relation Repair

Source packet: [Technique Reform Ingress](../README.md)

Wave packet:
[Selector Relation Wave F Capability Media History Review](selector-relation-wave-f-capability-media-history-review.md)

Touched bundle relations:

- [AOA-T-0064 capability-discovery](../../../../../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md)
- [AOA-T-0071 template-backed-field-extraction-after-ocr](../../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md)

Stable object-contract targets:

- [AOA-T-0063 versioned-agent-registry-contract](../../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md)
- [AOA-T-0070 two-stage-document-ocr-pipeline](../../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md)

Status: accepted direct relation repair.

## Verdict

Accept two narrow `requires` repairs:

- `AOA-T-0064 requires AOA-T-0063`
- `AOA-T-0071 requires AOA-T-0070`

`AOA-T-0064` owns bounded capability lookup over already-published registry
entries. Its intent, inputs, core procedure, contracts, checklist, and example
all make the published entry the object being queried. `AOA-T-0063` owns the
local registry-facing entry contract: a named versioned record with stable
reference and bounded metadata. That makes `requires AOA-T-0063` more accurate
than `complements AOA-T-0063` for this one downstream relation.

`AOA-T-0071` owns post-OCR field extraction. Its inputs, procedure, checklist,
and example all make a structured OCR handoff the bounded parsing input.
`AOA-T-0070` owns the local OCR handoff contract: staged detect/layout,
recognition, confidence, and source references before downstream extraction.
That makes `requires AOA-T-0070` the right direct relation for this field
extraction leaf.

The repair is intentionally narrow. It does not make the capability-registry
shelf a registry product, does not make media-ingest a document platform, does
not make all media bucketing depend on OCR, and does not turn history artifacts
into memory doctrine.

## Decision Table

| bundle | old edge | new edge | reason |
|---|---|---|---|
| `AOA-T-0064` | `complements AOA-T-0063` | `requires AOA-T-0063` | lookup operates over already-published registry entries, and `AOA-T-0063` owns the local entry-publication contract |
| `AOA-T-0071` | no direct edge to `AOA-T-0070` | `requires AOA-T-0070` | field extraction takes a structured OCR handoff as the bounded parsing input, and `AOA-T-0070` owns that local handoff contract |

## Holds

| bundle | held relation posture | why |
|---|---|---|
| `AOA-T-0063` | keep `complements AOA-T-0025` | a registry-facing entry can publish a capability spec but is not limited to that one spec technique |
| `AOA-T-0042` | keep `complements AOA-T-0041` | readiness can run before or beside curation without requiring a curated marketplace surface |
| `AOA-T-0093` | keep `complements AOA-T-0042` | host actionability needs recommendation and inventory context, not only upstream source readiness |
| `AOA-T-0073` | no `requires AOA-T-0070` | OCR is an optional side signal for bucketing rather than the required staged handoff contract |
| `AOA-T-0044` | keep `complements AOA-T-0026` | transcript packaging starts from saved artifacts, which can come from equivalent capture sources |
| `AOA-T-0053` | keep `complements AOA-T-0026` and `complements AOA-T-0044` | indexing needs saved sources and stable references, not one mandatory capture or transcript producer |
| `AOA-T-0066` | keep `complements AOA-T-0044` and `complements AOA-T-0053` | replay starts from saved session or transcript evidence; indexing is adjacent |
| `AOA-T-0067` | keep `complements AOA-T-0045` | lineage needs stable evidence, while witness trace is one possible evidence artifact |

## What Changed

- `AOA-T-0064` frontmatter now has a direct
  `requires AOA-T-0063` relation.
- `AOA-T-0071` frontmatter now has a direct
  `requires AOA-T-0070` relation.
- Generated relation consumers should be rebuilt from source after this
  repair: catalog, selection surfaces, topology scout, KAG export, and
  release-check companions that derive from catalog or frontmatter.

## What Did Not Change

- no new relation types;
- no relation schema migration;
- no relation rationale field;
- no generated graph behavior, traversal, ranking, or selector engine;
- no status, `domain`, `kind`, maturity, validation-strength, evidence,
  owner, or path changes;
- no canonical promotion;
- no empirical small-agent proof or `aoa-evals` verdict.

## Safety Read

This repair strengthens only two object dependencies:

- capability discovery needs a published registry-entry contract first;
- post-OCR field extraction needs an OCR handoff contract first.

It does not say that capability specs require registry publication, discovery
owns ranking, curated skill discovery owns installer behavior, OCR owns all
media ingest, field extraction owns accounting automation, or saved history
artifacts become memory truth.

## Stop Lines

- Do not use this repair as precedent for adding future sequence relation
  names to frontmatter.
- Do not strengthen `AOA-T-0063` to `requires AOA-T-0025` from this packet.
- Do not strengthen `AOA-T-0073` to `requires AOA-T-0070` from this packet.
- Do not strengthen history artifact relations from this packet.
- Do not collapse capability spec, registry entry, discovery query, skill
  curation, upstream readiness, OCR staging, field extraction, or history
  capture into broader product doctrine.
- Do not hand-edit generated surfaces. Rebuild them from source.

## Next Honest Move

Rebuild generated relation consumers, validate the repository, and land
Wave F.

After Wave F lands, continue the temporary plan with Phase 14 residual
singleton and cross-wave scan.
