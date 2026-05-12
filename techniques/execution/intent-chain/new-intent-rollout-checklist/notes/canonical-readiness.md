# Canonical Readiness

## Technique
- id: AOA-T-0005
- name: new-intent-rollout-checklist

## Verdict
- bounded defer for now

## Evidence summary
- origin evidence: `atm10-agent` documents the rollout policy as a bounded checklist for adding one new `intent_type` to an existing dry-run chain with canonical fixtures, strict routing assertions, and regression coverage
- origin reinforcement: merged `ATM10-Agent@7cf55f70badbe8b1a51e2eabbe1424f35b833dd3` now records reusable `M6.19` rollout evidence across `open_quest_book`, `check_inventory_tool`, and `open_world_map` in `docs/RUNBOOK.md`, with matching summary references in `README.md`, `MANIFEST.md`, and `ROADMAP.md`
- second context: `aoa-techniques` still shows the same contract in a public-safe repo-local adaptation with one generic rollout example, one concrete non-UI example, and a checklist that keeps fixture, smoke, contract-check, and artifact alignment explicit
- validation strength: the bundle now has stronger origin-side operating proof plus a clear repo-local adaptation, but it still lacks a non-origin live second context beyond `atm10-agent` and this repository-local sketch

## Default-use rationale
- this is the right checklist when a shared intent chain already exists and one new intent type needs to be added without bypassing the chain or inventing a shortcut path
- it stays narrower than the underlying chain contract in `AOA-T-0004`, and narrower than rollout planning in `AOA-T-0001`
- it is still not the default canonical choice because the current proof is one strong origin record set plus one bounded public sketch, not a second live reuse context in another repository

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the public technique keeps the reusable rollout checklist and removes donor-specific workflow names, payloads, and private operational detail
- public reuse check: the repo-local examples and triage note are understandable without origin-project access, and the merged `atm10-agent` rollout records materially strengthen origin proof, but they still do not create a second non-origin live context for canonical promotion

- 2026-05-12 long-pass searched-lane result: no exact-fit second consumer found in the Stage 2 promotion-evidence pass
- searched lane: public `expected_intent_type` / intent-evaluation repositories, assistant conversation-eval documentation, and chatbot/IBN intent-testing surfaces
- adjacent public examples: PRISM Monitor's manufacturing
  intent-classification dataset, ARTE Chatbot's `intent_type` evaluation
  harness, CS4730 IBN benchmark fixtures, Rasa assistant testing, and Botpress
  ADK evals all show useful intent or behavior validation patterns, but they do
  not show one new intent being rolled into an existing dry-run chain through a
  canonical fixture, dedicated smoke path, strict contract summary, published
  review surface, and regression proof
- conclusion: these lanes strengthen the negative boundary around the technique, but they do not close the second-context gap

## Remaining gaps
- the bundle still needs one non-origin live reuse context beyond `atm10-agent` and the repo-local rollout sketch before canonical promotion would be justified
- a future second live context should show the same checklist succeeding in practice on another shared intent chain, not only in the origin project plus a public-safe example form

## Recommendation
- bounded defer verdict: keep `AOA-T-0005` `promoted` for now and do not advance it to `canonical` until there is one non-origin live reuse context beyond `atm10-agent`
- smallest remaining gap: one live second-context reuse outside the origin project and this repository-local adaptation, showing the same checklist succeed in practice rather than only in origin rollout records plus public-safe example form
