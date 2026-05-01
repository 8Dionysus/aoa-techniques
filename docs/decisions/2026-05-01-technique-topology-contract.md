# Technique Topology Contract

Date: 2026-05-01

## Status

Accepted

## Context

The repo now explicitly defines a technique as one atomic executable move. That
solves the size and execution-shape problem, but it does not by itself solve the
classification problem.

The current corpus uses `domain` and `kind` as authoritative frontmatter axes
and has a scout-only `family` seed. That was enough for the first public corpus,
but a corpus aiming toward `1000+` techniques and then beyond cannot rely on a
small set of broad domains. Agent techniques will cover coding, documentation,
tool use, media, dialogue, planning, observation, recovery, history, and many
other capability surfaces.

## Options

- Keep the current `domain + kind + tags` scheme and let categories evolve
  locally as the corpus grows.
- Immediately migrate schema and all bundles to a large new taxonomy.
- Record a topology contract now, keep current authoritative axes stable, and
  mark future axes as design contracts until they are proven through mechanics,
  distillation, generated reports, and validators.

## Decision

Add `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md` as the repo-owned topology guide.

The contract defines classification as faceted rather than a single tree:
`domain`, `kind`, `family`, `capability_class`, `substrate`,
`execution_profile`, `risk_posture`, and typed `relations` each answer a
different routing question.

Only `domain` and `kind` remain current authoritative frontmatter. `family`
remains scout-only. The other axes are design axes for the next classification
wave, not immediate schema requirements.

## Consequences

Future mechanics and distillation passes can classify candidates against the
intended topology without pretending the schema migration has already happened.

This creates a stronger path toward a large corpus while avoiding a premature
all-bundle migration. The tradeoff is that contributors now need to distinguish
current truth from design axes: generated scout surfaces and topology notes can
guide future work, but authored technique bundles and current validators still
own present corpus truth.
