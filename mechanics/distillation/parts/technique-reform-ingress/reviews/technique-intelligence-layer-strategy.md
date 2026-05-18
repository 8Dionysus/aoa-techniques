# Technique Intelligence Layer Strategy

- status: strategic_audit_artifact
- created_at: 2026-05-18
- owner_repo_under_review: /srv/AbyssOS/aoa-techniques
- comparative_input: sibling registry work was used only as a cautionary donor, not as the framing authority
- purpose: prepare `aoa-techniques` for RAG, Agentic RAG, DAG, and agentic graph-ready move selection
- authority: review packet only; it does not replace root `AGENTS.md`, `DESIGN.md`, `DESIGN.AGENTS.md`, technique bundles, schemas, generated catalogs, KAG guides, or sibling-owner truth

## 0. Why This Artifact Exists

The central question is not which workflow to activate.

The central question is which atomic move fits the current material, what
evidence makes that move appropriate, where the move stops, and where a larger
owner should take over.

The technique-side goal is therefore:

```text
source technique canon
  -> deterministic technique intelligence registry
  -> portable lexical retrieval
  -> source-linked section and capsule evidence packets
  -> optional semantic retrieval and rerank
  -> topology and owner-boundary filters
  -> bounded technique selection, packing, or handoff
  -> future DAG/KAG/agentic graph projections that remain weaker than source
```

The goal is not "let embeddings choose a technique." The goal is to let a
future agent find the right atomic move, explain why it fits, know why adjacent
moves do not fit, load only the needed source, and hand off to a stronger owner
when the request is no longer technique-local.

## 1. Ground Rules

### 1.1 Technique source remains the authority

The repo already has the right ownership posture:

- authored `techniques/**/TECHNIQUE.md` bundles own technique meaning
- frontmatter owns current identity, `domain`, `kind`, status, direct
  relations, and evidence handles
- generated catalogs, capsules, manifests, reviews, scout reports, and exports
  are derived reader or review surfaces
- if generated output drifts, repair source or builder and regenerate

A Technique Intelligence Layer must make those surfaces easier to query, not
turn the query layer into a new source of truth.

### 1.2 Techniques are moves

The implementation must index a technique as a move, not as a capability,
service, workflow, or activation target.

Each registry entry should answer:

- what move this is
- what material it acts on
- when the move applies
- when it does not apply
- what input it needs
- what output it produces
- where it stops
- what can go wrong
- what minimal check confirms it worked

It should not answer "what should be invoked." Larger owners may compose,
activate, route, evaluate, or run things. This repo preserves and exposes the
move.

### 1.3 Scout axes stay scout axes

The current topology work produced useful design axes:

- `family`
- `capability_class`
- `substrate`
- `execution_profile`
- `risk_posture`
- richer relation pressure

Those are valuable filters for retrieval, but they remain weaker than
frontmatter truth until a separate schema/frontmatter decision promotes them.
The registry may include them as `scout_refs` or `topology_hints`; it must not
present them as required technique fields.

### 1.4 AG-ready means agentic graph-ready, not agent autonomy

In this packet, "AG-ready" means a technique can be discovered, explained,
packed, and graph-projected by an agentic layer while remaining source-linked
and bounded. It does not mean the technique becomes an agent, workflow, role
contract, proof verdict, playbook, or runtime behavior.

If a future sibling owner gives "AG" a narrower term, that owner owns the term.
This repo owns only the technique-side readiness shape.

## 2. Current Reconnaissance

### 2.1 Corpus

Current generated and source checks show:

- `107` technique bundles
- `98` `canonical` bundles
- `9` `promoted` bundles
- `6` frontmatter domains:
  `agent-workflows`, `docs`, `evaluation`, `history`, `system-recovery`,
  `validation-patterns`
- `12` current `kind` values:
  `artifact`, `assessment`, `composition`, `discovery`, `distribution`,
  `guardrail`, `handoff`, `ingest`, `lift`, `recovery`, `validation`,
  `workflow`

