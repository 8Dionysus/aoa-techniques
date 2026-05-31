# Method-Growth Pattern Adoption Gate

Status: accepted

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0028
- Original date: 2026-05-03
- Surface classes: mechanic package
- Technique axes: mechanic bridge, promotion
- Mechanic parents: method-growth
- Guard families: mechanic topology
- Posture: accepted

## Context

Method-growth already carried compact downstream adoption surfaces from the
v0.7 wave. The `pattern-adoption` part said that adoption must be explicit, that
local owner consent is required, and that durable behavior change needs
evidence, rollback, and retention. That was real mechanics signal, but it was
not yet a technique bundle.

The current repository direction now requires mechanics-to-canon movement to
extract only one atomic practice at a time. A full adoption lifecycle would be
too broad for one technique because it includes request, readiness, shadow,
decision, activation, retention, owner acceptance, and possible sibling
handoffs.

## Options

- Keep all pattern-adoption material mechanics-only until a later, broader
  Method-growth pass.
- Promote the whole pattern-adoption lifecycle as one technique.
- Extract only the local gate before adoption and leave lifecycle movement in
  Method-growth.

## Decision

Promote one atomic technique:
`AOA-T-0101 local-pattern-adoption-gate`.

The technique owns one guardrail: before one shared pattern becomes durable
local behavior, the adopting surface must name local owner consent,
compatibility evidence, rollback or quarantine, and retention watch.

Method-growth keeps the larger lifecycle route around request, readiness,
shadow, decision, activation, retention pressure, technique-to-skill handoff,
retention checks, and obsolescence.

## Consequences

- `pattern-adoption` now has a real bridge from mechanics into canon without
  pretending the whole mechanic became a technique.
- The new bundle can be used by external readers without deploying OS Abyss.
- `aoa-techniques` gains one more promoted bundle, moving the working corpus to
  `101` bundles: `25` canonical and `76` promoted.
- Promotion-readiness and roadmap counters must track the new working corpus
  while the released version remains `v0.4.2`.
- Future Method-growth passes should treat retention, obsolescence, and
  technique-to-skill handoff the same way: extract only one atomic practice when
  the atom survives the contract.

## Verification

The bundle is checked through normal technique validation and generated parity:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```
