# Selector Relation Wave B Instruction Knowledge Review

Source packet: [Technique Reform Ingress](../README.md)

Temporary plan:
[Temporary Selector Relation Long-Pass Plan](../TEMP_SELECTOR_RELATION_LONG_PASS_PLAN.md)

Prior wave:
[Selector Relation Wave A Proof Execution Review](selector-relation-wave-a-proof-execution-review.md)

Status: Wave B selector/relation review, with no accepted direct relation
repair.

## Verdict

Wave B is clean as a selector/relation wave.

The four shelves in scope are dense, but their current authored contracts are
clear enough for a selector to choose the correct leaf once `domain`, `kind`,
and tree placement have found the neighborhood:

- `instruction/instruction-surface`
- `knowledge-lift/kag-source-lift`
- `instruction/docs-boundary`
- `proof/skill-support`

The current relations should stay as they are. The tempting upgrades in this
wave mostly read like hidden sequence, narrower/wider sibling, or common-use
pressure rather than strict object dependency. The only strict dependencies
already present are `AOA-T-0020 requires AOA-T-0019` and
`AOA-T-0021 requires AOA-T-0019`, because provenance-note and relation-edge
lifts both depend on the metadata spine's explicit bundle handles.

No bundle relation, status, `domain`, `kind`, path, scout axis, schema, or
generated rule should change from this wave.

## Sources Read

Direct bundle reads:

- [AOA-T-0002 source-of-truth-layout](../../../../../techniques/instruction/docs-boundary/source-of-truth-layout/TECHNIQUE.md)
- [AOA-T-0009 lightweight-status-snapshot](../../../../../techniques/instruction/docs-boundary/lightweight-status-snapshot/TECHNIQUE.md)
- [AOA-T-0012 deterministic-context-composition](../../../../../techniques/instruction/instruction-surface/deterministic-context-composition/TECHNIQUE.md)
- [AOA-T-0013 single-source-rule-distribution](../../../../../techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md)
- [AOA-T-0015 contract-test-design](../../../../../techniques/proof/skill-support/contract-test-design/TECHNIQUE.md)
- [AOA-T-0016 bounded-context-map](../../../../../techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md)
- [AOA-T-0017 property-invariants](../../../../../techniques/proof/skill-support/property-invariants/TECHNIQUE.md)
- [AOA-T-0018 markdown-technique-section-lift](../../../../../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md)
- [AOA-T-0019 frontmatter-metadata-spine](../../../../../techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/TECHNIQUE.md)
- [AOA-T-0020 evidence-note-provenance-lift](../../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md)
- [AOA-T-0021 bounded-relation-lift-for-kag](../../../../../techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/TECHNIQUE.md)
- [AOA-T-0022 risk-and-negative-effect-lift](../../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md)
- [AOA-T-0024 upstream-mirroring-with-provenance](../../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md)
- [AOA-T-0027 cross-agent-skill-propagation](../../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md)
- [AOA-T-0029 nested-rule-loading](../../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md)
- [AOA-T-0030 fragmented-agent-context](../../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md)
- [AOA-T-0033 decision-rationale-recording](../../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md)
- [AOA-T-0034 public-safe-artifact-sanitization](../../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md)
- [AOA-T-0035 profile-preset-composition](../../../../../techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md)
- [AOA-T-0046 repo-doc-surface-lift](../../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md)
- [AOA-T-0047 github-review-template-lift](../../../../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md)
- [AOA-T-0048 semantic-review-surface-lift](../../../../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md)

Supporting review and generated surfaces:

- [Technique Selection](../../../../../docs/TECHNIQUE_SELECTION.md)
- [Selection Patterns](../../../../../docs/SELECTION_PATTERNS.md)
- [Technique Topology Scout](../../../../../reports/technique_topology_scout.md)
- [Instruction-Surface Semantic Review](../../../../../docs/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md)
- [KAG Source Lift Semantic Review](../../../../../docs/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md)
- [Docs Boundary Semantic Review](../../../../../docs/DOCS_BOUNDARY_SEMANTIC_REVIEW.md)
- [Skill-Support Semantic Review](../../../../../docs/SKILL_SUPPORT_SEMANTIC_REVIEW.md)

