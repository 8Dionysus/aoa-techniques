# Canonical Readiness

## Technique
- id: AOA-T-0021
- name: bounded-relation-lift-for-kag

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: the bundle came from relation consumers and relation-lift guidance, so it already has a bounded navigation anchor
- second context: the adaptation note now cites live donor surfaces in `aoa-evals` plus committed `aoa-routing@0f8f22f34c04eea8a2ef9bda892154a913d335c4`, where `generated/kag_source_lift_relation_hints.min.json` consumes the KAG/source-lift family's direct relations as one-hop hints
- validation strength: `aoa-evals/bundles/aoa-eval-integrity-check/eval.yaml` and `aoa-evals/generated/eval_catalog.json` verify direct typed relations as bounded edge metadata, while the new `aoa-routing` surface proves a second non-eval consumer can reuse those direct relations without changing `recommended_paths` semantics
- boundedness check: the routing consumer stays family-scoped, one-hop only, and explicitly avoids graph traversal, rationale layers, multi-hop inference, or same-kind exploration growth

## Default-use rationale
- this is now the right default when direct relations should only guide nearby inspection through one-step adjacency hints
- it remains narrower than any graph-oriented contract because the edge meaning stops at direct typed adjacency, not rationale or traversal policy
- the committed routing consumer now proves that the same relation layer remains useful outside eval bundles without becoming a rationale or traversal system

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable direct-edge contract and avoids repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files, and the new routing surface still routes back to source-owned technique bundles rather than copying their meaning

## Remaining gaps
- no blocking gap remains for canonical use as long as the relation layer stays family-scoped, one-hop only, and review-backed
- future review should keep watching for graph creep, but that is now an ongoing watch seam rather than a promotion blocker

## Recommendation
- promote `AOA-T-0021` to `canonical`
- use it as the default bounded direct-relation hint technique while keeping rationale, graph semantics, and multi-hop traversal deferred
