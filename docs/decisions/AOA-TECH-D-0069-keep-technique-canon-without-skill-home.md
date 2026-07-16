# Keep The Technique Canon Without A Skill Home

Status: accepted
Date: 2026-07-16

## Index Metadata

- Decision ID: AOA-TECH-D-0069
- Original date: 2026-07-16
- Surface classes: agent route, repository topology, owner boundary
- Technique axes: owner boundary, execution shape
- Mechanic parents: method-growth
- Guard families: owner boundary, prompt visibility, script topology, generated/read-model
- Posture: accepted no-home boundary

## Context

`aoa-techniques` carried 25 shared AoA skill bundles under `.agents/skills/`.
They were copied companions rather than repository-owned capabilities. Ten of
those bundles competed in the repository's initial agent prompt, and six
copied helper scripts were described by the local script inventory as if they
were active `aoa-techniques` organs.

That topology contradicted the current owner contract. This repository owns
atomic, public, reusable technique truth. Stateful workflows belong to
`aoa-skills`, recurring choreography belongs to `aoa-playbooks`, and routing
policy belongs to `aoa-routing`. A copied bundle can still look locally useful
while obscuring those boundaries, consuming prompt budget, and making a
projection appear to be owner truth.

## Options considered

1. Keep the 25 copied bundles and document them as advisory companions.
2. Replace them with a broad `aoa-techniques` search, selection, adaptation,
   validation, retry, and publication skill.
3. Remove the copied projection and keep no repository-local skill home until
   one repo-specific capability passes an explicit admission boundary.

## Decision

Choose option 3. `aoa-techniques` has no top-level `skills/` home and no
`.agents/skills/` projection while it owns no admitted repository-local skill.
Do not create an empty home port. Shared AoA bundles are supplied by host or
user-profile projections outside this repository.

Technique discovery and use start from authored route cards, indexes, and
`TECHNIQUE.md` bundles. Generated readers and KAG indexes may help discovery,
but they remain derived source-returning surfaces rather than skill truth.

A future repository-local bundle is admissible only when one concrete
capability has a distinct trigger, input/output contract, independent
composition value, bounded failure modes, and repeatable benefit in manual
positive, negative, no-skill, coexistence, and held-out trials. Technique-side
Method-growth and AOA-T-0102 may emit a proposal handoff to a receiving owner;
proposal, acceptance, activation, and projection remain separate events.

This decision supersedes AOA-TECH-D-0068 only where that record allowed copied
skill-local helpers to remain as active advisory script surfaces. The broader
script-inventory decision remains current.

## Rationale

Manual prompt inspection showed the copied bundles were agent-visible even
though this repository did not own them. After removing the projection, a
clean agent could still locate a requested technique, return to its authored
source and boundary, and avoid treating generated readers or tests as
authority. A separate negative trial correctly rejected a proposed broad
repository skill because its trigger, workflow owner, and verification
contract were not independently established.

These observations support removing interference, not claiming universal
no-skill superiority. The no-home posture is deliberately reversible when a
real repo-specific capability proves additive value.

## Consequences

- Remove all 25 copied bundles and their prompt-visible metadata.
- Remove six copied helper scripts from the local script topology, smoke tests,
  and inventory.
- Rebuild the AGENTS mesh and repo-local KAG projections without deleted paths
  as current artifacts; KAG event history may preserve their removal as
  provenance.
- Keep shared skill visibility in host or user-profile projections owned
  outside `aoa-techniques`.
- Do not add a permanent skill validator merely to enforce an empty directory;
  current route, inventory, mesh, and source-return checks cover the surviving
  owner surfaces.
- Revisit the boundary if repeated real tasks produce a repo-specific candidate
  that passes the stated manual admission trials.

## Source surfaces

- `AGENTS.md`
- `README.md`
- `CHARTER.md`
- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `.agents/AGENTS.md`
- `mechanics/method-growth/README.md`
- `mechanics/method-growth/TECHNIQUE_TO_SKILL_HANDOFF.md`
- `techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md`
- `docs/validation/SCRIPT_TOPOLOGY.md`
- `config/agents_mesh.json`

## Follow-up route

Revisit only when real `aoa-techniques` work yields a stable repository-local
trigger and contract. Route a technique-derived proposal through Method-growth
and AOA-T-0102; route admission, activation, versioning, and shared projection
to the receiving skill owner.

## Verification

- `source-fast` checks current owner routes, semantic AGENTS guidance, script
  inventory coverage, and the absence of stale active paths.
- `generated` checks decision indexes, AGENTS mesh, and repo-local KAG parity.
- `release` checks the public repository after the broad projection removal.
- Manual prompt inspection and positive, negative, no-skill, coexistence, and
  held-out trials remain the admission authority for any future skill candidate.
