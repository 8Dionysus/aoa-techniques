# Selector Relation Wave F Capability Media History Review

Source packet: [Technique Reform Ingress](../README.md)

Closeout ledger:
[Selector Relation Long-Pass Closeout Ledger](selector-relation-long-pass-closeout-ledger.md)

Prior wave:
[Selector Relation Wave E Continuity Recovery Review](selector-relation-wave-e-continuity-recovery-review.md)

Status: Wave F selector/relation review, with two accepted direct relation
repairs routed to
[Capability Media Direct Relation Repair](capability-media-direct-relation-repair.md).

## Verdict

Wave F keeps the instruction capability tail, media-ingest shelf, and history
artifact shelf legible while accepting two exact object-dependency repairs.

The shelves in scope stay separate:

- `instruction/capability-registry`
- `instruction/capability-boundary`
- `instruction/skill-discovery`
- `ingest/media-ingest`
- `history/history-artifacts`

Direct reading confirms that capability registry leaves form a spec, entry,
and lookup chain; capability-boundary leaves protect adjacent meaning without
owning discovery or runtime action; skill-discovery leaves surface upstream
skills without becoming installer or registry doctrine; media-ingest leaves
turn external media into reviewable objects; and history-artifacts leaves
preserve inspectable history without becoming memory truth.

Two direct relation repairs are justified:

- `AOA-T-0064 requires AOA-T-0063`, because capability discovery operates over
  already-published registry entries and `AOA-T-0063` owns the local
  registry-entry publication contract.
- `AOA-T-0071 requires AOA-T-0070`, because template-backed field extraction
  uses a structured OCR handoff as its bounded parsing input and `AOA-T-0070`
  owns the local OCR handoff contract.

Both repairs are object dependencies only. They do not create registry product
doctrine, media pipeline ownership, installer behavior, memory truth, graph
behavior, ranking, status movement, or new relation vocabulary.

## Sources Read

Direct bundle reads:

- [AOA-T-0025 capability-spec-versioning](../../../../../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md)
- [AOA-T-0063 versioned-agent-registry-contract](../../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md)
- [AOA-T-0064 capability-discovery](../../../../../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md)
- [AOA-T-0040 skill-vs-command-boundary](../../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md)
- [AOA-T-0043 multi-source-primary-input-provenance](../../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md)
- [AOA-T-0093 recommendation-truth-vs-host-actionability](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md)
- [AOA-T-0041 skill-marketplace-curation](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md)
- [AOA-T-0042 upstream-skill-health-checking](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md)
- [AOA-T-0070 two-stage-document-ocr-pipeline](../../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md)
- [AOA-T-0071 template-backed-field-extraction-after-ocr](../../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md)
- [AOA-T-0072 perceptual-media-dedupe-with-threshold-review](../../../../../techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md)
- [AOA-T-0073 semantic-media-bucketing-with-vision-plus-ocr](../../../../../techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md)
- [AOA-T-0074 telegram-export-normalization-to-local-store](../../../../../techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md)
- [AOA-T-0026 session-capture-as-repo-artifact](../../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md)
- [AOA-T-0044 versionable-session-transcripts](../../../../../techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md)
- [AOA-T-0053 local-first-session-index](../../../../../techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md)
- [AOA-T-0045 witness-trace-as-reviewable-artifact](../../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md)
- [AOA-T-0066 transcript-replay-artifact](../../../../../techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md)
- [AOA-T-0067 transcript-linked-code-lineage](../../../../../techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md)

Support files that clarified object shape:

- [AOA-T-0063 checklist](../../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/checks/versioned-agent-registry-contract-checklist.md)
- [AOA-T-0063 example](../../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/examples/minimal-versioned-agent-registry-contract.md)
- [AOA-T-0064 checklist](../../../../../techniques/instruction/capability-registry/capability-discovery/checks/capability-discovery-checklist.md)
- [AOA-T-0064 example](../../../../../techniques/instruction/capability-registry/capability-discovery/examples/minimal-capability-discovery.md)
- [AOA-T-0070 checklist](../../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/checks/two-stage-document-ocr-pipeline-checklist.md)
- [AOA-T-0070 example](../../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/examples/minimal-two-stage-document-ocr-pipeline.md)
- [AOA-T-0071 checklist](../../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/checks/template-backed-field-extraction-after-ocr-checklist.md)
- [AOA-T-0071 example](../../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/examples/minimal-template-backed-field-extraction-after-ocr.md)
- media-ingest checks and examples for `AOA-T-0072`, `AOA-T-0073`, and
  `AOA-T-0074`
