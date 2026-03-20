# Canonical Readiness

## Technique
- id: AOA-T-0004
- name: intent-plan-dry-run-contract-chain

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: `atm10-agent` records the chain as a real artifact-first automation workflow where intent is normalized into a plan, the plan is validated through dry-run, and contract checks gate the next step
- origin reinforcement: the origin notes show stable artifact families, explicit traceability metadata, and machine-readable contract output rather than log-only validation
- second context: `aoa-skills` reuses the same preview-first contract in a narrower skill surface, which confirms the invariant chain survives a different downstream form without collapsing into donor-specific implementation detail
- bounded transfer: the portability note states the minimum bar clearly and keeps the reusable contract centered on plan-first artifacts, dry-run-only execution, and explicit contract failure
- validation strength: the technique now has origin evidence, a bounded transfer note, a second-context adaptation note, examples, a checklist, and a semantic review that keeps it distinct from the extension checklist in `AOA-T-0005`

## Default-use rationale
- this is the default underlying contract when an intent-driven workflow must prove its plan before any real execution path is allowed
- it stays narrower than `AOA-T-0001`, which governs how repository changes are planned and reported, because `AOA-T-0004` is about the artifact-first execution chain itself
- `AOA-T-0005` remains a follow-on extension technique for adding one new intent to an already existing chain, not for defining the base contract

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the published technique keeps only the reusable intent-to-plan-to-dry-run contract and removes ATM10-specific command names, filenames, UI coordinates, and workflow wiring
- public reuse check: the bundle remains understandable without origin-project access and does not depend on hidden operational surfaces to explain the contract

## Remaining gaps
- a third live context would widen the proof surface further, but it is not required before a first canonical review of this bounded contract

## Recommendation
- approve `AOA-T-0004` for `promoted -> canonical`; the current support surfaces now make it read as the natural default underlying contract for intent-driven dry-run chains within its bounded scope
