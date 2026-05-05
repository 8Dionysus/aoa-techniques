# Antifragility-Recovery Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Preceding landed review:
[Landed History-Artifacts Pilot Review](landed-history-artifacts-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-fifteenth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `recovery/antifragility-recovery` as the fifteenth bounded tree
migration pilot.

Direct reading confirms that `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and
`AOA-T-0098` form one recovery shelf around stress-aware degraded continuation,
receipt-first regrounding, bounded substrate recovery, and evidence-led failure
analysis. The shelf is not Antifragility doctrine and not incident response. It
is the portable recovery corridor where a stress event stays bounded, visible,
receipt-backed, weaker than normal operation, and reviewable before later proof
or repair claims.

The shelf is accepted with one cross-domain watch. `AOA-T-0098` currently
lives under `validation-patterns/` and keeps `domain: validation-patterns` plus
`kind: validation`. Moving it under a recovery path would improve browsing only
if the migration preserves its validation nature rather than treating
validation as erased by path placement. Direct reading supports the move
because `AOA-T-0098` is the receipt-first analysis move that keeps the recovery
shelf honest after degraded continuation, isolated stop, and stress closeout.

This review does not move files. It only authorizes a later migration wave to
move exactly these four bundles into
`techniques/recovery/antifragility-recovery/` if that wave also updates the
recovery route card, root legacy receipts, authored links, generated surfaces,
and validation.

## Sources Read

- [AOA-T-0097 degrade-reground-recover](../../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md)
- [AOA-T-0097 checklist](../../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/checks/degrade-reground-recover-checklist.md)
- [AOA-T-0097 minimal example](../../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/examples/minimal-degraded-handoff.md)
- [AOA-T-0097 origin evidence](../../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/notes/origin-evidence.md)
- [AOA-T-0097 second context adaptation](../../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/notes/second-context-adaptation.md)
- [AOA-T-0099 isolated-service-stop-on-shared-substrate](../../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md)
- [AOA-T-0099 checklist](../../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/checks/isolated-service-stop-on-shared-substrate-checklist.md)
- [AOA-T-0099 minimal example](../../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/examples/minimal-isolated-service-stop.md)
- [AOA-T-0099 origin evidence](../../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/notes/origin-evidence.md)
- [AOA-T-0100 stress-receipt-reground-closeout](../../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md)
- [AOA-T-0100 checklist](../../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/checks/stress-receipt-reground-closeout-checklist.md)
- [AOA-T-0100 minimal example](../../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/examples/minimal-stress-closeout-lane.md)
- [AOA-T-0100 origin evidence](../../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/notes/origin-evidence.md)
- [AOA-T-0100 second context adaptation](../../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/notes/second-context-adaptation.md)
- [AOA-T-0098 receipt-first-failure-analysis](../../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md)
- [AOA-T-0098 checklist](../../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/checks/receipt-first-failure-analysis-checklist.md)
- [AOA-T-0098 minimal example](../../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/examples/minimal-receipt-review.md)
- [AOA-T-0098 origin evidence](../../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/notes/origin-evidence.md)
- [AOA-T-0098 second context adaptation](../../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/notes/second-context-adaptation.md)
- [Recovery route card](../../../../../techniques/recovery/AGENTS.md)
- [Techniques route card](../../../../../techniques/AGENTS.md)
- [Antifragility mechanic route card](../../../../antifragility/AGENTS.md)
- [Antifragility mechanic README](../../../../antifragility/README.md)
- [Antifragility provenance](../../../../antifragility/PROVENANCE.md)
- [Technique tree projection rows for `antifragility-recovery`](../../../../../reports/technique_tree_projection.md)
- [Technique family scout rows for `antifragility-recovery`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `antifragility-recovery`](../../../../../reports/technique_topology_scout.md)
- [Landed diagnosis-repair pilot review](landed-diagnosis-repair-pilot-review.md)
- [Landed history-artifacts pilot review](landed-history-artifacts-pilot-review.md)

## Direct Bundle Read

| technique | current path | domain | kind | status | direct-read result |
|---|---|---|---|---|---|
| `AOA-T-0097` | `techniques/system-recovery/degrade-reground-recover/` | `system-recovery` | `recovery` | `promoted` | owns the degrade -> reground -> recover posture where degraded mode stays weaker and recovery cites a source-owned receipt |
| `AOA-T-0099` | `techniques/system-recovery/isolated-service-stop-on-shared-substrate/` | `system-recovery` | `recovery` | `promoted` | owns one narrow service stop while shared substrate continuity remains explicit and verified |
| `AOA-T-0100` | `techniques/system-recovery/stress-receipt-reground-closeout/` | `system-recovery` | `recovery` | `promoted` | owns the stress -> receipt -> reground or hold -> reviewed closeout -> optional eval-bridge sequence |
| `AOA-T-0098` | `techniques/validation-patterns/receipt-first-failure-analysis/` | `validation-patterns` | `validation` | `promoted` | owns receipt-first failure analysis after a stress event, with facts separated from hypotheses and future checks named |

The shelf is intentionally a recovery shelf, not a doctrinal antifragility
package. The leaves compose around one bounded stress/recovery cycle, but no
leaf claims to be the whole cycle.

## Why The Shelf Holds

- `AOA-T-0097` supplies the immediate degraded continuation posture: continue
  smaller or stop, reground on stronger owner-local evidence, and leave a
  receipt.
- `AOA-T-0099` supplies the narrow mutation case: stop one named service and
  verify the shared substrate stayed usable instead of widening to full
  teardown.
- `AOA-T-0100` supplies the closeout lane: one stress family, one owner surface,
  one receipt, one honest continuation or hold, reviewed closeout, and only
  then optional eval intake.
- `AOA-T-0098` supplies the analysis lane: start from source-owned receipts,
  separate facts from hypotheses, propose one narrow change, and name the
  future receipt or eval path that could show improvement.
- All four leaves repeat the same authority family: owner-local evidence first,
  degraded or recovery claims weaker than normal operation, no hidden repair
  fan-out, and later proof weaker than actual eval verdicts.

## Cross-Domain Decision

Do not split before the fifteenth migration.

The only serious pre-migration split pressure is `AOA-T-0098`, because it is a
validation pattern rather than a `system-recovery` bundle. Direct reading says
that is a strength, not a blocker. This shelf needs one validation-shaped leaf
to keep recovery claims evidence-led after stress events.

The migration should preserve `AOA-T-0098` as `domain: validation-patterns` and
`kind: validation`. The path can say "this is the recovery neighborhood where
the technique is easiest to find"; frontmatter must keep saying "this move is
validation-shaped." That separation is exactly why the tree can scale beyond a
flat five-category taxonomy.

`AOA-T-0099` also deserves a watch line because it is the only explicitly
mutating runtime-adjacent leaf. It still fits because its invariant is not
runtime ownership; its invariant is bounded stop plus verified substrate
continuity under recovery pressure.

## Recovery Trunk Fit

`recovery/` remains the correct trunk because the shelf is about preserving an
honest recovery posture when a stressor, outage, degraded mode, or bounded stop
could otherwise widen into hidden repair theater. The shelf also gives
`recovery/` a second distinct precedent after `diagnosis-repair`: not diagnosis
and repair-shape selection, but stress-aware antifragile continuation and
receipt-first review.

The future shelf name should remain `antifragility-recovery`. `degraded-mode`
would under-name failure analysis and service stop, `stress-receipts` would
under-name recovery posture, and `system-recovery` would erase the
validation-pattern cross-domain seam. `antifragility-recovery` is broad enough
to hold the four current leaves without importing center-side Antifragility
doctrine.

## Boundary Watch Accepted

The projection marks `antifragility-recovery` as `candidate`, but direct
reading confirms several authority pressures:

- `AOA-T-0097` can drift into permanent degraded operation, speculative
  regrounding, or hidden auto-repair if the receipt and weaker-than-normal
  posture are skipped.
- `AOA-T-0099` can drift into incident response, deployment lifecycle, service
  catalog ownership, or broad rollback if the target and substrate boundaries
  are not named before mutation.
- `AOA-T-0100` can drift into routing, playbook, KAG, stats, runtime, or eval
  authority if owner-local receipt and reviewed closeout become symbolic.
- `AOA-T-0098` can drift into generic incident review, dashboard mythology, or
  proof claims if receipt-first facts and hypotheses are not separated.

The shelf is accepted because those pressures are already explicit in the
bundle contracts, checklists, examples, origin evidence, and second-context
adaptations. The migration should preserve those boundaries rather than
restating them as heavy shelf law.

## Proposed Move

Move exactly these four bundles in the migration wave:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0097` | `techniques/system-recovery/degrade-reground-recover/` | `techniques/recovery/antifragility-recovery/degrade-reground-recover/` |
| `AOA-T-0099` | `techniques/system-recovery/isolated-service-stop-on-shared-substrate/` | `techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/` |
| `AOA-T-0100` | `techniques/system-recovery/stress-receipt-reground-closeout/` | `techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/` |
| `AOA-T-0098` | `techniques/validation-patterns/receipt-first-failure-analysis/` | `techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/` |

Keep `domain`, `kind`, status, IDs, evidence, relations, maturity,
validation-strength metadata, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- `techniques/recovery/AGENTS.md`, because it will need to name the compact
  `antifragility-recovery/` shelf while preserving current recovery stop lines
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- authored relations and adjacent references from technique docs, support
  files, selection docs, generated readers, and review packets
- Antifragility mechanic anchor links in `mechanics/antifragility/README.md`
  and `mechanics/antifragility/PROVENANCE.md`
- generated catalogs, capsules, manifests, reports, KAG exports, docs readers,
  and source-lift surfaces after the path move
- mechanics review rows and tests that still point to `system-recovery/` or
  `validation-patterns/` homes
- release-check output touched by regenerated indexes and reports

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Why Not Neighbor Shelves In This Wave

`ready-work-graphs`, `intent-chain`, and `agent-workflows-core` should wait
because they add execution and orchestration pressure rather than
stress-recovery pressure.

`runtime-truth-lifecycle` should wait because it carries runtime truth and
lifecycle authority pressure that could blur `AOA-T-0099`.

`review-evidence` and `owner-truth-closeout` should wait because they move
closer to proof, owner acceptance, and closeout authority.

`automation-governance`, `approval-evidence`, and `tool-gateway` should wait
because they carry governance, approval, or tool-use authority that would make
this recovery pilot too broad.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not change `domain` or `kind`; this pilot tests path architecture, not
  frontmatter remap.
- Do not treat `antifragility-recovery` as Agents-of-Abyss Antifragility
  doctrine, via negativa law, fragile-pattern source truth, incident response
  doctrine, runtime self-healing, runtime ownership, proof authority, rollback
  policy, deployment lifecycle law, service catalog ownership, KAG authority,
  stats meaning, playbook choreography, or generic resilience platform.
- Do not erase `AOA-T-0098` as a validation pattern just because its proposed
  path is under `recovery/`.
- Do not collapse degraded continuation, isolated service stop, stress receipt,
  and receipt-first failure analysis into one recovery mega-technique.
- Do not move execution, continuity, governance, proof, automation, tool-use,
  runtime-truth, owner-truth, or neighboring recovery shelves in the same wave.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the fifteenth pilot migration.

Move exactly `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and `AOA-T-0098` into
`techniques/recovery/antifragility-recovery/`; update the compact recovery
route card; preserve a root `legacy/receipts/` migration receipt; repair
authored links including Antifragility mechanic anchors; rebuild generated
surfaces; and validate with the narrow tree-pilot tests plus
`python scripts/release_check.py`.
