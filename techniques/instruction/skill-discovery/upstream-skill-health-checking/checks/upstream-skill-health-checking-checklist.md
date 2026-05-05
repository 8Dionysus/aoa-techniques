# Upstream Skill Health Checking Checklist

- [ ] The check runs before the source is surfaced in a selector, catalog, or marketplace.
- [ ] Source availability is checked explicitly.
- [ ] Manifest or metadata readiness is checked explicitly.
- [ ] The bundle distinguishes `ready`, `review`, and `blocked` states.
- [ ] An unreachable source stays distinct from a malformed but reachable source.
- [ ] The verdict stays tied to one source entry rather than becoming a global registry score.
- [ ] The technique does not drift into `AOA-T-0024` mirroring or provenance behavior.
- [ ] The technique does not drift into `AOA-T-0041` editorial discovery or category curation.
- [ ] The technique does not widen into generic monitoring, registry governance, routing policy, or security scanning.
- [ ] The example still reads as a bounded pre-surface readiness pass rather than a full registry platform.
