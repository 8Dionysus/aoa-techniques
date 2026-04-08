---
id: AOA-T-0095
name: github-only-owner-endcap-with-reality-sync
domain: agent-workflows
kind: workflow
status: promoted
origin:
  project: Dionysus + ATM10-Agent + AoA ecosystem repos
  path: reports/ecosystem-audits/2026-04-07.cross-repo.federated-audit-remediation-rollout-session-harvest.md + reports/ecosystem-audits/2026-04-07.federated-audit-remediation.wave-4-ws12-github-track-packet.md + https://github.com/8Dionysus/ATM10-Agent/pull/50
  note: Extracted from the final federated audit-remediation endcap where a remote-only owner surface stayed GitHub-native through issue plus PR plus CI plus merge, and Dionysus then rebound its lineage and reality checks to the landed owner anchors.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - github
  - owner-truth
  - reality-sync
  - closeout
summary: Close a remote-only owner surface through GitHub-native issue and PR flow, then rebind staging and reality checks to the merged owner anchors so seed-garden truth does not outlive the landing.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-07
export_ready: true
relations:
  - type: complements
    target: AOA-T-0001
  - type: complements
    target: AOA-T-0092
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# github-only-owner-endcap-with-reality-sync

## Intent

Close a bounded remote-only owner surface through GitHub-native issue and PR
flow, then immediately sync the coordination or seed-garden layer to the merged
owner anchors so public staging truth does not linger past the real landing.

## When to use

- the final owning repository is intentionally GitHub-only in the current route
- the coordination layer can plan and track the work but must not pretend to
  own the landed meaning
- one bounded issue, milestone, or PR track is enough to express the owner-side
  endcap
- owner-native CI or PR checks can act as the validation surface before merge
- post-merge lineage and reality sync are necessary to keep staging markers
  honest

## When not to use

- a real local source checkout exists and is the intended execution surface
- the route still needs broader multi-repo choreography rather than one bounded
  owner-side endcap
- the work would require hidden credentials, private infra, or unrevealed host
  topology to explain the public contract
- the coordination layer is trying to keep sovereign meaning after the owner
  repo lands the change
- the route is really generic GitHub contribution hygiene without a staging or
  reality-sync seam

## Inputs

- one bounded owner-side goal with explicit non-goals
- one coordination or seed-garden surface that currently tracks the work
- one GitHub-native execution path such as issue plus milestone plus branch
  plus PR
- one owner-native validation surface such as CI jobs, repo checks, or review
  gates
- one explicit post-merge reality-sync path for the coordination layer

## Outputs

- one merged owner-side landing in the real repository
- one visible GitHub trail such as issue, milestone, and PR references
- one bounded validation result attached to the PR or merge
- one post-merge lineage update in the coordination layer
- one reality-check surface that now points at merged owner anchors instead of
  staged assumptions

## Core procedure

1. Start from one bounded track packet that names the goal, non-goals,
   validator of record, stop condition, and rollback marker.
2. Confirm that the owner surface should stay GitHub-only for this route and do
   not invent a local checkout as a hidden parallel source of execution.
3. Open or adopt one explicit GitHub tracking lane such as issue plus milestone
   plus PR branch so the owner-side work stays reviewable.
4. Land the smallest owner-side change that closes the bounded endcap without
   widening into broader product or runtime claims.
5. Let the owner-native PR checks or required reviews act as the proof surface
   before merge; repair inside that PR if the checks fail.
6. Merge in the owner repository first and treat the merged owner docs, code,
   or config as the new source anchor.
7. In the same follow-up pass, update the coordination or seed-garden layer so
   lifecycle markers, ledgers, and reality canaries point at the merged owner
   anchors rather than the old staged packet.
8. Preserve explicit non-goals and known limits so GitHub green checks do not
   inflate into broader platform or deployment claims.
9. Stop if the route starts requiring local execution, unrevealed host detail,
   or wider scenario policy than one owner-side endcap.

## Contracts

- the owner repository remains the source of truth for landed meaning
- GitHub-native execution does not create a second hidden local source of truth
- merge happens in the owner repo before coordination-layer truth is updated
- post-merge reality sync happens in the same closeout pass rather than as an
  optional later cleanup
- public claims stay bounded to what the owner-side docs and checks actually
  prove
- the technique stays smaller than full remediation-wave choreography or
  product support policy

