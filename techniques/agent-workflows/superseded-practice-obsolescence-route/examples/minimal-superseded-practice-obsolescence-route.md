# Minimal superseded-practice obsolescence route

```yaml
route_type: superseded_practice_obsolescence_route
practice: draft-wide-adoption-template
current_stage: shadowed_after_two_reviews
owner_receipt_target: technique authoring workflow owner
reason_not_active_as_is: the template combines adoption, retention, and skill proposal fields, so small-agent execution keeps drifting
route_label: reanchor
reanchor_target: split the reusable adoption gate, retention review, and skill proposal packet into separate technique candidates
replacement_or_target_known: true
source_evidence:
  - shadow review notes show repeated confusion between adoption and activation
  - later bundle extractions succeeded after the fields were split
rollback_or_quarantine_path: keep the draft template quarantined as source evidence until the split techniques are reviewed
retained_lesson: broad lifecycle templates hide owner boundaries unless each reusable move has its own stop-line
downstream_hints:
  memory: optional retained lesson after owner review
  stats: count as reanchored, not deleted
  proof: no proof verdict claimed
stop_line: this packet routes the practice; it does not delete the draft, mark it deprecated, or accept the replacement
```

The route names why the shadowed practice should not stay active and where it
should go next. It preserves the evidence and lesson without performing the
owner-local retirement action.
