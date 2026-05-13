# Canonical Readiness

## Technique
- id: AOA-T-0082
- name: repair-shape-from-diagnosis

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the second context adaptation kept the contract bounded around repair shaping rather than checkpoint doctrine, playbook rollout, or generic self-improvement
- the bundle has a checklist, a public-safe example, and downstream route evidence where diagnosis must land before bounded repair follow-through
- `aoa-sdk` at `931e7460ca4afb85dc20d400e8fad7d7d2c294e6` surfaces `aoa-session-self-repair` only when a reviewed diagnosis receipt exists and no repair-cycle receipt has landed, making diagnosis-before-repair an executable closeout rule without running the repair itself
- `aoa-skills` growth-cycle examples show a reviewed diagnosis packet followed by a bounded `REPAIR_PACKET`/repair-cycle receipt with target owner repo, target artifact class, execution posture, validation health check, rollback marker, approval posture, iteration limit, stop conditions, and escalation route
- `aoa-playbooks` real-run and gate-review surfaces reinforce that post-repair closeout receipts can preserve a bounded repair packet and owner handoff without becoming a new skill, proof surface, memo, automation, runtime, or playbook promotion

## Default-use rationale
- this is useful when diagnosis already exists and the missing object is the smallest honest repair artifact
- it is strongest when a repair should stay smaller than a playbook but still needs one owner target, validation plan, stop cue, and escalation path
- it is now proven as the default local technique for turning a reviewed diagnosis into one bounded repair-shape artifact before checkpoint posture or scenario rollout
- it is still not a general self-improvement loop, checkpoint stack, playbook scenario, proof verdict, or runtime self-healing surface

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the published technique keeps the reusable repair-shaping seam while stripping local closeout commands, `.aoa` storage layout, playbook route names, and repo-specific repair wrappers

## Remaining gaps
- no canonical blocker remains for this promotion wave; a future non-AoA external adoption would widen evidence further but is not required for this bounded local canonical review
- downstream evidence ref: `repo:aoa-sdk/src/aoa_sdk/closeout/api.py` hash `346eb177214934df59971c5db4f987aae0a2310f`
- downstream evidence ref: `repo:aoa-sdk/tests/test_closeout.py` hash `ba918ac60162a004c51d7c688dfebfd535e6e32d`
- downstream evidence ref: `repo:aoa-skills/mechanics/growth-cycle/examples/session-growth-artifacts/diagnosis_packet.derived-visibility-handoff.json` hash `37101f6b0a30676dbe92dad9ed220493f17cd9bc`
- downstream evidence ref: `repo:aoa-skills/mechanics/growth-cycle/examples/session-growth-artifacts/repair_cycle.kernel-maturity.json` hash `ec755ffec562a8b78c9eb11505c5b943b5dd22d2`
- downstream evidence ref: `repo:aoa-skills/mechanics/growth-cycle/examples/session-growth-artifacts/repair_cycle_receipt.kernel-maturity.json` hash `4dc51d378e4cfb4b2d96e9fb40e6c6b0bdca0e11`
- downstream evidence ref: `repo:aoa-skills/docs/reviews/status-promotions/aoa-session-self-repair.md` hash `0794e413dad92153bd96953837a8cbce641a8ce5`
- downstream evidence ref: `repo:aoa-playbooks/docs/real-runs/2026-04-22.closeout-owner-follow-through-continuity.wave5-repair-post-closeout.md` hash `e96707ce656a5a945216392bc54d32cc137ec3de`
- boundary preserved: repair shape still starts after diagnosis, stays smaller than scenario rollout, and does not own checkpoint posture
- boundary preserved: SDK closeout rules, skill execution, playbook continuity, proof, memo, stats, and owner-object authorship stay downstream or neighboring surfaces

## Recommendation
- move `AOA-T-0082` to `canonical`
