# Origin Evidence

## Technique
- id: AOA-T-0046
- name: repo-doc-surface-lift

## Source project
- name: aoa-techniques
- source files:
  - `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md`
  - `generated/repo_doc_surface_manifest.json`
  - `docs/REPO_DOC_SURFACES.md`

## Evidence
- `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md` explicitly frames a bounded public docs/status source class and excludes local planning docs, deeper guides, and review docs
- `generated/repo_doc_surface_manifest.json` shows the current public repo-doc set as a bounded derived routing surface
- `docs/REPO_DOC_SURFACES.md` exposes the same bounded routing contract to readers without replacing the authored docs

## Interpretation
- the live repository already uses a bounded public repo-doc routing layer as a derived reader surface
- the reusable pattern is repo-doc routing from authored markdown, not a generalized documentation taxonomy or policy engine
