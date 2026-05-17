# Execution Profile Small-Agent Wave B Review

Source packet: [Technique Reform Ingress](../README.md)

Status: direct-read review packet for the remaining Phase 1 small-agent
candidate shelves. No local small-agent harness was run. No frontmatter,
schema, generated scout rule, capsule builder, registry, or technique leaf was
changed.

## Verdict

Wave B confirms the current scout profiles for the reviewed shelves as static
execution-envelope estimates.

The reviewed `small-agent` rows stay good future fixture candidates because the
authored bundles define compact inputs, bounded output shapes, and visible stop
lines. That does not prove execution by a 2-4B model. It means a larger
orchestrator should be able to pack a tiny, synthetic or public-safe fixture for
later empirical testing.

The `medium-agent` rows remain Phase 2 calibration material. The
`orchestration-required` rows remain useful boundaries: they are often short
atomic moves, but their safe use depends on public-share, security, approval,
owner-truth, mutation, or review-pressure wrappers outside the small-agent
fixture lane.

Reviewed shelves:

- `history/history-artifacts`
- `instruction/capability-boundary`
- `instruction/docs-boundary`
- `knowledge-lift/kag-source-lift`
- `proof/evaluation-chain`
- `proof/owner-truth-closeout`
- `proof/review-evidence`
- `proof/skill-support`

Wave totals:

| profile | rows reviewed | verdict |
|---|---:|---|
| `small-agent` | 20 | keep as fixture candidates |
| `medium-agent` | 2 | keep for Phase 2 calibration |
| `orchestration-required` | 13 | boundary confirmed |

## Reviewed Surfaces

Reviewed before this packet:

- `AGENTS.md`
- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `docs/TECHNIQUE_TREE_CONTRACT.md`
- `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md`
- `docs/readers/runtime/TECHNIQUE_CAPSULES.md`
- `techniques/history/AGENTS.md`
- `techniques/instruction/AGENTS.md`
- `techniques/knowledge-lift/AGENTS.md`
- `techniques/proof/AGENTS.md`
- all `TECHNIQUE.md`, `examples/`, `checks/`, and `notes/` files under the
  eight reviewed shelves

## Small-Agent Rows

