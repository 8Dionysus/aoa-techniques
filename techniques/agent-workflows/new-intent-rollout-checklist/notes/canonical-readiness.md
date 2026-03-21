# Canonical Readiness

## Technique
- id: AOA-T-0005
- name: new-intent-rollout-checklist

## Verdict
- defer for now

## Evidence summary
- origin evidence: `atm10-agent` documents the rollout policy as a bounded checklist for adding one new `intent_type` to an existing dry-run chain with canonical fixtures, strict routing assertions, and regression coverage
- origin reinforcement: the origin notes describe the same extension path across fixture hardening, strict `expected_intent_type` checks, summary publication, and end-to-end regression proof for a new intent rollout
- second context: `aoa-techniques` now shows the same contract in a public-safe repo-local adaptation with one generic rollout example, one concrete non-UI example, and a checklist that keeps fixture, smoke, contract-check, and artifact alignment explicit
- validation strength: the bundle has strong checklist and example surfaces plus a rollout-failure triage note, but it still lacks a second live reuse context beyond the origin and this repo-local rollout sketch

## Default-use rationale
- this is the right checklist when a shared intent chain already exists and one new intent type needs to be added without bypassing the chain or inventing a shortcut path
- it stays narrower than the underlying chain contract in `AOA-T-0004`, and narrower than rollout planning in `AOA-T-0001`
- it is still not the default canonical choice because the current second-context evidence is a bounded public sketch rather than a second live reuse context with stronger operating proof

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the public technique keeps the reusable rollout checklist and removes donor-specific workflow names, payloads, and private operational detail
- public reuse check: the repo-local examples and triage note are understandable without origin-project access, but they do not yet prove enough live second-context reuse for canonical promotion

## Remaining gaps
- the bundle still needs live reuse beyond the repo-local rollout sketch before canonical promotion would be justified
- a future second live context should show the same checklist succeeding in practice, not only in public-safe example form

## Recommendation
- bounded defer verdict: keep `AOA-T-0005` `promoted` for now and do not advance it to `canonical` until there is live reuse beyond the repo-local rollout sketch
- smallest remaining gap: one live second-context reuse outside the origin project and this repository-local adaptation, showing the same checklist succeed in practice rather than only in public-safe example form