Relationship to adjacent techniques: unlike
[AOA-T-0092](../audit-to-closeout-proof-loop/TECHNIQUE.md), this technique is
not about finding-first remediation proof across live source checkouts. It
begins later, when one bounded owner-side endcap must land through GitHub
rather than a local checkout. Unlike [AOA-T-0001](../plan-diff-apply-verify-report/TECHNIQUE.md),
it adds a stricter owner-truth rule: the coordination layer must rebind itself
to merged owner anchors immediately after the GitHub-native landing.

## Risks

### Failure modes

- the coordination layer updates its own staging note before the owner PR is
  really merged
- GitHub CI goes green on a narrow doc or smoke lane and the route starts
  over-claiming broader support or runtime parity
- a hidden local checkout appears and silently becomes the real execution
  source even though the route was supposed to stay GitHub-only
- reality canaries keep pointing at staged packets or stale anchors after the
  owner repo has already moved

### Negative effects

- the route adds ceremony when a local owner checkout would have been simpler
- GitHub-only execution can slow iteration compared with local source edits
- post-merge sync adds one more cleanup step that contributors may forget

### Misuse patterns

- using the technique as generic GitHub contribution advice outside a real
  owner-truth sync problem
- treating a coordination repo as if it can declare closure before the owner
  repo lands
- using one green PR as proof of wide product support beyond the bounded
  owner-side contract
- widening the bundle into full remediation-wave planning or playbook doctrine

### Detection signals

- lifecycle markers in the coordination repo still say staged-only after the
  owner PR merged
- owner-side docs and the coordination-layer summary disagree about what landed
- the route quietly depends on local files that the public GitHub track never
  mentions
- the PR validation surface is too weak to support the public claim now stored
  in the owner repo

### Mitigations

- require one explicit validator of record in the GitHub track packet
- keep owner-side non-goals visible inside the landed docs or PR summary
- update lineage and reality surfaces immediately after merge
- reject wider product or deployment claims that the landed owner-side checks do
  not prove

## Validation

Verify the technique by confirming that:
- the owner-side goal, non-goals, and stop condition were explicit before the
  PR landed
- the owner repository merged the bounded change through a visible GitHub trail
- the PR checks or required reviews named in the track packet passed before
  closure
- the coordination layer updated lifecycle or reality-check surfaces after the
  merge
- the final public-safe summary now points at merged owner anchors instead of
  staged assumptions

See `checks/github-only-owner-endcap-with-reality-sync-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact GitHub lane shape such as issue plus PR, issue plus draft PR, or PR
  only
- the owner-side validation surface such as docs checks, smoke tests, or a full
  test workflow
- the coordination layer that performs post-merge reality sync
- the specific anchor form such as GitHub URLs, raw URLs, or mirrored public
  docs

What should stay invariant:
- the owner repo lands first
- GitHub stays the declared execution surface when the route is GitHub-only
- post-merge reality sync happens immediately after the owner landing
- public claims stay bounded to merged owner evidence

Project-shaped details that should not be treated as invariant:
- one milestone number such as `#1`
- one issue or PR number such as `#49` or `#50`
- one owner doc path such as `docs/PRODUCT_EDGE_POSTURE.md`
- one specific seed-garden repo such as `Dionysus`
- one exact anchor type such as GitHub raw URLs

AoA adaptation example:
- keep the final remote-only owner endcap in `ATM10-Agent` GitHub-native
- let PR checks prove the bounded product-edge contract before merge
- then update `Dionysus` lifecycle markers, ledger, and owner-repo reality
  canary to point at the merged owner anchors instead of the staged pack

## Public sanitization notes

This public bundle keeps only the reusable law: bounded GitHub-native owner
landing first, then immediate reality sync in the coordination layer. Raw
terminal output, local temporary paths, private host details, and broader
product-edge claims were intentionally stripped.

## Example

See `examples/minimal-github-only-owner-endcap-with-reality-sync.md`.

## Checks

See `checks/github-only-owner-endcap-with-reality-sync-checklist.md`.

## Promotion history

- born from the 2026-04-07 federated audit-remediation rollout closeout and its
  GitHub-only `ATM10-Agent` endcap
- promoted into `aoa-techniques` on 2026-04-07 as a bounded workflow law for
  GitHub-native owner closure with immediate coordination-layer truth sync

## Future evolution

- keep broader wave choreography in `aoa-playbooks` instead of widening this
  bundle into a remediation program playbook
- add another non-identical GitHub-only owner context before considering
  canonical promotion
- revisit stronger canary patterns only if remote-owner anchor checking becomes
  common across more than one coordination lineage
