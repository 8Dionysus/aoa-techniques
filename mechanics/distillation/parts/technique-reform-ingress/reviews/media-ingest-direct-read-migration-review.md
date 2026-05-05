# Media-Ingest Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Projection packet:
[First Tree Projection Review Pack](first-tree-projection-review-pack.md)

Prior pilot review:
[Landed Handoff-Continuation Pilot Review](landed-handoff-continuation-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-third-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `media-ingest` as the third migration pilot.

The move is clearer than current placement because the five bundles share one
ingest problem: external media, documents, or message exports must become a
bounded reviewable object before later extraction, routing, cleanup, memory, or
automation begins. `agent-workflows` remains true as their current `domain`,
but it is too broad as a browsing neighborhood for OCR handoff, post-OCR field
extraction, perceptual duplicate grouping, semantic bucketing, and Telegram
normalization.

This review does not move files. It only decides that the next bounded wave may
move exactly this shelf if route cards, root legacy receipts, link repair,
generated surfaces, and validation move together.

## Sources Read

- [AOA-T-0070 two-stage-document-ocr-pipeline](../../../../../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md)
- [AOA-T-0071 template-backed-field-extraction-after-ocr](../../../../../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md)
- [AOA-T-0072 perceptual-media-dedupe-with-threshold-review](../../../../../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md)
- [AOA-T-0073 semantic-media-bucketing-with-vision-plus-ocr](../../../../../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md)
- [AOA-T-0074 telegram-export-normalization-to-local-store](../../../../../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md)
- supporting `checks/`, `examples/`, and `notes/` files for the five bundles,
  scanned for invariant, adjacency, public-safety, and drift-pressure cues
- [Personal Ingest Wave 2](../../../../../incoming/personal-ingest-wave-2/README.md)
- [External Technique Candidates - Personal Ingest Wave 2](../../../../../incoming/personal-ingest-wave-2/docs/EXTERNAL_TECHNIQUE_CANDIDATES_PERSONAL_INGEST_WAVE_2.md)
- [Personal Ingest Wave 2 - Planting Order](../../../../../incoming/personal-ingest-wave-2/docs/PERSONAL_INGEST_WAVE_2_PLANTING_ORDER.md)
- [Personal Ingest Wave 2 Donor Sources](../../../../../incoming/personal-ingest-wave-2/support/DONOR_SOURCES.md)
- `reports/technique_tree_projection.md` rows for `AOA-T-0070` through
  `AOA-T-0074`
- `reports/technique_topology_scout.md` rows for `AOA-T-0070` through
  `AOA-T-0074`

## Direct Read

| technique | current kind | center of gravity | pilot reading |
|---|---|---|---|
| `AOA-T-0070` `two-stage-document-ocr-pipeline` | `ingest` | detect/layout plus recognize stages emit one structured OCR handoff with confidence and region references | document/image intake before extraction, not OCR serving or field parsing |
| `AOA-T-0071` `template-backed-field-extraction-after-ocr` | `ingest` | explicit templates or heuristics turn OCR handoff text into bounded fields with missing/conflict markers | post-OCR intake into a reviewable field object, not bookkeeping or parser implementation |
| `AOA-T-0072` `perceptual-media-dedupe-with-threshold-review` | `ingest` | perceptual similarity groups near-duplicates and separates borderline matches into review | media set intake and cleanup preparation, not deletion policy or semantic taxonomy |
| `AOA-T-0073` `semantic-media-bucketing-with-vision-plus-ocr` | `ingest` | bounded visual taxonomy plus optional OCR side text creates confidence-aware media buckets | media intake routing before action, not moderation, identity inference, or open-ended multimodal automation |
| `AOA-T-0074` `telegram-export-normalization-to-local-store` | `ingest` | Telegram-derived messages and media become stable local objects with provenance, reply edges, media refs, and resumable storage | source-specific data intake, not auth/session bridge, memory writeback, or general history canon |

The shelf is not merely "media tools." It is the narrower intake seam where raw
or semi-raw external material becomes a visible intermediate object that later
techniques or systems can inspect without inheriting donor runtime behavior.

## Boundary Read

The shelf remains useful only if the bundle boundaries stay sharp:

- `AOA-T-0070` owns OCR handoff, not downstream field semantics.
- `AOA-T-0071` owns bounded post-OCR field extraction, not OCR staging or
  accounting automation.
- `AOA-T-0072` owns duplicate grouping, not cleanup policy.
- `AOA-T-0073` owns bounded media bucketing, not dedupe, OCR handoff, field
  extraction, moderation, or identity inference.
- `AOA-T-0074` owns Telegram-source normalization, not credentials, session
  conversion, live agent control, memory writeback, or general history capture.

Those boundaries are strong enough for a pilot shelf because the techniques are
adjacent but not substitutable.

## Telegram Edge

`AOA-T-0074` is the stress case.

It should stay in the pilot because it is still an ingest technique: it turns a
bounded external source into a local reviewable store with source provenance,
media references, reply edges, and resume state. The held sibling
`telegram-account-auth-and-session-bridge` proves the right boundary: auth,
secret handling, session conversion, and live control-plane behavior are not
part of this shelf.

The migration should still preserve a watch line: if future source-specific
normalization techniques grow beyond media/document/message intake, a later
tree review may split `media-ingest` into a wider `source-ingest` shelf. That
future pressure does not block this pilot because the current five-bundle shelf
is coherent enough and already projected as `media-ingest`.

## Why Not Keep This As Agent Workflows

`agent-workflows` remains true as `domain`: all five bundles are reusable
agent-facing workflow techniques.

The directory tree now answers a browsing and placement question. On that
question, `ingest/media-ingest` is tighter than the old broad folder:

- all five bundles transform incoming external material into bounded
  intermediate objects
- all five are `kind: ingest`, unlike the previous continuity shelves that had
  cross-kind stress cases
- the Personal Ingest Wave 2 staging packet already groups the five landed
  bundles and keeps the auth/session bridge out
- direct links between these bundles become easier to read if they are shelf
  siblings
- the shelf tests a non-continuity trunk without touching boundary-watch or
  split-review-needed families

## Pilot Scope

Move exactly these five bundles in the next migration wave:

| technique | current path | pilot path |
|---|---|---|
| `AOA-T-0070` | `techniques/agent-workflows/two-stage-document-ocr-pipeline/` | `techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/` |
| `AOA-T-0071` | `techniques/agent-workflows/template-backed-field-extraction-after-ocr/` | `techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/` |
| `AOA-T-0072` | `techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/` | `techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/` |
| `AOA-T-0073` | `techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/` | `techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/` |
| `AOA-T-0074` | `techniques/agent-workflows/telegram-export-normalization-to-local-store/` | `techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/` |

Keep bundle IDs, `domain`, `kind`, `status`, owners, evidence, relations,
checklists, examples, notes, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored sibling links inside the five moved bundles, especially relative
  links among `AOA-T-0070`, `AOA-T-0071`, `AOA-T-0072`, and `AOA-T-0073`
- links from incoming Personal Ingest Wave 2 candidate and planting surfaces
- links from Audit promotion-readiness matrix rows for `AOA-T-0070` through
  `AOA-T-0074`
- generated reader docs such as `TECHNIQUE_INDEX.md`, `docs/TECHNIQUE_*`,
  `docs/EVIDENCE_NOTE_SURFACES.md`, and generated manifests
- generated reports for family, topology, and tree projection
- a new `techniques/ingest/AGENTS.md` route card, because `ingest/` would
  become the first non-continuity migrated trunk
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- release-check output touched by regenerated catalogs, capsules, sections,
  examples, checklists, evidence notes, and repo-doc surfaces

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `family` or `tree_path` frontmatter.
- Do not move another `pilot-candidate` shelf in the same wave.
- Do not rename `media-ingest` during the pilot move.
- Do not change `domain`; the pilot tests path architecture, not owner-lane
  frontmatter.
- Do not absorb `telegram-account-auth-and-session-bridge`; it remains outside
  the landed shelf because auth/session/control behavior is not the normalized
  local-store technique.
- Do not widen ingest into KAG, memory, moderation, deletion, account auth, or
  downstream automation doctrine.

## Next Honest Move

Run the third pilot migration.

Move exactly `AOA-T-0070` through `AOA-T-0074` into
`techniques/ingest/media-ingest/`, add the minimal `ingest/` route card, repair
authored links, preserve a root legacy receipt, rebuild generated surfaces, and
run `python scripts/release_check.py`.
