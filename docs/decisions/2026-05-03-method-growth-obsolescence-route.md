# Method-Growth Obsolescence Route

Status: accepted

Date: 2026-05-03

## Context

Method-growth already carried an `obsolescence` part. Its source signal was
that supersession and obsolescence must be explicit instead of silently deleting
owner evidence. AoA center pruning reinforces the same boundary: a route can
name why a practice should stop, reanchor, merge, defer, or drop, but it does
not erase owner history or write owner-local retirement truth.

The current repository direction requires mechanics-to-canon movement to
extract one atomic practice at a time. Promoting deletion or deprecation itself
would blur technique canon, owner-local status, proof, memory, skill, routing,
and runtime authority.

## Options

- Keep all obsolescence material mechanics-only.
- Promote actual deletion, retirement, or deprecation as a broad technique.
- Extract only the owner-aware obsolescence route packet and leave owner-local
  status changes outside the technique.

## Decision

Promote one atomic technique:
`AOA-T-0104 superseded-practice-obsolescence-route`.

The technique owns one handoff packet: route an adopted or shadowed practice
toward supersession, merge, reanchor, defer, drop, or deprecation review while
preserving current stage, owner receipt target, reason, source evidence,
rollback or quarantine posture, and retained lesson.

It does not delete, deprecate, erase evidence, issue proof, write memory truth,
activate a skill, change routing, mutate runtime behavior, or mark owner-local
retirement.

## Consequences

- `obsolescence` now has a real bridge from mechanics into canon without
  treating cleanup as erasure.
- The new bundle can be used by external readers without deploying OS Abyss.
- `aoa-techniques` gains one more promoted bundle, moving the working corpus to
  `104` bundles: `25` canonical and `79` promoted.
- Promotion-readiness and roadmap counters must track the new working corpus
  while the released version remains `v0.4.2`.
- Method-growth extraction now has separate atoms for adoption gate, skill
  proposal handoff, retention review, and obsolescence route.

## Verification

The bundle is checked through normal technique validation and generated parity:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```
