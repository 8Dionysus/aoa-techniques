# Second Context Adaptation

## Technique
- id: AOA-T-0048
- name: semantic-review-surface-lift

## Target project
- support name: aoa-playbooks review-status surface
- support repository: `aoa-playbooks`
- support public surfaces:
  - `docs/gate-reviews/*.md`
  - `docs/real-runs/*.md`
  - `docs/PLAYBOOK_EXECUTION_SEAM.md`
  - `scripts/generate_playbook_review_status.py`
  - `generated/playbook_review_status.min.json`

## What changed
- source review shape: `aoa-playbooks` keeps gate-review notes as authored markdown with required sections for gate header, minimum evidence threshold, latest reviewed run, dual signal check, current verdict, and next trigger.
- review evidence boundary: reviewed run summaries stay as authored markdown under `docs/real-runs/`, and gate-review notes must reference the exact reviewed run summaries accepted for the owning playbook.
- derived reader shape: `generated/playbook_review_status.min.json` exposes compact review-status entries with gate-review ref, reviewed-run refs, threshold, verdict token, next trigger, and composition-signal summary.
- generator contract: `scripts/generate_playbook_review_status.py` parses authored markdown, rejects missing sections, validates playbook ids, checks reviewed-run references against the committed real-run summaries, and emits the derived reader.
- source-of-truth statement: `docs/PLAYBOOK_EXECUTION_SEAM.md` states that the review-status output is an evidence-posture surface for downstream readers, not a replacement for authored reviewed summaries or gate-review notes.

## What stayed invariant
- authored review notes remain the source of review meaning.
- the derived reader is compact, review-shaped, and traceable back to markdown notes.
- the generated surface helps readers find review posture; it does not become the review authority.
- gate verdict tokens in `aoa-playbooks` remain playbook-layer evidence posture, not technique promotion verdicts.
- playbook scenario law, composition governance, real-run ownership, and release gates stay outside this technique.

## Risks introduced by adaptation
- a clean review-status reader can look more authoritative than the underlying gate-review notes.
- verdict tokens such as `hold` or `composition-landed` can be mistaken for generic quality scores if the playbook boundary is ignored.
- the technique could overreach if it imports playbook composition semantics instead of only reusing the source-review to derived-reader split.
- future review-status fields could widen toward dashboards or automation unless the source-trace rule stays explicit.

## Evidence
- `docs/gate-reviews/validation-driven-remediation.md` is an authored gate-review note with the required review sections and a bounded next trigger.
- `scripts/generate_playbook_review_status.py` requires gate-review sections, requires real-run summary sections, parses owning playbook ids, checks exact reviewed-run references, and renders `generated/playbook_review_status.min.json`.
- `generated/playbook_review_status.min.json` carries `gate_review_ref`, `reviewed_run_refs`, `minimum_evidence_threshold`, `gate_verdict`, `next_trigger`, and `composition_signal_summary` for downstream review lookup.
- `docs/PLAYBOOK_EXECUTION_SEAM.md` names `generated/playbook_review_status.min.json` as a downstream evidence-posture surface and explicitly keeps it subordinate to authored reviewed summaries and gate-review notes.

## Result
- cross-context adaptation accepted
- `aoa-playbooks` closes the missing non-origin review-reader proof for this bundle
- promote `AOA-T-0048` to canonical while keeping scoring, automated status transitions, graph semantics, playbook composition law, and review authority outside the technique
