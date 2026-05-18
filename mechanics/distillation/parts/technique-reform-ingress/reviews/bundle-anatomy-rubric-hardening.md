# Bundle Anatomy Rubric Hardening

Source packet: [Technique Reform Ingress](../README.md)

Baseline packet: [Bundle Anatomy Baseline Inventory](bundle-anatomy-baseline-inventory.md)

Durable closeout: [Bundle Anatomy Final Closeout Ledger](bundle-anatomy-final-closeout-ledger.md)

Status: direct-read-rubric-hardening, not leaf repair, not path movement, not
frontmatter migration, not status promotion.

## Verdict

Harden the bundle-reform audit rubric before shelf-wide audits begin.

The baseline inventory proved presence and parity across all `107` bundles, but
`inventory-pass` is not a quality verdict. Direct reading across five
representative bundles shows the reform audit needs three separated layers:

1. mechanical inventory signals
2. human anatomy verdicts
3. repair or route actions

This packet does not edit any technique leaf. It calibrates how later shelf
audits should classify atomicity, small-agent usability, portability,
generated-reader quality, owner-boundary pressure, and promotion evidence
without collapsing those concerns into one label.

## Direct-Read Set

| id | role in rubric test | bundle | result |
|---|---|---|---|
| `AOA-T-0001` | canonical core | `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md` | healthy canonical exemplar; old-template watch only |
| `AOA-T-0055` | promoted planning | `techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md` | healthy promoted external import; promotion evidence still held |
| `AOA-T-0074` | portability-heavy source ingest | `techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md` | healthy source-specific portable seam; auth/session/memory boundary watch |
| `AOA-T-0096` | proof/generated-publish adjacent | `techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md` | healthy technique atom; capsule short-text defect candidate |
| `AOA-T-0065` | tool/runtime adjacent | `techniques/tool-use/tool-gateway/mcp-gateway-proxy/TECHNIQUE.md` | healthy proxy-seam atom; runtime/security/platform boundary watch |

## Hardened Label Layers

### Layer 1: Inventory Signals

Use these only for mechanical presence or parity.

| label | meaning | may trigger |
|---|---|---|
| `inventory-pass` | catalog, capsule, tree projection, examples, checks, and notes are present enough for direct read | direct-read audit, not repair |
| `presence-gap` | required support surface is missing | direct read and support-surface repair planning |
| `projection-gap` | generated path/catalog/capsule row is missing or mismatched | generated parity investigation |
| `support-count-watch` | support files exist but count or shape looks unusually thin | direct read, not automatic repair |

### Layer 2: Human Anatomy Verdicts

Use these after direct reading authored bundle meaning and support surfaces.

| label | meaning | stop-line |
|---|---|---|
| `anatomy-pass` | one atomic move is clear, executable, portable enough, and supported | not a status promotion |
| `old-template-watch` | bundle predates explicit `Atomic move` or `Small-agent execution shape` sections but still carries the move clearly | do not rewrite only for template symmetry |
| `small-agent-gap` | selected technique would leave a small model unsure about action, stop line, or output | repair only after bundle-specific evidence |
| `portability-watch` | technique is portable, but one origin-specific boundary must stay visible | caution label, not failure |
| `owner-boundary-watch` | sibling-owner pressure is real but currently held outside the atom | do not route away unless the atom collapses |
| `capsule-gap` | generated capsule or source summary fails to carry the executable center | inspect source vs builder before repair |
| `atomicity-risk` | more than one independent move competes for the center | split or narrow only after direct review |
| `route-away-risk` | object is likely a skill, eval, routing object, playbook, role, memory/KAG object, or runtime object | owner route note before moving content |

### Layer 3: Repair Actions

Use these only after the anatomy verdict names a concrete gap.

| action | use when | first repair route |
|---|---|---|
| `no-repair` | the bundle is healthy at current contract strength | leave leaf untouched |
| `template-modernization-candidate` | old-template bundle would benefit from explicit atom or small-agent sections during a later repair wave | batch with similar old-template bundles |
| `support-surface-repair` | examples, checks, or notes fail to support the atom | edit support files before widening core text |
| `capsule-source-repair` | source summary or risk wording makes generated capsule weak | edit authored source, then rebuild generated surfaces |
| `capsule-builder-review` | source is healthy but extraction produces weak card text | inspect builder and tests before generated changes |
| `boundary-caution-repair` | portability or owner-boundary warning is present but too weak | repair local caution without importing sibling law |
| `split-review` | one bundle contains several moves | create a review packet before leaf surgery |
| `route-away-note` | stronger owner likely owns the object | record owner route and stop-line, no silent transfer |

## Direct-Read Findings

### `AOA-T-0001`

Finding: `anatomy-pass`, `old-template-watch`, `no-repair`.

Evidence:

- `TECHNIQUE.md` names a narrow change protocol with explicit plan, diff,
  apply, verify, and report stages.
- `checks/review-checklist.md` names concrete review checks, including
  public-hygiene review.
- `examples/minimal-change-flow.md` gives a portable documentation-change
  example.
- `notes/adverse-effects-review.md` already watches ceremony creep and
  symbolic verification.
- The capsule preserves the executable center.

Rubric lesson:

Do not label pre-current-template bundles as weak only because they lack
literal `Atomic move` and `Small-agent execution shape` headings. When intent,
procedure, contracts, checks, example, notes, and capsule carry the move, use
`old-template-watch` instead of `minor-repair`.