The corpus is already much better prepared for RAG than a loose markdown
library. It has stable IDs, consistent technique bundle contracts, generated
reader surfaces, direct relation syntax, evidence notes, and review packets.

### 2.2 Existing source and generated surfaces

Useful existing source surfaces:

- `techniques/**/TECHNIQUE.md`
- `TECHNIQUE_INDEX.md`
- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `docs/source-lift/*.md`
- `docs/review/*.md`
- `config/technique_kind_registry.yaml`
- part-local scout config under
  `mechanics/distillation/parts/technique-reform-ingress/config/`
- review packets under
  `mechanics/distillation/parts/technique-reform-ingress/reviews/`

Useful generated surfaces:

- `generated/technique_catalog.json`
- `generated/technique_catalog.min.json`
- `generated/technique_capsules.json`
- `generated/technique_capsules.min.json`
- `generated/technique_sections.full.json`
- `generated/technique_section_manifest.json`
- `generated/technique_section_manifest.min.json`
- `generated/technique_checklist_manifest.json`
- `generated/technique_checklist_manifest.min.json`
- `generated/technique_example_manifest.json`
- `generated/technique_example_manifest.min.json`
- `generated/technique_evidence_note_manifest.json`
- `generated/technique_evidence_note_manifest.min.json`
- `generated/github_review_template_manifest.json`
- `generated/semantic_review_manifest.json`
- `generated/shadow_review_manifest.json`
- `generated/repo_doc_surface_manifest.json`
- `generated/technique_kind_manifest.json`
- `generated/technique_promotion_readiness.min.json`
- `generated/kag_export.json`
- `generated/kag_export.min.json`

Important part-local review surfaces:

- `reports/technique_topology_scout.md`
- `reports/technique_family_scout.md`
- `reports/kind_ambiguity_audit.md`
- `reports/technique_tree_projection.md`
- `reviews/execution-profile-fixture-sketch-ledger.md`
- `reviews/execution-profile-empirical-harness-decision.md`
- `reviews/selector-relation-long-pass-closeout-ledger.md`
- `reviews/owner-boundary-bridge-long-pass-closeout-ledger.md`
- `reviews/template-modernization-skill-support-pilot.md`

### 2.3 What already works

The repo already has strong ingredients for an intelligence layer:

- full-corpus generated catalog and capsule cards
- section extraction from canonical headings
- checklist, example, evidence-note, semantic-review, shadow-review, and
  repo-doc lifted surfaces
- direct relation support in source frontmatter
- topology scout reports covering all `107` bundles
- selector/relation review coverage over all `28` shelves and `107` bundles
- owner-boundary review coverage over all `107` bundles
- future small-agent fixture sketches for all current `small-agent` scout rows
- explicit KAG source-lift guide that keeps generated graph surfaces weaker
  than authored markdown

This means `aoa-techniques` does not need to start with "add embeddings." It
needs a first deterministic registry that joins the already-good surfaces into
one queryable evidence packet.

### 2.4 What is missing

The missing center is a single Technique Intelligence surface:

- no `generated/technique_intelligence_registry.json`
- no minified portable intelligence registry
- no schema for the registry shape
- no local CLI for `build`, `query`, `explain`, and `status`
- no FTS5-backed search over technique sections, capsules, examples,
  checklists, risk text, and review refs
- no bounded candidate packet that says:
  "use this technique", "compare these techniques", "load these source
  sections", or "route away to a sibling owner"
- no uniform place where topology hints, direct relations, review pressure,
  owner-boundary stop-lines, and future eval fixture refs meet

The repo has many high-quality pieces. The next layer should connect them
without flattening them.

## 3. Target System Shape

Working name:

```text
Technique Intelligence Layer
```

First concrete slice:

```text
Technique Intelligence Registry
```

Minimum first-slice files:

