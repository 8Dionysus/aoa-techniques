# `aoa-techniques` Validation Routes

This is the on-demand human map for repository validation. Blocking lane
membership and command order remain owned by `config/validation_lanes.json`.
`scripts/ci_gate.py` executes lane modes and `scripts/release_check.py`
stabilizes the release lane; this file does not duplicate either authority.

A green local route proves only its declared repository contract. It does not
prove technique adoption, runtime use, eval verdicts, sibling-owner acceptance,
GitHub CI, review, merge, publication, or release availability.

## Lane entrypoints

Select the narrowest route justified by the changed surface.

| Lane | Entry | Use for |
| --- | --- | --- |
| `source-fast` | `python scripts/ci_gate.py --mode source-fast` | default authored source, route, topology, local KAG/stats, and technique-contract checks |
| `generated` | `python scripts/ci_gate.py --mode generated` | generated catalogs, readers, capsules, KAG export, decision indexes, mesh mirrors, and other declared projections |
| `mechanics/part-local` | `python scripts/ci_gate.py --mode mechanics-part-local` | current mechanic-part builders, validators, fixtures, and focused tests |
| `release` | `python scripts/release_check.py` | release-visible stabilization and the complete manifest-owned release route |
| `nightly` | `python scripts/ci_gate.py --mode nightly` | moving-main source, generated, and mechanic drift |
| `advisory` | `python scripts/ci_gate.py --mode advisory` | non-blocking export, runtime, eval, and security boundary inventory |

`source-fast` is the ordinary growth gate. Add `generated` when a declared
projection may change. Use `release` only for publication or broad
release-visible posture. Unknown ownership or uncertain generated impact is a
reason to inspect the manifest and owner source, not to invent a new sequence
in an AGENTS card.

## Focused owner routes

- technique bundle: validate the target `TECHNIQUE.md`, its checks, examples,
  notes, and source contract before broader lanes;
- AGENTS mesh: use the shape, mesh, mesh-builder check, generated-mesh, and
  nested-card owners recorded in the lane manifest and validator inventory;
- decision rationale: use the canonical decision-index builder in check mode;
- mechanic part: use its source packet and the exact builder, validator, or
  focused test discovered by the `mechanics/part-local` route;
- local KAG or stats port: use the owner-local validator and preserve the pinned
  stronger-owner boundary;
- GitHub or release surface: use `docs/RELEASING.md`, this map, and the workflow
  contract without treating workflow execution as already observed.

Exact focused commands that are not lane members stay with the corresponding
builder, validator, test inventory, or mechanic part. Do not copy them into
multiple inherited cards.

## Generated and source boundary

Change `TECHNIQUE.md`, authored docs, config, mechanic source packets, schemas,
or builder inputs first. Run the declared builder or lane in check/write mode as
owned by that source, inspect the diff, and keep generated/read-model outputs
weaker than their sources. Never hand-edit a projection to satisfy parity.

## Landing route

Branch, PR, required-check, merge-method, tagging, and release-note procedure is
owned by `docs/RELEASING.md`. Root AGENTS only routes there and keeps the
fail-closed stop-line. If GitHub status, review, or merge authority cannot be
observed, stop and report the missing evidence instead of inferring success.

## Evidence and closeout

Report the exact lane or focused owner run, its result, generated paths rebuilt,
skipped routes, external owner blockers, and the strongest claim the evidence
supports. Keep local validation, GitHub CI, review, merge, publication, runtime
use, adoption, and owner acceptance as separate claims.