### `AOA-T-0055`

Finding: `anatomy-pass`, `portability-watch`, `no-repair`,
`promotion-evidence-hold`.

Evidence:

- `TECHNIQUE.md` keeps one bounded pre-execution ladder:
  requirement -> design -> tasks.
- `checks/requirements-design-tasks-ladder-checklist.md` verifies layer
  separation and keeps command/template ecosystems out.
- `examples/minimal-requirements-design-tasks-ladder.md` shows one compact
  three-layer example.
- `notes/external-import-review.md` passes boundedness and provenance
  readability.
- `notes/canonical-readiness.md` explicitly defers canonical promotion until a
  stronger live adopter exists.

Rubric lesson:

Promotion evidence and anatomy health must stay separate. A promoted bundle can
be structurally healthy while still needing external evidence before canonical
review.

### `AOA-T-0074`

Finding: `anatomy-pass`, `portability-watch`, `owner-boundary-watch`,
`no-repair`.

Evidence:

- `TECHNIQUE.md` keeps Telegram-source normalization separate from auth,
  session conversion, memory writeback, and general history capture.
- `checks/telegram-export-normalization-to-local-store-checklist.md` verifies
  ids, media references, provenance, resume behavior, and out-of-scope auth.
- `examples/minimal-telegram-export-normalization-to-local-store.md` gives a
  source-object example with ids, media refs, source path, and resume cursor.
- `notes/external-origin.md` and `notes/external-import-review.md` preserve the
  donor family and exclusions.
- The capsule carries the normalization seam clearly.

Rubric lesson:

Source-specific techniques are not automatically portability gaps. The audit
should ask whether the source-specific seam is the atom and whether adjacent
auth/session/memory owners stay outside the invariant core.

### `AOA-T-0096`

Finding: `anatomy-pass`, `capsule-gap`, `capsule-builder-review` or
`capsule-source-repair` pending.

Evidence:

- `TECHNIQUE.md` keeps one generated-publish guardrail: reproduce the
  workflow-pinned matrix before publishing generated outputs.
- The bundle explicitly stays smaller than full release automation or
  split-wave playbook doctrine.
- `checks/pinned-validation-matrix-before-generated-publish-checklist.md`
  verifies named generated outputs, pinned refs, same-matrix rebuild, and
  repo-native validators.
- The generated capsule's `main_risk_short` ends awkwardly at `older or.`,
  which weakens small runtime-card readability even though the authored source
  is coherent.

Rubric lesson:

Capsule issues must branch before repair:

- if authored source is too hard to extract, use `capsule-source-repair`
- if authored source is healthy and extraction truncates badly, use
  `capsule-builder-review`

Do not edit generated capsule output by hand.

### `AOA-T-0065`

Finding: `anatomy-pass`, `owner-boundary-watch`, `portability-watch`,
`no-repair`.

Evidence:

- `TECHNIQUE.md` keeps one runtime proxy seam: a bounded gateway fronts
  configured upstream MCP servers with explicit metadata and mediation.
- `checks/mcp-gateway-proxy-checklist.md` verifies more than one upstream,
  one proxy surface, visible metadata, gateway-routed calls, and sanitization
  at the boundary.
- `examples/minimal-mcp-gateway-proxy.md` keeps lifecycle, scanner modes, and
  registry product behavior out.
- `notes/external-import-review.md` passes boundedness and provenance
  readability.
- The capsule preserves the proxy-seam center.

Rubric lesson:

Tool/runtime-adjacent techniques can remain valid technique atoms when they
name one portable seam and explicitly keep lifecycle, security-platform,
registry, and runtime-product doctrine outside the invariant core.

## Rubric Changes To Carry Into Shelf Waves

- Replace broad `minor-repair` with explicit action labels:
  `template-modernization-candidate`, `support-surface-repair`,
  `capsule-source-repair`, `capsule-builder-review`, and
  `boundary-caution-repair`.
- Keep `inventory-pass` out of quality verdicts.
- Add `old-template-watch` so older healthy bundles are not rewritten for
  symmetry alone.
- Add `promotion-evidence-hold` to separate status readiness from bundle
  anatomy.
- Treat source-specific techniques through `portability-watch`, not automatic
  `portability-gap`.
- Treat owner pressure through `owner-boundary-watch` until direct reading
  proves the technique atom belongs elsewhere.
- Treat generated capsule defects as their own lane before leaf repair.
- Keep the first full shelf waves in markdown review packets. Do not add a
  machine-readable audit builder until repeated rows prove the need.

## Next Gate

Begin Wave A shelf audit with the hardened labels:

1. `execution/agent-workflows-core`
2. `execution/intent-chain`
3. `execution/ready-work-graphs`
4. `execution/runtime-truth-lifecycle`
5. `instruction/docs-boundary`
6. `instruction/instruction-surface`
7. `instruction/capability-registry`
8. `instruction/capability-boundary`
9. `instruction/skill-discovery`

The first wave should produce bundle-level labels, evidence refs, and smallest
repair actions without editing leaf bundles.

## Stop Lines

- Do not repair `AOA-T-0096` from this packet alone.
- Do not rewrite older healthy bundles only to match the newest template.
- Do not promote any bundle from anatomy health alone.
- Do not route source-specific bundles away when the source-specific seam is
  the actual atom.
- Do not treat owner-boundary watch as sibling-owner acceptance or rejection.
- Do not add machine-readable audit output before markdown wave evidence proves
  the schema is stable.
