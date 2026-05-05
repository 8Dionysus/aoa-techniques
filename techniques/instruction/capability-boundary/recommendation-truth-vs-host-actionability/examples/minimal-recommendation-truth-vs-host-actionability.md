# minimal recommendation-truth-vs-host-actionability

```yaml
skill_dispatch:
  router_recommendations:
    activate_now:
      - aoa-change-protocol
      - aoa-sanitized-share
  host_inventory:
    source: repo-install
    roots_checked:
      - /workspace/project/.agents/skills
      - /workspace/.agents/skills
      - /user-skill-root/.agents/skills
    present_skills:
      - aoa-change-protocol
  annotated_result:
    activate_now:
      - skill_name: aoa-change-protocol
        host_availability:
          status: host-executable
          source: repo-install
    must_confirm:
      - skill_name: aoa-sanitized-share
        reason: strong router match; host inventory is router-only for this skill
        host_availability:
          status: router-only
          source: repo-install
          manual_fallback_allowed: true
    actionability_gaps:
      - aoa-sanitized-share
```

Why this example stays bounded:

- it separates recommendation truth from host actionability instead of blending them into one verdict
- it demotes a non-executable auto-action instead of silently dropping it
- it keeps install-root discovery explicit without widening into marketplace or registry policy
