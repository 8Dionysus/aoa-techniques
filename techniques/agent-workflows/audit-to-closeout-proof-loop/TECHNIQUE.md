---
id: AOA-T-0092
name: audit-to-closeout-proof-loop
domain: agent-workflows
kind: workflow
status: promoted
origin:
  project: Dionysus + AoA ecosystem repos
  path: reports/ecosystem-audits/2026-04-06.cross-repo.audit-remediation-session-harvest.md + aoa-playbooks/docs/real-runs/2026-04-05.validation-driven-remediation.md
  note: Extracted from reviewed cross-repo audit remediation runs where findings were re-confirmed in live code, fixed at the owning source surface, and closed through targeted proof plus full verification.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - audit
  - closeout
  - proof
  - remediation
summary: Turn a reviewed audit finding set into a live-confirmed, proof-backed closeout loop so remediation claims rest on named evidence instead of audit wording alone.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-04-06
export_ready: true
relations:
  - type: complements
    target: AOA-T-0001
  - type: complements
    target: AOA-T-0052
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# audit-to-closeout-proof-loop

## Intent

Turn a reviewed audit finding set into a proof-backed closeout loop by requiring live confirmation of each finding, a bounded owner-surface fix, a targeted regression seam, and a final closeout pass before the finding is treated as closed.

## When to use

- a reviewed audit, review packet, or bounded findings set already exists
- the route must prove that each finding still lives in current code before patching
- remediation claims need stronger closure than "tests are green now"
- the work may cross more than one repository but still stays anchored to named findings
- the team needs an honest way to record non-repro, defer, or follow-on outcomes instead of forcing synthetic closure

## When not to use

- the source findings are still raw, unreviewed, or too vague to bound
- the work is a generic rollout request rather than a failure-anchored remediation route
- the route is mainly live incident stabilization, release cutover, or backlog policy
- the change fits one tiny local fix with no meaningful proof or closeout boundary
- there is no realistic way to rerun a targeted proof seam or owner-level closeout surface

## Inputs

- one reviewed audit artifact or bounded findings set
- live source checkouts for the owning repositories
- one owner map for the touched findings
- one targeted proof surface per finding or finding cluster
- one owner-level closeout surface such as full tests, validators, or bounded runtime checks

## Outputs

- one live-confirmed finding map
- one bounded owner-surface fix slice per finding or cluster
- one targeted regression proof result per closed finding
- one owner-level closeout verification pack
- one honest closure record with deferred, non-repro, or follow-on items left explicit

## Core procedure

1. Start from a reviewed findings set and split it into bounded finding units or tight clusters.
2. Re-confirm each finding against live code before patching. If it does not reproduce cleanly, mark it `non-repro`, `uncertain`, or `needs follow-on` instead of pretending it closed.
3. Map each finding to its owning repository and source checkout before mutation begins. Reject mirror-only or downstream-only fixes when another source surface owns the meaning.
4. Define the smallest remediation slice that addresses the named failure mode without widening into unrelated cleanup.
5. Add or tighten one targeted proof seam that would actually exercise the named failure mode or its contract boundary.
6. Apply the bounded fix and rerun the targeted proof immediately.
7. After the local slice closes, rerun the owner-level closeout surface such as the full test suite, repo validator, or bounded runtime check.
8. Record which proof surfaces ran for each closed finding and which findings were deferred, non-repro, or handed off.
9. Stop and escalate when a finding needs a new owner, a new route, or a broader structural change instead of forcing false closeout.

## Contracts

- no finding closes without live confirmation or an explicit non-repro explanation
- fixes land in the owning source repository or source checkout
- each closed finding names a targeted proof surface that matches the failure mode
- targeted proof does not replace owner-level closeout
- owner-level closeout does not replace targeted proof
- deferred, uncertain, and follow-on outcomes remain visible
- the technique stays smaller than incident response, release cutover, and generic issue-management doctrine

