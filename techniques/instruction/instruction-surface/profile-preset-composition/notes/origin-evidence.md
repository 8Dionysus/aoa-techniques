# Origin Evidence

## Technique
- id: AOA-T-0035
- name: profile-preset-composition

## Source project
- name: abyss-stack
- source files:
  - `Configs/docs/PROFILES.md`
  - `Configs/docs/PRESETS.md`
  - `Configs/docs/PROFILE_RECIPES.md`
  - `Configs/compose/README.md`
  - `Configs/compose/presets/README.md`
  - `Configs/scripts/aoa-lib.sh`
  - `Configs/scripts/aoa-preset-profiles`
  - `Configs/scripts/aoa-profile-modules`
  - `Configs/scripts/aoa-profile-endpoints`

## Evidence
- the donor docs define profiles as small ordered module lists rather than as hidden fragments of one giant compose file
- the donor docs and preset files define presets as named ordered bundles of profiles one layer above direct profile composition
- the donor resolution logic expands presets first, appends directly selected profiles afterward, and keeps duplicate profiles and modules only once at first appearance
- the donor inspection scripts expose resolved presets, profiles, modules, paths, and expected endpoints before launch instead of making launch the first point where composition becomes visible

## Interpretation
- the reusable object is the layered composition contract across modules, profiles, and presets
- the public technique can stay bounded to ordered composition, first-appearance dedupe, and inspection-before-run without importing donor-specific ports, deployment roots, or lifecycle wrappers
