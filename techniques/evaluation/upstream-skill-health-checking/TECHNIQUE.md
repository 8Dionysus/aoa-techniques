---
id: AOA-T-0042
name: upstream-skill-health-checking
domain: evaluation
status: promoted
origin:
  project: n-skills + MCP Gateway Registry
  path: README.md
  note: Distilled from external skill-source flows that combine declared upstream manifests with pre-surface URL and metadata checks so broken or malformed sources do not silently reach discovery surfaces.
owners:
  - 8Dionysus
tags:
  - evaluation
  - upstream
  - skills
  - health
  - manifest
summary: Check upstream-owned skill sources for availability and manifest-readiness before surfacing them as selectable inputs so broken entries stay visible and reviewable without widening into generic monitoring, registry governance, or security doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0041
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# upstream-skill-health-checking

## Intent

Expose whether an upstream-owned skill source is selectable enough before it reaches a catalog or selector by checking source availability and manifest-readiness through one bounded pre-surface readiness pass.

## When to use

- a catalog, marketplace, or selector depends on upstream-owned skill sources that can disappear, move, or degrade
- reviewers need one bounded readiness verdict before a source is surfaced as selectable input
- the source contract depends on a declared manifest, card, or metadata file being reachable and minimally parseable
- you need to distinguish unreachable sources from malformed source declarations without widening into a broader registry program
- the reusable object is source-readiness checking, not mirroring, curation, or security scanning

## When not to use

- the main need is upstream mirroring plus provenance preservation
- the main need is editorial discovery and category curation over already-readable skills
- the real need is generic uptime monitoring, alerting, or continuous observability
- the real need is registry governance, access control, or routing policy
- the real need is vulnerability scanning, trust scoring, or broader supply-chain review

## Inputs

- one upstream source entry that names the skill location
- one expected manifest or metadata shape such as `SKILL.md`, frontmatter, or an equivalent card
- one bounded fetch or read path that can confirm whether the source is reachable
- one minimal readiness rule that distinguishes selectable, review-needed, and blocked states
- one pre-surface checkpoint where the result can be reviewed before catalog or selector publication

## Outputs

- one source-readiness verdict for the upstream entry before it is surfaced
- explicit visibility into whether the source is unreachable, malformed, or ready enough to inspect
- lower pressure to let broken upstream entries silently appear in curated discovery surfaces
- one bounded handoff into curation, mirroring, or manual review after the source-readiness check

## Core procedure

1. Resolve the upstream source entry that is supposed to feed the local catalog, registry, or selector.
2. Check that the source location is reachable through the same public path the local surface would depend on.
3. Confirm that the expected manifest or metadata file exists at the declared location.
4. Parse only the minimal shape needed to decide whether the source can be surfaced for inspection or selection.
5. Emit an explicit readiness verdict such as `ready`, `review`, or `blocked` so broken entries do not fail silently.
6. Keep the result tied to one source entry rather than turning it into a global registry score.
7. Hand off curation, mirroring, security review, or deeper policy decisions to separate sibling techniques.

## Contracts

- the check stays upstream-source-facing and runs before catalog or selector surfacing
- source availability and manifest-readiness remain the center of the verdict
- the technique keeps unreachable, malformed, and ready-enough states distinct
- one broken source does not require the bundle to become a full registry-governance or monitoring program
- the result can block or flag one source entry without becoming a quality ranking system
- the technique does not own mirroring, provenance, editorial curation, capability contracts, routing policy, or security scanning doctrine

Relationship to adjacent techniques: unlike `AOA-T-0024 upstream-mirroring-with-provenance`, this technique does not mirror upstream content or preserve provenance metadata; it stops at source readiness before any sync or local copy exists. Unlike `AOA-T-0041 skill-marketplace-curation`, it does not decide how readable or well-grouped a surfaced skill collection should be; it decides only whether one upstream source is selectable enough to reach that curation layer. Unlike `AOA-T-0032 context-report-for-ci`, it is not a broad CI-facing composition report; it stays attached to one upstream source entry and one bounded readiness decision. Unlike the broader MCP Gateway Registry platform, it does not own registry governance, access control, federation policy, or security scanning.

## Risks

### Failure modes

- transient network issues get mistaken for permanent source invalidity
- the check surface grows until it behaves like a generic monitoring suite
- manifest validation drifts from minimal readiness into policy enforcement or quality scoring
- teams assume a ready source is trustworthy or high quality simply because it is reachable and parseable

### Negative effects

- pre-surface checks add gating friction for upstream-source additions
- a strict blocked verdict can temporarily hide otherwise useful sources during short outages
- minimal readiness checks can give false confidence if reviewers forget they only test availability and shape
- maintaining a readiness surface adds upkeep beyond plain catalog ingestion

### Misuse patterns

- widening the check into generic monitoring, incidents, or uptime dashboards
- widening the check into registry policy, permissions, or federation governance
- bundling in vulnerability scanning or broader security doctrine to make the verdict feel more complete
- turning readiness into a ranking or trust score for upstream sources

### Detection signals

- the output starts reading like a monitoring dashboard instead of a bounded pre-surface verdict
- contributors discuss policy gates, registry modes, or permissions more than source reachability and manifest shape
- vulnerability scans or compliance labels appear in the same verdict that is supposed to stay readiness-only
- selectors still surface broken sources even though the readiness pass exists

### Mitigations

- keep the readiness rule minimal and limited to source availability plus manifest-readiness
- separate transient `review` states from hard `blocked` states whenever the evidence is ambiguous
- route security scanning, governance, and curation into sibling techniques instead of widening this bundle
- review the minimal manifest requirements whenever upstream source formats change

## Validation

Verify the technique by confirming that:
- an unreachable source is distinguishable from a malformed but reachable source
- the verdict stays tied to source availability and manifest-readiness rather than broader policy
- broken upstream entries are visible before they reach catalog or selector surfaces
- the bundle does not drift into mirroring, curation, monitoring, registry governance, or security scanning
- reviewers can explain why a source is `ready`, `review`, or `blocked`

See `checks/upstream-skill-health-checking-checklist.md`.

## Adaptation notes

What can vary across projects:
- the source location format
- the exact manifest or metadata carrier
- whether the check runs in CI, a publish step, or a manual review command
- the exact wording of the readiness states

What should stay invariant:
- the verdict runs before selector or catalog surfacing
- source availability remains explicit
- minimal manifest-readiness remains explicit
- the bundle stays bounded to source-readiness rather than broader governance or monitoring

Project-shaped details that should not be treated as invariant:
- daily sync schedules
- registry UI modes
- security-scanner products
- authentication or access-control flows
- semantic-search or ranking behavior

## Public sanitization notes

This public bundle keeps only the reusable source-readiness contract: check that an upstream skill source is reachable and minimally parseable before it is surfaced locally. Registry governance, security scanning, identity systems, sync automation, and donor-specific URLs were intentionally left out of the public technique contract.

## Example

See `examples/minimal-upstream-skill-health-checking.md`.

## Checks

See `checks/upstream-skill-health-checking-checklist.md`.

## Promotion history

- shaped from `n-skills` source-manifest posture and MCP Gateway Registry skills-source checks
- promoted to `aoa-techniques` on 2026-03-23 as a bounded evaluation technique for pre-surface upstream source readiness

## Future evolution

- keep `AOA-T-0041` as the curated discovery sibling rather than widening this bundle into editorial marketplace policy
- keep `AOA-T-0024` as the mirroring and provenance sibling rather than turning readiness into sync doctrine
- add a second live context that uses the same readiness boundary without dragging in security or governance control planes