## Selector Prompts

| selector prompt | first correct pick | why adjacent leaves lose |
|---|---|---|
| "Several context fragments must render into one repeatable agent context artifact with source traceability." | `AOA-T-0012` | fragment-first authoring stops before assembly; rule distribution fans one source out to many targets |
| "One local canonical rule source must refresh several managed agent instruction files without copy-paste drift." | `AOA-T-0013` | deterministic context composition is many sources to one output; upstream mirroring keeps source ownership outside the repo |
| "One upstream-owned source must be mirrored locally with attribution and repeatable resync." | `AOA-T-0024` | local fan-out owns a local canonical source; skill propagation owns managed agent targets, not upstream provenance |
| "One shared skill or rule core must propagate into several managed agent-facing targets." | `AOA-T-0027` | broad rule distribution remains the default local-source pattern; upstream mirror ownership is external |
| "Parent and nested rule layers need explicit precedence without making child layers canonical." | `AOA-T-0029` | single-source distribution is fan-out; deterministic context composition is output assembly rather than layered precedence |
| "Agent context is too large and needs bounded source fragments before any assembly step becomes the focus." | `AOA-T-0030` | `AOA-T-0012` owns the generated artifact; this leaf owns source partitioning before assembly |
| "Runtime posture needs named profiles and presets with inspectable resolution before launch." | `AOA-T-0035` | context composition renders agent docs; this leaf composes runtime posture layers and stops before runtime truth checks |
| "A repo needs one canonical home per recurring doc role and explicit update-routing rules." | `AOA-T-0002` | snapshot discipline assumes entrypoint trim pressure; decision notes record one choice, not the whole doc map |
| "README or MANIFEST has become a status archive and needs to become a short link-driven entrypoint again." | `AOA-T-0009` | source-of-truth layout owns the larger role map; repo-doc lift only derives routing knowledge from existing docs |
| "One meaningful architectural choice needs context, options, rationale, and consequences recorded." | `AOA-T-0033` | source-of-truth layout decides document roles; bounded-context map clarifies semantic scope before work |
| "A diagnostic artifact should be shared publicly without leaking private detail or pretending the action is approved." | `AOA-T-0034` | approval evidence and dry-run workflows live outside this shelf; this leaf owns share-prep sanitization only |
| "A reader needs stable section lookup inside technique markdown after bundle-level routing already found the bundle." | `AOA-T-0018` | metadata spine routes at bundle level; semantic-review lift routes cluster review docs, not bundle sections |
| "A generated catalog needs shallow bundle identity, status, kind, and direct adjacency handles without replacing markdown." | `AOA-T-0019` | section lift opens markdown sections; provenance and relation lifts depend on explicit metadata handles |
| "A KAG surface needs note-kind and note-path provenance handles without flattening notes into a graph." | `AOA-T-0020` | metadata spine is upstream routing; bounded relation lift exposes adjacent technique edges instead of note provenance |
| "A KAG surface needs one-step typed relation hints without graph traversal or rationale fields." | `AOA-T-0021` | metadata spine gives the bundle handle; semantic-review lift exposes review clusters, not direct bundle edges |
| "Review needs bounded caution lookup over Risks language without scoring or generated policy." | `AOA-T-0022` | section lift is generic section lookup; public-safe sanitization is share-prep, not caution taxonomy |
| "A reader needs to know which authoritative repo doc or status file anchors a question." | `AOA-T-0046` | source-of-truth layout authors the doc role map; this leaf derives a routing surface from existing docs |
| "A repo wants GitHub issue and PR templates lifted into intake knowledge without workflow automation." | `AOA-T-0047` | metadata spine is broader bundle routing; public-safe sanitization handles shareable artifacts, not intake prompt lookup |
| "A repo wants authored semantic-review docs discoverable as review-cluster lookup without automatic verdicts." | `AOA-T-0048` | section lift opens bundle headings; this leaf lifts human review surfaces |
| "A boundary must be verified through expected inputs, outputs, and consumer-visible behavior." | `AOA-T-0015` | property invariants broaden coverage over a stable truth; bounded-context map clarifies scope before validation |
| "Example tests are too narrow and one stable truth should hold across many inputs or states." | `AOA-T-0017` | contract-test design starts from a named boundary; signal-first gate promotion governs enforcement, not invariant design |
| "Naming and ownership are blurred, and a future change needs a semantic map before implementation." | `AOA-T-0016` | source-of-truth layout maps docs roles; contract and invariant techniques validate behavior after scope is clear |