- history-artifact checks and examples for `AOA-T-0026`, `AOA-T-0044`,
  `AOA-T-0053`, `AOA-T-0045`, `AOA-T-0066`, and `AOA-T-0067`

Supporting review and generated surfaces:

- [Technique Selection](../../../../../docs/TECHNIQUE_SELECTION.md)
- [Technique Topology Scout](../reports/technique_topology_scout.md)
- [Technique Tree Projection](../reports/technique_tree_projection.md)
- [Capability-Registry Direct-Read Migration Review](capability-registry-direct-read-migration-review.md)
- [Landed Capability-Registry Pilot Review](landed-capability-registry-pilot-review.md)
- [Capability-Boundary Direct-Read Migration Review](capability-boundary-direct-read-migration-review.md)
- [Landed Capability-Boundary Pilot Review](landed-capability-boundary-pilot-review.md)
- [Skill-Discovery Direct-Read Migration Review](skill-discovery-direct-read-migration-review.md)
- [Landed Skill-Discovery Pilot Review](landed-skill-discovery-pilot-review.md)
- [Media-Ingest Direct-Read Migration Review](media-ingest-direct-read-migration-review.md)
- [Landed Media-Ingest Pilot Review](landed-media-ingest-pilot-review.md)
- [History-Artifacts Direct-Read Migration Review](history-artifacts-direct-read-migration-review.md)
- [Landed History-Artifacts Pilot Review](landed-history-artifacts-pilot-review.md)

## Selector Prompts

| selector prompt | first correct pick | why adjacent leaves lose |
|---|---|---|
| "One named capability needs versioned inputs, outputs, invariants, and compatibility review." | `AOA-T-0025` | registry entries publish a record; discovery only queries published entries |
| "A capability-like object must be published as a named versioned registry entry with a stable reference." | `AOA-T-0063` | capability spec owns internal contract; discovery owns lookup over entries |
| "A reader needs bounded fielded lookup over already-published capability records." | `AOA-T-0064` | registry entry publication creates entries; marketplace curation adds editorial grouping |
| "A reusable skill artifact and a user-facing command artifact are being confused." | `AOA-T-0040` | skill discovery curates upstream sources; propagation mirrors one source into targets |
| "Several inputs feed a bridge, but one must remain primary and cited as such." | `AOA-T-0043` | KAG relation lift creates bounded graph-like relations; this only preserves source priority |
| "A router recommendation is semantically correct, but the current host cannot execute it." | `AOA-T-0093` | upstream health checks source readiness before surfacing; this separates recommendation truth from actionability |
| "A local page should help users browse upstream-owned skills by category and summary." | `AOA-T-0041` | health checking emits readiness verdicts; skill-command boundary separates artifact from invocation |
| "One upstream skill source should be checked before it appears in a selector." | `AOA-T-0042` | curation decides display; capability discovery queries registry records |
| "A document image needs detect/layout, recognition, confidence, and a handoff object before extraction." | `AOA-T-0070` | field extraction starts after OCR; media bucketing uses visual semantics and optional OCR side text |
| "A receipt-like OCR result needs merchant/date/amount fields with missing and conflict markers." | `AOA-T-0071` | OCR staging produces the handoff; semantic bucketing chooses media class, not fields |
| "A media set needs near-duplicate groups and uncertain review groups without deletion." | `AOA-T-0072` | semantic bucketing names categories; Telegram normalization creates message/store objects |
| "Mixed media should be bucketed by a small visual taxonomy with OCR only as a side signal." | `AOA-T-0073` | OCR pipeline owns text handoff; dedupe groups near-identical files |
| "Telegram export data should become resumable normalized message objects." | `AOA-T-0074` | media bucketing classifies items; history capture preserves sessions, not chat export stores |
| "AI coding sessions should be saved as project-scoped artifacts before later review." | `AOA-T-0026` | transcript packaging starts after capture; indexing starts after saved artifacts exist |
| "Already-saved sessions need a versionable transcript package for one review thread." | `AOA-T-0044` | first capture owns persistence; replay is a derivative viewer artifact |
| "Saved session artifacts need a local rebuildable index with references back to sources." | `AOA-T-0053` | transcript packaging creates curated exports; lineage links code anchors to evidence |
| "One nontrivial run needs an ordered witness trace and compact summary before writeback." | `AOA-T-0045` | transcript packaging preserves conversation text; replay packages a saved source for review |
| "A saved session or transcript needs a derivative replay artifact." | `AOA-T-0066` | local index improves lookup; lineage connects code anchors to evidence |
| "Code anchors should point back to stable saved evidence references." | `AOA-T-0067` | witness trace captures a bounded run; index supports lookup over many saved artifacts |

