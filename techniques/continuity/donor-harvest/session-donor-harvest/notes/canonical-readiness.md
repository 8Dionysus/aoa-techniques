# Canonical Readiness

## Technique
- id: AOA-T-0075
- name: session-donor-harvest

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the second context adaptation kept the contract bounded around post-session donor extraction rather than live capture, memory, or promotion doctrine
- `aoa-sdk` now provides a second live consumer outside the originating `aoa-session-donor-harvest` skill bundle: the checkpoint-closeout bridge starts from a reviewed artifact, blocks pending checkpoint reviews, aggregates runtime-session checkpoint notes, rereads the reviewed artifact, derives an ordered donor -> progression -> quest plan, and builds donor harvest outputs without treating checkpoint capture as harvest verdict
- the inspected `aoa-sdk` source is commit `f74c037e0f346713001516f7f3abddabbf64d02a` with commit date `2026-05-12T04:44:46+03:00`; inspected file hashes include `src/aoa_sdk/checkpoints/registry.py` (`71a6246f8f6ddcea3f33f540db50f2fc7cd39672`), `tests/test_checkpoints.py` (`326f6050516f26e031e8c8e88695139c028966df`), `tests/test_closeout.py` (`ba918ac60162a004c51d7c688dfebfd535e6e32d`), `README.md` (`c2f267fbe6fa4a652d41f17354f09f46edb73077`), `docs/session-growth-checkpoints.md` (`dc725cfaf477dabc1c8918bf34901cac0a83ee40`), and `docs/checkpoint-note-promotion.md` (`7f1778771ad4a87d162d40d993880f12146df6fd`)
- exact `aoa-sdk` evidence: `_build_donor_harvest_outputs` creates accepted candidates from shortlisted clusters, emits a `HARVEST_PACKET.json` with `session_ref`, `route_ref`, authority contract, reviewed artifact reference, checkpoint review carry, accepted candidates, deferred candidates, extract counts, owner-layer distribution, and reviewed evidence density, then writes a `HARVEST_PACKET_RECEIPT.json` and a core skill application receipt
- exact validation evidence: SDK tests assert closeout chain outputs carry checkpoint semantic review into `HARVEST_PACKET`, preserve multiple reviewed checkpoint reviews in the packet carry, emit harvest/progression/quest artifacts and receipts even without a local checkpoint note, and keep owner handoff rooted in evidence instead of hidden memory
- supporting public external lane: LangSmith annotation queues publicly document a workflow where human reviewers attach feedback to specific runs, mark reviewed queue items complete, edit a run's input/output into a corrected reference example, and add it to a dataset; LangSmith dataset docs and automations further show traces/runs filtered or reviewed into datasets for testing, few-shot examples, or finetuning. This supports the broader reviewed-run-to-bounded-downstream-data pressure, but it stays supporting rather than primary proof because it does not carry AoA-style owner hints or donor-pack lineage fields

## Default-use rationale
- this is the right canonical default when the missing object is a bounded donor pack over a reviewed session artifact rather than a transcript export, recap, checkpoint note, or final promotion verdict
- it is strongest when several reusable units may have emerged from one reviewed session and later owner placement should start from explicit candidate records
- it is now proven across the origin skill bundle, the public technique adaptation, the SDK checkpoint-closeout consumer, and an external supporting reviewed-run data workflow
- it remains narrower than checkpoint capture, closeout execution, owner-layer triage, quest promotion, memory writeback, and evaluation dataset curation

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the published technique keeps the reusable donor-pack workflow while keeping AoA repo mapping in adaptation notes only and excluding SDK hook plumbing, local `.aoa` storage layout, exact command wrappers, checkpoint capture, closeout execution, owner handoff files, memory writeback, stats refresh, and final promotion authority

## Remaining gaps
- no blocker remains for canonical status
- future sources can reinforce the default, but they must preserve the narrow boundary: reviewed artifact first, bounded candidate records, visible evidence anchors, hold or defer posture, and an explicit stop-line before owner placement, routing, memory, evaluation, or final promotion claims

## Recommendation
- move `AOA-T-0075` to `canonical`
- add an adverse-effects review so future edits do not widen donor harvest into checkpoint capture, transcript packaging, memory canon, owner placement, or promotion verdicts
