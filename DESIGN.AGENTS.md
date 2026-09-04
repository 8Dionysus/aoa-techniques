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

- root card for repository identity, owner boundaries, and route modes
- district cards for source class and validation posture
- mechanic cards for practice-motion work
- technique trunk cards for published bundle meaning
- deep cards for generated, legacy, part-local, or agent-lane risk
- validators and generated companions that check and summarize the mesh

Agent guidance is not authority by volume. It is authority by placement,
proximity, owner fit, validation, and explicit return.

Root names the road system. The nearest card narrows the lane. The technique
bundle keeps the move. The validator checks the claim. Closeout returns the
work to the next reader.

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
- risk-based validation selection and an on-demand procedure route
- closeout expectations that name changed surfaces, skipped checks, remaining
  risk, and next owner route
- generated mesh companions that expose coverage without authoring meaning

Ritual, game, or AoA language is allowed when it makes recurring work more
memorable and bounded. It fails when it hides source truth, validation, public
safety, or owner review.

## Design as Anatomy

| Surface class | Role |
|---|---|
| Root card | repository identity, owner boundaries, route modes, validation selection, and closeout |
| District cards | local source class, local risks, source surfaces, and the nearest on-demand validation route |
| Technique cards | protection for bundle meaning and the split between tree placement and frontmatter truth |
| Mechanic cards | practice-motion routes, provenance, generated mirrors, and sibling-owner stop lines |
| Deep cards | high-friction generated, legacy, part-local, schema, manifest, or agent-lane surfaces |
| Generated companions | reproducible mesh summaries that point back to source cards |

The source surfaces still keep meaning: technique bundles, docs contracts,
schemas, builders, validators, mechanics packages, generated-source configs,
and neighboring owner repositories. Agent cards route to them; they do not
become source truth by repetition.

Executable procedure has the same placement rule. Active `AGENTS.md` cards
name the applicable evidence class or owner route after the touched surface is
known. Root `VALIDATION.md`, `config/validation_lanes.json`, the nearest focused
owner, and `docs/RELEASING.md` carry exact human or machine procedure. Copying
command batteries into inherited cards makes the mesh heavier without making
the command owner stronger.

## Design as Operation

A safe agent move follows a route before it touches content.

1. Read the root card and nearest local card for every touched path.
2. Read the owner source surfaces named by those cards.
3. Make the smallest change that preserves the owner boundary.
4. Run narrow validation first, then broader gates for release-facing,
   route-facing, generated, structural, or cross-owner changes.
5. Close out with changed surfaces, checks run, checks skipped, remaining risk,
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
mesh design. That migration has now been closed into canonical shape:

- canonical cards follow the full shape and are enforced by shape validation
- `config/agents_mesh.json` keeps `migration_allowed` false while the mesh is
  fully canonical
- new durable districts should not enter as silent rooms
- any future migration status must be an explicit temporary exception with a
  decision or review note, not background drift

The correct steady state is canonical shape everywhere useful, not permanent
legacy-card drift.

## Design Principles

1. Locality before abstraction: the nearest relevant card carries the local rule.
2. Routes before commands: a good card names owner, route, check, and handoff.
3. Source before instruction: when instruction and source conflict, stop and
   route to the owner.
4. Negative boundaries are design: a clear "do not" prevents silent authority
   transfer.
5. Validation is the handshake with reality: local checks keep broad gates honest.
6. Closeout is memory: say what changed, what was checked, what was skipped,
   what remains risky, and where work resumes.
7. Generated companions are companions: they compress and route, never author
   meaning.
8. Portability comes from repeated discipline, not copied text.
9. Agency must remain returnable: durable action preserves review, rollback,
   evidence, and a way back to the owner surface.
10. Human maps stay on demand: README explains the public canon, mechanic,
    contract, or usage route; AGENTS does not preload it unless the selected
    task needs that explanation.
