# AGENTS Mesh Protocol

## Purpose

The AGENTS mesh makes agent guidance local without letting local cards steal
authority from technique bundles, source docs, schemas, generated-source
configs, mechanics packages, or neighboring owner repositories.

`DESIGN.AGENTS.md` describes the desired form of the agent-facing layer. This
protocol defines the current checkable mesh contract for `aoa-techniques`.

## Contract

Every durable district that agents may edit should have a local `AGENTS.md` or
an explicit migration/exemption posture in `config/agents_mesh.json`.

Canonical cards include:

- `## Applies to`
- `## Role`
- `## Read before editing`
- `## Boundaries`
- `## Validation`
- `## Closeout`

Cards must be readable Markdown, not minified instruction blobs. They should
make the next safe action obvious to a low-context agent.

## Precedence

1. Root `AGENTS.md` owns repository identity, route modes, owner boundaries,
   GitHub landing, and broad validation posture.
2. Nearer `AGENTS.md` files own local file posture, local checks, and local
   risks.
3. Technique bundles, source docs, schemas, builders, validators, mechanics
   packages, and owner repositories own their stronger claims.
4. Generated mirrors reflect source contracts and do not author meaning.
5. `DESIGN.AGENTS.md` shapes the agent-surface form; it does not replace the
   root card, local cards, this protocol, config, validators, or generated
   mirrors.

## Growth Rule

When a durable directory appears, choose one of these actions in the same
change:

1. add a local canonical `AGENTS.md`;
2. register the path under the mesh exemption posture with a reason;
3. prove it is temporary and should not be committed as a durable district.

Reopening migration status is a temporary exception. It requires an explicit
decision or review note and should name the cleanup route before landing.

New root or docs-root surfaces should also pass through
`docs/ROOT_SURFACE_LAW.md`.

## Migration Rule

The current mesh is fully canonical. `config/agents_mesh.json` keeps
`migration_allowed` false so noncanonical cards fail the mesh lane instead of
quietly becoming background debt.

Migration status is not a permission to ignore owner truth. It only means the
card shape has not yet been fully lifted into the canonical form, and it should
exist only as a short-lived, reviewed exception.

## Must Not Claim

The AGENTS mesh must not claim hidden autonomy, memory sovereignty, live runtime
authority, proof sovereignty, skill execution authority, routing dispatch,
ToS canon authority, or owner-local acceptance.

It gives agents safer roads. It does not become the technique canon.

## Check Route

Use `docs/guardrails/AGENTS.md` for the current command lane.
