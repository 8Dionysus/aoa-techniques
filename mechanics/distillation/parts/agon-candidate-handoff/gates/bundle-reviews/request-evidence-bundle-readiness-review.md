# Request Evidence Bundle Readiness Review

Candidate:
`candidate:aoa-techniques:agon/request-evidence-practice`

Gate card:
[request-evidence-practice](../request-evidence-practice.md)

Gate example:
[request-evidence-minimal-public-safe](../examples/request-evidence-minimal-public-safe.md)

Gate checklist:
[request-evidence-gate-checklist](../checklists/request-evidence-gate-checklist.md)

Gate evidence note:
[request-evidence-gate-evidence-note](../evidence-notes/request-evidence-gate-evidence-note.md)

Status: bundle-readiness-review-landed, not a technique bundle.

## Verdict

Result: ready for one-bundle draft.

This verdict means the candidate has enough bounded shape to draft one
technique bundle under the normal `techniques/` path. It does not approve the
future bundle, change Agon source status, or promote this candidate.

Suggested draft slug: `single-missing-evidence-request`.

Landed bundle:
[single-missing-evidence-request](../../../../../../techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md)

## Atom Contract Read

- Atomic move: ask for exactly one missing evidence object that could change
  the current review state.
- Inputs are bounded: reviewed claim or decision point, current review state,
  acceptable evidence format, and stop line.
- Output is bounded: one evidence request with object, reason, and return
  condition for present or absent evidence.
- Stop condition is visible: if the object appears, update the review state; if
  it stays absent, keep the claim under review instead of issuing a verdict.
- Small-agent shape is plausible when an orchestrator supplies the claim,
  current state, and acceptable evidence format.

## Topology Read

- draft domain: `agent-workflows`
- draft kind: `guardrail`
- likely family: evidence-request or review-state narrowing; no stable
  frontmatter family yet
- likely capability class: request-evidence
- likely substrate: review state, claim text, citation gap, command receipt, or
  missing source artifact
- execution profile: small-agent after orchestration supplies local facts
- risk posture: read-only, external-evidence, proof-overclaim risk

The `evidence-request` wording belongs in family or capability notes, not in
current `kind` frontmatter. The bundle draft should use `guardrail` because the
move narrows review action and prevents closure without one concrete evidence
object.

## Draft Bounds

The later bundle draft should include:

- one `TECHNIQUE.md` centered on the single missing evidence request
- one checklist that fails broad research, verdicts, and evidence theater
- one public-safe example using a fictional review state
- origin evidence pointing back to this handoff packet
- a canonical-readiness note that keeps the first bundle below canonical
  promotion

The draft should not include Agon move law, actor behavior, arena protocol,
rank, scar, trust, routing, memory, KAG, ToS, runtime, skill workflow, or proof
authority.

## What This Does Not Support

- This review by itself does not promote the candidate into `techniques/`.
- It did not approve a future bundle before the draft existed.
- It does not change Agon source status or accept an owner request.
- It does not prove a claim or evaluate correctness.
- It does not authorize route, memory, KAG, runtime, rank, scar, skill, or arena
  effects.

## Stop Lines

- Do not define Agon evidence move law.
- Do not issue proof, verdict, route, memory, rank, scar, KAG, ToS, runtime, or
  skill effects.
- Do not carry `evidence-request` as current technique `kind`; use `guardrail`
  for the bundle draft unless the kind registry changes first.
- Do not treat this review as acceptance evidence for the future bundle; bundle
  local notes must carry bundle-local review evidence.
