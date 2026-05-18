# Incoming Evidence-Only Closeout

Status: accepted
Date: 2026-05-18

## Context

`incoming/` kept six public-safe donor packets after their first-pass landing
queues were exhausted. The packets still used active-wave wording, and three
packet roots still carried `candidate_bundles/**` seed drafts for techniques
that had already landed as canonical bundles.

That made the quarantine look like a live drafting lane and duplicated
`techniques/**/TECHNIQUE.md` meaning.

## Options considered

1. Keep the packet roots as active staging surfaces.
2. Move all packet material into Distillation legacy.
3. Keep the packet roots under `incoming/` as evidence-only closeout packets,
   remove duplicate seed bundles for already landed techniques, and close all
   non-landed tails instead of leaving packet-local debt.

## Decision

Keep current packet roots under `incoming/` as evidence-only provenance and
closed-verdict surfaces.

Remove packet-local `candidate_bundles/**` seed drafts once their corresponding
techniques have landed. Former narrowing and incubation tails become
`closed-no-import` records with closeout memos. Any future attempt must start as
a new Distillation intake with fresh evidence instead of reusing old seed
drafts or packet-local queues.

## Rationale

`incoming/` is still the right place for quarantine packet evidence: it keeps
donor-wave accounting close to the original packet and avoids turning
Distillation legacy into a second active intake tree.

The duplicate seed bundles were the wrong surviving surface. Landed technique
meaning belongs in `techniques/**/TECHNIQUE.md`; a remaining packet should
point to landed bundles, closeout memos, or explicit exclusions without
pretending a seed bundle or live backlog is still present.

## Consequences

- `incoming/` becomes lighter and no longer visually competes with canon.
- Non-landed tails are closed: six former narrowing/incubation items now use
  `closed-no-import`, and explicit exclusions remain closed.
- Future work requires a new Distillation intake with fresh evidence and
  operator approval, not a packet-local resume lane.
- Historical seed-draft phrasing is no longer retained as separate packet-local
  files after landing; the canonical bundle and packet docs preserve the public
  route instead.

## Source surfaces

- `incoming/AGENTS.md`
- `incoming/README.md`
- `incoming/*/README.md`
- `incoming/*/docs/*CLOSEOUT_MEMO.md`
- `incoming/*/support/registry.json`
- `mechanics/distillation/PROVENANCE.md`

## Follow-up route

Start a new candidate only when fresh public evidence can name one atomic move,
likely domain/kind, owner boundary, and stop line. Use Distillation and the
normal technique authoring route before creating any new bundle. Do not revive
old packet-local queues.

## Verification

Validate the resulting route with:

```bash
python -m unittest tests.test_incoming_topology
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
git diff --check
```