- `schemas/technique_intelligence_registry.schema.json`
- `scripts/technique_intelligence_surface.py`
- `scripts/technique_intelligence.py`
- `generated/technique_intelligence_registry.json`
- `generated/technique_intelligence_registry.min.json`
- focused tests for registry build, query, explanation, and schema stability

The registry should be source-derived and reproducible. It should consume
existing generated surfaces rather than hand-maintaining a new truth file.

## 4. Registry Logical Views

### 4.1 Identity view

Each entry should carry:

- `id`
- `name`
- `status`
- `domain`
- `kind`
- source `technique_path`
- source hash or section content hash
- generated freshness refs
- stable source refs for every quoted or summarized field

### 4.2 Atom view

The atom view should help an agent understand the smallest move:

- summary
- one-line intent
- `Intent`
- `When to use`
- `When not to use`
- `Inputs`
- `Outputs`
- `Core procedure`
- `Contracts`
- `Risks`
- `Validation`
- optional `Atomic move`
- optional `Topology fit`
- optional `Small-agent execution shape`

Old-template bundles should not be rewritten just to satisfy this registry.
Optional modern sections should be indexed when present and absent when not.

### 4.3 Capsule view

The capsule view should reuse `generated/technique_capsules.json`:

- compact intent
- short use and do-not-use cues
- short input and output cues
- compact contract
- main risk
- validation cue

This is the right first payload for small context windows.

### 4.4 Search document view

The registry should emit search documents rather than one large blob. Useful
document classes:

- `capsule`
- `intent`
- `use_when`
- `do_not_use`
- `inputs`
- `outputs`
- `core_procedure`
- `contracts`
- `risks`
- `validation`
- `adaptation_notes`
- `example`
- `checklist`
- `evidence_note`
- `semantic_review`
- `shadow_review`
- `repo_doc_ref`

Each search document should include `technique_id`, `source_ref`,
`section_name`, `text`, and a source-derived hash.

### 4.5 Topology view

The topology view should join current truth with scout-only hints:

- current truth: `domain`, `kind`, direct relations, evidence refs
- current tree path: authored file path and current shelf/trunk projection
- scout-only: `family`, `capability_class`, `substrate`,
  `execution_profile`, `risk_posture`
- review state: selector/relation and owner-boundary review refs

The field name should make weakness explicit, for example:

```json
"topology_hints": {
  "authority": "scout_only",
  "family": "...",
  "execution_profile": "...",
  "source_refs": [...]
}
```

### 4.6 Relation view

Relations should stay bounded:

- include direct source frontmatter relations
- include relation source refs
- include held relation pressure from review packets as review refs, not as
  edges
- do not infer graph truth from co-occurrence, family membership, or semantic
  similarity

Future relation-rationale work can grow from this view, but the first slice
should not invent new relation vocabulary.

### 4.7 Boundary and owner handoff view

Each entry needs stop-lines and allowed handoff hints:

- route to the workflow owner when the request asks for reusable multi-step
  execution
- route to `aoa-evals` when the request asks for empirical proof or model
  verdicts
- route to `aoa-routing` when the request is owner dispatch or route policy
- route to `aoa-kag` when the request is knowledge substrate behavior,
  graph-ranking, or retrieval platform authority
- route to `aoa-playbooks` when the request is recurring scenario
  choreography
- route to `aoa-agents` when the request is role contract or agent persona
  law
- route to `abyss-stack` when runtime, deployment, storage, lifecycle, or
  infrastructure behavior is the real owner

This view prevents technique retrieval from silently becoming routing,
workflow, proof, graph, or execution authority.

### 4.8 Fixture and proof-readiness view

The registry may include future fixture sketch refs from
`execution-profile-fixture-sketch-ledger.md`, but only as readiness evidence:

- candidate fixture sketch exists
- minimal input shape
- allowed context
- forbidden hidden context
- expected output cue
- pass/fail cue
- eval owner warning

It must not claim empirical small-agent proof. The current decision routes real
model execution to `aoa-evals`.

## 5. RAG Model

