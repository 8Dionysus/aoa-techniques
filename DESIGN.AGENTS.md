# aoa-techniques Agent Surface Design

## Role

`DESIGN.AGENTS.md` describes the desired form of agent-facing guidance within
`aoa-techniques`.

It is not an `AGENTS.md` card, prompt library, policy bundle, technique
contract, validator, or generated index.

It answers one question:

What shape should agent-facing surfaces take so agents can work inside the
practice canon without losing technique source truth, owner boundaries,
validation, public safety, or return routes?

## Design Thesis

`aoa-techniques` should not give agents one giant instruction wall.

It should give them a navigable mesh:

- a root card that names repository identity, owner boundaries, and route
  modes
- top-level district cards that narrow source class and validation posture
- mechanic package cards that keep practice-motion work owner-routed
- technique trunk cards that protect published bundle meaning
- deep cards for high-risk generated, legacy, part-local, or agent-lane
  surfaces
- validation surfaces that make the route checkable
- generated companions that summarize the mesh without becoming the mesh

Agent guidance is not authority by volume. It is authority by placement,
proximity, owner fit, validation, and explicit return.

The root names the road system.
The nearest card narrows the lane.
The technique bundle keeps the move.
The validator checks the claim.
The closeout returns the work to the next reader.

## Design as Appearance

Agent guidance should appear as a readable practice-route network.

A healthy agent-facing layer has:

- a clear root `AGENTS.md`
- local `AGENTS.md` cards in durable districts
- a repeated card shape for low-context agents
- visible owner boundaries and route-away rules
- named source surfaces for technique meaning, mechanics, generated outputs,
  schemas, tests, and legacy
- negative boundaries that prevent authority drift
- validation and generated-freshness routes
- closeout expectations that name changed surfaces, skipped checks, remaining
  risk, and next owner route
- generated mesh companions that expose coverage without authoring meaning

Ritual, game, or AoA language is allowed when it makes recurring work more
memorable and bounded. It fails when it hides source truth, validation, public
safety, or owner review.

## Design as Anatomy

### Root card

The root `AGENTS.md` owns repository identity, owner boundaries, route modes,
GitHub landing workflow, broad validation posture, and closeout expectations.

It should not contain every local rule. Root law routes; local cards narrow.

### District cards

Top-level district cards own local source class, local risks, local source
surfaces, and local validation.

Examples include `docs/`, `techniques/`, `mechanics/`, `generated/`, `schemas/`,
`templates/`, `tests/`, `.agents/`, and `.github/`.

### Technique cards

Technique trunk cards protect published bundle meaning. They should distinguish
tree placement from frontmatter truth, and they should route agents back to
`TECHNIQUE.md` instead of making the card a second technique.

Bundle-local cards should be rare. Use them only when a surface has a genuine
local rule that cannot live cleanly in the bundle.

### Mechanic cards

Mechanic cards protect practice-motion surfaces around canon. They should name
active package surfaces, owner request or provenance routes, generated mirrors,
local validation, and stop-lines to sibling AoA owners.

They may shape candidate movement. They must not promote a candidate into canon
by proximity.

### Deep cards

Deep cards protect high-friction surfaces such as legacy, generated reports,
part-local scripts, manifests, schemas, or agent-lane exports.

They exist because proximity matters. The safest rule is often nearest to the
file that can be harmed.

### Source surfaces

Technique bundles, docs contracts, schemas, builders, validators, mechanics
packages, generated-source configs, and neighboring owner repos keep meaning.

`AGENTS.md` cards route agents to source truth. They do not become source truth
by repetition.

### Generated companions

Generated AGENTS mesh indexes and other compact read models help low-context
agents navigate.

They are mirrors and companions. They must point back to source surfaces,
remain reproducible, and avoid authoring new meaning.

## Design as Operation

A safe agent move follows a route before it touches content.

1. Read the root card.
2. Read the nearest local card for every touched path.
3. Read the owner source surfaces named by those cards.
4. Make the smallest change that preserves the owner boundary.
5. Run the narrowest relevant validation first.
6. Run broader gates when the change is release-facing, route-facing,
   generated, structural, or cross-owner.
7. Close out with changed surfaces, checks run, checks skipped, remaining risk,
   and next owner route.

Agency becomes stronger when it can stop, explain itself, and hand off cleanly.

## Design as Authority

Agent guidance has limited authority.

It may:

- route work
- name local risks
- name owner surfaces
- require reading order
- require validation
- set closeout shape
- prevent common unsafe claims

It must not:

- override technique bundle meaning
- override source docs, schemas, builders, validators, or owner repos
- claim hidden autonomy
- claim live runtime state unless the runtime owner proves it
- claim skill, eval, routing, KAG, memory, playbook, role, stats, or ToS
  authority
- turn generated surfaces into authority
- convert AoA vocabulary into permission
- bury semantic changes under "docs-only" wording

The agent layer is a road law. It is not the canon, proof system, skill runtime,
memory layer, or routing engine.

## Canonical Card Shape

Every durable `AGENTS.md` card that adopts the canonical shape should begin
from this form:

```markdown
# AGENTS.md

## Applies to

## Role

## Read before editing

## Boundaries

## Validation

## Closeout
```

`Applies to` names scope.
`Role` names what the lane is for.
`Read before editing` gives the minimum route.
`Boundaries` prevents authority drift.
`Validation` turns action into checkable work.
`Closeout` preserves handoff memory.

Optional sections may be added when the lane needs them: `Purpose`, `Owner
lane`, `Route modes`, `Source Surfaces`, `Post-change route review`, `Editing
posture`, `Part evolution`, `Decision review`, `Generated companions`, or
local equivalents.

Optional sections should sharpen the route. They should not decorate it into
fog.

## Migration Posture

This repository already had many useful local cards before adopting the full
mesh design. The migration should be explicit:

- canonical cards follow the full shape and are enforced by shape validation
- migration cards remain registered and visible in the generated mesh while
  they are normalized in later waves
- new durable districts should not enter as silent rooms
- a migration card should not be treated as exempt from source truth or owner
  boundaries

The correct end state is canonical shape everywhere useful, not permanent
legacy-card drift.

## Design Principles

### 1. Locality before abstraction

The nearest relevant card should carry the local rule. Root guidance should
stay readable.

### 2. Routes before commands

A good card says which surface owns the claim, which route to follow, which
check to run, and where to hand off.

### 3. Source before instruction

Instructions guide. Source surfaces own meaning. When they conflict, stop and
route to the owner.

### 4. Negative boundaries are design

A clear "do not" prevents silent authority transfer.

### 5. Validation is the handshake with reality

Every substantial card should name the smallest useful validation path. Broad
gates matter, but local checks keep work from becoming theatrical.

### 6. Closeout is memory

A closeout is the next agent's doorway: what changed, what was checked, what
was skipped, what remains risky, and where work resumes.

### 7. Generated companions are companions

Machine-readable summaries are useful when they compress and route. They become
dangerous when they author meaning or hide their source.

### 8. Portability comes from repeated shape

A portable agent layer is not copied text. It is copied discipline: same card
shape, same owner logic, same validation posture, same closeout memory, adapted
to local truth.

### 9. Agency must remain returnable

An agent may act, propose, validate, route, summarize, and hand off. Durable
action should preserve review, rollback, evidence, and a way back to the owner
surface.
