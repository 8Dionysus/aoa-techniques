# AGENTS.md

Guidance for coding agents and humans working under `techniques/instruction/`.

## Purpose

`instruction/` stores technique bundles whose primary placement question is how
agent-facing instruction, context, rule, mirror, fragment, layer, or profile
surfaces, or document-boundary surfaces, stay explicit, managed, reviewable,
and subordinate to their real source of truth.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current scope

Accepted pilot shelves:

- `instruction-surface/`: composes, distributes, mirrors, loads, fragments, or
  names agent-facing instruction/context surfaces while keeping source and
  target authority visible
- `docs-boundary/`: keeps document truth, entrypoint status, public-share
  artifacts, and decision rationale legible without making this trunk the
  owner of governance, approval, proof, runtime, or architecture-taxonomy
  authority

## Domain rules

Keep the instruction or document-boundary object explicit:

- what source, fragment, layer, target, mirror, profile, document role,
  status snapshot, public artifact, or decision note is being shaped
- what remains authored source versus derived or managed target
- what provenance, precedence, fan-out, or review boundary must stay visible
- what runtime, skill-acceptance, constitutional, generated-authority, or
  deployment detail is refused

Do not turn an instruction technique into AoA doctrine, skill marketplace
policy, runtime role law, generated context authority, hidden prompt control, or
private operator procedure.

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
