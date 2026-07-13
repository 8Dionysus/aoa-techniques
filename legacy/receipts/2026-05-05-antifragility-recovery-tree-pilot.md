# Antifragility-Recovery Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Scope

This receipt preserves the fifteenth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/antifragility-recovery-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0097` | `techniques/system-recovery/degrade-reground-recover/` | `techniques/recovery/antifragility-recovery/degrade-reground-recover/` |
| `AOA-T-0099` | `techniques/system-recovery/isolated-service-stop-on-shared-substrate/` | `techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/` |
| `AOA-T-0100` | `techniques/system-recovery/stress-receipt-reground-closeout/` | `techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/` |
| `AOA-T-0098` | `techniques/validation-patterns/receipt-first-failure-analysis/` | `techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/` |

## Preservation Rule

Active technique bundles moved directly from old authored homes to new authored
homes. They did not pass through root `legacy/`.

Root legacy preserves only this migration accounting.

## Invariants

- Keep bundle IDs unchanged.
- Keep `domain`, `kind`, `status`, owners, evidence, relations, checklists,
  examples, notes, maturity, validation-strength metadata, and public-safety
  posture unchanged.
- Preserve `AOA-T-0098` as `domain: validation-patterns` and
  `kind: validation`.
- Do not add `tree_path` frontmatter.
- Do not move any other shelf in this wave.
- Keep degraded continuation, isolated service stop, stress receipt closeout,
  and receipt-first failure analysis as four separate leaf bundles under one
  recovery shelf.
- Do not treat `antifragility-recovery` as Agents-of-Abyss Antifragility
  doctrine, via negativa law, fragile-pattern source truth, incident response
  doctrine, runtime self-healing, runtime ownership, proof authority, rollback
  policy, deployment lifecycle law, service catalog ownership, KAG authority,
  stats meaning, playbook choreography, or a generic resilience platform.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