Relationship to adjacent techniques: unlike [AOA-T-0052](../review-findings-compaction/TECHNIQUE.md), this technique starts after the findings are already reviewed and focuses on proof-backed closure rather than dedupe and stale-finding reduction. Unlike [AOA-T-0001](../plan-diff-apply-verify-report/TECHNIQUE.md), it adds a stricter finding-first proof loop where live confirmation, targeted regression evidence, and final closeout must all attach to named audit findings before closure is credible.

## Risks

### Failure modes

- audit wording is treated as truth without live confirmation
- the chosen targeted proof seam exercises the wrong thing
- a full-suite rerun passes even though the named failure mode never received direct proof
- the fix lands in a runtime mirror or derived surface instead of the owning source checkout

### Negative effects

- the technique can slow genuinely tiny fixes that do not need a full finding-level proof loop
- large audit packets can become operationally heavy if each finding is over-sliced
- a too-local fix can miss a shared structural cause when the route needed escalation instead

### Misuse patterns

- closing findings on one green full-suite pass without targeted proof
- skipping live confirmation because the audit wording looks obvious
- converting non-repro findings into silent drops
- widening the bundle into multi-repo program management or backlog governance

### Detection signals

- closeout notes cannot say which proof surface closed which finding
- the route patched code before the owner map or source checkout was explicit
- the only evidence is one final green suite with no finding-level trace
- findings disappear from the closeout narrative without defer or non-repro posture

### Mitigations

- require one visible finding map and owner map before mutation
- keep one targeted proof seam attached to each named failure mode
- preserve defer and non-repro outcomes as honest closure states
- stop and reroute when the route needs structural redesign or a different owner layer

## Validation

Verify the technique by confirming that:
- at least one finding was re-confirmed against live code or explicitly marked non-repro
- each closed finding names a targeted proof surface
- the owner-level closeout surface reran before final closure
- fixes landed in the owning source checkout rather than a mirror
- deferred or follow-on findings remained explicit instead of disappearing

See `checks/audit-to-closeout-proof-loop-checklist.md`.

## Adaptation notes

What can vary across projects:
- the source artifact format for the audit or findings set
- whether the closeout surface is `pytest`, a repo validator, a smoke pack, or another bounded verification path
- how findings are grouped into one remediation slice
- how non-repro or defer states are recorded
- whether the route spans one repository or several owner repositories

What should stay invariant:
- start from reviewed findings, not raw chatter
- re-confirm the finding in live code before patching
- attach one targeted proof seam to each closed finding
- rerun one owner-level closeout surface before final closure
- keep unresolved findings visible

Project-shaped details that should not be treated as invariant:
- one audit filename
- one exact CI or validator command
- one sibling workspace layout
- one local source-checkout exception such as `~/src/abyss-stack`
- one receipt or closeout packet schema

AoA adaptation example:
- confirm each finding against the current owner repo checkout
- reject fixes in mirrors when the source checkout owns the meaning
- pair targeted `pytest` slices or validators with a later full repo rerun
- keep harvest and stats publication adjacent but separate from the closeout proof loop itself

## Public sanitization notes

This public bundle keeps only the reusable proof discipline: confirm the finding in live code, fix it at the owner surface, prove the failure mode locally, then rerun the broader closeout surface. Specific audit files, local path quirks, repo-private runtime details, and session-specific telemetry were reduced to adaptation examples or left out.

## Example

See `examples/minimal-audit-to-closeout-proof-loop.md`.

## Checks

See `checks/audit-to-closeout-proof-loop-checklist.md`.

## Promotion history

- extracted from reviewed AoA cross-repo audit remediation runs on 2026-04-05 and 2026-04-06
- promoted into `aoa-techniques` on 2026-04-06 as a bounded finding-first remediation closeout workflow

## Future evolution

- keep findings compaction in `AOA-T-0052` instead of widening this bundle backward into review dedupe
- keep scenario-level multi-repo choreography in `aoa-playbooks` instead of absorbing route semantics here
- revisit canonical readiness only after another non-identical public context proves the same finding-first proof boundary