The first useful RAG path should be local-first and deterministic:

```text
intent
  -> owner/layer precheck
  -> exact ID/name/frontmatter/capsule preselect
  -> SQLite FTS5 search over registry search_documents
  -> topology and boundary filters
  -> optional semantic retrieval
  -> optional rerank
  -> source-linked evidence packet
```

### 5.1 Owner and layer precheck

Before searching techniques, ask whether the user needs:

- one atomic practice move
- a reusable workflow
- an eval/proof surface
- a route decision
- a KAG graph/retrieval platform feature
- a playbook or scenario
- an agent role/handoff contract
- runtime/infrastructure behavior

If the answer is not technique-local, the registry should return a route-away
packet with source refs, not force a technique match.

### 5.2 Lexical and exact preselect

First preselect should handle:

- exact `AOA-T-*` ID
- technique slug or name
- `domain`
- `kind`
- capsule fields
- source heading names
- relation target IDs

This should work without embeddings and without a network service.

### 5.3 FTS search

The local FTS corpus should index:

- all registry search documents
- capsule summaries
- risk and negative-effect text
- validation cues
- examples and checklists
- evidence note summaries
- semantic and shadow review refs

This keeps the first retrieval slice technique-specific: search over move
evidence, not over executable workflow state.

### 5.4 Optional semantic retrieval

Semantic retrieval can appear later as acceleration:

- never required for correctness
- never the only source of candidate ranking
- every semantic hit must point to source refs
- semantic near-misses should be reported as near-misses, not silent winners

### 5.5 Evidence packet shape

The RAG answer should be a packet, not a detached summary:

- chosen candidate or ranked candidates
- positive evidence with source refs
- negative or adjacent evidence with source refs
- why the candidate is technique-local
- why sibling-owner routes were not chosen, or which route-away applies
- source files to load next
- compact execution pack shape
- freshness status of generated registry against current source

## 6. Agentic RAG Model

Agentic RAG for techniques should be a bounded selector/composer loop:

```text
interpret intent
  -> decide technique-local vs route-away
  -> retrieve candidates
  -> compare adjacent techniques
  -> load only needed sections/support refs
  -> emit technique-use, compare, compose, or handoff packet
  -> record evidence gaps
```

Allowed actions:

- select one technique for a narrow move
- compare a small set of adjacent techniques
- propose a technique sequence as a candidate composition
- prepare a source-linked handoff to a workflow, eval, route, playbook, KAG, or
  agent owner
- report that no current technique fits

Not allowed:

- activate or run a workflow
- mutate technique source
- promote a status
- add relation edges
- create proof verdicts
- claim generated graph truth
- choose sibling-owner policy

The point is move discipline: a technique intelligence agent prepares bounded
use and handoff. It does not become an execution agent.

## 7. DAG And Graph Model

The DAG should be an explanation and navigation graph.

Useful node kinds:

- `technique`
- `technique_section`
- `technique_capsule`
- `checklist`
- `example`
- `evidence_note`
- `semantic_review`
- `shadow_review`
- `repo_doc_surface`
- `topology_hint`
- `direct_relation`
- `review_pressure`
- `fixture_sketch`
- `generated_surface`
- `owner_route`

Useful edge kinds:

- `generated_from`
- `has_section`
- `has_capsule`
- `has_checklist`
- `has_example`
- `evidenced_by`
- `directly_relates_to`
- `requires`
- `complements`
- `used_together_for`
- `has_topology_hint`
- `reviewed_by`
- `has_fixture_sketch`
- `routes_to_owner`
- `supports_handoff`

Graph rules:

- source direct relations outrank generated graph edges
- topology hints are filters, not truth
- review pressure is evidence, not mutation
- multi-hop graph inference is never authority
- graph ranking may suggest where to read next, not what the technique means

## 8. First Implementation Slice

The first slice should be intentionally boring and source-derived:

1. Add a decision note before code lands, because this becomes a durable
   registry surface.