| technique | current profile | direct-read verdict | orchestrator must supply | future fixture sketch |
|---|---|---|---|---|
| `AOA-T-0053` `local-first-session-index` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | already-saved session artifacts, metadata fields, index target, query or browse goal, memory/dashboard stop line | two tiny saved session files plus metadata; expect a local index entry set with source paths and no memory-object or dashboard doctrine |
| `AOA-T-0026` `session-capture-as-repo-artifact` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | public-safe session excerpt, artifact path, capture boundary, retention/sanitization cues | short sanitized session recap; expect a repo artifact record with provenance and explicit exclusions, not a raw transcript dump |
| `AOA-T-0045` `witness-trace-as-reviewable-artifact` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | ordered witness steps, state-delta notes, review target, promotion/writeback stop line | five-step run trace with one ambiguous state change; expect reviewable witness artifact, not proof verdict, telemetry, or memory entry |
| `AOA-T-0066` `transcript-replay-artifact` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | already-saved transcript material, message order, timeline cues, redaction posture, replay output shape | synthetic transcript with timestamps and redacted private turn; expect replay artifact preserving order and source refs without hosted replay-platform claims |
| `AOA-T-0067` `transcript-linked-code-lineage` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | saved transcript evidence, code or commit anchor, lineage link shape, analytics stop line | one commit-like code change plus one saved session rationale; expect source-linked lineage note, not repo analytics or memory doctrine |
| `AOA-T-0043` `multi-source-primary-input-provenance` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | one primary source, supporting sources, priority rule, bridge-output shape, ranking/graph stop line | primary README plus two supporting notes; expect primary/supporting provenance split and no graph ranking doctrine |
| `AOA-T-0002` `source-of-truth-layout` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | overlapping doc list, intended owner surface, entrypoint role, conflict cue | three docs with one stale instruction; expect source-of-truth layout and link-driven entrypoint guidance, not broad governance doctrine |
| `AOA-T-0009` `lightweight-status-snapshot` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | current state facts, stale or unknown claims, snapshot audience, update boundary | tiny project status packet with one unknown; expect compact snapshot with stale/unknown visible, not roadmap or status authority |
| `AOA-T-0033` `decision-rationale-recording` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | one meaningful decision, alternatives, rationale, consequence list, authority stop line | design choice with two rejected options; expect bounded rationale note, not architecture taxonomy or governance layer |
| `AOA-T-0019` `frontmatter-metadata-spine` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | source frontmatter, derived manifest need, allowed fields, source-priority stop line | bundle frontmatter plus derived catalog row; expect metadata spine that routes back to source, not a replacement source |
| `AOA-T-0020` `evidence-note-provenance-lift` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | evidence note kinds, note paths, derived manifest target, note-graph stop line | two evidence notes with kinds and paths; expect provenance handles in a manifest while note meaning remains in markdown |
| `AOA-T-0021` `bounded-relation-lift-for-kag` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | direct relation fields, target IDs, relation type vocabulary, graph-authority stop line | three direct relation entries; expect bounded edge hints for selection and no KAG scoring or traversal doctrine |
| `AOA-T-0022` `risk-and-negative-effect-lift` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | risk/adverse-effect text, derived caution target, allowed caution vocabulary, policy stop line | Risks section plus adverse-effect note; expect caution lift with source refs and no automated policy or scoring |
| `AOA-T-0003` `contract-first-smoke-summary` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | contract statement, smoke output, pass/fail or inconclusive state, summary schema | one contract check transcript; expect compact smoke summary tied to contract, not proof verdict law |
| `AOA-T-0032` `context-report-for-ci` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | CI context facts, changed surface, report consumer, CI-policy stop line | small CI context packet with changed files and environment facts; expect read-only context report, not CI gate policy |
| `AOA-T-0091` `workspace-root-ingress-and-mutation-gate` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | workspace root, owner repo, intent text, mutation surface, guard result, no-real-mutation fixture rule | synthetic workspace ingress plus blocked/allowed guard report; expect explicit ingress and guard posture, not workspace law or hidden operator memory |
| `AOA-T-0106` `single-scoped-evidence-reference` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | one claim, one evidence reference, relevance statement, scope limit, reliance condition | claim plus one cited source line; expect one scoped evidence reference with limits, not evidence adequacy scoring |
| `AOA-T-0016` `bounded-context-map` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | target area, overloaded terms, neighboring contexts, interface or handoff cue | three overlapping responsibilities; expect compact context map with boundaries and handoff surfaces |
| `AOA-T-0015` `contract-test-design` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | boundary, expected inputs/outputs, downstream expectation, smallest check cue | simple API or file-boundary contract; expect test/check design around contract rather than internals |
| `AOA-T-0017` `property-invariants` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | stable truth, input/state space, examples and non-examples, check form | config transformation rule; expect invariant statements and check sketch beyond one handpicked example |

Small-agent pattern found:

- The history rows can be tested only with sanitized synthetic artifacts or
  already-public saved history. They must not import private transcripts.
- The instruction and docs rows are small-agent shaped when the orchestrator
  provides a short visible source set and one target role.
- The knowledge-lift rows are compact because they lift one source object into
  one bounded derived reader object; they become unsafe if treated as KAG graph
  semantics, proof, scoring, or generated truth.
- The proof-support rows are good fixture candidates when they remain one
  map, one contract, one invariant set, one smoke summary, or one scoped
  evidence reference.

## Medium Rows Deferred To Phase 2

| technique | current profile | wave B note |
|---|---|---|
| `AOA-T-0092` `audit-to-closeout-proof-loop` | `medium-agent` | direct reading shows one loop, but the agent must compare reviewed audit wording against live remediation evidence and preserve closeout limits; keep for Phase 2 |
| `AOA-T-0095` `github-only-owner-endcap-with-reality-sync` | `medium-agent` | one owner endcap is atomic, but reality-sync requires comparing GitHub-native state with source truth and local closeout claims |

## Orchestration Boundaries

