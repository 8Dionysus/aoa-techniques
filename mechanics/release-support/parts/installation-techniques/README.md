# Installation Techniques

Version: 1.0.0

## Purpose

This part defines reusable practice for staged landing, migration safety, smoke
gates, rollback, and replay audits.

It belongs to the local release-support mechanic as practice pressure, not as
release authority. It can help shape a future technique bundle only after the
practice becomes atomic, public-safe, and reviewable.

## Owns

- technique notes
- safe patterns
- repeatable practices

## Must Not Do

- source truth
- runtime authority
- release approval
- uncited doctrine
- operator substitution

## Flow

```text
owner-local artifact
  -> validation
  -> operator review
  -> activation or denial
```

## Authority Route

AoA release-support law, public claim gates, and federation release protocol
belong to `Agents-of-Abyss:mechanics/release-support/`. Tree-of-Sophia
no-direct-write boundary lives in
`Tree-of-Sophia:docs/NO_DIRECT_EXPERIENCE_INSTALL_WRITE.md`.

This `aoa-techniques` part only defines owner-local practice behavior and
consumes those upstream gates.

## Exit Signal

This surface is ready to become a technique candidate only when it can name one
atomic installation move, route the artifact to the true owner, survive replay,
and fail closed when authority is missing.

## Provenance

This part preserves the pre-split `INSTALLATION_TECHNIQUES.md` surface. See
[Provenance](../../PROVENANCE.md).
