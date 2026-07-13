# aoa-techniques System Design

## Role

`DESIGN.md` describes the system form of `aoa-techniques`.

It is not the charter, roadmap, technique index, authoring contract, or
agent-instruction file.

It answers one question:

What shape should the reusable practice canon take as it grows as both a public
library and an AoA organ?

## Design Thesis

`aoa-techniques` is a public canon of reusable engineering practice.

It preserves small, source-authored technique meaning while giving humans,
agents, and sibling AoA repositories enough structure to select, verify, adapt,
and lift a technique without confusing it with a skill, proof surface, playbook,
memory object, routing policy, or runtime body.

The bundle owns the move. Mechanics explain how practice moves. Generated
surfaces help readers orient. Neighboring repositories own their stronger
layers.

## Design as Appearance

The repository should appear as a practice library with a clear public front
door:

- compact entry route
- durable authority and contract docs
- readable technique tree
- mechanic districts for practice movement
- generated companions for selection
- local agent cards for nearest-route safety

A reader should be able to ask: what does this repo own, what is one technique,
where does this bundle live, how mature is it, what validates it, and when
should I leave for another AoA owner?

## Design as Anatomy

`aoa-techniques` is composed of different source classes:

- root public entry and authority surfaces
- source-authored technique bundles under [techniques](techniques/)
- technique contracts and reader guides under [docs](docs/README.md)
- practice-motion mechanics under [mechanics](mechanics/README.md)
- repo-wide schemas, templates, configs, and examples
- generated reader and machine companions
- an owner-local statistical measurement port for bounded corpus questions
- public-safe legacy and provenance surfaces
- agent-facing route cards

Each class supports the others. No class should silently steal another class's
authority.

## Design as Operation

A good practice-canon operation has:

- an entry route
- a named owner surface
- one bounded change target
- an evidence or provenance path
- a validation path
- a generated-freshness path when derived outputs move
- a closeout path that leaves the next reader less lost

Practice moves should become more portable, more bounded, and more reviewable
as they mature.

## Design as Aim

The long aim is a technique canon that can scale beyond a small hand-curated
library without becoming a pile of snippets.

The repository should support:

- thousands of compact technique bundles
- stable IDs and source-authored bundle meaning
- faceted topology beyond overloaded domains
- generated readers for low-context selection
- safe lift into skills, evals, routing, KAG, playbooks, memory, and runtime
  owners without transferring authority by accident

The canon grows well when every new surface makes selection, ownership,
validation, or return clearer than before.

## Design Principles

### 1. Atomic practice before orchestration

One technique describes one reusable move. Chains, workflows, scenarios, and
live execution belong in stronger neighboring owners.

### 2. Source before generated

Generated catalogs, capsules, manifests, and route readers summarize source
truth. They do not become technique meaning.

### 3. Standalone before hidden ecosystem dependency

AoA provenance and owner routes are allowed, but a public reader should still
understand the bounded practice without deploying OS Abyss.

### 4. Topology before sprawl

Domain, kind, tree placement, family, capability, substrate, execution profile,
risk posture, and relation topology should make scale legible. They should not
be collapsed into vague tags.

### 5. Mechanics before promotion pressure

Candidate movement, donor intake, audit, recurrence, growth, and release
support belong in mechanics until a stable atomic technique is ready.

### 6. Owner split before absorption

Skills, evals, routing, KAG, memory, playbooks, roles, stats, runtime, and ToS
meaning have stronger owners. This repo may route to them but should not absorb
their truth.

Owner-local measurement meaning remains here when it concerns the technique
canon. Cross-owner statistical grammar, aggregation, and views remain with
`aoa-stats`, and neither side may turn a corpus ratio into technique status or
promotion authority.

### 7. Validation before confidence

Every meaningful change should have a local check, a generated-freshness check
when needed, and a closeout that names what was not checked.

### 8. Agent guidance is a route layer

Agent-facing cards should tell an agent where it is, what owns the claim, what
not to claim, how to verify, and how to hand off. They should not become the
technique canon.

## Good Design Feels Like

- a public reader can find one useful technique
- an agent can find the nearest rule
- a maintainer can find the owner surface
- a generated file can find its source
- a candidate can find its review path
- a sibling repository can receive a bounded handoff
- a future contributor can find why the route exists

## Bad Design Smells Like

- root inflation
- duplicate technique doctrine
- generated files cited as source truth
- mechanics turning into canon by proximity
- technique bundles widening into skill workflows or playbooks
- private project residue disguised as reusable practice
- topology labels that do not change selection quality
- public promises without validation or owner evidence

## Relationship to Other Root Surfaces

[README](README.md) introduces. [CHARTER](CHARTER.md) authorizes.
[START_HERE](docs/START_HERE.md) routes. [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md)
maps the corpus. [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) governs
placement. [AGENTS](AGENTS.md) routes agents. [DESIGN.AGENTS](DESIGN.AGENTS.md)
holds the design form of the agent-facing layer. `DESIGN.md` holds the system
form of the practice canon.

## Use by Agents

Agents should consult this file when a change alters:

- repository shape
- root surfaces
- technique tree posture
- source versus generated authority
- mechanics-to-canon boundaries
- standalone versus AoA-organ posture
- agent-facing layer design
- generated companion posture
- neighboring owner handoffs

This file does not override local owner truth. It tells agents what kind of
shape they are preserving.
