# Diagnosis-Repair Direct Relation Repair

Source packet: [Technique Reform Ingress](../README.md)

Wave packet:
[Selector Relation Wave E Continuity Recovery Review](selector-relation-wave-e-continuity-recovery-review.md)

Touched bundle relation:
[AOA-T-0082 repair-shape-from-diagnosis](../../../../../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md)

Stable diagnosis-packet target:
[AOA-T-0081 diagnosis-from-reviewed-evidence](../../../../../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md)

Status: accepted direct relation repair.

## Verdict

Accept `AOA-T-0082 requires AOA-T-0081`.

`AOA-T-0082` owns the repair-shape move after diagnosis. Its inputs, core
procedure, validation, and adjacent-technique paragraph all say the move starts
from a reviewed diagnosis packet, not from raw friction, aspiration, or a broad
self-improvement request.

`AOA-T-0081` owns the local diagnosis-packet contract: reviewed friction
evidence becomes symptoms, probable causes, owner hints, and explicit unknowns
without mutation. That makes `requires AOA-T-0081` more accurate than
`complements AOA-T-0081` for this one downstream relation.

The repair is intentionally narrow. It does not strengthen
`AOA-T-0083` to `requires AOA-T-0082`, because checkpoint-bound self-repair can
wrap any bounded repair shape that already exists. It also does not strengthen
`AOA-T-0081` to require `AOA-T-0080`, because drift taxonomy is optional input
to diagnosis rather than the only path into it.

## Decision Table

| bundle | old edge | new edge | reason |
|---|---|---|---|
| `AOA-T-0082` | `complements AOA-T-0081` | `requires AOA-T-0081` | repair-shape selection explicitly starts from one reviewed diagnosis packet and `AOA-T-0081` owns that packet contract |

## Holds

| bundle | held relation posture | why |
|---|---|---|
| `AOA-T-0080` | keep `complements AOA-T-0081` and `complements AOA-T-0076` | taxonomy helps diagnosis and owner hints without becoming required owner routing or probable-cause analysis |
| `AOA-T-0081` | keep `complements AOA-T-0080` | drift taxonomy is useful input, but diagnosis can start from reviewed symptoms directly |
| `AOA-T-0081` | keep `complements AOA-T-0082` | diagnosis often feeds repair shaping, but a diagnosis packet can remain read-only evidence |
| `AOA-T-0082` | keep `complements AOA-T-0083` | repair-shape selection does not own checkpoint posture, approval posture, rollback, or iteration limits |
| `AOA-T-0083` | keep `complements AOA-T-0082` and `complements AOA-T-0028` | checkpoint-bound repair needs a bounded repair shape, but that shape can come from equivalent reviewed planning; confirmation gating is a neighboring approval seam |

## What Changed

- `AOA-T-0082` frontmatter now has a direct
  `requires AOA-T-0081` relation.
- Generated relation consumers should be rebuilt from source after this repair:
  catalog, selection surfaces, topology scout, KAG export, and release-check
  companions that derive from catalog or frontmatter.

## What Did Not Change

- no new relation types;
- no relation schema migration;
- no relation rationale field;
- no generated graph behavior, traversal, ranking, or selector engine;
- no status, `domain`, `kind`, maturity, validation-strength, evidence, owner,
  or path changes;
- no canonical promotion;
- no empirical small-agent proof or `aoa-evals` verdict.

## Safety Read

This repair strengthens only one object dependency:

- repair-shape selection needs diagnosis first;
- the local diagnosis-packet contract lives in `AOA-T-0081`.

It does not say taxonomy is mandatory, repair is approved, checkpoint posture
is implied, rollback exists automatically, or diagnosis-repair owns system
recovery, role law, proof verdicts, memory truth, runtime behavior, or
playbook rollout.

## Stop Lines

- Do not use this repair as precedent for adding future sequence relation
  names to frontmatter.
- Do not strengthen `AOA-T-0083` to `requires AOA-T-0082` from this packet.
- Do not strengthen `AOA-T-0081` to `requires AOA-T-0080` from this packet.
- Do not collapse taxonomy, diagnosis, repair shape, and checkpoint-bound
  repair into one recovery mega-technique.
- Do not hand-edit generated surfaces. Rebuild them from source.

## Next Honest Move

Rebuild generated relation consumers, validate the repository, and land
Wave E.

After Wave E lands, continue the temporary plan with Wave F over the remaining
instruction capability tail, media-ingest, and history-artifacts shelves.