2. Add `schemas/technique_intelligence_registry.schema.json`.
3. Add `scripts/technique_intelligence_surface.py` to build the payload from
   existing generated surfaces and source bundles.
4. Add `scripts/technique_intelligence.py` with:
   - `build --check`
   - `query <intent> --limit N`
   - `explain <AOA-T-XXXX> --intent "..."`
   - `status`
5. Generate:
   - `generated/technique_intelligence_registry.json`
   - `generated/technique_intelligence_registry.min.json`
6. Add tests for:
   - schema validity
   - full-corpus entry count
   - source hash/freshness behavior
   - FTS or fallback query
   - explanation packet source refs
   - no activation or invocation fields
   - scout axes marked weaker than source truth
7. Add the check to the repo validation menu only after the builder is stable.

The first slice should not require:

- new frontmatter
- mass bundle rewrites
- relation vocabulary expansion
- semantic backend
- KAG platform behavior
- eval harness execution
- downstream install projection

## 9. Later Phases

Recommended phase order:

1. Registry first slice.
2. Portable FTS query and explanation.
3. Technique pack profiles:
   `capsule`, `small-agent`, `orchestrator`, `workflow-handoff`,
   `eval-fixture`.
4. Optional semantic backend and rerank.
5. DAG/graph export as source-linked navigation.
6. `aoa-routing` integration for owner-route precheck.
7. Workflow-owner integration for technique lineage and handoff.
8. `aoa-evals` integration for fixture execution and empirical small-agent
   proof.
9. `aoa-kag` integration for broader graph substrate, still source-linked.
10. Workspace rollout or SDK wrapper after the registry is stable.

## 10. Risks

### 10.1 Semantic layer steals authority

Risk: embeddings rank a plausible technique over the source-defined one.

Guard: semantic retrieval is optional acceleration; exact ID, lexical source
matches, direct relations, and owner-boundary filters stay visible.

### 10.2 Technique layer becomes a workflow router

Risk: technique retrieval starts acting like workflow activation.

Guard: no activation fields, no invocation policy, no install freshness, no
runtime state. The output is select, compare, pack, or route away.

### 10.3 Scout axes become fake schema

Risk: `family`, `capability_class`, `substrate`, `execution_profile`, and
`risk_posture` are treated as canonical frontmatter.

Guard: include them only under explicit scout authority with source refs.

### 10.4 DAG becomes fake world model

Risk: graph adjacency gets mistaken for proof, route law, or technique meaning.

Guard: graph edges explain where to read next. They do not decide truth.

### 10.5 KAG export expands too early

Risk: the narrow `AOA-T-0043` KAG pilot becomes a broad graph export before
the source registry exists.

Guard: keep `generated/kag_export.*` narrow until the technique intelligence
registry can provide corpus-wide source-linked packets.

### 10.6 Small-agent readiness is overclaimed

Risk: `execution_profile=small-agent` is mistaken for empirical model proof.

Guard: keep fixture sketches as readiness refs only; real runs belong in
`aoa-evals`.

## 11. Success Criteria

The first slice is successful when a local agent can:

- verify registry freshness from source and generated inputs
- query by intent without a semantic service
- explain why a technique fits with source refs
- explain why adjacent techniques are near-misses
- distinguish technique-local use from workflow, eval, routing, KAG, playbook,
  agent, and runtime handoff
- pack a compact technique evidence packet without loading the whole repo
- prove scout axes are labeled as scout-only
- run the check in CI without network dependencies

## 12. Recommended Next Move

Do not start with broad semantic infrastructure.

The next implementation should be the deterministic registry first slice:

```text
source bundles + current generated surfaces
  -> technique_intelligence_registry
  -> local query/explain/status
```

This gives RAG, Agentic RAG, DAG, and agentic graph work a stable move
substrate. Only after that should the repo grow semantic rerank, DAG export, or
sibling integration.

The important rule is: build one source-derived move evidence packet before any
semantic or agentic layer tries to reason over the corpus.
