# Origin Evidence

## Technique
- id: AOA-T-0036
- name: render-truth-before-startup

## Source project
- name: abyss-stack
- source files:
  - `docs/RENDER_TRUTH.md`
  - `docs/FIRST_RUN.md`
  - `docs/LIFECYCLE.md`
  - `docs/DEPLOYMENT.md`
  - `scripts/aoa-render-services`
  - `scripts/aoa-render-config`

## Evidence
- the donor explicitly separates docs and profile descriptions, profile/module introspection, post-start probes, and the actual composed runtime truth that Compose sees before launch
- the donor provides one render path for the effective service list and a deeper render path for the full composed config before startup
- the donor repeatedly places rendered-truth review before `up`, `wait`, or smoke steps in first-run and lifecycle guidance
- the donor warns that full rendered config may be secret-bearing and should stay local rather than becoming a committed or public artifact

## Interpretation
- the reusable object is a read-only pre-start render-review seam over the actual composed runtime view
- the public technique can stay bounded to pre-start rendered truth without importing donor-specific lifecycle wrappers, deployment paths, or post-start health logic