## Relation Read

| relation | verdict | reason |
|---|---|---|
| `AOA-T-0002 complements AOA-T-0009` | keep | the broader doc-role map and the narrower snapshot discipline strengthen each other without forcing a strict prerequisite |
| `AOA-T-0009 complements AOA-T-0002` | keep | snapshot trim can be applied lightly, but reads best beside a role map; `requires` would overstate dependency |
| `AOA-T-0013 complements AOA-T-0002` | keep | local rule-source fan-out benefits from source-of-truth discipline without requiring the full docs layout technique |
| `AOA-T-0024 complements AOA-T-0013` | keep | upstream mirroring and local source fan-out are neighboring distribution contracts with different source ownership |
| `AOA-T-0027 complements AOA-T-0013` | keep | managed-target skill or rule propagation is narrower than broad local rule distribution, not a strict prerequisite chain |
| `AOA-T-0029 complements AOA-T-0013` | keep | hierarchical loading and fan-out share source ownership discipline but differ on precedence versus target distribution |
| `AOA-T-0030 complements AOA-T-0012` | keep | fragment-first authoring prepares a possible source layer; deterministic assembly is a later generated-artifact contract |
| `AOA-T-0035 complements AOA-T-0012` | keep | profile/preset composition shares deterministic composition pressure but owns runtime posture rather than agent context output |
| `AOA-T-0018 complements AOA-T-0019` | keep | section lift and metadata spine support different depths of lookup and should not collapse |
| `AOA-T-0019 complements AOA-T-0018` | keep | bundle-level metadata and section-level markdown lift are peers, not a single stack step in every use |
| `AOA-T-0019 used_together_for AOA-T-0020` | keep | metadata handles commonly travel with provenance-note lift, but the stricter dependency is already expressed from `0020` to `0019` |
| `AOA-T-0019 used_together_for AOA-T-0021` | keep | metadata handles commonly travel with relation lift, while relation lift keeps the exact `requires` edge |
| `AOA-T-0020 requires AOA-T-0019` | keep | note-kind and note-path lift needs an explicit metadata spine and bundle handles |
| `AOA-T-0021 requires AOA-T-0019` | keep | direct relation hints need metadata identity and adjacency handles before derived consumers can lift edges |
| `AOA-T-0022 complements AOA-T-0018` | keep | caution lookup and section lift both use markdown authority, but caution should not become a mandatory section-lift consumer |
| `AOA-T-0046 complements AOA-T-0002` | keep | repo-doc surface lift derives routing over authored docs; it should not own the doc-role layout itself |
| `AOA-T-0046 complements AOA-T-0009` | keep | repo-doc routing may expose entrypoint snapshots without making snapshot trim a strict dependency |
| `AOA-T-0047 complements AOA-T-0019` | keep | GitHub template lift can sit beside metadata-spine routing without requiring bundle catalog semantics |
| `AOA-T-0048 complements AOA-T-0018` | keep | semantic-review lift and section lift are both markdown-first lookup patterns, but one is cluster-review shaped |
| `AOA-T-0015 complements AOA-T-0003` | keep | contract-test design can use stable summary contracts, but does not require the smoke-summary technique itself |
| `AOA-T-0015 complements AOA-T-0001` | keep | contract validation often supports implementation workflow without becoming the workflow prerequisite |
| `AOA-T-0016 complements AOA-T-0002` | keep | bounded-context mapping can clarify docs/source ownership, but it is not document-role layout |
| `AOA-T-0016 complements AOA-T-0001` | keep | context mapping can scope implementation work, but does not require the plan/diff/apply workflow |
| `AOA-T-0017 complements AOA-T-0007` | keep | invariant checks may later provide signal for gate promotion, but promotion governance is a separate step |
| `AOA-T-0017 complements AOA-T-0001` | keep | invariant validation can support a change workflow without becoming a workflow dependency |

