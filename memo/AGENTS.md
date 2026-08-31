# AGENTS.md

## Applies to

This card applies to `memo/`.

## Role

`memo/` is the aoa-techniques local memory port. It holds technique-canon memory
candidates, receipts, exports, and local notes before reviewed landing in
`aoa-memo`.

## Read before editing

1. Root `AGENTS.md`
2. `CHARTER.md`
3. `DESIGN.md`
4. `PORT.yaml`
5. `aoa-memo` memory operation contracts when a candidate should move centrally
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

Use this port for `write_candidate_only` work. Keep technique truth in
`TECHNIQUE.md`, contracts, and generated-source owners; use this port for
recall, candidate memory, receipts, and reviewed handoff.

Do not promote local candidates, generated indexes, or MCP landing plans into
durable memory without `aoa-memo` reviewed intake.

Use `PORT.yaml` for the local port contract and `INDEX.md` / `index.min.json`
as generated read models. Use `candidates/` for proposed memory, `receipts/`
for review or handoff traces, `exports/` for packets meant for `aoa-memo`, and
`local/` for technique-layer memory that stays local for now.

## Candidate Route

Use the explicit `aoa-memo` candidate-intake owner with reviewed evidence refs; this card does not embed a launcher or infer a host checkout.
Validate the emitted candidate through the owner contract before any export or landing decision.

## Reviewed Landing Route

After review, route exports to the `aoa-memo` owner for intake and landing review.
A landing plan is an access-plane check; durable memory remains owner-reviewed and is not authored by this local port.

## Validation

Select the narrowest owner route: `source-fast` for the local owner; add `generated` for derived indexes and `advisory` only for non-blocking boundaries. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report candidate path, evidence refs, validation result, and whether the item
stayed local, was exported for reviewed intake, or was landed in `aoa-memo`.
