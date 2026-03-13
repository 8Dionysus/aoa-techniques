# Canonical Readiness

## Technique
- id: AOA-T-0002
- name: source-of-truth-layout

## Verdict
- go

## Evidence summary
- origin evidence: `atm10-agent/docs/SOURCE_OF_TRUTH.md` explicitly defines canonical roles and update rules across status, plans, history, decisions, and run instructions
- origin reinforcement: `atm10-agent/README.md` and `atm10-agent/MANIFEST.md` already behave as lightweight entrypoints that link to `TODO`, `PLANS`, `docs/RUNBOOK.md`, `docs/DECISIONS.md`, `docs/SESSION_2026-03-13.md`, and `docs/SOURCE_OF_TRUTH.md`
- second context: `aoa-techniques` applies the same one-home-per-information-class rule to a smaller public repository with `README`, `TECHNIQUE_INDEX`, `AGENTS`, `CONTRIBUTING`, and `SECURITY`
- validation strength: the technique has a reusable example, checklist, public second-context adaptation note, and clearer separation between invariant routing rules and project-shaped file names

## Default-use rationale
- this is a good default for repositories that keep accumulating top-level docs because it prevents status, policy, and operating instructions from drifting across multiple files
- the technique adapts well: smaller repos can use a reduced role map, while larger repos can expand to `TODO`, `PLANS`, `RUNBOOK`, and history docs

## Remaining gaps
- the public second context is smaller than the origin and does not exercise every operational role in the recommended map
- a future context with issue-tracker-backed active work or non-file-backed runbooks would broaden the proof surface

## Recommendation
- ready for a future `promoted -> canonical` PR if reviewers accept the reduced public-repository variant as sufficient reuse evidence for a default documentation pattern
