# Contextual Host Doctor Checklist

- [ ] The diagnostic runs before startup.
- [ ] The selected runtime changes which checks are relevant.
- [ ] Item-level `ok`, `warn`, and `fail` signals remain visible.
- [ ] Context-specific checks do not appear when the selected runtime does not make them relevant.
- [ ] Hard blockers remain distinct from advisory warnings.
- [ ] Strict mode behavior is explicit rather than implicit.
- [ ] The technique stays diagnostic and read-only.
- [ ] The bundle does not drift into rendered runtime truth.
- [ ] The bundle does not drift into smoke, health, or internal probes.
- [ ] The bundle does not widen into generic monitoring or lifecycle control.
