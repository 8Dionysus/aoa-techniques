# Tool-Gateway Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Tool-Gateway Direct-Read Singleton Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/tool-gateway-direct-read-singleton-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Twenty-eighth authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0065` | `techniques/agent-workflows/mcp-gateway-proxy/` | `techniques/tool-use/tool-gateway/mcp-gateway-proxy/` |

## Preserved

- ID stayed unchanged.
- `domain` stayed unchanged as `agent-workflows`.
- `kind` stayed unchanged as `composition`.
- The bundle stayed `promoted`; path movement did not imply canonical
  promotion.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with the bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`tool-gateway` remains a tool-use shelf for one reviewable gateway proxy seam
in front of configured upstream MCP or tool-provider surfaces. It does not
become runtime deployment ownership, local stack lifecycle, connector registry
authority, API gateway product doctrine, tool marketplace curation,
security-scanner doctrine, trust scoring, skill activation, proof verdict
authority, route mutation, or canonical promotion.

## Verification Lane

Expected validation for the migration wave:

```bash
python -m unittest tests.test_distillation_mechanics_topology tests.test_root_legacy_topology tests.test_validate_repo tests.test_skill_discovery_tree_pilot tests.test_roadmap_parity
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python scripts/release_check.py
```
