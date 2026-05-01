# Mechanics Law, Local Implementation, And Bridge Alignment

Status: accepted
Date: 2026-05-01

## Context

The first mechanics passes moved practice-motion material out of flat docs and
then proved the active/legacy pattern through Agon and Distillation. The
subsequent atom and topology contracts clarified that `aoa-techniques` should
grow toward a large corpus of small executable moves, not broad mini-skills.

That still left one ambiguity: a mechanics package can mention AoA-wide law,
local repository implementation, bridge behavior, donor evidence, and technique
candidate movement in the same surface. If those layers are not separated,
future agents can mistake local mechanics for higher law or turn a bridge into
an overloaded doctrine bundle.

## Decision

Add a mechanics-wide reading rule: larger mechanics should separate higher law,
local implementation, and bridges whenever that distinction helps the project.

- Higher law belongs to the owning AoA source that defines meaning, authority,
  and stop-lines.
- Local implementation belongs to the `aoa-techniques` mechanics package that
  explains how candidate movement, intake, review, registries, ledgers, or
  package shape work here.
- Bridges must stay narrow, provenance-linked, and explicit about both sides,
  input/output shape, and stop line.

Tie that split to the technique atom and topology contracts before any mechanics
candidate becomes a technique bundle.

## Consequences

Mechanics entrypoints now carry a stronger gate for future work without forcing
an immediate schema migration or a bulk rewrite of every package. Distillation
names this as the next alignment pass before structured registries, while Agon
records the split in its tracked package entrypoint before any promotion work.

The tradeoff is another explicit review layer. It is worth it because the
project needs many mechanics to connect across repos without confusing source
law, owner-local execution, and candidate bridges.
