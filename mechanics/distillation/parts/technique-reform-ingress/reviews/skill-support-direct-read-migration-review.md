# Skill-Support Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Preceding landed review:
[Landed Skill-Discovery Pilot Review](landed-skill-discovery-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-eleventh-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `skill-support` as the eleventh bounded tree migration pilot.

Direct reading confirms that `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017`
form one proof-side support shelf. The shelf helps an agent make a capability
or subsystem seam usable before stronger proof or execution work begins:
first name the bounded context, then make the consumer-visible contract
explicit, then broaden validation around stable invariants when examples are
too narrow.

The shelf is not proof authority. `AOA-T-0016` remains a docs artifact,
`AOA-T-0015` remains boundary-contract validation, and `AOA-T-0017` remains
invariant-oriented validation. The move would only make the support triangle
easier to browse under `techniques/proof/skill-support/` while keeping
`domain`, `kind`, status, IDs, evidence, relations, examples, checks, and
public-safety posture unchanged.

This review does not move files. It only authorizes a later migration wave to
move exactly these three bundles into `techniques/proof/skill-support/` if
that wave also updates route cards, root legacy receipts, authored links,
generated surfaces, and validation.

## Sources Read

- [AOA-T-0016 bounded-context-map](../../../../../techniques/docs/bounded-context-map/TECHNIQUE.md)
- [AOA-T-0016 checklist](../../../../../techniques/docs/bounded-context-map/checks/bounded-context-map-checklist.md)
- [AOA-T-0016 minimal example](../../../../../techniques/docs/bounded-context-map/examples/minimal-context-boundary-map.md)
- [AOA-T-0016 concrete example](../../../../../techniques/docs/bounded-context-map/examples/concrete-infra-context-map.md)
- [AOA-T-0016 canonical readiness](../../../../../techniques/docs/bounded-context-map/notes/canonical-readiness.md)
- [AOA-T-0016 adverse effects review](../../../../../techniques/docs/bounded-context-map/notes/adverse-effects-review.md)
- [AOA-T-0016 origin evidence](../../../../../techniques/docs/bounded-context-map/notes/origin-evidence.md)
- [AOA-T-0016 second context adaptation](../../../../../techniques/docs/bounded-context-map/notes/second-context-adaptation.md)
- [AOA-T-0015 contract-test-design](../../../../../techniques/evaluation/contract-test-design/TECHNIQUE.md)
- [AOA-T-0015 checklist](../../../../../techniques/evaluation/contract-test-design/checks/contract-test-design-checklist.md)
- [AOA-T-0015 minimal example](../../../../../techniques/evaluation/contract-test-design/examples/minimal-contract-boundary.md)
- [AOA-T-0015 concrete example](../../../../../techniques/evaluation/contract-test-design/examples/concrete-api-contract-boundary.md)
- [AOA-T-0015 canonical readiness](../../../../../techniques/evaluation/contract-test-design/notes/canonical-readiness.md)
- [AOA-T-0015 adverse effects review](../../../../../techniques/evaluation/contract-test-design/notes/adverse-effects-review.md)
- [AOA-T-0015 origin evidence](../../../../../techniques/evaluation/contract-test-design/notes/origin-evidence.md)
- [AOA-T-0015 second context adaptation](../../../../../techniques/evaluation/contract-test-design/notes/second-context-adaptation.md)
- [AOA-T-0017 property-invariants](../../../../../techniques/evaluation/property-invariants/TECHNIQUE.md)
- [AOA-T-0017 checklist](../../../../../techniques/evaluation/property-invariants/checks/property-invariants-checklist.md)
- [AOA-T-0017 minimal example](../../../../../techniques/evaluation/property-invariants/examples/minimal-invariant-check.md)
- [AOA-T-0017 concrete example](../../../../../techniques/evaluation/property-invariants/examples/concrete-config-invariant-check.md)
- [AOA-T-0017 canonical readiness](../../../../../techniques/evaluation/property-invariants/notes/canonical-readiness.md)
- [AOA-T-0017 adverse effects review](../../../../../techniques/evaluation/property-invariants/notes/adverse-effects-review.md)
- [AOA-T-0017 origin evidence](../../../../../techniques/evaluation/property-invariants/notes/origin-evidence.md)
- [AOA-T-0017 second context adaptation](../../../../../techniques/evaluation/property-invariants/notes/second-context-adaptation.md)
- [Docs route card](../../../../../techniques/docs/AGENTS.md)
- [Evaluation route card](../../../../../techniques/evaluation/AGENTS.md)
- [Techniques route card](../../../../../techniques/AGENTS.md)
- [Technique family seed row for `skill-support`](../../../../../config/technique_family_seed.yaml)
- [Technique tree projection rows for `skill-support`](../../../../../reports/technique_tree_projection.md)
- [Technique family scout rows for `skill-support`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `skill-support`](../../../../../reports/technique_topology_scout.md)
- [Landed skill-discovery pilot review](landed-skill-discovery-pilot-review.md)

## Direct Bundle Read

| technique | current path | domain | kind | direct-read result |
|---|---|---|---|---|
| `AOA-T-0016` | `techniques/docs/bounded-context-map/` | `docs` | `artifact` | names neighboring responsibilities, vocabulary, and handoff points so scope does not blur before implementation or validation widens |
| `AOA-T-0015` | `techniques/evaluation/contract-test-design/` | `evaluation` | `validation` | defines consumer-visible boundary assumptions and checks the contract surface without freezing hidden internals or broad invariant coverage |
| `AOA-T-0017` | `techniques/evaluation/property-invariants/` | `evaluation` | `validation` | expresses meaningful stable truths as bounded invariant-oriented checks after the boundary or rule is understood |

The kinds are mixed, but the shelf is coherent because the browsing question is
not one move kind. It is the support question a small agent faces when it must
make a seam reviewable: what vocabulary names the boundary, what contract
protects the boundary, and what invariant constrains broader behavior?

## Why The Shelf Holds

- `AOA-T-0016` supplies the vocabulary and responsibility map that keeps later
  proof or implementation work from widening into the wrong context.
- `AOA-T-0015` supplies the consumer-visible contract discipline once the
  boundary has an observable surface.
- `AOA-T-0017` supplies the invariant-oriented coverage discipline once a
  stable truth should hold across more cases than examples alone cover.
- All three bundles are canonical and public-safe.
- The support files keep the leaves distinct: context mapping rejects generic
  architecture formalism, contract tests reject surrogate/internal checks, and
  property invariants reject generator theater or vague "stronger tests"
  language.
- The generated topology scout marks all three as small-agent and read-only,
  which fits a compact support shelf that agents can select without requiring
  runtime orchestration.

## Proof Trunk Fit

`proof/` is the better trunk because this shelf prepares the evidence surface
around a boundary before stronger proof, evaluation, or owner-truth work tries
to depend on it.

This does not erase the historical domains. `AOA-T-0016` is still a docs
artifact, while `AOA-T-0015` and `AOA-T-0017` are still evaluation
validations. The proposed path answers a library-placement question: where
should a reader find compact support techniques for making a boundary
nameable, contract-visible, and invariant-constrained?

The shelf should not be called `testing-core` or `architecture-support`.
Direct reading shows the center is narrower: support around capability seams
and boundary proof surfaces, not testing doctrine or architecture taxonomy.

## Boundary Watch Accepted

The projection marks `skill-support` as `candidate`, but direct reading still
shows authority pressure:

- `AOA-T-0016` can drift into DDD formalism or architecture theater.
- `AOA-T-0015` can drift into oversized contract suites or hidden internal
  surrogate checks.
- `AOA-T-0017` can drift into generic property-testing glamour, weak
  invariants, or generator-first validation.

The shelf is accepted because each bundle already names those risks and keeps
its own role narrow. The later migration must preserve that separation.

## Proposed Move

Move exactly these three bundles in the migration wave:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0016` | `techniques/docs/bounded-context-map/` | `techniques/proof/skill-support/bounded-context-map/` |
| `AOA-T-0015` | `techniques/evaluation/contract-test-design/` | `techniques/proof/skill-support/contract-test-design/` |
| `AOA-T-0017` | `techniques/evaluation/property-invariants/` | `techniques/proof/skill-support/property-invariants/` |

Keep `domain`, `kind`, status, IDs, evidence, relations, maturity,
validation-strength metadata, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- `techniques/proof/AGENTS.md`, because this would be the first landed
  proof-side trunk shelf
- `techniques/docs/AGENTS.md` and `techniques/evaluation/AGENTS.md` only where
  representative bundle lists or local guidance still name the old homes
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- authored relations and adjacent references from docs, evaluation, skill,
  contract, invariant, and proof-adjacent surfaces
- generated catalogs, capsules, manifests, reports, KAG exports, docs readers,
  and source-lift surfaces after the path move
- mechanics review rows and tests that still point to the old homes
- release-check output touched by regenerated indexes and reports

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Why Not Neighbor Shelves In This Wave

`evaluation-chain` should wait. It produces machine-readable validation
contracts and staged enforcement signals, which is close to `skill-support`
but stronger than this boundary-support triangle.

`published-summary` should wait because summary integrity and rendering policy
are proof-adjacent but centered on published surfaces, not seam support.

`review-evidence` and `owner-truth-closeout` should wait because they carry
review-state and owner-truth pressure that can easily overclaim proof
authority.

`runtime-truth-lifecycle`, governance shelves, and automation shelves should
also wait because they add runtime, approval, owner, or promotion authority
pressure that this first proof-side shelf does not need.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not move `evaluation-chain`, `published-summary`, `review-evidence`,
  `owner-truth-closeout`, runtime, governance, automation, or other proof-side
  shelves in the same wave.
- Do not treat `skill-support` as proof authority, eval-suite ownership,
  mandatory testing doctrine, DDD formalism, architecture taxonomy, runtime
  readiness, owner-truth law, or policy enforcement.
- Do not collapse the three leaves into one mega-technique; the shelf holds
  because vocabulary mapping, contract-boundary validation, and invariant
  coverage stay distinct.
- Do not change canonical status, maturity, evidence, validation-strength
  metadata, or public-safety posture during the path migration.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the eleventh pilot migration.

Move exactly `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017` into
`techniques/proof/skill-support/`; add a compact proof trunk route card;
preserve a root `legacy/receipts/` migration receipt; repair authored links;
rebuild generated surfaces; and validate with the narrow tree-pilot tests plus
`python scripts/release_check.py`.
