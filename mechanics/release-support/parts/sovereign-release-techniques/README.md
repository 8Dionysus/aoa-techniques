# Sovereign Release Techniques

Version: 1.0.0

## Purpose

This part defines reusable practice for release ritual, decision sealing,
rollback rehearsal, and post-release watch.

It belongs to the local release-support mechanic as practice pressure, not as
release approval, public claim proof, or policy precedent.

## Owns

- release practice notes
- rollback patterns
- watch practices

## Must Not Do

- seal authority
- operator substitution
- policy precedent
- public claim proof
- runtime rollback execution

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
atomic release-support move, route the artifact to the true owner, survive
rollback rehearsal, and fail closed when authority is missing.

## Provenance

This part preserves the pre-split `SOVEREIGN_RELEASE_TECHNIQUES.md` surface.
See [Provenance](../../PROVENANCE.md).
