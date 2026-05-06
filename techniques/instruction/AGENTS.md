# AGENTS.md

Guidance for coding agents and humans working under `techniques/instruction/`.

## Purpose

`instruction/` stores technique bundles whose primary placement question is how
agent-facing instruction, context, rule, mirror, fragment, layer, profile,
document-boundary, capability-registry, capability-boundary, or
skill-discovery surfaces stay explicit, managed, reviewable, and subordinate to
their real source of truth.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `instruction-surface/`: composes, distributes, mirrors, loads, fragments, or
  names agent-facing instruction/context surfaces while keeping source and
  target authority visible
- `docs-boundary/`: keeps document truth, entrypoint status, public-share
  artifacts, and decision rationale legible without making this trunk the
  owner of governance, approval, proof, runtime, or architecture-taxonomy
  authority
- `capability-registry/`: keeps capability specs, registry-facing entries, and
  lookup contracts legible without making this trunk the owner of registry
  product doctrine, ranking, marketplace curation, trust policy, graph
  semantics, runtime resolution, skill acceptance, or agent-role authority
- `capability-boundary/`: keeps skill-command boundaries, primary source
  priority, and recommendation/actionability splits legible without making
  this trunk the owner of marketplace curation, upstream health validation,
  routing policy, KAG graph semantics, runtime law, host inventory, command
  product design, shell doctrine, registry product doctrine, or agent-role
  authority
- `skill-discovery/`: keeps curated skill discovery and pre-surface upstream
  source readiness legible without making this trunk the owner of installer
  behavior, sync substrate, registry governance, trust scoring, security
  scanning, generic monitoring, routing policy, runtime law, or agent-role
  authority

## Trunk Rules

Keep the instruction, document-boundary, capability-registry,
capability-boundary, or skill-discovery object explicit:

- what source, fragment, layer, target, mirror, profile, document role,
  status snapshot, public artifact, decision note, capability spec,
  registry-facing entry, discovery query, skill-command split, primary source
  priority, recommendation/actionability boundary, curated skill discovery, or
  pre-surface upstream source readiness is being shaped
- what remains authored source versus derived or managed target
- what provenance, precedence, fan-out, or review boundary must stay visible
- what runtime, skill-acceptance, constitutional, generated-authority, or
  deployment detail is refused

Do not turn an instruction technique into AoA doctrine, skill marketplace
policy, upstream health policy, sync substrate, registry governance, trust
scoring, security scanning, generic monitoring, routing law, generated context
authority, runtime role law, hidden prompt control, or private operator
procedure.

## Boundary

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing instruction techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.
