# Challenge Claim Practice Gate Card

Source candidate:
`candidate:aoa-techniques:agon/challenge-claim-practice`

Source route:
[Agon Move Technique Bridge](../../../../agon/parts/move-technique-bridge/README.md)
via [Agon Candidate Handoff](../README.md).

Center source check:
`Agents-of-Abyss` lawful move grammar lists `challenge_claim` as a pre-protocol
stance move that contests a claim by naming the vulnerable locus without
issuing a verdict. Owner binding keeps the center law, technique practice,
skill workflow, eval relevance check, and actor-eligibility surfaces separate,
with no live protocol or runtime effect.

## Gate Posture

Status: gate-packet-landed, not a technique bundle.

Lane: `first_narrowing_watch`.

This card proves only that the candidate can be challenged as one portable
practice move. It does not define Agon stance law, create a skill, issue a
proof verdict, write memory, or start arena behavior.

## Atom

Challenge exactly one claim by naming its vulnerable locus and the next support
question, without deciding whether the claim is false.

The move has five fields:

- target claim
- challenged locus inside the claim
- pressure reason
- next evidence, scope, or revision question
- non-verdict stop condition

## Gate Example

- [challenge-claim-minimal-public-safe](examples/challenge-claim-minimal-public-safe.md)

## Gate Checklist

- [challenge-claim-gate-checklist](checklists/challenge-claim-gate-checklist.md)

## Gate Evidence Note

- [challenge-claim-gate-evidence-note](evidence-notes/challenge-claim-gate-evidence-note.md)

## Topology Read

| Axis | Read |
|---|---|
| likely domain | `agent-workflows` |
| primary kind | `challenge` as handoff-facing posture; later bundle must map to a registry kind |
| family posture | claim-pressure and review-evidence practice; gate packet landed locally |
| capability class | challenge-claim |
| substrate | claim text, asserted summary, generated statement, or review claim |
| execution profile | small-agent when the target claim is already bounded |
| risk posture | argument escalation, tone-as-evidence, hidden verdict drift |

The `challenge` wording is useful as a family or capability posture. It is not
currently a frontmatter `kind`; any later bundle must choose an existing kind
such as `guardrail` or `assessment` before promotion.

## Portable Core

The portable core is not Agon law. It is a small review move:

1. Name the exact claim being challenged.
2. Name the vulnerable locus inside that claim.
3. State why that locus is under pressure.
4. Ask the next evidence, scope, or revision question.
5. Stop before proof, verdict, rank, scar, route, memory, or arena effects.

This works outside OS Abyss when the orchestrator supplies the claim, current
review state, and acceptable next-support form.

## AoA-Only Context

Inside AoA, Agon may supply the pressure source and legal move name. That
context stays outside the technique atom. The technique candidate may learn the
hand motion, not the law of the arena.

## Nearest Overlaps

- [single-missing-evidence-request](../../../../../techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md):
  asks for one missing evidence object; this candidate first names the claim
  locus that makes the request relevant.
- `localize_contradiction-practice`:
  narrows a contradiction after conflicting claims are already in view; this
  candidate can challenge one claim before a contradiction is established.
- [diagnosis-from-reviewed-evidence](../../../../../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md):
  diagnoses from reviewed evidence; this candidate only applies pressure to one
  claim and names the next support question.

## Stop Lines

- Do not define Agon stance move law.
- Do not issue proof, verdict, route, memory, rank, scar, KAG, ToS, runtime, or
  skill effects.
- Do not turn challenge into tone, personal attack, debate theater, or final
  adjudication.
- Do not treat `challenge` as a current frontmatter kind.
- Do not draft a technique bundle until the readiness review chooses a
  registry-backed kind.

## Next Move

Run one bundle-readiness review only if the challenge stays one claim, one
locus, one pressure reason, one next support question, and one non-verdict stop
condition.
