# Render Truth Before Startup Checklist

- [ ] The runtime selection can be rendered before startup.
- [ ] The render step shows the actual composed runtime view rather than only declared profiles or modules.
- [ ] A lightweight service-list render exists.
- [ ] A deeper full-config render exists when deeper local review is needed.
- [ ] Full rendered config is treated as potentially secret-bearing local material.
- [ ] The render step is clearly read-only.
- [ ] The workflow reviews rendered truth before `up`, `wait`, or similar startup steps.
- [ ] The technique does not drift into host-readiness checks.
- [ ] The technique does not drift into smoke, probe, or lifecycle control.
- [ ] Rendered config is not treated as a public artifact or new canonical source of truth.
