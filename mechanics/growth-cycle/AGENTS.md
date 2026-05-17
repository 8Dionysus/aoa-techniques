# AGENTS.md

## Applies to

This card applies to `mechanics/growth-cycle/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This package owns the `aoa-techniques` side of Growth Cycle: technique-layer
harvest posture, feat-reader reflection, questbook followthrough, and reviewed
closeout incubation.

It does not own AoA Growth Cycle stage law, hooks, executable cycle skills,
proof verdicts, memory canon, role progression, runtime exports, or playbook
choreography.

## Read before editing

1. Root `AGENTS.md`.
2. `mechanics/AGENTS.md`.
3. `mechanics/growth-cycle/README.md`.
4. `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, and the touched part README.
5. `mechanics/REQUEST_RECEIPTS.md` only when naming AoA center-side pressure.

## Boundaries

- Keep Growth Cycle here technique-layered: harvest, feat reflection, quest
  routing, and promotion-readiness incubation.
- Do not import `Agents-of-Abyss` stage law as local implementation authority.
- Do not treat feat cards, mastery wording, or quest pressure as technique
  canon.
- Do not create achievement authority, permanent rank, hidden automation,
  memory canon, proof verdict, or owner acceptance.
- If a stable reusable practice emerges, route it into `techniques/` through
  the normal technique review path.

## Validation

Use the root validation path after changes:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
