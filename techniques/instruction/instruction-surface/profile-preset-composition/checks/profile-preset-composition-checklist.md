# Profile Preset Composition Checklist

- [ ] Atomic runtime units are defined separately from profiles and presets.
- [ ] Each profile is an ordered list of modules or equivalent atomic units.
- [ ] Each preset is an ordered list of profile names.
- [ ] Preset-expanded profiles resolve before direct profile additions.
- [ ] Duplicate profiles are kept only once, at first appearance.
- [ ] Duplicate modules are kept only once, at first appearance.
- [ ] Profile and preset definitions stay small, plain, and reviewable.
- [ ] Missing profile or module references fail fast instead of degrading silently.
- [ ] A read-only inspection path exists before launch.
- [ ] The technique does not drift into rendered runtime truth, readiness checks, or lifecycle control.
- [ ] Presets do not become a hiding place for unrelated capability bundles.
- [ ] The example and wording remain public-safe and portable.
