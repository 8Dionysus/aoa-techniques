# Canonical Retro Audit Part

Status: accepted
Date: 2026-05-14

## Context

After the remaining promotion queue was reduced to `9` rows, the next risk was
not another promotion sprint. The risk was that earlier canonical rows might
hide stale metadata or contradictory readiness notes.

Audit already owned promoted-corpus readiness, external evidence sprinting, and
searched-lane memory. It did not yet have a bounded home for rechecking
already-canonical rows without turning that recheck into proof doctrine or an
automatic demotion mechanism.

## Options

- Put retro-audit notes into the promotion-readiness matrix.
- Treat the check as a one-off chat result and leave no durable artifact.
- Add a separate Audit part for canonical retro-checks and keep bundle-local
  notes as the authority for any real status change.

## Decision

Add `mechanics/audit/parts/canonical-retro-audit/README.md`.

The part records corpus-wide internal coherence checks over canonical rows:
status, maturity, validation strength, evidence declarations, and
canonical-readiness verdict language.

It does not browse every external source by default, issue proof verdicts, or
demote techniques from Audit pressure. If a future pass finds a real
contradiction, the affected bundle-local notes and `TECHNIQUE.md` move first.

## Consequences

Future agents have a durable route for asking whether the canonical corpus still
lines up with its own review contract.

The first pass found no reopen candidates and no status downgrades. It did find
five stale metadata fields, which were corrected in the owning technique
frontmatter without changing canonical-readiness verdicts.

The tradeoff is one more active Audit part, so `PARTS.md`, `PROVENANCE.md`,
entrypoint docs, and topology tests must name the part explicitly.
