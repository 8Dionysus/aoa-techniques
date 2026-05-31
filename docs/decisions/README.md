# Decisions District

This district holds decision records explaining why a route, owner split,
placement, validator, or public contract was chosen in `aoa-techniques`.

Decision records explain why. Current source surfaces define what.

## District Law

Keep this district reviewable and labeled. A reader or agent should know
whether a surface is current law, evidence, historical receipt, transition
note, or compatibility reference before citing it.

Use [TEMPLATE](TEMPLATE.md) for new records. Use [AGENTS](AGENTS.md) for the
local editing and validation route.

## Current Surface Families

| Family | Typical records | Role |
|---|---|---|
| Root and docs topology | root source-of-truth, root legacy, root data, root Markdown slimming, docs surface guardrails | why public entry, docs-root, legacy, and root districts are placed where they are |
| Technique contracts | atom, topology, tree, kind remaps, template modernization | why reusable practice is shaped, classified, or constrained a certain way |
| Mechanics packages | active/legacy splits, package-card standards, mechanic-local artifacts | why mechanic packages own movement, provenance, parts, and local validation |
| Reform and review homes | scout inputs, reports, review packets, contract packets, scripts, tests | why evidence or helper surfaces moved to owner-local part homes |
| Agent and platform routes | GitHub landing, Spark lane home, Spark registry-backed scenarios, agent-surface mesh | why agent-facing, platform, and generated mesh surfaces are arranged as they are |

## Index Shape

Each decision owns:

- a canonical `Decision ID: AOA-TECH-D-####`;
- a full canonical-ID filename, for example
  `AOA-TECH-D-0001-*.md`;
- an `## Index Metadata` block naming original date, surface classes,
  technique axes, mechanic parents, guard families, and posture.

The lookup indexes under [indexes](indexes/README.md) are generated from that
metadata:

- [Decisions by canonical ID and number](indexes/by-number.md)
- [Decisions by date](indexes/by-date.md)
- [Decisions by surface class](indexes/by-surface.md)
- [Decisions by technique axis](indexes/by-technique-axis.md)
- [Decisions by mechanic parent](indexes/by-mechanic.md)
- [Decisions by validation or guard family](indexes/by-guard.md)

Use them in both directions:

- top down: repo route -> source class -> technique axis -> mechanic parent ->
  validation guard -> decision rationale;
- bottom up: changed source surface -> local route card or generated read model
  -> validator guard -> decision rationale -> stronger owner surface.

Regenerate the read models after decision metadata changes:

```bash
python scripts/generate_decision_indexes.py
```

Check generated parity before closeout:

```bash
python scripts/generate_decision_indexes.py --check
```

## Addressing

Full canonical-ID decision paths are the active source files:

- `docs/decisions/AOA-TECH-D-0001-*.md`
- `docs/decisions/AOA-TECH-D-0002-*.md`
- `docs/decisions/AOA-TECH-D-####-*.md`

Canonical IDs remain the stable handles. Previous date-prefixed paths are not
live files and are not preserved as a repository lookup layer.

## Record Shape

Decision records should use this standard shape:

- `Status`
- `Date`
- `Context`
- `Options considered`
- `Decision`
- `Rationale`
- `Consequences`
- `Source surfaces`
- `Follow-up route`
- `Verification`

Older records may use `Options` or `Validation`; keep new records closer to
the template unless a local reason requires a narrower shape.

## Must Not Claim

Decisions must not replace current source surfaces.

Do not use this district to absorb technique meaning, mechanic-local operating
truth, generated meaning, or sibling-owner authority.

## Promotion Path

A decision may influence current law only when a change names the surviving
canonical source surface, updates links, rebuilds generated mirrors when
needed, and runs the relevant validators.
