# Origin Evidence

## Technique
- id: AOA-T-0042
- name: upstream-skill-health-checking

## Source project
- name: `n-skills + MCP Gateway Registry`
- source files:
  - `n-skills/README.md`
  - `mcp-gateway-registry/README.md`

## Evidence
- `n-skills` keeps upstream-owned skills behind a declared `sources.yaml` manifest, daily sync, and preserved attribution, which makes source entry shape and upstream availability meaningful preconditions for any local surfacing
- the `n-skills` repository separates source declaration from editorial discovery, which supports a smaller pre-surface readiness seam before catalog curation
- MCP Gateway Registry describes an Agent Skills Registry with YAML frontmatter parsing for metadata extraction and health monitoring through URL accessibility checks
- MCP Gateway Registry also keeps broader registry capabilities, security scanning, and governance features visible as adjacent but larger concerns, which helps isolate a smaller readiness-only contract

## Interpretation
- the reusable object is one bounded readiness pass over upstream-owned skill sources before those sources are surfaced as selectable inputs
- the public technique can stay centered on source availability and manifest-readiness without importing sync automation, editorial discovery policy, registry governance, or security-scanning doctrine
