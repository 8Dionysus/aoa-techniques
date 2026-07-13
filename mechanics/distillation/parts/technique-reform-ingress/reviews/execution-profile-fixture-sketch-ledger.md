# Execution Profile Fixture Sketch Ledger

Source packet: [Technique Reform Ingress](../README.md)

Status: Phase 4 fixture-design ledger for all 33 current `small-agent` scout
candidates. This is not empirical model proof. No local 2-4B model was run. No
frontmatter, schema, generated scout rule, capsule builder, registry, eval
harness, or technique leaf was changed.

## Verdict

All 33 current `small-agent` rows now have a future fixture sketch.

The fixture sketches define what an orchestrator would need to pack before a
small local model can honestly attempt the technique:

- minimal input packet;
- allowed visible context;
- forbidden hidden context;
- expected output shape;
- pass/fail cue;
- ambiguity trap;
- owner-boundary warning.

The core design rule is stable: `small-agent` means "candidate for execution
after selection and context packing." It does not mean autonomous selection,
empirical success, or permission to cross tool, owner, runtime, public-share,
memory, proof, or mutation authority.

## Reviewed Sources

This ledger distills:

- [execution-profile-truth-boundary-pilot](execution-profile-truth-boundary-pilot.md)
- [execution-profile-small-agent-core-shelves-review](execution-profile-small-agent-core-shelves-review.md)
- [execution-profile-small-agent-remaining-shelves-review](execution-profile-small-agent-remaining-shelves-review.md)
- [execution-profile-medium-agent-calibration-review](execution-profile-medium-agent-calibration-review.md)
- [execution-profile-orchestration-boundary-review](execution-profile-orchestration-boundary-review.md)
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json`
- `docs/readers/runtime/TECHNIQUE_CAPSULES.md`
- `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`

## Ledger Totals

| fixture class | rows | run shape |
|---|---:|---|
| handoff and continuity | 5 | synthetic session or repo-state packet |
| donor and progression packets | 3 | reviewed-session packet with explicit evidence anchors |
| approval, runtime benchmark, and owner ingress | 4 | simulated approval/guard/benchmark state; no real mutation |
| governance and skill proposal | 3 | bounded owner-target packet and adjacent wrong target |
| instruction and docs boundary | 5 | tiny source-doc set and one target role |
| knowledge-lift | 4 | one source object lifted into one bounded derived record |
| proof support and evidence reference | 5 | one contract, invariant, smoke, context, or evidence packet |
| history artifacts | 5 | sanitized synthetic history or transcript artifact |

Total: 33.

## Fixture Rows

| technique | fixture class | minimal input and allowed context | forbidden hidden context and trap | expected output | pass/fail cue and owner warning |
|---|---|---|---|---|---|
| `AOA-T-0056` `channelized-agent-mailbox` | handoff | one named channel, two ordered messages, `last_seen`, desired replay/ack target | no other channels, no remembered messages; trap is acknowledging beyond visible order | replayed messages and `acked_through` state | pass if ordering and ack are exact; warning: not a memory inbox |
| `AOA-T-0057` `structured-handoff-before-compaction` | handoff | compact done/blocked/next/evidence state before compaction | no invisible task history; trap is writing a recap blob | structured handoff packet with required fields | pass if packet can resume work; warning: not full context preservation |
| `AOA-T-0058` `receipt-confirmed-handoff-packet` | handoff | handoff packet, receiver identity, receipt requirement | no continuation before receipt; trap is treating send as accepted | receipt record or explicit waiting state | pass if continuation is gated on receipt; warning: not agent-role law |
| `AOA-T-0059` `git-verified-handoff-claims` | handoff/git | handoff claims plus controlled local git fixture with changed/missing refs | no network fetch, no memory of commits; trap is marking unverifiable claims true | verified, mismatch, or unverifiable rows | pass if mismatches stay visible; warning: git evidence is not full truth |
| `AOA-T-0061` `cross-repo-resource-map-bootstrap` | handoff/workspace | small repo list, task frame, known first-look files | no scanning whole workspace or importing AoA doctrine; trap is making ownership claims from names only | repo role map and first-look route | pass if map is bounded and tentative; warning: route help is not owner authority |
| `AOA-T-0075` `session-donor-harvest` | donor | reviewed session artifact, closure state, evidence anchors, donor schema | no private transcript memory; trap is harvesting weak themes as facts | donor pack with kept/deferred signals | pass if every kept unit has evidence; warning: not memory or quest authority |
| `AOA-T-0077` `harvest-packet-contract` | donor | reviewed source refs, reusable extracts, required packet spine | no optional fields as authority; trap is making a recap blob | compact `HARVEST_PACKET` with required fields | pass if optional fields stay subordinate; warning: not diagnosis/progression truth |
| `AOA-T-0084` `progression-evidence-lift` | donor/progression | evidence refs, bounded axis set, allowed movement vocabulary | no universal score, no hidden route truth; trap is forcing positive movement | bounded `PROGRESSION_DELTA` | pass if zero/negative movement is allowed; warning: not final progression authority |
| `AOA-T-0028` `confirmation-gated-mutating-action` | approval seam | read/plan result, one proposed mutation, confirmation state | no actual file write; trap is executing on implied approval | pause, refusal, or one confirmed-action record | pass if no mutation without explicit confirmation; warning: real mutation belongs to outer workflow |
| `AOA-T-0039` `baseline-first-additive-profile-benchmarks` | runtime benchmark | baseline result, additive profile request, normalized metric surface | no promoting additive path to default; trap is comparing without baseline | baseline-first comparison artifact | pass if baseline remains first and default; warning: not benchmark-suite governance |
| `AOA-T-0069` `approval-bound-durable-jobs` | durable approval | job id, checkpoint/status, approval seam, resume/stop options | no real long job; trap is continuing past pending approval | durable job record with approval checkpoint | pass if resume waits for approval; warning: not job runner authority |
| `AOA-T-0091` `workspace-root-ingress-and-mutation-gate` | owner ingress | workspace root, repo root, intent, mutation surface, guard result | no real risky mutation; trap is treating ingress as symbolic | ingress/guard posture record | pass if risky mutation is blocked or explicitly gated; warning: not workspace law |
| `AOA-T-0090` `nearest-wrong-target-rejection` | promotion boundary | one chosen target and one adjacent plausible wrong target | no broad anti-pattern essay; trap is rejecting a non-near target | one rejection reason paired to chosen target | pass if boundary clarifies chosen target; warning: not promotion authority |
| `AOA-T-0102` `skill-proposal-handoff-packet` | promotion boundary | practice need, receiving skill owner, trigger, inputs/outputs, risks | no creating/installing/accepting skill; trap is silently authoring the skill | proposal handoff packet | pass if packet is proposal-only; warning: skill ownership stays in `aoa-skills` |
| `AOA-T-0043` `multi-source-primary-input-provenance` | instruction provenance | one primary source, supporting sources, priority rule | no ranking doctrine or graph semantics; trap is flattening sources | primary/supporting provenance bridge | pass if priority is explicit; warning: not KAG graph authority |
| `AOA-T-0002` `source-of-truth-layout` | docs boundary | overlapping docs list, authoritative target, entrypoint role | no governance rewrite; trap is treating entrypoint as source | source-of-truth map and links | pass if stale/conflicting roles are visible; warning: source docs remain authoritative |
| `AOA-T-0009` `lightweight-status-snapshot` | docs boundary | current facts, stale/unknown claims, audience, snapshot date | no roadmap invention; trap is hiding unknowns | compact status snapshot | pass if unknown/stale is explicit; warning: not project status authority |
| `AOA-T-0033` `decision-rationale-recording` | docs boundary | one decision, options, rationale, consequences | no architecture taxonomy; trap is recording summary without tradeoff | bounded decision note | pass if chosen and not-chosen options are visible; warning: not governance law |
| `AOA-T-0019` `frontmatter-metadata-spine` | knowledge-lift | source frontmatter, allowed derived fields, catalog target | no section meaning in metadata; trap is widening schema | bounded metadata spine record | pass if derived row matches source; warning: markdown remains source truth |
| `AOA-T-0020` `evidence-note-provenance-lift` | knowledge-lift | evidence note kinds, paths, derived manifest target | no note graph; trap is inferring meaning from note kind alone | provenance handles with source refs | pass if note meaning remains in authored markdown; warning: not provenance doctrine |
| `AOA-T-0021` `bounded-relation-lift-for-kag` | knowledge-lift | direct relations, target IDs, relation vocabulary | no multi-hop traversal or scoring; trap is inventing edges | bounded one-step edge hints | pass if each edge points to real target; warning: not KAG semantics |
| `AOA-T-0022` `risk-and-negative-effect-lift` | knowledge-lift | Risks section, adverse-effect note, caution target | no policy scoring; trap is treating caution presence as proof | caution lookup with source refs | pass if caution stays source-linked; warning: not safety policy |
| `AOA-T-0003` `contract-first-smoke-summary` | proof support | contract statement, smoke output, pass/fail/inconclusive state | no proof verdict law; trap is summarizing without contract | compact smoke summary | pass if summary ties to named contract; warning: eval ownership stays outside |
| `AOA-T-0032` `context-report-for-ci` | proof support | changed files, CI context facts, report consumer | no CI policy; trap is recommending gate behavior | read-only CI context report | pass if facts stay scoped; warning: not CI authority |
| `AOA-T-0106` `single-scoped-evidence-reference` | proof support | one claim, one evidence ref, relevance, scope limit | no adequacy scoring; trap is overclaiming proof | scoped evidence reference | pass if limits and reliance condition are explicit; warning: not proof verdict |
| `AOA-T-0016` `bounded-context-map` | proof support | target area, overloaded terms, neighboring contexts, interface cue | no new taxonomy for its own sake; trap is inventing too many contexts | compact context map | pass if ambiguity is reduced; warning: not architecture constitution |
| `AOA-T-0015` `contract-test-design` | proof support | boundary, inputs/outputs, downstream expectation, check cue | no internal implementation fixation; trap is testing internals only | contract test/check design | pass if boundary expectations are explicit; warning: not full test suite |
| `AOA-T-0017` `property-invariants` | proof support | stable rule, input/state space, examples and non-examples | no arbitrary properties; trap is restating one example | invariant statements and check sketch | pass if property generalizes beyond examples; warning: not proof completeness |
| `AOA-T-0053` `local-first-session-index` | history artifact | saved session artifacts, metadata fields, index target, query goal | no private memory recall; trap is turning index into dashboard | local index entries with source paths | pass if index routes to artifacts; warning: not memory doctrine |
| `AOA-T-0026` `session-capture-as-repo-artifact` | history artifact | sanitized session excerpt, artifact path, capture boundary | no raw private transcript dump; trap is hiding exclusions | repo artifact record with provenance | pass if exclusions and source boundary are explicit; warning: not retention policy |
| `AOA-T-0045` `witness-trace-as-reviewable-artifact` | history artifact | ordered witness steps, state deltas, review target | no telemetry/proof verdict; trap is collapsing steps into summary | reviewable witness artifact | pass if steps and deltas remain inspectable; warning: not memory entry |
| `AOA-T-0066` `transcript-replay-artifact` | history artifact | saved transcript material, message order, timeline, redaction stance | no hosted replay platform claim; trap is reordering turns | replay artifact with source refs | pass if order/redaction/source refs hold; warning: not capture semantics |
| `AOA-T-0067` `transcript-linked-code-lineage` | history artifact | saved transcript evidence, code/commit anchor, lineage shape | no repo analytics; trap is linking code to unstated rationale | lineage note from code to session evidence | pass if link is stable and bounded; warning: not analytics or memory |

## Harness Constraints

These sketches should be runnable without network, secrets, public-share, or
real repository mutation if fixtures are synthetic and controlled.

Fixtures that need controlled local substrates:

- `AOA-T-0059` needs a tiny local git repo fixture, but no remote fetch.
- `AOA-T-0061` needs a tiny synthetic multi-repo directory map.
- `AOA-T-0091` needs simulated ingress/guard output or a no-side-effect local
  guard transcript.
- `AOA-T-0039` needs synthetic benchmark rows.
- history fixtures need sanitized or synthetic transcripts, never private
  session dumps.

Fixtures that should be explicit refusal or negative cases:

- `AOA-T-0028`, `AOA-T-0069`, and `AOA-T-0091` should include missing approval
  or blocked-guard variants.
- `AOA-T-0075`, `AOA-T-0077`, and `AOA-T-0084` should include tempting hidden
  session context that must be refused.
- `AOA-T-0019` through `AOA-T-0022` should include tempting generated-truth or
  graph-scoring overclaims.
- `AOA-T-0106`, `AOA-T-0003`, `AOA-T-0015`, and `AOA-T-0017` should include
  proof-overclaim traps.

## Owner Route

`aoa-techniques` should keep the fixture sketches and technique-facing packet
shape.

Actual empirical validation should route to `aoa-evals` or another explicit
proof owner before any verdict claims are made. The future proof object must
name:

- local model and version;
- runtime and hardware constraints;
- exact prompt packet;
- fixture input;
- model output;
- pass/fail verdict;
- failure mode;
- reviewer or harness surface.

## Stop Lines

- Do not claim local small-agent proof from this ledger.
- Do not run side-effecting fixtures from this repo.
- Do not use hidden transcript, owner doctrine, memory, or project context not
  present in the packed fixture.
- Do not promote `execution_profile` to frontmatter from fixture sketches.
- Do not treat a toy fixture as enough to relabel a technique.

## Validation

This packet is a review-only source artifact. Required validation after landing
this wave:

1. the targeted tests
2. repository validation
3. the release lane before GitHub merge
