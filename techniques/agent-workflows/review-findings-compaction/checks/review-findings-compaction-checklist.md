# review-findings-compaction checklist

Use this checklist when reviewing whether a findings compaction pass still behaves like a bounded verification-and-consolidation surface instead of drifting into issue management or remediation policy.

- [ ] duplicate grouping stays reviewable and explainable
- [ ] findings are revalidated against current code before they survive
- [ ] stale findings are removed or marked explicitly
- [ ] representative findings keep traceability back to source findings
- [ ] merged findings still cite live code locations
- [ ] the compacted artifact stays smaller than generic issue-management doctrine
- [ ] compaction remains separate from remediation and prioritization
- [ ] at least one example shows both dedupe and stale-finding handling
