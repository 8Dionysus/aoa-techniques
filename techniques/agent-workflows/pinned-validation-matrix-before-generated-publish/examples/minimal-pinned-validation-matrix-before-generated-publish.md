# minimal pinned-validation-matrix-before-generated-publish

```yaml
generated_publish:
  repo_root: /workspace/aoa-routing
  outputs:
    - generated/owner_layer_shortlist.min.json
  workflow_pinned_inputs:
    - repo: aoa-playbooks
      ref: origin/main
      required_surface: generated/playbook_review_status.min.json
    - repo: aoa-skills
      ref: workflow-pinned-sibling
      required_surface: generated/core_skill_receipt_contracts.min.json
  rebuild:
    command: python scripts/build_router.py --check
  publish_gate:
    requires:
      - pinned_matrix_rebuilt
      - generated_diff_honest
      - repo_validators_green
```

Why this example stays bounded:

- it names the generated outputs and the workflow-pinned inputs before publish
- it makes the pinned matrix explicit instead of treating local workspace state
  as automatically sufficient
- it shows one publish gate without widening into full release choreography