| technique | current profile | direct-read verdict | why the outer wrapper remains required |
|---|---|---|---|
| `AOA-T-0044` `versionable-session-transcripts` | `orchestration-required` | `orchestration-boundary-confirmed` | transcript packaging is atomic, but public-safety, redaction, versioning, and private-session boundaries require a larger wrapper |
| `AOA-T-0093` `recommendation-truth-vs-host-actionability` | `orchestration-required` | `orchestration-boundary-confirmed` | the split is simple in prose, but host inventory and actionability can leak sensitive local capability truth unless routed through a guarded selector context |
| `AOA-T-0040` `skill-vs-command-boundary` | `orchestration-required` | `orchestration-boundary-confirmed` | distinguishing a reusable skill from a command may affect public capability surfaces and acceptance routes outside this repo |
| `AOA-T-0034` `public-safe-artifact-sanitization` | `orchestration-required` | `orchestration-boundary-confirmed` | sanitization prepares a shareable object, but actual disclosure safety and approval remain public-share gates |
| `AOA-T-0018` `markdown-technique-section-lift` | `orchestration-required` | `orchestration-boundary-confirmed` | section lift feeds generated reader surfaces and can alter source interpretation if not rebuilt and checked by an outer workflow |
| `AOA-T-0046` `repo-doc-surface-lift` | `orchestration-required` | `orchestration-boundary-confirmed` | repo-doc lifts cross route cards, status docs, and derived routing knowledge; security-sensitive and owner-priority checks need orchestration |
| `AOA-T-0047` `github-review-template-lift` | `orchestration-required` | `orchestration-boundary-confirmed` | template lift touches GitHub-facing intake language and must not become workflow automation, policy scoring, or platform behavior |
| `AOA-T-0048` `semantic-review-surface-lift` | `orchestration-required` | `orchestration-boundary-confirmed` | semantic-review lift can feed boundary-review knowledge, but automatic semantic verdicts or proof authority require owner controls |
| `AOA-T-0007` `signal-first-gate-promotion` | `orchestration-required` | `orchestration-boundary-confirmed` | staged signal promotion can block or enable later gates; approval, irreversibility, and rollout sequencing cannot be fixture-only |
| `AOA-T-0094` `canonical-owner-with-validated-mirror` | `orchestration-required` | `orchestration-boundary-confirmed` | canonical owner and local mirror parity require cross-repo owner comparison and validation, not a small isolated rewrite |
| `AOA-T-0096` `pinned-validation-matrix-before-generated-publish` | `orchestration-required` | `orchestration-boundary-confirmed` | generated publish safety depends on workflow-pinned refs, rebuilds, checks, and public-share mutation controls |
| `AOA-T-0105` `single-missing-evidence-request` | `orchestration-required` | `orchestration-boundary-confirmed` | the object is tiny, but requesting evidence mutates review pressure and can become proof-board behavior without an outer review wrapper |
| `AOA-T-0107` `single-locus-claim-challenge` | `orchestration-required` | `orchestration-boundary-confirmed` | one challenge is atomic, but challenge wording changes review posture and must avoid becoming adjudication authority or broad claim scoring |

## Calibration Notes

- Wave B completes the direct-read Phase 1 coverage for the remaining
  `small-agent` candidate shelves outside the landed pilot and Wave A.
- No `small-agent` row in this wave should be demoted from direct reading
  alone. The repeated caveat is fixture packing, not profile contradiction.
- `history/history-artifacts` is the clearest public-safety edge: fixtures must
  be synthetic or explicitly sanitized and must name forbidden hidden private
  transcript context.
- `knowledge-lift/kag-source-lift` confirms that a small agent can lift one
  bounded object, but not own graph semantics, scoring, retrieval policy, or
  proof authority.
- The review-evidence shelf shows why "single" does not always mean
  `small-agent`: `single-scoped-evidence-reference` is a bounded reference
  output, while `single-missing-evidence-request` and
  `single-locus-claim-challenge` change review pressure and need an outer
  wrapper.
- `workspace-root-ingress-and-mutation-gate` is small-agent shaped only as a
  packet-reading and guard-recording move. Real risky mutation remains outside
  the fixture.

## Useful Threads

Carry these forward:

- The fixture ledger should group small-agent candidates by substrate:
  `history artifact`, `doc/status/decision`, `knowledge-lift`, `proof-support`,
  `owner-ingress`, `handoff`, `governance packet`, and `runtime benchmark`.
- Fixture rows need `forbidden hidden context` fields, especially for history
  artifacts, owner-ingress, evidence references, and knowledge-lift rows.
- Some apparently simple proof moves are orchestration-required because they
  change social or review pressure, not because the text is complex.
- Future empirical harness work should include at least one trap fixture where
  the tempting answer imports owner doctrine or private history not present in
  the packed prompt.

## Stop Lines

- Do not relabel any profile from this wave alone.
- Do not promote `execution_profile` to frontmatter.
- Do not treat fixture sketches as empirical validation.
- Do not route private transcript handling, GitHub platform behavior, KAG graph
  semantics, eval verdicts, public-share approval, or cross-repo owner parity
  into `aoa-techniques`.
- Do not mutate technique leaves as part of this review-only wave.

## Validation

This packet is a review-only source artifact. Required validation after landing
this wave:

1. `python -m unittest tests.test_distillation_mechanics_topology`
2. `python scripts/validate_repo.py`
3. `python scripts/release_check.py` before GitHub merge
