# Origin Evidence

## Technique
- id: AOA-T-0019
- name: frontmatter-metadata-spine

## Source project
- name: aoa-techniques
- source files:
  - `scripts/build_catalog.py`
  - `generated/technique_catalog.json`
  - `generated/technique_catalog.min.json`
  - `docs/FRONTMATTER_METADATA_SPINE_GUIDE.md`

## Evidence
- `scripts/build_catalog.py` already projects bounded frontmatter into derived catalog outputs rather than asking maintainers to keep a second metadata source by hand
- `generated/technique_catalog.json` and `.min.json` already act as bundle-level routing surfaces for status, domain, summary, evidence handles, and direct adjacency
- `docs/FRONTMATTER_METADATA_SPINE_GUIDE.md` explicitly frames this behavior as a metadata spine and keeps section meaning outside frontmatter

## Interpretation
- the technique is grounded in an active public repository where shallow frontmatter already powers real generated navigation outputs
- the reusable contract is the bounded metadata split, not the exact shape of one repository's catalog JSON
