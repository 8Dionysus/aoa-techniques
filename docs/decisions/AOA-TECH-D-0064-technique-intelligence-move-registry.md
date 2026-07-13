# Technique Intelligence Move Registry

Status: accepted
Date: 2026-05-18

## Index Metadata

- Decision ID: AOA-TECH-D-0064
- Original date: 2026-05-18
- Surface classes: technique intelligence, generated/readout
- Technique axes: intelligence
- Mechanic parents: none
- Guard families: generated/read-model
- Posture: accepted

## Context

`aoa-techniques` needs to prepare its technique canon for RAG, Agentic RAG,
DAG navigation, and future agentic graph use without confusing techniques with
larger workflow, routing, proof, runtime, role, or graph owners.

The central object here is a technique: one atomic executable move. The first
intelligence layer therefore needs to focus agent attention on source-linked
moves, not on activation, autonomy, or sibling-repository workflow shape.

## Options considered

1. Copy a workflow-oriented registry shape from a sibling repository.
2. Start with embeddings or graph inference before a deterministic registry.
3. Build a source-derived move registry first, then expose query, explanation,
   packing, and a navigation DAG as weaker derived surfaces.

## Decision

Add a deterministic Technique Intelligence layer built around atomic moves:

- `generated/technique_intelligence_registry.json`
- `generated/technique_intelligence_registry.min.json`
- `generated/technique_intelligence_dag.json`
- `generated/technique_intelligence_dag.min.json`
- `docs/readers/intelligence/TECHNIQUE_INTELLIGENCE.md`
- `scripts/technique_intelligence_surface.py`
- `scripts/technique_intelligence.py`
- `scripts/build_technique_intelligence.py`
- registry and DAG schemas

The registry joins existing source-derived surfaces into queryable packets. It
does not become technique authority.

## Rationale

The deterministic layer gives future agents a stable first attention surface:
find likely moves, explain evidence, compare nearby moves, load source refs,
and stop when the object changes owner.

This is safer than starting with embeddings or graph inference because the
repo already has stable IDs, source sections, capsules, manifests, review
refs, direct relations, and scout outputs. Joining those surfaces first makes
later semantic retrieval or graph work reviewable instead of magical.

## Consequences

- Technique lookup becomes locally runnable and validator-backed.
- A small agent can receive a bounded packet without inheriting unrelated
  source surfaces.
- The DAG is explicitly a navigation DAG, not relation truth or composition
  order.
- Scout axes remain scout-only until a separate decision promotes them.
- Larger execution, proof, routing, role, runtime, scenario, memory, and graph
  questions must still route away to their owners.

## Source surfaces

- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `docs/selection/TECHNIQUE_INTELLIGENCE_GUIDE.md`
- `mechanics/distillation/parts/technique-reform-ingress/reviews/technique-intelligence-layer-strategy.md`
- `scripts/technique_intelligence_surface.py`
- `generated/technique_intelligence_registry.json`
- `generated/technique_intelligence_dag.json`

## Follow-up route

Future semantic retrieval, reranking, external vector stores, or graph
projection should consume this registry as a source-linked derived packet and
must preserve the source bundle as stronger authority.

If scout axes become stable enough for frontmatter, open a new topology
decision instead of silently upgrading the registry fields.

## Verification

Use:

Verification was routed through the targeted owner checks and repository validation lanes.
