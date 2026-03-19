# Origin Evidence

## Technique
- id: AOA-T-0018
- name: markdown-technique-section-lift

## Source project
- name: aoa-techniques
- source files:
  - `scripts/build_section_manifest.py`
  - `generated/technique_section_manifest.json`
  - `docs/KAG_SOURCE_LIFT_GUIDE.md`

## Evidence
- `scripts/build_section_manifest.py` already derives a bounded section manifest from authoritative `TECHNIQUE.md` bundles instead of asking maintainers to author section metadata separately
- `generated/technique_section_manifest.json` shows the current repo already consumes that lift as a stable derived surface
- `docs/KAG_SOURCE_LIFT_GUIDE.md` explicitly frames section lift as a bounded family member rather than a graph or schema program

## Interpretation
- the reusable pattern already exists in a live public repository as markdown-first source lift with a generated section surface
- the technique is not speculative; it is a compact generalization of the section-manifest behavior that `aoa-techniques` already uses
