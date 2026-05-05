# Canonical Readiness

## Technique
- id: AOA-T-0023
- name: stateless-single-shot-agent

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around provider-profile breadth, history toggles, and other product-width behavior
- second context: GitHub Copilot CLI now provides an independent public shell-side fast path where a single prompt can run programmatically, complete, and exit while mutating or command-executing tools stay approval-gated by default
- local boundary sweep: `aoa-routing`, `aoa-agents`, `aoa-evals`, `aoa-skills`, and `aoa-playbooks` all stayed adjacent-only on the latest local pass, which closed false-positive lanes around routing, checkpoint, dry-run, and governed multi-step flows rather than weakening the current bundle
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, a closed adjacent-only local lane sweep, and one real public terminal-agent second context beyond the donor lineage

## Default-use rationale
- this is the right default when shell-side agent work should stay mostly stateless, low-ceremony, and confirmation-gated instead of widening into a hidden multi-step session
- it remains narrower than `AOA-T-0001`, which stays the default workflow backbone for non-trivial repository changes that need planning, verification, and reporting across more than one step
- it remains narrower than `AOA-T-0028`, which centers the explicit confirmation seam itself, and `AOA-T-0031`, which centers shell composability through stdin/stdout/files rather than the broader low-memory fast-path posture
- the current evidence now shows that the single-shot fast path survives outside the original donor lineage, so the bundle reads as the natural default when quick shell-side work should stay bounded before escalating to a richer workflow

## Fresh public-safety check
- review date: 2026-03-23
- result: pass
- sanitization still holds: the bundle keeps only the reusable single-shot invocation contract and excludes donor-specific configuration, provider, and install detail
- public reuse check: the public examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on one-prompt shell-side fast paths and does not widen into interactive session doctrine, general approval policy, or multi-step autonomous loops
- future review should keep watching for hidden continuity, broad auto-approval defaults, and tool-step creep that would make the contract less bounded than this current canonical default

## Recommendation
- promote `AOA-T-0023` to `canonical`
- use `AOA-T-0023` as the default shell-side fast-path technique when quick agent work should stay mostly stateless, low-memory, and explicitly approval-gated before broader workflow escalation
