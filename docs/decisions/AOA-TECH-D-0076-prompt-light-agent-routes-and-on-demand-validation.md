# Prompt-Light Agent Routes And On-Demand Validation

Status: accepted
Date: 2026-08-31

## Index Metadata

- Decision ID: AOA-TECH-D-0076
- Original date: 2026-08-31
- Surface classes: agent route, validation route, public documentation, release/GitHub
- Technique axes: agent mesh, command authority, public practice canon
- Mechanic parents: release-support
- Guard families: AGENTS/mesh, validation lane, README boundary, release/tooling, generated/read-model
- Posture: accepted prompt-light route law; partially supersedes only procedure placement in AOA-TECH-D-0043, AOA-TECH-D-0045, and AOA-TECH-D-0059

## Context

`aoa-techniques` already separates authored technique meaning from generated
readers and already gives blocking validation commands one machine owner in
`config/validation_lanes.json`. The root and local `AGENTS.md` mesh nevertheless
copies runnable commands, full validation batteries, broad README inventories,
and ordinary GitHub landing procedure into inherited context.

The duplication is especially costly here because the public practice canon has
many durable local cards. An agent touching one deep technique or mechanic path
inherits several cards before it has selected a surface, while exact procedure is
needed only after the surface and risk are known.

README files have a different role. Root README is the public and standalone
library entrance. Local README files explain mechanic cards, technique districts,
contracts, usage, provenance, or human navigation. Moving that material into
automatically inherited cards would increase prompt pressure and weaken the
public library rather than simplify it.

## Options considered

1. Keep executable procedure in every local card and shorten only prose.
2. Move README content into neighboring AGENTS cards and delete the README files.
3. Keep only one large root AGENTS card and remove local owner cards.
4. Keep inherited cards semantic and local, route procedure to an on-demand
   validation layer, and retain README files according to their human function.

## Decision

Choose option 4.

Root and nested `AGENTS.md` remain the automatically inherited route mesh. They
own applicable scope, the local practice or operation role, source and stronger
owner routes, public-safety and authority boundaries, risk-based validation
selection, and closeout claims. They do not store executable fences, runnable
command lines, complete inspection transcripts, universal README reading lists,
or the ordinary branch/PR/CI/merge sequence.

Add root `VALIDATION.md` as the on-demand human entrypoint. It maps focused
checks, lane entrypoints, generated parity, agent-mesh checks, mechanic-part
validation, release stabilization, checkpoint review, and the landing route.
It is a human map, not machine command authority.

`config/validation_lanes.json` remains the only blocking lane command store,
as established by AOA-TECH-D-0066. `scripts/ci_gate.py` remains the lane
executor. `scripts/release_check.py` remains the release stabilizer.
Part-local procedure belongs in the nearest part `VALIDATION.md`; current parts
that lack such a surface may use the exact focused owner named in the lane
manifest until a separately justified local validation card is added.

Root `README.md` remains the public and standalone first-reading surface. Local
README files remain human maps when they explain an existing technique family,
mechanic, part, contract, usage route, or provenance boundary. README is
task-conditional agent reading and never technique authority merely because of
its filename. No blanket README deletion or consolidation follows from this
decision.

Ordinary landing procedure lives in `docs/RELEASING.md` and root
`VALIDATION.md`. Root AGENTS retains only the route, evidence boundary, and
fail-closed stop-line when GitHub status or merge authority cannot be observed.

Generated catalogs, readers, capsules, KAG exports, mesh mirrors, decision
indexes, and mechanic projections remain derived. Change source or builder
inputs first and rebuild through the declared owner; do not hand-edit a
projection while changing the route mesh.

## Rationale

Technique meaning, public safety, provenance, portability, owner limits, and
return routes affect how every local action is interpreted, so they belong near
the path in inherited guidance. Exact commands and landing mechanics matter
after a path and evidence class have been selected, so an on-demand layer is the
more faithful placement.

Keeping local cards preserves proximity without forcing root to become a giant
instruction wall. Keeping README preserves the repository's second audience:
humans and external builders who reuse the public canon without deploying OS
Abyss.

## Consequences

- Inherited context becomes smaller without removing local owner boundaries.
- A validator must reject executable procedure, unconditional README
  inventories, empty procedural sections, and extraction residue in active
  cards.
- Exact command discoverability remains testable through the lane manifest,
  root and part validation maps, release guide, and focused owners.
- A green source-fast or generated lane remains distinct from release proof,
  GitHub CI, review, merge, runtime use, adoption, or sibling-owner acceptance.
- README disposition remains per-file and evidence-based; root README is kept by
  default.

## Supersession boundary

This decision preserves the owner and mesh meaning of AOA-TECH-D-0043,
AOA-TECH-D-0045, and AOA-TECH-D-0059. It supersedes only their placement of the
full landing or focused executable procedure in inherited `AGENTS.md` cards.
AOA-TECH-D-0066 remains the stronger command-authority decision.

## Source surfaces

- `AGENTS.md`
- `DESIGN.AGENTS.md`
- `DESIGN.md`
- `README.md`
- `VALIDATION.md`
- `docs/RELEASING.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `config/agents_mesh.json`
- `config/validation_lanes.json`
- `scripts/ci_gate.py`
- `scripts/release_check.py`
- `scripts/validate_agents_md_shape.py`
- `scripts/validate_agents_mesh.py`
- `scripts/validate_nested_agents.py`
- `tests/test_validation_command_authority.py`

## Follow-up route

Apply the route split to every tracked README and AGENTS surface before any
repository merge. Rebuild generated companions only from their owners. After
all owner repositories are complete, run the workspace census and cross-owner
review before the final dependency-ordered merge wave.

## Verification

Use decision-index parity, the AGENTS mesh and shape checks, nested route checks,
command-authority tests, source-fast, generated parity when projections change,
and the release lane through root `VALIDATION.md`. These local results do not
claim external CI, review, merge, adoption, runtime use, or owner acceptance.