## Relation Read

| relation | verdict | reason |
|---|---|---|
| `AOA-T-0025 complements AOA-T-0013` | keep | source-to-target propagation can carry capability specs, but spec versioning stays a capability contract |
| `AOA-T-0063 complements AOA-T-0025` | keep | a registry entry may publish a capability contract, but it can also publish a bounded record whose full spec is elsewhere |
| `AOA-T-0064 requires AOA-T-0063` | repair | discovery operates over already-published registry entries, and `AOA-T-0063` owns the local entry-publication contract |
| `AOA-T-0040 complements AOA-T-0027` | keep | propagation can reuse skills after the boundary is clear, but command separation is its own artifact boundary |
| `AOA-T-0043 complements AOA-T-0020` and `AOA-T-0021` | keep | source priority supports KAG lifts without becoming graph or traversal policy |
| `AOA-T-0093 complements AOA-T-0091` and `AOA-T-0042` | keep | owner-truth and upstream readiness inform actionability without making recommendation/actionability a registry health pass |
| `AOA-T-0041 complements AOA-T-0024` | keep | mirroring/provenance can feed curation, but the curated discovery layer can also sit over already-readable upstream entries |
| `AOA-T-0042 complements AOA-T-0041` | keep | readiness commonly gates curation, but it can also block or flag one source before any catalog grouping exists |
| `AOA-T-0070` has no outgoing relation | keep | OCR handoff is the producer object for later extraction, not dependent on downstream field parsing |
| `AOA-T-0071 requires AOA-T-0070` | repair | field extraction takes the structured OCR handoff as its bounded parsing input and `AOA-T-0070` owns that handoff contract |
| `AOA-T-0072` has no outgoing relation | keep | perceptual dedupe groups candidates without needing taxonomy, OCR, or deletion policy |
| `AOA-T-0073` has no outgoing relation | keep | OCR side text is optional; media bucketing is not a staged OCR consumer |
| `AOA-T-0074` has no outgoing relation | keep | Telegram normalization owns message/store objects, not media taxonomy or memory |
| `AOA-T-0026 complements AOA-T-0002` | keep | session capture stays separate from repository source-of-truth layout |
| `AOA-T-0044 complements AOA-T-0026` | keep | transcript packaging starts from saved artifacts, which can come from equivalent capture sources |
| `AOA-T-0053 complements AOA-T-0026` and `AOA-T-0044` | keep | indexing starts from saved artifacts and can index raw captures or curated transcript packages |
| `AOA-T-0045 complements AOA-T-0026` and `AOA-T-0044` | keep | witness traces can sit near saved sessions and transcripts without becoming either object |
| `AOA-T-0066 complements AOA-T-0044` and `AOA-T-0053` | keep | replay can start from a saved session or transcript and may be indexed, but neither neighbor is mandatory |
| `AOA-T-0067 complements AOA-T-0045` | keep | lineage links code anchors to stable evidence; witness traces are one useful evidence source, not the only source |

