# audit-to-closeout-proof-loop checklist

Use this checklist when reviewing whether an audit remediation pass still behaves like a bounded proof-backed closeout loop instead of drifting into generic triage or rollout theater.

- [ ] the source findings set is reviewed and bounded before remediation starts
- [ ] each closed finding was re-confirmed against live code or explicitly marked non-repro
- [ ] the owner repository and source checkout are named before mutation
- [ ] each closed finding has one targeted proof surface that matches the named failure mode
- [ ] an owner-level closeout surface reran after the bounded fixes landed
- [ ] deferred, uncertain, or follow-on findings remain explicit
- [ ] the route did not close findings only because one final full-suite pass was green
- [ ] the example still shows the difference between finding-level proof and broader closeout
