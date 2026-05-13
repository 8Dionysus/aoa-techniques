# Canonical Readiness

## Technique
- id: AOA-T-0077
- name: harvest-packet-contract

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the second context adaptation kept the contract bounded around one reviewed-session packet spine instead of widening into memory or routing doctrine
- `aoa-sdk` now provides a second live consumer outside the originating packet reference: the checkpoint-closeout bridge writes `HARVEST_PACKET.json` as a bounded packet nucleus, and the closeout API can later read the packet's accepted candidates into owner follow-through briefs without treating the packet as final owner truth
- the inspected `aoa-sdk` source is commit `f74c037e0f346713001516f7f3abddabbf64d02a` with commit date `2026-05-12T04:44:46+03:00`; inspected file hashes include `src/aoa_sdk/checkpoints/registry.py` (`71a6246f8f6ddcea3f33f540db50f2fc7cd39672`), `tests/test_checkpoints.py` (`326f6050516f26e031e8c8e88695139c028966df`), `tests/test_closeout.py` (`ba918ac60162a004c51d7c688dfebfd535e6e32d`), `README.md` (`c2f267fbe6fa4a652d41f17354f09f46edb73077`), `docs/session-growth-checkpoints.md` (`dc725cfaf477dabc1c8918bf34901cac0a83ee40`), and `docs/checkpoint-note-promotion.md` (`7f1778771ad4a87d162d40d993880f12146df6fd`)
- exact `aoa-sdk` evidence: the packet carries `artifact_kind: harvest_packet`, `session_ref`, `route_ref`, authority contract, owner repo, reviewed artifact reference, session trace references, checkpoint note and surface handoff refs, checkpoint-review carry, accepted candidates, deferred candidates, extract counts, promotion candidate count, owner-layer distribution, and reviewed evidence density
- exact consumer evidence: `test_closeout_api_run_builds_owner_follow_through_from_harvest_packet` writes a harvest packet with accepted candidates containing `candidate_ref`, `unit_name`, `abstraction_shape`, `owner_repo_recommendation`, `chosen_next_artifact`, `nearest_wrong_target`, `owner_reason`, and `evidence_anchors`, then asserts `sdk.closeout.run(...)` emits an owner follow-through brief with source kind `harvest-candidate`, action `draft-owner-artifact`, owner repo, next surface, and unit name
- supporting public external lane: LangSmith annotation queues and dataset docs show a different public packet-like path where reviewed runs are corrected into reference examples, copied with metadata or feedback into datasets, versioned, filtered, and consumed by evaluation. This supports the bounded reviewed-run handoff pressure, while staying supporting evidence because it does not own AoA's packet fields, owner hints, or nearest-wrong-target posture

## Default-use rationale
- this is the right canonical default when the missing object is a bounded post-session nucleus packet rather than donor extraction, checkpoint capture, or a later verdict seam
- it is strongest when several later family seams should be able to read one explicit packet without collapsing into one oversized recap
- it is now proven across the origin skill reference, the public technique adaptation, the SDK checkpoint-closeout artifact builder, and a downstream closeout consumer that turns packet candidates into owner follow-through briefs
- it remains narrower than memory canon, routing authority, closeout dashboard schema, owner placement, diagnosis, repair, progression, quest verdict, or final promotion

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the published technique keeps the reusable packet contract while excluding SDK hook plumbing, local `.aoa` storage paths, exact closeout commands, full checkpoint capture, memory writeback, stats refresh, owner-handoff queue behavior, and final owner acceptance

## Remaining gaps
- no blocker remains for canonical status
- future sources can reinforce the default, but they must keep the required packet spine small and keep optional family fields subordinate to later explicit seams

## Recommendation
- move `AOA-T-0077` to `canonical`
- add an adverse-effects review so future edits do not let the packet become memory canon, routing authority, dashboard schema, or final owner verdict