## Repair Gate

Accepted:

| bundle | old edge | new edge | why |
|---|---|---|---|
| `AOA-T-0064` | `complements AOA-T-0063` | `requires AOA-T-0063` | capability discovery starts over already-published registry entries, and `AOA-T-0063` owns the local entry-publication contract |
| `AOA-T-0071` | no direct edge to `AOA-T-0070` | `requires AOA-T-0070` | field extraction takes an OCR handoff as its bounded parsing input, and `AOA-T-0070` owns the local handoff contract |

Held:

| pressure | hold reason |
|---|---|
| `AOA-T-0063 requires AOA-T-0025` | a registry-facing entry can publish a capability spec, but it can also publish another bounded versioned record |
| `AOA-T-0042 requires AOA-T-0041` | source-readiness can run before curation or stand as a pre-surface block for one source entry |
| `AOA-T-0093 requires AOA-T-0042` | host-actionability filtering starts from recommendation plus host inventory, not upstream-source readiness alone |
| `AOA-T-0073 requires AOA-T-0070` | OCR side text is optional evidence for bucketing, not a staged OCR handoff dependency |
| `AOA-T-0044 requires AOA-T-0026` | transcript packaging requires saved artifacts, not necessarily this exact capture technique |
| `AOA-T-0053 requires AOA-T-0026` | local indexing needs saved artifacts and stable references, which can come from equivalent sources |
| `AOA-T-0066 requires AOA-T-0044` or `AOA-T-0053` | replay starts from a saved session or transcript; indexing is helpful but not required |
| `AOA-T-0067 requires AOA-T-0045` | code lineage needs stable evidence, while witness traces are one possible evidence artifact |
| new relation vocabulary | Wave F needs two `requires` object edges, not new `follows`, `produces`, `consumes`, or indexing relation types |

## Axis Usefulness

| axis | value in Wave F | limit |
|---|---|---|
| `domain` | shows mixed docs, evaluation, agent-workflows, and history truth across the wave | cannot choose between entry publication, lookup, curation, readiness, media handoff, and history artifact shapes |
| `kind` | separates artifact, discovery, validation, ingest, handoff, and lift shapes | not enough to express object dependency inside dense shelves |
| tree shelf | strongest first selector neighborhood for registry, skill discovery, media ingest, and history artifacts | shelf placement does not create product doctrine or one mandatory pipeline |
| `execution_profile` | helps notice which leaves can be handed to smaller agents after orchestration chooses context | scout suitability only; no empirical local-agent proof is claimed |
| `risk_posture` | keeps public-share, host-actionability, external-source, media, and history sensitivity visible | risk posture cannot justify a relation without direct object dependency |
| `relations` | useful for exact object inspection between entry/query and OCR/extraction | should stay direct edges, not a graph traversal or generated workflow engine |

## What Changed

- added this Wave F review packet;
- routed two direct repairs:
  `AOA-T-0064 requires AOA-T-0063` and
  `AOA-T-0071 requires AOA-T-0070`;
- preserved capability-boundary, skill-discovery, media-ingest, and
  history-artifacts as distinct selector neighborhoods.

## What Did Not Change

- no relation schema migration;
- no new relation types;
- no relation rationale fields;
- no generated graph behavior, traversal, scoring, or ranking;
- no status, `domain`, `kind`, path, family, capability, substrate,
  execution-profile, risk, maturity, evidence, or owner changes;
- no canonical promotion;
- no empirical small-agent proof claim.

## Public-Safety Read

The review uses existing public bundle text, generated public repo surfaces,
and sanitized review language. It avoids credential material, non-public donor
material, live endpoints, private transcripts, and environment-specific
operational detail. Registry, installer, host-actionability, media, history,
and public-share terms are review subjects only; they do not expose operational
detail or import sibling-owner authority.

## Next Honest Move

Land Wave F with the two direct relation repairs, regenerated relation
consumers, and narrow validation.

After landing, continue the temporary plan with Phase 14: residual singleton
and cross-wave scan, including `tool-use/tool-gateway`, low-density holds, and
relation candidates held from Waves A through F.
