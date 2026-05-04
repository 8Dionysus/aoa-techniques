# Challenge Claim Bundle Readiness Review

Candidate:
`candidate:aoa-techniques:agon/challenge-claim-practice`

Gate card:
[challenge-claim-practice](../challenge-claim-practice.md)

Gate example:
[challenge-claim-minimal-public-safe](../examples/challenge-claim-minimal-public-safe.md)

Gate checklist:
[challenge-claim-gate-checklist](../checklists/challenge-claim-gate-checklist.md)

Gate evidence note:
[challenge-claim-gate-evidence-note](../evidence-notes/challenge-claim-gate-evidence-note.md)

Status: bundle-readiness-review-landed, not a technique bundle.

## Verdict

Result: ready for one-bundle draft.

This verdict means the candidate has enough bounded shape to draft one
technique bundle under the normal `techniques/` path. It does not approve the
future bundle, change Agon source status, or promote this candidate.

Suggested draft slug: `single-locus-claim-challenge`.

## Atom Contract Read

- Atomic move: challenge exactly one target claim by naming one vulnerable
  locus, one pressure reason, one next support question, and one non-verdict
  stop condition.
- Inputs are bounded: target claim, current review state, challenged locus,
  pressure reason, and acceptable next-support form.
- Output is bounded: one challenge card that applies pressure without proving
  or disproving the claim.
- Stop condition is visible: once the challenge is stated, do not expand into
  proof, eval, routing, memory, actor eligibility, or debate choreography.
- Small-agent shape is plausible when an orchestrator supplies the target claim
  and acceptable next-support form.

## Topology Read

- draft domain: `agent-workflows`
- draft kind: `guardrail`
- likely family: claim-pressure or review-evidence practice; no stable
  frontmatter family yet
- likely capability class: challenge-claim
- likely substrate: claim text, asserted summary, generated statement, or
  review claim
- execution profile: small-agent after orchestration supplies local facts
- risk posture: read-only, tone-as-evidence, hidden-verdict risk

The `challenge` wording belongs in family, capability, substrate, or tag notes,
not in current `kind` frontmatter. The bundle draft should use `guardrail`
because the move blocks overclaim and false closure while staying smaller than
proof, diagnosis, or adjudication.

## Draft Bounds

The later bundle draft should include:

- one `TECHNIQUE.md` centered on the single-locus claim challenge
- one checklist that fails broad debate, tone-as-evidence, hidden verdicts, and
  multi-claim pressure
- one public-safe example using a fictional review state
- origin evidence pointing back to this handoff packet
- a canonical-readiness note that keeps the first bundle below canonical
  promotion

The draft should not include Agon move law, actor behavior, arena protocol,
rank, scar, trust, routing, memory, KAG, ToS, runtime, skill workflow, eval
adequacy, or proof authority.

## Reform Thread

This candidate is a useful topology probe for the later technique reform. It
shows why the corpus needs family, capability, substrate, execution profile, and
risk axes: `guardrail` is the current kind, while challenge-claim is the
capability, claim text is the substrate, and hidden-verdict drift is the risk
posture.

## What This Does Not Support

- This review by itself does not promote the candidate into `techniques/`.
- It did not approve a future bundle before the draft existed.
- It does not change Agon source status or accept an owner request.
- It does not prove or disprove a claim.
- It does not authorize route, memory, KAG, runtime, rank, scar, skill, actor,
  or arena effects.

## Stop Lines

- Do not define Agon stance move law.
- Do not issue proof, verdict, route, memory, rank, scar, KAG, ToS, runtime, or
  skill effects.
- Do not carry `challenge` as current technique `kind`; use `guardrail` for the
  bundle draft unless the kind registry changes first.
- Do not treat this review as acceptance evidence for the future bundle; bundle
  local notes must carry bundle-local review evidence.