## Repair Gate

Accepted: none.

Held:

| pressure | hold reason |
|---|---|
| `AOA-T-0027 requires AOA-T-0013` | narrower managed-target propagation shares the local-source contract but can stand as its own technique; `complements` keeps it adjacent without hiding the distinction |
| `AOA-T-0029 requires AOA-T-0013` | nested rule loading needs source ownership discipline, not the multi-target fan-out contract owned by `AOA-T-0013` |
| `AOA-T-0030 requires AOA-T-0012` | fragment-first authoring intentionally precedes any generated assembly requirement |
| `AOA-T-0035 requires AOA-T-0012` | runtime profile/preset composition is a sibling composition shape, not a context-composition consumer |
| `AOA-T-0046 requires AOA-T-0002` or `AOA-T-0009` | repo-doc surface lift can route over a bounded docs set without forcing full source-of-truth layout or snapshot discipline |
| `AOA-T-0047 requires AOA-T-0019` | GitHub template lift is adjacent to metadata spine but does not depend on technique-bundle frontmatter |
| `AOA-T-0048 requires AOA-T-0018` | semantic-review docs are authored review surfaces, not lifted `TECHNIQUE.md` sections |
| `AOA-T-0015 shares_contract_with AOA-T-0017` | the two validation techniques share testing language, but their contracts are different enough that a new edge would add noise |
| `AOA-T-0034` relation to approval evidence | share-prep deliberately stays distinct from approval classification and execution permission |
| new sequence vocabulary | Wave B exposes "precedes", "narrows", and "same family" pressure, but no current relation type should be overloaded to encode those ideas |

## Axis Usefulness

| axis | value in Wave B | limit |
|---|---|---|
| `domain` | groups the docs-heavy shelves and separates evaluation validation leaves | nearly every instruction and KAG leaf is `docs`, so this axis cannot choose a leaf alone |
| `kind` | separates composition, distribution, lift, artifact, guardrail, and validation shapes | dense shelves still have multiple leaves with the same kind |
| tree shelf | gives the strongest second-stage neighborhood for instruction, KAG, docs-boundary, and skill-support reads | shelf placement does not imply relation direction or mandatory sequence |
| `execution_profile` | correctly warns that some lift/distribution rows need orchestration while contract/invariant/context-map rows are small-agent shaped | scout suitability is still not empirical proof from a local model |
| `risk_posture` | keeps public-share, external-evidence, approval, and security-sensitive rows from being treated as simple doc reads | risk posture does not decide whether a relation is `requires` |
| `relations` | useful where a true object dependency exists, especially `0020`/`0021` -> `0019` | relation hints should not become rationale, sequence vocabulary, or graph traversal |

## What Changed

- added this Wave B review packet;
- recorded that no direct relation repair is justified for Wave B.

## What Did Not Change

- no source bundle frontmatter;
- no generated catalog or selection surface;
- no relation schema migration;
- no new relation types;
- no relation rationale fields;
- no generated graph behavior, traversal, scoring, or ranking;
- no status, `domain`, `kind`, path, family, capability, substrate,
  execution-profile, risk, maturity, evidence, or owner changes;
- no empirical small-agent proof claim.

## Public-Safety Read

The review uses existing public bundle text, generated public repo surfaces, and
sanitized review language. It does not include secrets, tokens, private
topology, operational hostnames, internal runtime details, or non-public donor
material. Mentions of sanitization and public share are technique-subject
references, not leaked sensitive content.

## Next Honest Move

Land Wave B as a review-only wave with no generated rebuild and no direct
relation repair.

After landing, continue the temporary plan with Wave C:
`execution/agent-workflows-core`, `execution/runtime-truth-lifecycle`,
`proof/owner-truth-closeout`, and `governance/approval-evidence`.
